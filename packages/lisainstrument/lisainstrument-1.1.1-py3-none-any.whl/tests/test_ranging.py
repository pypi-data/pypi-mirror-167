#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=missing-module-docstring

import numpy as np
from pytest import approx
from lisaconstants import c
from lisainstrument import Instrument


def test_no_prn_ambiguity():
    """Test that we can use MPRs without ambiguities."""

    pprs = {
        '12': 8.33242295, '23': 8.30282196, '31': 8.33242298,
        '13': 8.33159404, '32': 8.30446786, '21': 8.33159402,
    }

    instru = Instrument(size=100, prn_ambiguity=None, orbits=pprs)
    assert instru.prn_ambiguity is None
    instru.disable_clock_noises()
    instru.disable_ranging_noises()
    instru.simulate()
    instru.write(mode='w')
    for mosa in instru.MOSAS:
        assert instru.mprs[mosa][50:] == approx(pprs[mosa])

    # Setting `prn_ambiguity` to 0 is equivalent to using `None`
    instru = Instrument(size=100, prn_ambiguity=0)
    assert instru.prn_ambiguity is None

def test_prn_ambiguity_with_static_orbits():
    """Test that MPRs follow PRN cycle length for static orbits."""

    pprs = {
        '12': 8.33242295, '23': 8.30282196, '31': 8.33242298,
        '13': 8.33159404, '32': 8.30446786, '21': 8.33159402,
    }

    instru = Instrument(size=100, prn_ambiguity=300E3)
    assert instru.prn_ambiguity == approx(300E3)
    instru.disable_clock_noises()
    instru.disable_ranging_noises()
    instru.simulate()
    instru.write(mode='w')
    for mosa in instru.MOSAS:
        assert instru.mprs[mosa][50:] == approx(pprs[mosa] % (300E3 / c))

    instru = Instrument(size=100, prn_ambiguity=100E3)
    assert instru.prn_ambiguity == approx(100E3)
    instru.disable_clock_noises()
    instru.disable_ranging_noises()
    instru.simulate()
    instru.write(mode='w')
    for mosa in instru.MOSAS:
        assert instru.mprs[mosa][50:] == approx(pprs[mosa] % (100E3 / c))

def test_prn_ambiguity_with_esa_orbits():
    """Test that MPRs are below ambiguity for realistic orbits."""

    instru = Instrument(
        size=100, dt=2E5,
        prn_ambiguity=300E3,
        aafilter=None, physics_upsampling=1,
        orbits='tests/esa-trailing-orbits-2-0.h5')

    instru.disable_clock_noises()
    instru.disable_ranging_noises()
    instru.simulate()
    instru.write(mode='w')

    for mosa in instru.MOSAS:
        assert np.all(instru.mprs[mosa][50:] <= 300E3 / c)
