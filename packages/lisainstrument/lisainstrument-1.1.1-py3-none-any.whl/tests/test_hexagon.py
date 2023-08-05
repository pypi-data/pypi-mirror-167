#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=missing-module-docstring

import os
from lisainstrument import Hexagon


def test_run():
    """Test that simulations can run."""
    hexagon = Hexagon()
    hexagon.simulate()

def test_write():
    """Test that simulations can run and be written."""
    hexagon = Hexagon()
    hexagon.simulate()
    hexagon.write('measurements.h5', mode='w')

    assert os.path.isfile('measurements.h5')
