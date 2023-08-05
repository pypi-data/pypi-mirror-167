#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=missing-module-docstring

import pytest
from lisainstrument import Instrument


def test_run():
    """Test that simulations can run."""
    instru = Instrument(size=100)
    instru.simulate()
    instru.write(mode='w')

def test_run_no_aafilter():
    """Test that simulations can run with no filter."""
    instru = Instrument(size=100, aafilter=None)
    instru.simulate()
    instru.write(mode='w')

def test_run_no_upsampling():
    """Test that simulations can run with no filter."""
    instru = Instrument(size=100, physics_upsampling=1, aafilter=None)
    instru.simulate()
    instru.write(mode='w')

def test_no_orbit_file():
    """Test that simulations fail with an invalid orbit file."""
    with pytest.raises(FileNotFoundError):
        Instrument(size=100, orbits='tests/nonexistent-orbits.h5')
    with pytest.raises(FileNotFoundError):
        Instrument(size=100, t0=0, orbits='tests/nonexistent-orbits.h5')

def test_keplerian_orbits_1_0_2():
    """Test that simulations can run with Keplerian orbit files v1.0.2."""
    instru = Instrument(size=100, orbits='tests/keplerian-orbits-1-0-2.h5')
    instru.simulate()
    instru.write(mode='w')

def test_esa_orbits_1_0_2():
    """Test that simulations can run with ESA orbit files v1.0.2."""
    instru = Instrument(size=100, orbits='tests/esa-orbits-1-0-2.h5')
    instru.simulate()
    instru.write(mode='w')

def test_keplerian_orbits_2_0():
    """Test that simulations can run with Keplerian orbit files v2.0."""
    instru = Instrument(size=100, orbits='tests/keplerian-orbits-2-0.h5')
    instru.simulate()
    instru.write(mode='w')

def test_esa_trailing_orbits_2_0():
    """Test that simulations can run with ESA trailing orbit files v2.0."""
    instru = Instrument(size=100, orbits='tests/esa-trailing-orbits-2-0.h5')
    instru.simulate()
    instru.write(mode='w')

def test_locking():
    """Test that simulations can run with various lock configurations."""
    # Test six free-running lasers
    instru = Instrument(size=100, lock='six')
    instru.simulate()
    instru.write(mode='w')
    # Test non-swap configurations
    for i in range(1, 6):
        for primary in ['12', '23', '31', '13', '32', '21']:
            instru = Instrument(size=100, lock=f'N{i}-{primary}')
            instru.simulate()
            instru.write(mode='w')
    # Test that any other raises an error
    with pytest.raises(ValueError):
        Instrument(size=100, lock='whatever')
    with pytest.raises(ValueError):
        Instrument(size=100, lock='N7-12')
    with pytest.raises(ValueError):
        Instrument(size=100, lock='N1-67')
