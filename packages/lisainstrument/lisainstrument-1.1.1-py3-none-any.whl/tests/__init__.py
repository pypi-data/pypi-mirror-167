#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test setup functions."""

import os


def teardown_module(_):
    """Remove test measurement file after all tests are executed."""

    try:
        os.remove('measurements.h5')
    except FileNotFoundError:
        pass
