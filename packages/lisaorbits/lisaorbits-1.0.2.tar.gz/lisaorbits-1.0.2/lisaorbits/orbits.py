#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=C0302
"""
LISA Orbits

This module generates orbit files, which contain information about nominal state of the
constellation, along with derived quantities such as spacecraft proper times, light travel
times and proper pseudo-ranges.

Authors:
    Jean-Baptiste Bayle <j2b.bayle@gmail.com>
    Marc Lilley <marc.lilley@gmail.com>
    Aurelien Hees <aurelien.hees@obspm.fr>
"""

import abc
import logging
import h5py
import numpy
from numpy import cos, sin, sqrt, log, pi
import matplotlib.pyplot
import scipy.interpolate

from lisaconstants import c
from lisaconstants import ASTRONOMICAL_UNIT
from lisaconstants import ASTRONOMICAL_YEAR
from lisaconstants import SUN_SCHWARZSCHILD_RADIUS

from . import meta
from .utils import dot, norm

logger = logging.getLogger(__name__)


class Orbits(abc.ABC):
    """Abstract base class for orbit-file generators.

    This abstract class provides the structure for all orbit generators. In particular, it
    implements the orbit-file generation method as well as generic implementations of light
    travel times, proper pseudo-ranges (PPRs) and derivatives thereof.

    This class is intended to be subclassed for each concrete type of orbits, such as
    Keplerian orbits, or orbits initially read from external files.

    The following methods MUST be implemented,

        * compute_spacecraft_position()
        * compute_spacecraft_velocity()
        * compute_spacecraft_acceleration()
        * compute_spacecraft_proper_time()
        * compute_deriv_spacecraft_proper_time()

    The following methods CAN be overriden by subclasses,

        * compute_spacecraft_tcb()
        * compute_light_travel_times()
        * compute_link_unit_vector()
        * compute_proper_pseudo_ranges()
        * compute_deriv_light_travel_times()
        * compute_deriv_proper_pseudo_range()

    An `Orbits` instance defines two time grids, used to sample the various quantities when
    plotting or writing to an orbit file,

        * one TCB time grid `t`, used for all quantities,
        * one receiver's TPS time grid `tau` which refers to `tau-tau_init`, used for proper
          pseudo-ranges and derivative thereof.

    At construction, use the `dt`, `size`, and `t0` arguments to define regular TCB and TPS grids.
    You can use the `t` and `tau` init's arguments to define custom (possible irregular)
    time vectors (note that doing so overrides the arguments `dt`, `size`, and `t0`).

    If `compute_...()` methods are called with the default argument, quantities are evaluated
    on the time vector `t` or `taut`; otherwise, quantities are evaluated for the time(s)
    passed as argument.

    Calling `precompute()` computes and saves all quantities on TCB and TPS grids.
    """
    SC_INDICES = [1, 2, 3]
    LINK_INDICES = ["12", "23", "31", "13", "32", "21"]

    def __init__(self,
                 dt=8640,
                 size=3650,
                 t0=0,
                 tinit=0,
                 tt_method='analytic',
                 tt_order=2,
                 tt_niter=4,
                 t=None,
                 tau=None):
        """Initialize an abstract orbit generator.

        Use the `dt`, `size`, and `t0` arguments to define regular TCB and TPS time vector,
        stored as `t` and `tau`. You can use `t` and `tau` init's arguments to define custom
        (possible irregular) TCB and TPS time vectors, in which case the `dt`, `size`, and `t0`
        arguments are ignored.

        To compute light travel times, we use `compute_light_travel_time()` if it is overriden
        by the subclass. Otherwise, light travel times are computed

            * from an analytical expansion, if `tt_method = 'analytic'`, at order `tt_order`,
            * or from an iterative expansion if `tt_method = 'iterative'`,
              with `tt_niter` iterations.

        To compute light travel time derivatives, we use `compute_deriv_light_travel_time()`
        if the subclass overrides it. Otherwise, light travel time derivatives are computed from
        an analytic expansion at order `tt_order`.

        When you subclass `Orbits`, you MUST call `super().__init__()` and `self.precompute()`
        in your implementation of `__init__()`.

        Args:
            dt: sampling period, in s
            size: simulation size, in number of samples
            t0: initial TCB time used for simulation sampling, in s
            tinit: TCB time at which initial conditions are provided
            tt_method: method to compute light travel time, one of 'analytic' or 'iterative'
            tt_order: twice the relativistic order used for analytical expansion of light travel times, 0, 1 or 2
            tt_niter: number of iterations used for iterative expansion of light travel times
            t: list of times defining a custom (possible irregular) TCB sampling, in s
            tau: list of times defining a custom (possible irregular) TPS sampling `tau-tau_init`, in s
        """
        self.git_url = 'https://gitlab.in2p3.fr/lisa-simulation/orbits'
        self.version = meta.__version__
        self.generator = self.__class__.__name__
        logger.info("Initializing orbits (lisaorbit verion %s)", self.version)

        self.tt_method = str(tt_method)
        self.tt_order = int(tt_order)
        self.tt_niter = int(tt_niter)

        if t is None:
            logger.debug("Initializing regular TCB sampling (dt=%f, t0=%f, size=%d)", dt, t0, size)
            self.dt = float(dt)
            self.t0 = float(t0)
            self.tinit = float(tinit)
            self.tsize = int(size)
            self.tduration = self.tsize * self.dt
            self.t = self.t0 + numpy.arange(self.tsize, dtype=numpy.float64) * self.dt
        else:
            if len(t) < 1:
                raise ValueError(f"Invalid custom TCB sampling '{t}'.")
            logger.debug("Initializing custom TCB sampling (size=%d)", len(t))
            self.dt = None
            self.t = numpy.array(t, dtype=numpy.float64)
            self.t.sort()
            self.tinit = float(tinit)
            self.t0 = self.t[0]
            self.tsize = len(t)
            self.tduration = self.t[-1] - self.t[0]

        if tau is None:
            logger.debug("Initializing regular TPS sampling (dt=%f, tau0=%f, size=%d)", dt, t0 - tinit, size)
            self.dtau = float(dt)
            self.tau0 = self.t0 - self.tinit
            self.tausize = int(size)
            self.tauduration = self.tausize * self.dtau
            self.tau = self.t - self.tinit
        else:
            logger.debug("Initializing custom TPS sampling (size=%d)", len(tau))
            self.dtau = None
            self.tau = numpy.array(tau, dtype=numpy.float64)
            self.tau.sort()
            self.tau0 = self.tau[0]
            self.tausize = len(tau)
            self.tauduration = self.tau[-1] - self.tau[0]

    def precompute(self):
        """Compute all quantities on the TCB and TPS time grids.

        This methods calls all `compute_...()` methods with default time arguments, so that
        quantities are evaluated on either the TCB or the receiver's TPS time grids.

        Quantities are then stored on the following properties,

            * spacecraft_positions
            * spacecraft_velocities
            * spacecraft_accelerations
            * spacecraft_proper_times
            * deriv_spacecraft_proper_times
            * spacecraft_tcb
            * light_travel_times
            * link_unit_vector
            * proper_pseudo_ranges
            * proper_pseudo_ranges_tps
            * deriv_light_travel_times
            * deriv_proper_pseudo_ranges
            * deriv_proper_pseudo_ranges_tps

        Subclasses MUST call `super().precompute()` in their implementation.
        """
        # pylint: disable=W0201

        # Spacecraft positions in the BCRS, in m
        # A dictionnary of arrays containing the position of each spacecraft 1, 2, 3
        # Each array contains 3 columns `x`, `y`, `z`, and `tsize` rows
        logger.info("Computing spacecraft positions")
        self.spacecraft_positions = {
            sc: self.compute_spacecraft_position(sc)
            for sc in self.SC_INDICES
        }

        # Spacecraft velocities in the BCRS, in m/s
        # A dictionnary of arrays containing the velocity of each spacecraft 1, 2, 3
        # Each array contains 3 columns `vx`, `vy`, `vz`, and `tsize` rows
        logger.info("Computing spacecraft velocities")
        self.spacecraft_velocities = {
            sc: self.compute_spacecraft_velocity(sc)
            for sc in self.SC_INDICES
        }

        # Spacecraft accelerations in the BCRS, in m/s**2
        # A dictionnary of arrays containing the acceleration of each spacecraft 1, 2, 3
        # Each array contains 3 columns `ax`, `ay`, `az`, and `tsize` rows
        logger.info("Computing spacecraft acelerations")
        self.spacecraft_accelerations = {
            sc: self.compute_spacecraft_acceleration(sc)
            for sc in self.SC_INDICES
        }

        # Spacecraft proper times (TPSs) in the BCRS, in s
        # A dictionnary of arrays containing the TPSs for each spacecraft 1, 2, 3
        # Each array contains 1 column `tau`, and `tsize` rows
        logger.info("Computing spacecraft proper times")
        self.spacecraft_proper_times = {
            sc: self.compute_spacecraft_proper_time(sc)
            for sc in self.SC_INDICES
        }

        # 1-PN part of the derivative of spacecraft proper times (TPSs) in the BCRS
        # A dictionnary of arrays containing the derivative of the TPSs for each spacecraft 1, 2, 3
        # Each array contains 1 column `tau`, and `tsize` rows
        logger.info("Computing spacecraft proper time derivatives")
        self.deriv_spacecraft_proper_times = {
            sc: self.compute_deriv_spacecraft_proper_time(sc)
            for sc in self.SC_INDICES
        }

        # Spacecraft TCB times given as a function of the proper time (TPS) grid, in s
        # A dictionnary of arrays containing the TCB of each spacecraft 1, 2, 3
        # Each array contains 1 column `t`, and `tausize` rows
        logger.info("Computing spacecraft TCB times")
        self.spacecraft_tcb = {
            sc: self.compute_spacecraft_tcb(sc, self.tau)
            for sc in self.SC_INDICES
        }

        # Light travel times between spacecraft on the TCB grid, in s
        # A dictionnary of arrays containing the light travel times along links 12, 23, 31, 13, 32, 21
        # Each array contains 1 colum `tt`, and `tausize` rows
        logger.info("Computing light travel times")
        self.light_travel_times = {
            link: self.compute_light_travel_time(int(link[1]), int(link[0]))
            for link in self.LINK_INDICES
        }

        # Unit link between spacecraft on the TCB grid
        # A dictionnary of arrays containing the unit vector along links 12, 23, 31, 13, 32, 21
        # Each array contains 1 colum `tt`, and `tausize` rows
        logger.info("Computing unit vectors")
        self.link_unit_vector = {
            link: self.compute_link_unit_vector(int(link[1]), int(link[0]))
            for link in self.LINK_INDICES
        }

        # Proper pseudo-ranges (PPRs) between spacecraft on the TCB grid, in s
        # A dictionnary of arrays containing the proper pseudo-ranges along links 12, 23, 31, 13, 32, 21
        # Each array contains 1 colum `ppr`, and `tsize` rows
        logger.info("Computing proper pseudo-range")
        self.proper_pseudo_ranges = {
            link: self.compute_proper_pseudo_range(int(link[1]), int(link[0]))
            for link in self.LINK_INDICES
        }

        # Proper pseudo-ranges (PPRs) between spacecraft, on receiver's TPS grid, in s
        # A dictionnary of arrays containing the proper pseudo-ranges along links 12, 23, 31, 13, 32, 21
        # Each array contains 1 colum `ppr_tps`, and `tausize` rows
        logger.info("Computing proper pseudo-ranges on receiver's proper time grid")
        self.proper_pseudo_ranges_tps = {
            link: self.compute_proper_pseudo_range(int(link[1]), int(link[0]), self.spacecraft_tcb[int(link[0])])
            for link in self.LINK_INDICES
        }

        # Derivative of the light travel time w.r.t. TCB on the TCB grid, in s/s
        # A dictionnary of arrays containing the light travel time derivative along links 12, 23, 31, 13, 32, 21
        # Each array contains 1 colum `d_tt`, and `tsize` rows
        logger.info("Computing light travel time derivatives")
        self.deriv_light_travel_times = {
        link: self.compute_deriv_light_travel_time(int(link[1]), int(link[0]))
        for link in self.LINK_INDICES
        }

        # Derivative of PPRs with respect to the receiving TPS on the TCB grid, in s/s
        # A dictionnary of arrays containing the proper pseudo-range derivative along links 12, 23, 31, 13, 32, 21
        # Each array contains 1 colum `d_ppr`, and `tsize` rows
        logger.info("Computing derivative of proper pseudo-ranges")
        self.deriv_proper_pseudo_ranges = {
            link: self.compute_deriv_proper_pseudo_range(int(link[1]), int(link[0]))
            for link in self.LINK_INDICES
        }

        # Derivative of PPRs with respect to the receiving TPS on receiver's TPS grid, in s/s
        # A dictionnary of arrays containing the proper pseudo-range derivative along links 12, 23, 31, 13, 32, 21
        # Each array contains 1 colum `d_ppr_tps`, and `tausize` rows
        logger.info("Computing derivative of proper pseudo-ranges on receiver's proper time grid")
        self.deriv_proper_pseudo_ranges_tps = {
            link: self.compute_deriv_proper_pseudo_range(int(link[1]), int(link[0]), self.spacecraft_tcb[int(link[0])])
            for link in self.LINK_INDICES
        }

    @abc.abstractmethod
    def compute_spacecraft_position(self, sc, t=None):
        """Compute the BCRS position of a spacecraft, in m.

        Args:
            sc: spacecraft index, one of 1, 2, 3
            t: array of TCB times, in s (compute for `self.t` if None)

        Return:
            Array of positions of spacecraft `sc` at TCB times `t`.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def compute_spacecraft_velocity(self, sc, t=None):
        """Compute the BCRS velocity of a spacecraft.

        Args:
            sc: spacecraft index, one of 1, 2, 3
            t: array of TCB times, in s (compute for `self.t` if None)

        Return:
            Array of velocities of spacecraft `sc` at TCB times `t`.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def compute_spacecraft_acceleration(self, sc, t=None):
        """Compute the BCRS acceleration of a spacecraft.

        Args:
            sc: spacecraft index, one of 1, 2, 3
            t: array of TCB times, in s (compute for `self.t` if None)

        Return:
            Array of accelerations of spacecraft `sc` at TCB times `t`.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def compute_spacecraft_proper_time(self, sc, t=None):
        """Compute the deviation of the proper time of a spacecraft w.r.t. TCB time.

        We compute `tau(t) - tau(tinit) - (t - tinit)`, where `tau` is the spacecraft proper
        time and `t` the associated TCB time.

        Args:
            sc: spacecraft index, one of 1, 2, 3
            t: array of TCB times, in s (compute for `self.t` if None)

        Return:
            Array of proper time deviations of spacecraft `sc` at TCB times `t`.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def compute_deriv_spacecraft_proper_time(self, sc, t=None):
        """Compute the time derivative of the proper time of a spacecraft w.r.t. TCB time.

        We compute `d(tau - t)/dt = dtau/dt - 1`, where `tau` is the spacecraft proper time
        and `t` the associated TCB time.

        Args:
            sc: spacecraft index, one of 1, 2, 3
            t: array of TCB times, in s (compute for `self.t` if None)

        Return:
            Array of derivatives of the proper time of spacecraft `sc` at times `t`.
        """
        raise NotImplementedError

    def compute_spacecraft_tcb(self, sc, tau=None):
        """Compute the TCB time from spacecraft proper time to first order.

        We compute

            t(tau)

        where `tau` is the spacecraft proper time (TPS) with respect to `tau_init`
        (i.e. `tau-tau_init`), `t` the associated TCB time.

        Args:
            sc: spacecraft index, one of 1, 2, 3
            tau: array of array TPS times with respect to `tau_init`, in s (compute for `self.tau` if None)

        Return:
            Array of TCB times associated to the TPS times `tau` of spacecraft `sc`.
        """
        if tau is None:
            tau = self.tau
        return self.tinit + tau - self.compute_spacecraft_proper_time(sc, self.tinit + tau)

    def compute_light_travel_time(self, emitter, receiver, t=None):
        """Compute relativistic light travel times by the method define in `self.tt_method`.

        The light travel time is the time difference measured in the BCRS between two events:
        the reception of a photon in one spacecraft, and the emission of the same photon by
        another spacecraft.

        We use the method (analytic or iterative) and the precision (order or number of iterations)
        set in `self.tt_method` and `self.tt_order` or `self.tt_niter`.

        Args:
            emitter: index of emitting spacecraft, one of 1, 2, 3
            receiver: index of receiving spacecraft, one of 1, 2, 3
            t: array of TCB times, in s (compute for `self.t` if None)

        Raises:
            ValueError if the light travel time computation method `self.tt_method` is not valid.
        """
        if self.tt_method == 'analytic':
            return self.compute_analytic_travel_time(emitter, receiver, t)
        if self.tt_method == 'iterative':
            return self.compute_iterative_travel_time(emitter, receiver, t)
        raise ValueError(f"Invalid light travel time computation method '{self.tt_method}', "
                         "must be 'analytic' or 'iterative'.")

    def compute_analytic_travel_time(self, emitter, receiver, t=None):
        """Compute relativistic light travel times using an analytical expansion.

        Follow equations 3 and 6 from [1].

            [1] Hees, A., Bertone, S., Le Poncin-Lafitte, C. (2014).
                Relativistic formulation of coordinate light time, Doppler and astrometric
                observables up to the second post-Minkowskian order.
                Physical Review D - Particles, Fields, Gravitation and Cosmology, 89(6).
                https://doi.org/10.1103/PhysRevD.89.064045

        Args:
            emitter: index of emitting spacecraft, one of 1, 2, 3
            receiver: index of receiving spacecraft, one of 1, 2, 3
            t: array of TCB times, in s (compute for `self.t` if None)

        Raises:
            ValueError if the expansion order is invalid.
        """
        if self.tt_order < 0 or self.tt_order > 2:
            raise ValueError(f"Invalid light travel time computation order '{self.tt_order}', "
                             "should be one of 0, 1, or 2 when computed with analytical expansion.")

        if t is None:
            pos_em = self.spacecraft_positions[emitter]
            pos_rec = self.spacecraft_positions[receiver]
        else:
            pos_em = self.compute_spacecraft_position(emitter, t)
            pos_rec = self.compute_spacecraft_position(receiver, t)

        # Order 0
        d_er = norm(pos_rec - pos_em)
        tt = d_er
        # Order 1
        if self.tt_order >= 1:
            if t is None:
                vel_em = self.spacecraft_velocities[emitter]
            else:
                vel_em = self.compute_spacecraft_velocity(emitter, t)
            r_er = (pos_rec - pos_em) # vector from emitter to receiver
            velem_rer = dot(vel_em, r_er)
            tt += velem_rer / c
        # Order 2
        if self.tt_order == 2:
            if t is None:
                acc_em = self.spacecraft_accelerations[emitter]
            else:
                acc_em = self.compute_spacecraft_acceleration(emitter, t)
            # This part is a correction arising from emitter motion
            tt += 0.5 * (dot(vel_em, vel_em) + (velem_rer / d_er)**2 - dot(acc_em, r_er)) * d_er / c**2
            # The following part is the Shapiro delay
            r_em = norm(pos_em)
            r_rec = norm(pos_rec)
            tt += SUN_SCHWARZSCHILD_RADIUS * log((r_em + r_rec + d_er) / (r_em + r_rec - d_er))
        return tt / c

    def compute_iterative_travel_time(self, emitter, receiver, t=None):
        """Compute relativistic light travel times using an iterative procedure.

        The iterative procedure is standard and is described, e.g.,
        in [1] (see Eqs. (7), (3) and (59a)).

            [1] Hees, A., Bertone, S., Le Poncin-Lafitte, C. .
                Relativistic formulation of coordinate light time, Doppler, and astrometric
                observables up to the second post-Minkowskian order.
                Physical Review D 86, 064045, 2014.

        Args:
            emitter: index of emitting spacecraft, one of 1, 2, 3
            receiver: index of receiving spacecraft, one of 1, 2, 3
            t: array of TCB times, in s (compute for `self.t` if None)

        Raises:
            ValueError if the number of iterations is invalid.
        """
        if t is None:
            treceiver = self.t
            pos_em = self.spacecraft_positions[emitter]
            pos_rec = self.spacecraft_positions[receiver]
        else:
            treceiver = t
            pos_em = self.compute_spacecraft_position(emitter, treceiver)
            pos_rec = self.compute_spacecraft_position(receiver, treceiver)

        if self.tt_niter < 0:
            raise ValueError(f"Invalid number of iterations '{self.tt_niter}' for iterative procedure when "
                             "computing the light travel times.")

        # First the iteration to find the flat spacetime travel time
        tt = norm(pos_rec - pos_em) / c
        for _ in range(self.tt_niter):
            temitter = treceiver - tt
            pos_em = self.compute_spacecraft_position(emitter, temitter)
            tt = norm(pos_rec - pos_em) / c
        # And the Shapiro time delay
        r_em = norm(pos_em)
        r_rec = norm(pos_rec)
        d_er = c * tt
        tt += SUN_SCHWARZSCHILD_RADIUS * log((r_em + r_rec + d_er) / (r_em + r_rec - d_er)) / c
        return tt

    def compute_proper_pseudo_range(self, emitter, receiver, t=None):
        """Compute relativistic proper pseudo-range (PPR) between two spacecraft.

        The proper pseudo-range is computed by forming the difference between the time of reception
        expressed in the TPS of the receiving spacecraft, and the time of emission expressed in the
        TPS of the emitting spacecraft. Note that it includes the light traveltime in the BCRS,
        as well as the conversion between the TPSs and the TCB.

        This function uses the light travel times computed in the BCRS, and accounts for
        the proper times of the emitting and receiving spacecraft.

        Args:
            emitter: index of emitting spacecraft, one of 1, 2, 3
            receiver: index of receiving spacecraft, one of 1, 2, 3
            t: array of TCB reception times, in s (compute for `self.t` if None)

        Return:
            A numpy array containing the proper pseudo-ranges between `emitter` and `receiver` at TCB times `t`.
        """
        if t is None:
            t = self.t
            tau_receiver = self.spacecraft_proper_times[receiver]
            tt = self.light_travel_times[f'{receiver}{emitter}']
        else:
            tau_receiver = self.compute_spacecraft_proper_time(receiver, t)
            tt = self.compute_light_travel_time(emitter, receiver, t)

        return tt + tau_receiver - self.compute_spacecraft_proper_time(emitter, t - tt)

    def compute_deriv_light_travel_time(self, emitter, receiver, t=None):
        """Compute time derivative light travel times using an analytical expansion.

        Args:
            emitter: index of emitting spacecraft, one of 1, 2, 3
            receiver: index of receiving spacecraft, one of 1, 2, 3
            t: optional numpy array of receiving time in TCB
        """
        if t is None:
            treceiver = self.t
            pos_rec = self.spacecraft_positions[receiver]
            vel_rec = self.spacecraft_velocities[receiver]
            light_travel_time = self.light_travel_times[f'{receiver}{emitter}']
        else:
            treceiver = t
            pos_rec = self.compute_spacecraft_position(receiver, treceiver)
            vel_rec = self.compute_spacecraft_velocity(receiver, treceiver)
            light_travel_time = self.compute_light_travel_time(emitter, receiver, t)

        # Note that the position and velocity of the emitter are evaluated
        # at receiver time for order 0 and 1, but at emitter time for order 2
        temitter = treceiver - light_travel_time
        if self.tt_order < 2 and self.tt_method == 'analytic':
            if t is None:
                pos_em = self.spacecraft_positions[emitter]
                vel_em = self.spacecraft_velocities[emitter]
            else:
                pos_em = self.compute_spacecraft_position(emitter, treceiver)
                vel_em = self.compute_spacecraft_velocity(emitter, treceiver)
        else:
            pos_em = self.compute_spacecraft_position(emitter, temitter)
            vel_em = self.compute_spacecraft_velocity(emitter, temitter)

        r_er = pos_rec - pos_em # vector from emitter to receiver
        d_er = norm(pos_rec - pos_em)
        n_er = r_er / d_er[:, numpy.newaxis] # unit vector from emitter to receiver
        ner_vr = dot(n_er, vel_rec)
        ner_ve = dot(n_er, vel_em)

        if self.tt_order < 2 and self.tt_method == 'analytic':
            # This is the zeroth order term which contributes only
            # for order 0 or order 1
            # all quantities being evaluated at the receiver time
            d_tt = (ner_vr - ner_ve) / c
        else:
            # The derivation is different if one goes to 2nd order.
            # See Eq. 27 in Hees et al CQG 29(23):235027 (2012).
            r_em = norm(pos_em)
            r_rec = norm(pos_rec)
            den = (r_em + r_rec)**2 - d_er**2
            dq_rec = ner_vr + 2 * SUN_SCHWARZSCHILD_RADIUS * \
                ((r_em + r_rec) * ner_vr - d_er * dot(pos_rec,vel_rec) / r_rec) / den
            dq_em = ner_ve + 2 * SUN_SCHWARZSCHILD_RADIUS * \
                ((r_em + r_rec) * ner_ve + d_er * dot(pos_em,vel_em) / r_em) / den
            d_tt = (dq_rec - dq_em) / (c - dq_em)

        if self.tt_order == 1 and self.tt_method == 'analytic':
            # This is the first order contribution, to be included only if
            # the order is strictly less than 2
            if t is None:
                acc_em = self.spacecraft_accelerations[emitter]
            else:
                acc_em = self.compute_spacecraft_acceleration(emitter, treceiver)
            d_tt += (dot(vel_rec - vel_em, vel_em) + dot(pos_rec - pos_em, acc_em)) / c**2

        return d_tt

    def compute_deriv_proper_pseudo_range(self, emitter, receiver, t=None):
        """Compute the derivative of proper pseudo-range.

        This function uses the derivative of the light travel times computed in the BCRS,
        and accounts for the proper times of the emitting and receiving spacecraft.

        Args:
            emitter: index of emitting spacecraft, one of 1, 2, 3
            receiver: index of receiving spacecraft, one of 1, 2, 3
            t: array of TCB times, in s (compute for `self.t` if None)

        Return:
            A numpy array containing the derivative of proper pseudo-range between `emitter` and `receiver`.
        """
        if t is None:
            link = f'{receiver}{emitter}'
            d_tt = self.deriv_light_travel_times[link]
            tt = self.light_travel_times[link]
            t = self.t
            dtau_receiver = self.deriv_spacecraft_proper_times[receiver]
        else:
            dtau_receiver = self.compute_deriv_spacecraft_proper_time(receiver, t)
            d_tt = self.compute_deriv_light_travel_time(emitter, receiver, t)
            tt = self.compute_light_travel_time(emitter, receiver, t)
        dtau_emitter = self.compute_deriv_spacecraft_proper_time(emitter, t - tt)
        return (dtau_receiver - dtau_emitter + d_tt * (1 + dtau_emitter)) / (1 + dtau_receiver)

    def compute_link_unit_vector(self, emitter, receiver, t=None):
        """Compute the unit vector for a link in BCRS coordinates.

        The unit vector pointsfrom the emittter towards the receiver.
        We compute

           n = x_receiver(t_receiver) - x_emitter(t_emitter) / | x_receiver - x_emitter |

        Args:
            emitter: index of emitting spacecraft, one of 1, 2, 3
            receiver: index of receiving spacecraft, one of 1, 2, 3
            t: array of TCB receiving times, in s (compute for `self.t` if None)
        """
        if t is None:
            treceiver = self.t
            link = f'{receiver}{emitter}'
            tt = self.light_travel_times[link]
            pos_rec = self.spacecraft_positions[receiver]
        else:
            treceiver = t
            tt = self.compute_light_travel_time(emitter, receiver, treceiver)
            pos_rec = self.compute_spacecraft_position(receiver, treceiver)
        pos_em = self.compute_spacecraft_position(emitter, treceiver - tt)

        return (pos_rec - pos_em) / norm(pos_rec - pos_em)[:, numpy.newaxis]

    def plot_spacecraft(self, sc, output=None):
        """Plot quantities associated with the spacecraft.

        Args:
            sc: spacecraft index, one of 1, 2, 3
            output: output file, None to show the plots
        """
        # Precompute time series
        self.precompute()
        # Initialize the plot
        _, axes = matplotlib.pyplot.subplots(5, 1, figsize=(12, 20))
        axes[0].set_title(f"Spacecraft {sc}")
        axes[4].set_xlabel("Barycentric time (TCB) [s]")
        # Plot positions
        logger.info("Plotting positions for spacecraft %d", sc)
        axes[0].set_ylabel("Position [m]")
        axes[0].plot(self.t[:], self.spacecraft_positions[sc][:, 0], label=r'$x$')
        axes[0].plot(self.t[:], self.spacecraft_positions[sc][:, 1], label=r'$y$')
        axes[0].plot(self.t[:], self.spacecraft_positions[sc][:, 2], label=r'$z$')
        # Plot velocities
        logger.info("Plotting velocities for spacecraft %d", sc)
        axes[1].set_ylabel("Velocity [m/s]")
        axes[1].plot(self.t[:], self.spacecraft_velocities[sc][:, 0], label=r'$v_x$')
        axes[1].plot(self.t[:], self.spacecraft_velocities[sc][:, 1], label=r'$v_y$')
        axes[1].plot(self.t[:], self.spacecraft_velocities[sc][:, 2], label=r'$v_z$')
        # Plot accelerations
        logger.info("Plotting accelerations for spacecraft %d", sc)
        axes[2].set_ylabel("Acceleration [m/s^2]")
        axes[2].plot(self.t[:], self.spacecraft_accelerations[sc][:, 0], label=r'$a_x$')
        axes[2].plot(self.t[:], self.spacecraft_accelerations[sc][:, 1], label=r'$a_y$')
        axes[2].plot(self.t[:], self.spacecraft_accelerations[sc][:, 2], label=r'$a_z$')
        # Plot proper times
        logger.info("Plotting proper times for spacecraft %d", sc)
        axes[3].set_ylabel("Proper time deviation [s]")
        axes[3].plot(self.t[:], self.spacecraft_proper_times[sc], label=r'$\delta \tau$')
        # Plot proper time derivatives
        logger.info("Plotting proper time derivatives for spacecraft %d", sc)
        axes[4].set_ylabel("Proper time deviation derivative [s/s]")
        axes[4].plot(self.t[:], self.deriv_spacecraft_proper_times[sc], label=r'$\dot \delta \tau$')
        # Add legend and grid
        for axis in axes:
            axis.legend()
            axis.grid()
        # Show or save figure
        if output is not None:
            logger.info("Saving plots to %s", output)
            matplotlib.pyplot.savefig(output, bbox_inches='tight')
        else:
            logger.info("Showing plots")
            matplotlib.pyplot.show()

    def plot_links(self, output=None):
        """Plot link light travel time, proper pseudo-ranges, and derivatives.

        Args:
            output: output file, None to show the plots
        """
        # Precompute time series
        self.precompute()
        # Initialize the plot
        _, axes = matplotlib.pyplot.subplots(4, 1, figsize=(12, 16))
        axes[0].set_title("Light travel times, proper pseudo-range and derivatives")
        axes[3].set_xlabel("Barycentric time (TCB) [s]")
        # Plot light travel times
        logger.info("Plotting light travel times")
        axes[0].set_ylabel("Light travel time [s]")
        for link in self.LINK_INDICES:
            axes[0].plot(self.t[:], self.light_travel_times[link], label=link)
        # Plot proper pseudo-ranges
        logger.info("Plotting proper pseudo-ranges")
        axes[1].set_ylabel("Proper pseudo-range [s]")
        for link in self.LINK_INDICES:
            axes[1].plot(self.t[:], self.proper_pseudo_ranges[link], label=link)
        # Plot light travel time derivatives
        logger.info("Plotting light travel time derivatives")
        axes[2].set_ylabel("Light travel time derivative [s/s]")
        for link in self.LINK_INDICES:
            axes[2].plot(self.t[:], self.deriv_light_travel_times[link], label=link)
        # Plot proper pseudo-range derivatives
        logger.info("Plotting proper pseudo-range derivatives")
        axes[3].set_ylabel("Proper pseudo-range derivative [s/s]")
        for link in self.LINK_INDICES:
            axes[3].plot(self.t[:], self.deriv_proper_pseudo_ranges[link], label=link)
        # Add legend and grid
        for axis in axes:
            axis.legend()
            axis.grid()
        # Show or save figure
        if output is not None:
            logger.info("Saving plots to %s", output)
            matplotlib.pyplot.savefig(output, bbox_inches='tight')
        else:
            logger.info("Showing plots")
            matplotlib.pyplot.show()

    def write_metadata(self, hdf5):
        """Set all properties as HDF5 attributes on `object`.

        Args:
            hdf5: an HDF5 file, or a dataset
        """
        for key, value in self.__dict__.items():
            try:
                hdf5.attrs[key] = value
            except (TypeError, RuntimeError):
                try:
                    hdf5.attrs[key] = str(value)
                except RuntimeError:
                    logger.warning("Cannot write metadata '%s' on '%s'", key, hdf5)

    def write(self, path="orbits.h5", mode='x'):
        """Generate the orbit file.

        The orbits are generated at sampling rate `fs` and `duration`, defining the
        TCB time grid `t`, with a total number of samples of

            N = `duration` * `fs`.

        The HDF5 orbit file has the following structure,
            |- group `tcb` for quantities evaluated on the TCB time grid
            |    |
            |    |- TCB time dataset `t`, of shape (tsize), in s
            |    |
            |    |- spacecraft datasets `sc_1`, `sc_2`, and `sc_3`, of shape (7, tsize),
            |    |    |- `x`, `y`, `z`, for the position in m
            |    |    |- `vx`, `vy`, `vz` for the velocity in m/s
            |    |    |- `tau` for the spacecraft proper time (TPS) in s
            |    |
            |    |- link datasets `l_12`, `l_23`, `l_31`, `l_13`, `l_32`, and `l_21`, of shape (7, tsize),
            |    |    |- `tt`, for the light travel time, in s
            |    |    |- `ppr`, for the proper pseudo-range, in s
            |    |    |- `d_tt`, for light travel time derivative, in s/s
            |    |    |- `d_ppr`, for proper pseudo-range derivative, in s/s
            |    |    |- `nx`, `ny`, `nz`, for the unit vector pointing from the emitter to the receiver
            |
            |- group `tps` for quantities evaluated on the TPS time grid
            |    |
            |    |- TPS time dataset `tau`, of shape (tausize), in s
            |    |
            |    |- spacecraft datasets `sc_1`, `sc_2`, and `sc_3`, of shape (1, tausize),
            |    |    |- `t`, for the barycentric coordinated time (TCB), in s
            |    |
            |    |- link datasets `l_12`, `l_23`, `l_31`, `l_13`, `l_32`, and `l_21`, of shape (2, tausize),
            |    |    |- `ppr`, for the proper pseudo-range, in s
            |    |    |- `d_ppr`, for proper pseudo-range derivative, in s/s


        Metadata are saved as attributes of the orbit HDF5 file,

            * `generator`, name of orbit generator class,
            * `version`, git version identifier of lisaorbits,
            * any other property of the orbit generator with a scalar type.

        Args:
            path: path to the generated orbit file
            mode: open mode, default 'x' (create file, fail if exists)
        """
        # Precompute time series
        self.precompute()
        # Open orbit file
        logger.info("Creating orbit file %s", path)
        hdf5 = h5py.File(path, mode)
        # Setting metadata
        logger.debug("Setting metadata")
        self.write_metadata(hdf5)
        # Create time datasets
        logger.debug("Creating TCB time dataset")
        hdf5.create_dataset('tcb/t', data=self.t)
        logger.debug("Creating TPS time dataset")
        hdf5.create_dataset('tps/tau', data=self.tau)
        # Create TCB spacecraft datasets
        logger.info("Creating TCB spacecraft datasets")
        sc_columns = ['x', 'y', 'z', 'vx', 'vy', 'vz', 'tau', 'd_tau']
        sc_dtype = numpy.dtype({'names': sc_columns, 'formats': [numpy.float64] * len(sc_columns)})
        for sc in self.SC_INDICES:
            dname = f'tcb/sc_{sc}'
            hdf5.create_dataset(dname, (self.tsize,), dtype=sc_dtype)
            logger.debug("Writing spacecraft %d positions", sc)
            hdf5[dname]['x'] = self.spacecraft_positions[sc][:, 0]
            hdf5[dname]['y'] = self.spacecraft_positions[sc][:, 1]
            hdf5[dname]['z'] = self.spacecraft_positions[sc][:, 2]
            logger.debug("Writing spacecraft %d velocities", sc)
            hdf5[dname]['vx'] = self.spacecraft_velocities[sc][:, 0]
            hdf5[dname]['vy'] = self.spacecraft_velocities[sc][:, 1]
            hdf5[dname]['vz'] = self.spacecraft_velocities[sc][:, 2]
            logger.debug("Writing spacecraft %d proper times", sc)
            hdf5[dname]['tau'] = self.spacecraft_proper_times[sc]
            logger.debug("Writing spacecraft %d proper time derivatives", sc)
            hdf5[dname]['d_tau'] = self.deriv_spacecraft_proper_times[sc]
        # Create TPS spacecraft datasets
        logger.info("Creating TPS spacecraft datasets")
        sc_columns = ['t']
        sc_dtype = numpy.dtype({'names': sc_columns, 'formats': [numpy.float64] * len(sc_columns)})
        for sc in self.SC_INDICES:
            dname = f'tps/sc_{sc}'
            hdf5.create_dataset(dname, (self.tausize,), dtype=sc_dtype)
            logger.debug("Writing spacecraft %d barycentric times", sc)
            hdf5[dname]['t'] = self.spacecraft_tcb[sc]
        # Create TCB link datasets
        logger.info("Creating TCB link datasets")
        link_columns = ['tt', 'ppr', 'd_tt', 'd_ppr','nx','ny','nz']
        link_dtype = numpy.dtype({'names': link_columns, 'formats': [numpy.float64] * len(link_columns)})
        for link in self.LINK_INDICES:
            dname = f'tcb/l_{link}'
            hdf5.create_dataset(dname, (self.tsize,), dtype=link_dtype)
            logger.debug("Writing light travel times %s", link)
            hdf5[dname]['tt'] = self.light_travel_times[link]
            logger.debug("Writing proper pseudo-ranges %s", link)
            hdf5[dname]['ppr'] = self.proper_pseudo_ranges[link]
            logger.debug("Writing light travel time derivatives %s", link)
            hdf5[dname]['d_tt'] = self.deriv_light_travel_times[link]
            logger.debug("Writing proper pseudo-range derivatives %s", link)
            hdf5[dname]['d_ppr'] = self.deriv_proper_pseudo_ranges[link]
            logger.debug("Writing unit vector %s", link)
            hdf5[dname]['nx'] = self.link_unit_vector[link][:,0]
            hdf5[dname]['ny'] = self.link_unit_vector[link][:,1]
            hdf5[dname]['nz'] = self.link_unit_vector[link][:,2]

        # Create TPS link datasets
        logger.info("Creating TPS link datasets")
        link_columns = ['ppr', 'd_ppr']
        link_dtype = numpy.dtype({'names': link_columns, 'formats': [numpy.float64] * len(link_columns)})
        for link in self.LINK_INDICES:
            dname = f'tps/l_{link}'
            hdf5.create_dataset(dname, (self.tausize,), dtype=link_dtype)
            logger.debug("Writing proper pseudo-ranges %s", link)
            hdf5[dname]['ppr'] = self.proper_pseudo_ranges_tps[link]
            logger.debug("Writing proper pseudo-range derivatives %s", link)
            hdf5[dname]['d_ppr'] = self.deriv_proper_pseudo_ranges_tps[link]
        # Closing file
        logger.info("Closing orbit file %s", path)
        hdf5.close()


class KeplerianOrbits(Orbits):
    """Orbit generator based on Keplerian orbits.

    The orbits are obtained for a 2-body problem (spacecraft and Sun) in a Newtonian theory
    of gravitation. The orbital period of the spacecraft is fixed to 1 astronomical year.

    From [1], we use spacecraft positions and velocities for Keplerian orbits reducing
    LISA's flexing to second order of α = l/(2R).

    The implementation in this class is based on section VI from [2] (the eccentric anomaly
    from that paper is different from [1] and is more commonly used).

        [1] K. Rajesh Nayak, S. Koshti, S. V. Dhurandhar, and J. Y. Vinet. On the minimum flexing of LISA’s arms.
            Classical and Quantum Gravity, 23(5):1763– 1778, 2006.

       [2] B. Chauvineau, T. Regimbeau, J-Y Vinet, S. Pireaux, Relativistic analysis of the LISA long range
           optical links, Phys. Rev. D72, 122003, 2005.
    """
    def __init__(self, L=2.5E9, a=ASTRONOMICAL_UNIT, delta=5/8, lambda1=0, m_init1=0, kepler_order=2, **kwargs):
        """Initialize an orbit generator for a set of Keplerian orbits.

        In these orbits, we consider the Sun only in Newtonian gravity.

        The Kepler equation is solved by using an iterative procedure that itself starts from a low
        eccentricity expansion (to third order).

        Args:
            L: mean inter-spacecraft distance, in m
            a: semi-major axis for an orbital period of 1 yr, in m
            delta: small perturbation to tilt angle, in units of the characteristic ratio
            lambda1: longitude of periastron for spacecraft 1, in rad
            m_init1: mean anomaly at tinit for spacecraft 1, in rad
            kepler_order: number of iterations used to solve Kepler equation
            **kwargs: all other args from `Orbits`
        """
        super().__init__(**kwargs)

        self.a = float(a)
        self.L = float(L)
        self.delta = float(delta)
        self.kepler_order = int(kepler_order)
        self.m_init1 = float(m_init1)
        self.lambda1 = float(lambda1)
        self.init_orbital_parameters()

    def init_orbital_parameters(self):
        """Pre-compute orbital parameters on the `self.t` time grid."""
        logger.info("Initializing orbital parameters")

        self.alpha = self.L / (2 * self.a)
        self.nu = pi / 3 + self.delta * self.alpha

        self.e = sqrt(1 + 4 * self.alpha * cos(self.nu) / sqrt(3) + 4 * self.alpha**2 / 3) - 1
        self.tan_i = self.alpha * sin(self.nu) / ((sqrt(3) / 2) + self.alpha * cos(self.nu))
        self.cos_i = 1 / sqrt(1 + self.tan_i**2)
        self.sin_i = self.tan_i * self.cos_i

        self.n = 2 * pi / ASTRONOMICAL_YEAR
        self.theta = {sc: (sc - 1) * 2 * pi / 3 for sc in self.SC_INDICES}
        self.m_init = {sc: self.m_init1 - self.theta[sc] for sc in self.SC_INDICES}
        self.lambda_k = {sc: self.lambda1 + self.theta[sc] for sc in self.SC_INDICES}
        self.sin_lambda = {sc: sin(self.lambda_k[sc]) for sc in self.SC_INDICES}
        self.cos_lambda = {sc: cos(self.lambda_k[sc]) for sc in self.SC_INDICES}

        self.psi = {sc: self.compute_eccentric_anomaly(sc, self.t) for sc in self.SC_INDICES}
        self.cos_psi = {sc: cos(self.psi[sc]) for sc in self.SC_INDICES}
        self.sin_psi = {sc: sin(self.psi[sc]) for sc in self.SC_INDICES}
        self.dpsi = {sc: self.n / (1 - self.e * self.cos_psi[sc]) for sc in self.SC_INDICES}
        self.psi_init = {sc: self.compute_eccentric_anomaly(sc, self.tinit) for sc in self.SC_INDICES}

        self.gr_const = (self.n * self.a / c)**2

    def compute_eccentric_anomaly(self, sc, t):
        """Compute the eccentric anomaly of spacecraft `sc` for time `t`.

        We solve the Kepler equation `psi - e sin (psi) = M(t)`, with M(t) the mean anomaly.

        Args:
            sc: spacecraft index, one of 1, 2, 3
            t: time or array of times, in s

        Return:
            If `t` is a scalar, returns the eccentric anomaly of spacecraft `sc` at time `t`.
            If `t` is an array, returns an array containing the eccentric anomalies of spacecraft `sc` at times `t`.
        """
        # Compute the mean anomaly
        logger.debug("Computing eccentric anomaly for spacecraft %s at time %s s", sc, t)
        m = self.m_init[sc] + self.n * (t - self.tinit)
        # The following expression is valid up to e**4
        ecc_anomaly = m + (self.e - self.e**3/8) * sin(m) + 0.5 * self.e**2 * sin(2 * m) \
            + 3/8 * self.e**3 * sin(3 * m)
        # Standard Newton-Raphson iterative procedure
        for _ in range(self.kepler_order):
            error = ecc_anomaly - self.e * sin(ecc_anomaly) - m
            ecc_anomaly -= error / (1 - self.e * cos(ecc_anomaly))
        return ecc_anomaly

    def compute_spacecraft_position(self, sc, t=None):
        """Compute position of spacecraft `sc` at time `t`.

        If `t` is None, we use `self.t` and optimize the computation by reusing the pre-computed
        eccentric anomalies for these times.
        """
        if t is None:
            cos_psi = self.cos_psi[sc]
            sin_psi = self.sin_psi[sc]
        else:
            psi = self.compute_eccentric_anomaly(sc, t)
            cos_psi = cos(psi)
            sin_psi = sin(psi)
        # Reference position
        ref_x = self.a * self.cos_i * (cos_psi - self.e)
        ref_y = self.a * sqrt(1 - self.e**2) * sin_psi
        ref_z = -self.a * self.sin_i * (cos_psi - self.e)
        # Spacecraft position
        sc_x = self.cos_lambda[sc] * ref_x - self.sin_lambda[sc] * ref_y
        sc_y = self.sin_lambda[sc] * ref_x + self.cos_lambda[sc] * ref_y
        sc_z = ref_z
        # Stack coordinates
        return numpy.column_stack((sc_x, sc_y, sc_z))

    def compute_spacecraft_velocity(self, sc, t=None):
        """Compute velocity of spacecraft `sc` at time `t`.

        If `t` is None, we use `self.t` and optimize the computation by reusing the pre-computed
        eccentric anomalies and their derivatives for these times.
        """
        if t is None:
            cos_psi = self.cos_psi[sc]
            sin_psi = self.sin_psi[sc]
            dpsi = self.dpsi[sc]
        else:
            psi = self.compute_eccentric_anomaly(sc, t)
            cos_psi = cos(psi)
            sin_psi = sin(psi)
            dpsi = self.n / (1 - self.e * cos_psi)
        # Reference velocity
        ref_vx = -self.a * dpsi * self.cos_i * sin_psi
        ref_vy = self.a * dpsi * sqrt(1 - self.e**2) * cos_psi
        ref_vz = self.a * self.sin_i * dpsi * sin_psi
        # Spacecraft velocity
        sc_vx = self.cos_lambda[sc] * ref_vx - self.sin_lambda[sc] * ref_vy
        sc_vy = self.sin_lambda[sc] * ref_vx + self.cos_lambda[sc] * ref_vy
        sc_vz = ref_vz
        # Stack coordinates
        return numpy.column_stack((sc_vx, sc_vy, sc_vz))

    def compute_spacecraft_acceleration(self, sc, t=None):
        """Compute acceleration of spacecraft `sc` at time `t`."""
        if t is None:
            pos = self.spacecraft_positions[sc]
        else:
            pos = self.compute_spacecraft_position(sc, t)
        # Spacecraft acceleration
        a3_dist3 = float(self.a**3) / norm(pos)**3
        return -self.n**2 * pos * a3_dist3[:, numpy.newaxis]

    def compute_spacecraft_proper_time(self, sc, t=None):
        """Computed according to Eq. (7) from [1].

        If `t` is None, we use `self.t` and optimize the computation by reusing the pre-computed
        eccentric anomalies for these times.

            [1] Pireaux, Time scales in LISA, CQG 24, 2271, 2007.
        """
        if t is None:
            t = self.t
            sin_psi = self.sin_psi[sc]
        else:
            sin_psi = sin(self.compute_eccentric_anomaly(sc, t))
        # Proper time deviation
        return -1.5 * self.gr_const * (t - self.tinit) \
            - 2 * self.gr_const * (self.e / self.n) * (sin_psi - sin(self.psi_init[sc]))

    def compute_deriv_spacecraft_proper_time(self, sc, t=None):
        """Compute the derivative of the proper time w.r.t. to TCB.

        This is computed using a leading order expansion in the eccentricity e.

        Returns:
            The quantity `dtau/dt - 1`.
        """
        if t is None:
            dpsi = self.dpsi[sc]
            cos_psi = self.cos_psi[sc]
        else:
            psi = self.compute_eccentric_anomaly(sc, t)
            cos_psi = cos(psi)
            dpsi = self.n / (1 - self.e * cos_psi)
        # Compute proper time deviation
        return -(3 + self.e * cos_psi) / (2 * self.n) * self.gr_const * dpsi


class EqualArmlengthOrbits(Orbits):
    """Orbit generator based on equal-armlength orbits, see e.g., [1].

    This assumes that the orbital period is one astronomical year.

    This means that:

        G * M_Sun = aR**3 * barycenter_angular_velocity**2,

    with `a` the semi-major axis and `barycenter_angular_velocity` = 2 * pi / ASTRONOMICAL_YEAR.

        [1] Cornish, LISA Response function, Phys. Rev. D 67, 022001, 2003, Eq. A6.
    """
    def __init__(self, L=2.5E9, a=ASTRONOMICAL_UNIT, lambda1=0, m_init1=0, **kwargs):
        """Initialize an orbit generator for a set of equal-armlength orbits.

        Args:
           L: mean inter-spacecraft distance, in m
           a: semi-major axis for an orbital period of 1 yr, in m
           lambda1: longitude of periastron for spacecraft 1, in rad
           m_init1: mean anomaly at tinit for spacecraft 1, in rad
           **kwargs: all other args from `Orbits`
        """
        super().__init__(**kwargs)

        self.a = float(a)
        self.L = float(L)
        self.m_init1 = float(m_init1)
        self.lambda1 = float(lambda1)

        self.init_orbital_parameters()

    def init_orbital_parameters(self):
        """Pre-compute orbital parameters on the `self.t` time grid."""
        logger.info("Initializing orbital parameters")

        self.e = self.L / (2 * self.a) / sqrt(3)

        self.n = 2 * pi / ASTRONOMICAL_YEAR
        self.theta = {sc: (sc - 1) * 2 * pi / 3 for sc in self.SC_INDICES}
        self.beta = {sc: self.theta[sc] + self.lambda1 for sc in self.SC_INDICES}
        self.cos_beta = {sc: cos(self.beta[sc]) for sc in self.SC_INDICES}
        self.sin_beta = {sc: sin(self.beta[sc]) for sc in self.SC_INDICES}
        self.mbar, self.cos_mbar, self.sin_mbar = self.compute_mbar()

        self.gr_const = (self.n * self.a / c)**2

    def compute_mbar(self, t=None):
        """Computes `mbar`, the BCRS angle of the constellation center of mass, its sine and cosine.

        Returns:
            3-tuple (mbar, cos(mbar), sin(mbar)).
        """
        if t is None:
            t = self.t
        # Compute m_bar
        mbar = self.n * (t - self.tinit) + self.m_init1 + self.lambda1
        return (mbar, cos(mbar), sin(mbar))

    def compute_spacecraft_position(self, sc, t=None):
        """Compute analitically the position of spacecraft `sc` at time `t` in the BCRS.

        Returns:
            3-tuple (x_position, y_position, z_position).
        """
        if t is None:
            mbar = self.mbar
            cos_mbar = self.cos_mbar
            sin_mbar = self.sin_mbar
        else:
            mbar, cos_mbar, sin_mbar = self.compute_mbar(t)
        # Compute positions
        sc_x = self.a * cos_mbar + self.a * self.e * (sin_mbar * cos_mbar * self.sin_beta[sc] \
                - (1 + sin_mbar**2) * self.cos_beta[sc])
        sc_y = self.a * sin_mbar + self.a * self.e * (sin_mbar * cos_mbar * self.cos_beta[sc] \
                - (1 + cos_mbar**2) * self.sin_beta[sc])
        sc_z = -self.a * self.e * sqrt(3) * cos(mbar - self.beta[sc])
        # Stack coordinates
        return numpy.column_stack((sc_x, sc_y, sc_z))

    def compute_spacecraft_velocity(self, sc, t=None):
        """Compute analytically the velocity of spacecraft `sc` at time `t` in the BCRS.

        These are the time derivatives of the positions.

        Returns:
            3-tuple (x_velocity, y_velocity, z_velocity).
        """
        if t is None:
            mbar = self.mbar
            cos_mbar = self.cos_mbar
            sin_mbar = self.sin_mbar
        else:
            mbar, cos_mbar, sin_mbar = self.compute_mbar(t)
        # Compute velocities
        sc_vx = -self.a * self.n * sin_mbar + self.a * self.e * self.n * ((cos_mbar**2 - sin_mbar**2) \
            * self.sin_beta[sc] - 2 * sin_mbar * cos_mbar * self.cos_beta[sc])
        sc_vy = self.a * self.n * cos_mbar + self.a * self.e * self.n * ((cos_mbar**2 - sin_mbar**2) \
            * self.cos_beta[sc] + 2 * sin_mbar * cos_mbar * self.sin_beta[sc])
        sc_vz = self.a * self.e * self.n * sqrt(3) * sin(mbar - self.beta[sc])
        # Stack coordinates
        return numpy.column_stack((sc_vx, sc_vy, sc_vz))

    def compute_spacecraft_acceleration(self, sc, t=None):
        """Compute analytically the acceleration of spacecraft `sc` at time `t` in the BCRS.

        These are the time derivatives of the positions.

        Returns:
            3-tuple (x_velocity, y_velocity, z_velocity).
        """
        if t is None:
            mbar = self.mbar
            cos_mbar = self.cos_mbar
            sin_mbar = self.sin_mbar
        else:
            mbar, cos_mbar, sin_mbar = self.compute_mbar(t)
        # Compute velocities
        sc_ax = -self.a * self.n**2 * cos_mbar - 4 * self.a * self.e * self.n**2 \
            * (sin_mbar * cos_mbar * self.sin_beta[sc] + (0.5 - sin_mbar**2) * self.cos_beta[sc])
        sc_ay = -self.a * self.n**2 * sin_mbar - 4 * self.a * self.e * self.n**2 \
            * (sin_mbar * cos_mbar * self.cos_beta[sc] + (0.5 - cos_mbar**2) * self.sin_beta[sc])
        sc_az = self.a * self.e * self.n**2 * sqrt(3) * cos(mbar - self.beta[sc])
        # Stack coordinates
        return numpy.column_stack((sc_ax, sc_ay, sc_az))

    def compute_spacecraft_proper_time(self, sc, t=None):
        """Compute the difference between the proper time and the TCB.

        This is computed using a leading order expansion in the eccentricity e.

        Returns:
            The quantity (tau - tau_0) - (t - t_0).
        """
        if t is None:
            t = self.t
            mbar = self.mbar
        else:
            mbar, _, _ = self.compute_mbar(t)
        # Compute proper time deviation
        return -self.gr_const * (1.5 * (t - self.tinit) \
            + 2 * self.e / self.n * (sin(mbar - self.beta[sc]) - sin(self.m_init1 - self.theta[sc])))

    def compute_deriv_spacecraft_proper_time(self, sc, t=None):
        """Compute the derivative of the proper time w.r.t. to TCB.

        This is computed using a leading order expansion in the eccentricity e.

        Returns:
            The quantity `dtau/dt - 1`.
        """
        if t is None:
            t = self.t
            mbar = self.mbar
        else:
            mbar, _, _ = self.compute_mbar(t)
        # Compute proper time deviation
        return -self.gr_const * (1.5 + 2 * self.e * cos(mbar - self.beta[sc]))


class InterpolatedOrbits(Orbits):
    """Orbit generator based on interpolated time series of spacecraft positions.

    We use spline interpolation of order 1 to 5 (left as a parameter) to interpolate the spacecraft
    positions, and use the analytical derivatives of the splines to compute velocities and
    accelerations.
    """
    def __init__(self, t, spacecraft_positions, interp_order=5, ext='raise', check_input=True, **kwargs):
        """Initialize an orbit generator from arrays of spacecraft positions.

        Args:
            t: array of times [s]
            spacecraft_positions: array of spacecraft positions of shape (t, sc, coordinate) [m]
            interp_order: interpolation order to be used, must be one of 1, 2, 3, 4, 5
            ext: extrapolation mode for elements not in the interval defined by the knot sequence
            check_input: whether to check that input contains only finite numbers -- disabling may give
                a performance gain, but may result in problems (crashes, non-termination or invalid results)
                if input file contains infinities or NaNs
            **kwargs: all other args from `Orbits`
        """
        super().__init__(**kwargs)

        self.interp_t = numpy.sort(t)
        self.spacecraft_positions = numpy.asarray(spacecraft_positions)
        self.interp_order = int(interp_order)
        self.ext = str(ext)
        self.check_input = bool(check_input)

        # Check t and spacecraft_positions' shapes
        self.check_shapes()

        interpolate = lambda x: scipy.interpolate.InterpolatedUnivariateSpline(
            self.interp_t, x,
            k=self.interp_order,
            ext=self.ext,
            check_finite=self.check_input
        )

        # Compute spline interpolation for positions
        logger.debug("Computing spline interpolation for spacecraft positions")
        self.interp_x = {sc: interpolate(self.spacecraft_positions[:, sc - 1, 0]) for sc in self.SC_INDICES}
        self.interp_y = {sc: interpolate(self.spacecraft_positions[:, sc - 1, 1]) for sc in self.SC_INDICES}
        self.interp_z = {sc: interpolate(self.spacecraft_positions[:, sc - 1, 2]) for sc in self.SC_INDICES}

        # Compute derivatives of spline objects for spacecraft velocities
        logger.debug("Computing spline derivatives for spacecraft velocities")
        self.interp_vx = {sc: self.interp_x[sc].derivative() for sc in self.SC_INDICES}
        self.interp_vy = {sc: self.interp_y[sc].derivative() for sc in self.SC_INDICES}
        self.interp_vz = {sc: self.interp_z[sc].derivative() for sc in self.SC_INDICES}

        # Compute derivatives of spline objects for spacecraft accelerations
        logger.debug("Computing spline derivatives for spacecraft accelerations")
        self.interp_ax = {sc: self.interp_vx[sc].derivative() for sc in self.SC_INDICES}
        self.interp_ay = {sc: self.interp_vy[sc].derivative() for sc in self.SC_INDICES}
        self.interp_az = {sc: self.interp_vz[sc].derivative() for sc in self.SC_INDICES}

        logger.debug("Computing spline interpolation for spacecraft proper times")
        self.interp_dtau = {}
        self.interp_tau = {}
        self.tau_0 = {}
        for sc in self.SC_INDICES:
            pos_norm = numpy.linalg.norm(self.spacecraft_positions[:, sc - 1], axis=-1)
            v_squared = self.interp_vx[sc](self.interp_t)**2 \
                + self.interp_vy[sc](self.interp_t)**2 \
                + self.interp_vz[sc](self.interp_t)**2
            dtau = -0.5 * (SUN_SCHWARZSCHILD_RADIUS / pos_norm + v_squared / c**2)
            self.interp_dtau[sc] = interpolate(dtau)
            self.interp_tau[sc] = self.interp_dtau[sc].antiderivative()
            self.tau_0[sc] = self.interp_tau[sc](self.tinit)

    def check_shapes(self):
        """Check array shapes for `t` and `spacecraft_positions`.

        We check that `t` is of shape (N), and `spacecraft_positions` of shape (N, 3, 3).

        Raises:
            ValueError if the shapes are invalid.
        """
        if len(self.interp_t.shape) != 1:
            raise ValueError(f"time array has shape {self.interp_t.shape}, must be (N).")

        size = self.interp_t.shape[0]
        if len(self.spacecraft_positions.shape) != 3 or \
           self.spacecraft_positions.shape[0] != size or \
           self.spacecraft_positions.shape[1] != 3 or \
           self.spacecraft_positions.shape[2] != 3:
            raise ValueError(f"spacecraft position array has shape {self.spacecraft_positions.shape}, "
                             f"expected ({size}, 3, 3).")

    def compute_spacecraft_position(self, sc, t=None):
        if t is None:
            t = self.t

        sc_x = self.interp_x[sc](t)
        sc_y = self.interp_y[sc](t)
        sc_z = self.interp_z[sc](t)
        return numpy.column_stack((sc_x, sc_y, sc_z))

    def compute_spacecraft_velocity(self, sc, t=None):
        if t is None:
            t = self.t

        sc_vx = self.interp_vx[sc](t)
        sc_vy = self.interp_vy[sc](t)
        sc_vz = self.interp_vz[sc](t)
        return numpy.column_stack((sc_vx, sc_vy, sc_vz))

    def compute_spacecraft_acceleration(self, sc, t=None):
        if t is None:
            t = self.t

        sc_ax = self.interp_ax[sc](t)
        sc_ay = self.interp_ay[sc](t)
        sc_az = self.interp_az[sc](t)
        return numpy.column_stack((sc_ax, sc_ay, sc_az))

    def compute_spacecraft_proper_time(self, sc, t=None):
        """Numerically integrated according to Eq. (4) from [1].

        Choosing the lower bound of the integral at `t0` implies that clocks are
        synchronized at `t0`.

            [1] Pireaux, Time scales in LISA, CQG 24, 2271, 2007.

        Returns:
            The quantity (tau - tau_0) - (t - t_0).
        """
        if t is None:
            t = self.t

        return self.interp_tau[sc](t) - self.tau_0[sc]

    def compute_deriv_spacecraft_proper_time(self, sc, t=None):
        """Numerically integrated according to Eq. (4) from [1].

            [1] Pireaux, Time scales in LISA, CQG 24, 2271, 2007.

        Returns:
            The quantity dtau/dt - 1.
        """
        if t is None:
            t = self.t

        return self.interp_dtau[sc](t)


class ESAOrbits(InterpolatedOrbits):
    """Orbit generator based on an external ESA ASCII-formatted orbit file.

    We use conventional ESA 3D-orbit text files as input.
    The structure of such input files is the following:

        - col. 0: time in MJD
        - col. 1-3: position of spacecraft 1, in km
        - col. 4-6: velocity of spacecraft 1, in km/s
        - col. 7-9: position of spacecraft 2, in km
        - col. 10-12: velocity of spacecraft 2, in km/s
        - col. 13-15: position of spacecraft 3, in km
        - col. 16-18: velocity of spacecraft 3, in km/s

    """
    def __init__(self, filename, mjd_init=None, skiprows=3, **kwargs):
        """Initialize an orbit generator from an ESA 3D-orbit text file.

        Args:
            filename: path to input file
            mjd_init: this variable defines the reference epoch (tinit=0). Its value needs to be between
               the minimum and maximum values of the MJD time from the input file. If None, it is set to
               the smallest integer larger than the minimal value of the MJD times from the input file.
            skiprows: number of header rows to skip when reading input file
            **kwargs: all other args from `InterpolatedOrbits`
        """
        self.filename = str(filename)
        self.skiprows = int(skiprows)

        # Load ESA orbit file
        logger.info("Reading ESA orbit file '%s'", self.filename)
        logger.debug("Skipping %d rows", self.skiprows)
        file_data = numpy.loadtxt(self.filename, skiprows=self.skiprows)
        self.check_file_format(file_data)

        # Check and set `mjd_init`
        # `mjd_init` is set by the user to translate origin of time
        mjd_min = numpy.min(file_data[:, 0])
        mjd_max = numpy.max(file_data[:, 0])
        if mjd_init is None:
            self.mjd_init = float(mjd_min)
        else:
            if mjd_init < mjd_min or mjd_init > mjd_max:
                raise ValueError(f"invalid mjd_init {mjd_init}, should be between {mjd_min} and {mjd_max}.")
            self.mjd_init = float(mjd_init)

        # We convert days (in file) to seconds (in `InterpolatedOrbits`)
        # and translate times using `mjd_init`
        t = (file_data[:, 0] - self.mjd_init) * (24 * 60 * 60)

        # `tinit` is set to zero, meaning that it is implicitely equal to user-defined `mjd_init`
        # Also means that `tinit` plays the role of `t0` in other classes
        tinit = 0

        # Reshape spacecraft position array
        equatorial_positions = numpy.stack((file_data[:, 1:4], file_data[:, 7:10], file_data[:, 13:16]), axis=1)
        # Convert from km (in file) to meters (in `InterpolatedOrbits`)
        equatorial_positions *= 1E3
        # Convert from equatorial coordinates (in file) to ecliptic coordinates (in `InterpolatedOrbits`)
        # The conversion uses the obliquity of the ecliptic (84381".406 from IAU 2006)
        # To be changed to LISA Constant's `obliquity` constant when v1.2 is released
        obliquity = 84381.406 / (60 * 60) * (2 * numpy.pi / 360)
        to_ecliptic = numpy.array([
            [1, 0, 0],
            [0, numpy.cos(obliquity), -numpy.sin(obliquity)],
            [0, numpy.sin(obliquity), numpy.cos(obliquity)]
        ])
        ecliptic_positions = numpy.einsum('ijk,kl->ijl', equatorial_positions, to_ecliptic)

        super().__init__(t, ecliptic_positions, ext='raise', tinit=tinit, **kwargs)

    @staticmethod
    def check_file_format(file_data):
        """Check ESA orbit file format.

        We check that the array is of shape (N, 19).

        Args:
            file_data: result of `numpy.readtxt()`

        Raises:
            ValueError if the orbit file is invalid.
        """
        if len(file_data.shape) != 2 or file_data.shape[1] != 19:
            raise ValueError(f"invalid ESA orbit file format, got {file_data.shape}, expected (N, 19).")

class ResampledOrbits(InterpolatedOrbits):
    """Orbit generator based on resampling of an existing orbit file.

    We use spline interpolation to resample an existing orbit file to another sampling rate.
    """
    def __init__(self, orbits, **kwargs):
        """Initialize an orbit generator from an existing orbit file.

        Args:
            orbits: path to orbit file
            **kwargs: all other args from `InterpolatedOrbits`
        """
        self.orbits_path = str(orbits)

        # Load ESA orbit file
        logger.info("Reading orbit file '%s'", self.orbits_path)
        t, spacecraft_positions = self.read_orbit_file()

        with h5py.File(self.orbits_path, 'r') as orbitf:
            self.original_attrs = dict(orbitf.attrs)

        super().__init__(t, spacecraft_positions, ext='extrapolate', **kwargs)

    def read_orbit_file(self):
        """Read orbit file in the correct format.

        Returns:
            Tuple (t, spacecraft_positions) of arrays of times [s] and spacecraft positions [m]
            with shape (t, sc, coordinate).

        Raises:
            ValueError if the orbit file's version is not supported.
        """
        with h5py.File(self.orbits_path, 'r') as orbitf:
            if 'version' not in orbitf.attrs:
                raise ValueError(f"cannot read version of orbit file '{self.orbits_path}'.")
            orbits_version = orbitf.attrs['version']

            if orbits_version == '1.0':
                logger.debug("Using orbit file version 1.0")
                sc_1 = numpy.stack((orbitf['tcb/sc_1'][coord] for coord in ['x', 'y', 'z']), axis=-1)
                sc_2 = numpy.stack((orbitf['tcb/sc_2'][coord] for coord in ['x', 'y', 'z']), axis=-1)
                sc_3 = numpy.stack((orbitf['tcb/sc_3'][coord] for coord in ['x', 'y', 'z']), axis=-1)
                spacecraft_positions = numpy.stack((sc_1, sc_2, sc_3), axis=1)
                return orbitf['tcb/t'], spacecraft_positions

            raise ValueError(f"unsupported orbit file version '{orbits_version}'")
