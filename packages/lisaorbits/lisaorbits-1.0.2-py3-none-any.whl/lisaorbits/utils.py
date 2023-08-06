#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Utility functions.

This module provides utility functions for usual linear algebra operations on Numpy arrays.

Authors:
    Jean-Baptiste Bayle <j2b.bayle@gmail.com>
"""

import numpy


def dot(a, b):
    """Dot product on the last axis."""
    return numpy.einsum('ij, ij->i', a, b)

def norm(a):
    """Norm on the last axis."""
    return numpy.linalg.norm(a, axis=-1)
