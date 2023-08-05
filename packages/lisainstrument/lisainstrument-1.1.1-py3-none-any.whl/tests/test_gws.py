#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test reading of GW response and GW files."""

import numpy as np
from pytest import approx
from h5py import File
from lisainstrument import Instrument


def test_no_gws():
    """Test that we simulate without GWs."""

    instru = Instrument(size=100, gws=None)
    instru.disable_all_noises()

    assert instru.gw_file is None
    for mosa in instru.MOSAS:
        assert instru.gws[mosa] == 0

    instru.simulate()
    instru.write(mode='w')

    for mosa in instru.MOSAS:
        assert instru.distant_carrier_fluctuations[mosa] == approx(0)
        assert instru.distant_usb_fluctuations[mosa] == approx(0)
        assert instru.tps_isi_carrier_fluctuations[mosa] == approx(0)
        assert instru.tps_isi_usb_fluctuations[mosa] == approx(0)
        assert instru.isi_carrier_fluctuations[mosa] == approx(0)
        assert instru.isi_usb_fluctuations[mosa] == approx(0)

def test_dict_of_gws():
    """Test that we pass link responses in a dictionary."""

    responses = {
        mosa: np.random.normal(size=100 * 16)
        for mosa in Instrument.MOSAS
    }

    instru = Instrument(size=100, lock='six', gws=responses)
    instru.disable_all_noises()

    assert instru.gw_file is None
    for mosa in instru.MOSAS:
        assert np.all(instru.gws[mosa] == responses[mosa])

    instru.simulate()
    instru.write(mode='w')

    for mosa in instru.MOSAS:
        assert approx(instru.distant_carrier_fluctuations[mosa]) == \
            -(instru.central_freq + instru.local_carrier_offsets[mosa]) * responses[mosa]
        assert approx(instru.distant_usb_fluctuations[mosa]) == \
            -(instru.central_freq + instru.local_usb_offsets[mosa]) * responses[mosa]
        assert approx(instru.tps_isi_carrier_fluctuations[mosa]) == \
            -(instru.central_freq + instru.local_carrier_offsets[mosa]) * responses[mosa]
        assert approx(instru.tps_isi_usb_fluctuations[mosa]) == \
            -(instru.central_freq + instru.local_usb_offsets[mosa]) * responses[mosa]

def test_gw_file_1_1():
    """Test that we can read GW files v1.1 with orbit files v1.0.2.

    Test GW file can be generated using LISA GW Response and the following script.

        from h5py import File
        from lisagwresponse import GalacticBinary

        orbits = 'tests/keplerian-orbits-1-0-2.h5'
        with File(orbits, 'r') as f:
            t0 = f.attrs['t0'] + 10

        galbin = GalacticBinary(
            A=1.0,
            f=1E-3,
            orbits=orbits,
            t0=t0,
            size=100,
            gw_beta=0, gw_lambda=0,
        )

        galbin.write('tests/gws-1-1.h5')
    """

    gw_file = 'tests/gws-1-1.h5'
    gwf = File(gw_file, 'r')

    instru = Instrument(
        size=100,
        t0=gwf.attrs['t0'],
        dt=gwf.attrs['dt'],
        physics_upsampling=1,
        aafilter=None,
        lock='six',
        gws=gw_file,
        orbits='tests/keplerian-orbits-1-0-2.h5',
        orbit_dataset='tcb/ltt')
    instru.disable_all_noises()

    assert instru.gw_file is gw_file
    for mosa in instru.MOSAS:
        assert instru.gws[mosa] == approx(gwf[f'tcb/l_{mosa}'][:])

    instru.simulate()
    instru.write(mode='w')

    for mosa in instru.MOSAS:
        assert approx(instru.distant_carrier_fluctuations[mosa]) == \
            -(instru.central_freq + instru.local_carrier_offsets[mosa]) * gwf[f'tcb/l_{mosa}'][:]
        assert approx(instru.distant_usb_fluctuations[mosa]) == \
            -(instru.central_freq + instru.local_usb_offsets[mosa]) * gwf[f'tcb/l_{mosa}'][:]
        assert approx(instru.tps_isi_carrier_fluctuations[mosa]) == \
            -(instru.central_freq + instru.local_carrier_offsets[mosa]) * gwf[f'tcb/l_{mosa}'][:]
        assert approx(instru.tps_isi_usb_fluctuations[mosa]) == \
            -(instru.central_freq + instru.local_usb_offsets[mosa]) * gwf[f'tcb/l_{mosa}'][:]

    instru = Instrument(
        size=100,
        t0=gwf.attrs['t0'],
        dt=gwf.attrs['dt'],
        physics_upsampling=1,
        aafilter=None,
        lock='six',
        gws=gw_file,
        orbits='tests/keplerian-orbits-1-0-2.h5',
        orbit_dataset='tps/ppr')
    instru.disable_all_noises()

    assert instru.gw_file is gw_file
    for mosa in instru.MOSAS:
        assert instru.gws[mosa] == approx(gwf[f'tcb/l_{mosa}'][:])

    instru.simulate()
    instru.write(mode='w')

    for mosa in instru.MOSAS:
        assert approx(instru.distant_carrier_fluctuations[mosa]) == \
            -(instru.central_freq + instru.local_carrier_offsets[mosa]) * gwf[f'tps/l_{mosa}'][:]
        assert approx(instru.distant_usb_fluctuations[mosa]) == \
            -(instru.central_freq + instru.local_usb_offsets[mosa]) * gwf[f'tps/l_{mosa}'][:]
        assert approx(instru.tps_isi_carrier_fluctuations[mosa]) == \
            -(instru.central_freq + instru.local_carrier_offsets[mosa]) * gwf[f'tps/l_{mosa}'][:]
        assert approx(instru.tps_isi_usb_fluctuations[mosa]) == \
            -(instru.central_freq + instru.local_usb_offsets[mosa]) * gwf[f'tps/l_{mosa}'][:]

def test_gw_file_2_0_dev():
    """Test that we can read GW files v2.0.dev with orbit files v2.0.

    Test GW file can be generated using LISA GW Response and the following script.

        from h5py import File
        from lisagwresponse import GalacticBinary

        orbits = 'tests/keplerian-orbits-2-0.h5'
        with File(orbits, 'r') as f:
            t0 = f.attrs['t0'] + 10

        galbin = GalacticBinary(
            A=1.0,
            f=1E-3,
            orbits=orbits,
            t0=t0,
            size=100,
            gw_beta=0, gw_lambda=0,
        )

        galbin.write('tests/gws-2-0-dev.h5')
    """

    gw_file = 'tests/gws-2-0-dev.h5'
    gwf = File(gw_file, 'r')

    instru = Instrument(
        size=100,
        t0=gwf.attrs['t0'],
        dt=gwf.attrs['dt'],
        physics_upsampling=1,
        aafilter=None,
        lock='six',
        gws=gw_file,
        orbits='tests/keplerian-orbits-2-0.h5',
        orbit_dataset='tcb/ltt')
    instru.disable_all_noises()

    assert instru.gw_file is gw_file
    for imosa, mosa in enumerate(instru.MOSAS):
        assert instru.gws[mosa] == approx(gwf['tcb/y'][:, imosa])

    instru.simulate()
    instru.write(mode='w')

    for imosa, mosa in enumerate(instru.MOSAS):
        assert approx(instru.distant_carrier_fluctuations[mosa]) == \
            -(instru.central_freq + instru.local_carrier_offsets[mosa]) * gwf['tcb/y'][:, imosa]
        assert approx(instru.distant_usb_fluctuations[mosa]) == \
            -(instru.central_freq + instru.local_usb_offsets[mosa]) * gwf['tcb/y'][:, imosa]
        assert approx(instru.tps_isi_carrier_fluctuations[mosa]) == \
            -(instru.central_freq + instru.local_carrier_offsets[mosa]) * gwf['tcb/y'][:, imosa]
        assert approx(instru.tps_isi_usb_fluctuations[mosa]) == \
            -(instru.central_freq + instru.local_usb_offsets[mosa]) * gwf['tcb/y'][:, imosa]

    instru = Instrument(
        size=100,
        t0=gwf.attrs['t0'],
        dt=gwf.attrs['dt'],
        physics_upsampling=1,
        aafilter=None,
        lock='six',
        gws=gw_file,
        orbits='tests/keplerian-orbits-2-0.h5',
        orbit_dataset='tps/ppr')
    instru.disable_all_noises()

    assert instru.gw_file is gw_file
    for imosa, mosa in enumerate(instru.MOSAS):
        assert instru.gws[mosa] == approx(gwf['tcb/y'][:, imosa])

    instru.simulate()
    instru.write(mode='w')

    for imosa, mosa in enumerate(instru.MOSAS):
        assert approx(instru.distant_carrier_fluctuations[mosa]) == \
            -(instru.central_freq + instru.local_carrier_offsets[mosa]) * gwf['tps/y'][:, imosa]
        assert approx(instru.distant_usb_fluctuations[mosa]) == \
            -(instru.central_freq + instru.local_usb_offsets[mosa]) * gwf['tps/y'][:, imosa]
        assert approx(instru.tps_isi_carrier_fluctuations[mosa]) == \
            -(instru.central_freq + instru.local_carrier_offsets[mosa]) * gwf['tps/y'][:, imosa]
        assert approx(instru.tps_isi_usb_fluctuations[mosa]) == \
            -(instru.central_freq + instru.local_usb_offsets[mosa]) * gwf['tps/y'][:, imosa]
