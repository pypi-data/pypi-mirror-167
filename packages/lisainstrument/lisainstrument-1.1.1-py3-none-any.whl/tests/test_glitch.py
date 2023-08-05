#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test reading of glitch files."""

import numpy as np
from pytest import approx
from h5py import File
from lisaconstants import c
from lisainstrument import Instrument


def test_no_glitches():
    """Test that we can simulate no glitches."""

    instru = Instrument(size=100, glitches=None)
    instru.disable_all_noises()

    assert instru.glitch_file is None
    for mosa in instru.MOSAS:
        assert instru.glitch_tms[mosa] == 0
        assert instru.glitch_lasers[mosa] == 0

    instru.simulate()
    instru.write(mode='w')

    for mosa in instru.MOSAS:
        assert instru.local_carrier_fluctuations[mosa] == approx(0)
        assert instru.local_tmi_carrier_fluctuations[mosa] == approx(0)
        assert instru.local_tmi_usb_fluctuations[mosa] == approx(0)

def test_glitch_file_1_0():
    """Test that we can read test-mass and laser glitches from files v1.0.

    Test glitch file can be generated using LISA Glitch and the following script.

    from lisaglitch import ShapeletGlitch
    path = 'tests/glitch-1-0.h5'
    ShapeletGlitch(beta=2, quantum_n=1, inj_point='tm_12', t_inj=10.0, size=200).write(path, mode='w')
    ShapeletGlitch(beta=1, quantum_n=2, inj_point='tm_23', t_inj=0.0).write(path)
    ShapeletGlitch(beta=3, quantum_n=2, inj_point='tm_31', t_inj=5.0).write(path)
    ShapeletGlitch(beta=4, quantum_n=1, inj_point='laser_12', t_inj=0.0).write(path)
    ShapeletGlitch(beta=4, quantum_n=3, inj_point='laser_31', t_inj=0.0).write(path)
    """

    glitch_file = 'tests/glitch-1-0.h5'
    glitchf = File(glitch_file, 'r')

    instru = Instrument(
        size=glitchf.attrs['size'],
        t0=glitchf.attrs['t0'],
        dt=glitchf.attrs['dt'],
        physics_upsampling=1,
        aafilter=None,
        lock='six',
        glitches=glitch_file,
        orbits='tests/keplerian-orbits-1-0-2.h5')
    instru.disable_all_noises()

    assert instru.glitch_file is glitch_file
    for mosa in instru.MOSAS:

        # Missing datasets should be zero
        tm_dataset = f'tm_{mosa}'
        if tm_dataset in glitchf:
            assert instru.glitch_tms[mosa] == approx(glitchf[tm_dataset][:])
        else:
            assert instru.glitch_tms[mosa] == 0

        laser_dataset = f'laser_{mosa}'
        if laser_dataset in glitchf:
            assert instru.glitch_lasers[mosa] == approx(glitchf[laser_dataset][:])
        else:
            assert instru.glitch_lasers[mosa] == 0

    instru.simulate()
    instru.write(mode='w')

    for mosa in instru.MOSAS:

        laser_dataset = f'laser_{mosa}'
        if laser_dataset in glitchf:
            assert approx(instru.local_carrier_fluctuations[mosa]) == \
                glitchf[laser_dataset][:]
        else:
            assert approx(instru.local_carrier_fluctuations[mosa]) == 0

        tm_dataset = f'tm_{mosa}'

        if tm_dataset in glitchf:
            assert approx(instru.local_tmi_carrier_fluctuations[mosa], abs=1E-6) == \
                instru.local_carrier_fluctuations[mosa] \
                + 2 * glitchf[tm_dataset][:] / c \
                * (instru.central_freq + instru.local_tmi_carrier_offsets[mosa])
        else:
            assert approx(instru.local_tmi_carrier_fluctuations[mosa]) == \
                instru.local_carrier_fluctuations[mosa]

        if tm_dataset in glitchf:
            assert approx(instru.local_tmi_usb_fluctuations[mosa], abs=1E-6) == \
                instru.local_usb_fluctuations[mosa] \
                + 2 * glitchf[tm_dataset][:] / c \
                * (instru.central_freq + instru.local_tmi_usb_offsets[mosa])
        else:
            assert approx(instru.local_tmi_usb_fluctuations[mosa]) == \
                instru.local_usb_fluctuations[mosa]

def test_glitch_file_1_1():
    """Test that we can read test-mass and laser glitches from files v1.1.

    Test glitch file can be generated using LISA Glitch and the following script.

    from lisaglitch import ShapeletGlitch
    path = 'tests/glitch-1-1.h5'
    ShapeletGlitch(beta=2, quantum_n=1, inj_point='tm_12', t_inj=10.0, size=200).write(path, mode='w')
    ShapeletGlitch(beta=1, quantum_n=2, inj_point='tm_23', t_inj=0.0).write(path)
    ShapeletGlitch(beta=3, quantum_n=2, inj_point='tm_31', t_inj=5.0).write(path)
    ShapeletGlitch(beta=4, quantum_n=1, inj_point='laser_12', t_inj=0.0).write(path)
    ShapeletGlitch(beta=4, quantum_n=3, inj_point='laser_31', t_inj=0.0).write(path)
    """

    glitch_file = 'tests/glitch-1-1.h5'
    glitchf = File(glitch_file, 'r')

    instru = Instrument(
        size=glitchf.attrs['size'],
        t0=glitchf.attrs['t0'],
        dt=glitchf.attrs['dt'],
        physics_upsampling=1,
        aafilter=None,
        lock='six',
        glitches=glitch_file,
        orbits='tests/keplerian-orbits-1-0-2.h5')
    instru.disable_all_noises()

    assert instru.glitch_file is glitch_file
    for mosa in instru.MOSAS:

        # Missing datasets should be zero
        tm_dataset = f'tm_{mosa}'
        if tm_dataset in glitchf:
            assert instru.glitch_tms[mosa] == approx(glitchf[tm_dataset][:])
        else:
            assert instru.glitch_tms[mosa] == 0

        laser_dataset = f'laser_{mosa}'
        if laser_dataset in glitchf:
            assert instru.glitch_lasers[mosa] == approx(glitchf[laser_dataset][:])
        else:
            assert instru.glitch_lasers[mosa] == 0

    instru.simulate()
    instru.write(mode='w')

    for mosa in instru.MOSAS:

        laser_dataset = f'laser_{mosa}'
        if laser_dataset in glitchf:
            assert approx(instru.local_carrier_fluctuations[mosa]) == \
                glitchf[laser_dataset][:]
        else:
            assert approx(instru.local_carrier_fluctuations[mosa]) == 0

        tm_dataset = f'tm_{mosa}'

        if tm_dataset in glitchf:
            assert approx(instru.local_tmi_carrier_fluctuations[mosa], abs=1E-6) == \
                instru.local_carrier_fluctuations[mosa] \
                + 2 * glitchf[tm_dataset][:] / c \
                * (instru.central_freq + instru.local_tmi_carrier_offsets[mosa])
        else:
            assert approx(instru.local_tmi_carrier_fluctuations[mosa]) == \
                instru.local_carrier_fluctuations[mosa]

        if tm_dataset in glitchf:
            assert approx(instru.local_tmi_usb_fluctuations[mosa], abs=1E-6) == \
                instru.local_usb_fluctuations[mosa] \
                + 2 * glitchf[tm_dataset][:] / c \
                * (instru.central_freq + instru.local_tmi_usb_offsets[mosa])
        else:
            assert approx(instru.local_tmi_usb_fluctuations[mosa]) == \
                instru.local_usb_fluctuations[mosa]
