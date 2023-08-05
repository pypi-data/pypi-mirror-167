#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test the usage of frequency plans."""

import numpy as np
import pytest

from h5py import File
from scipy.interpolate import interp1d
from lisainstrument import Instrument


def _consistent_locking_beatnotes(instru, fplan=None):
    """Check that TPS locking beatnotes are consistent with ``fplan``.

    We check that locking beatnotes are equal up to machine precision.

    Args:
        instru (:class:`lisainstrument.Instrument`): instrument object
        fplan (dict or None): dictionary of locking beatnotes [Hz] or None to read fplan file

    Returns:
        (bool) Whether the locking beatnotes are valid.
    """
    # Read fplan file
    if fplan is None:
        with File(instru.fplan_file, 'r') as fplanf:
            t = np.arange(fplanf.attrs['size']) * fplanf.attrs['dt']
            if instru.lock_config == 'N1-12':
                fplan = {
                    '13': interp1d(t, -fplanf[instru.lock_config]['rfi_12'][:] * 1E6)(instru.physics_t),
                    '31': interp1d(t, fplanf[instru.lock_config]['isi_31'][:] * 1E6)(instru.physics_t),
                    '32': interp1d(t, -fplanf[instru.lock_config]['rfi_31'][:] * 1E6)(instru.physics_t),
                    '21': interp1d(t, fplanf[instru.lock_config]['isi_21'][:] * 1E6)(instru.physics_t),
                    '23': interp1d(t, fplanf[instru.lock_config]['rfi_23'][:] * 1E6)(instru.physics_t),
                }
            elif instru.lock_config == 'N1-21':
                fplan = {
                    '23': interp1d(t, fplanf[instru.lock_config]['rfi_23'][:] * 1E6)(instru.physics_t),
                    '32': interp1d(t, fplanf[instru.lock_config]['isi_32'][:] * 1E6)(instru.physics_t),
                    '31': interp1d(t, fplanf[instru.lock_config]['rfi_31'][:] * 1E6)(instru.physics_t),
                    '12': interp1d(t, fplanf[instru.lock_config]['isi_12'][:] * 1E6)(instru.physics_t),
                    '13': interp1d(t, -fplanf[instru.lock_config]['rfi_12'][:] * 1E6)(instru.physics_t),
                }
            elif instru.lock_config == 'N4-12':
                fplan = {
                    '13': interp1d(t, -fplanf[instru.lock_config]['rfi_12'][:] * 1E6)(instru.physics_t),
                    '31': interp1d(t, fplanf[instru.lock_config]['isi_31'][:] * 1E6)(instru.physics_t),
                    '32': interp1d(t, -fplanf[instru.lock_config]['rfi_31'][:] * 1E6)(instru.physics_t),
                    '23': interp1d(t, fplanf[instru.lock_config]['isi_23'][:] * 1E6)(instru.physics_t),
                    '21': interp1d(t, fplanf[instru.lock_config]['isi_21'][:] * 1E6)(instru.physics_t),
                }
    # Check locking beatnotes
    if instru.lock_config == 'N1-12':
        return np.all([
            np.allclose(instru.tps_rfi_carrier_offsets['13'], fplan['13']),
            np.allclose(instru.tps_isi_carrier_offsets['31'], fplan['31']),
            np.allclose(instru.tps_rfi_carrier_offsets['32'], fplan['32']),
            np.allclose(instru.tps_isi_carrier_offsets['21'], fplan['21']),
            np.allclose(instru.tps_rfi_carrier_offsets['23'], fplan['23']),
        ])
    if instru.lock_config == 'N1-21':
        return np.all([
            np.allclose(instru.tps_rfi_carrier_offsets['23'], fplan['23']),
            np.allclose(instru.tps_isi_carrier_offsets['32'], fplan['32']),
            np.allclose(instru.tps_rfi_carrier_offsets['31'], fplan['31']),
            np.allclose(instru.tps_isi_carrier_offsets['12'], fplan['12']),
            np.allclose(instru.tps_rfi_carrier_offsets['13'], fplan['13']),
        ])
    if instru.lock_config == 'N4-12':
        return np.all([
            np.allclose(instru.tps_rfi_carrier_offsets['13'], fplan['13']),
            np.allclose(instru.tps_isi_carrier_offsets['31'], fplan['31']),
            np.allclose(instru.tps_rfi_carrier_offsets['32'], fplan['32']),
            np.allclose(instru.tps_isi_carrier_offsets['23'], fplan['23']),
            np.allclose(instru.tps_isi_carrier_offsets['21'], fplan['21']),
        ])
    raise ValueError(f"unsupported lock configuration '{instru.lock_config}'")

def test_static_fplan():
    """Test the default static set of locking beatnotes."""

    # Check fplan initialization
    instru = Instrument(size=100, fplan='static')
    static = {
        '12': 8E6, '23': 9E6, '31': 10E6,
        '13': -8.2E6, '32': -8.5E6, '21': -8.7E6,
    }
    for mosa in instru.MOSAS:
        assert instru.fplan[mosa] == static[mosa]

    # Check locking beatnotes
    instru = Instrument(size=100, lock='N1-12', fplan='static')
    instru.simulate()
    instru.write(mode='w')
    assert _consistent_locking_beatnotes(instru, static)
    instru = Instrument(size=100, lock='N1-21', fplan='static')
    instru.simulate()
    instru.write(mode='w')
    assert _consistent_locking_beatnotes(instru, static)
    instru = Instrument(size=100, lock='N4-12', fplan='static')
    instru.simulate()
    instru.write(mode='w')
    assert _consistent_locking_beatnotes(instru, static)

def test_static_fplan_valid_with_all_lock_configs():
    """Check that 'static' fplan is valid for all lock configs.

    We check that all beatnotes are between 5 and 25 MHz (and negative)
    for all locking configurations, using the default static set of locking
    beatnotes.
    """
    for primary in Instrument.MOSAS:
        for topology in Instrument.LOCK_TOPOLOGIES:
            instru = Instrument(size=100, lock=f'{topology}-{primary}', fplan='static')
            instru.disable_all_noises()
            instru.simulate()
            instru.write(mode='w')

            for mosa in instru.MOSAS:
                assert np.all(5E6 <= np.abs(instru.isi_carriers[mosa]))
                assert np.all(5E6 <= np.abs(instru.isi_usbs[mosa]))
                assert np.all(5E6 <= np.abs(instru.rfi_carriers[mosa]))
                assert np.all(5E6 <= np.abs(instru.rfi_usbs[mosa]))
                assert np.all(np.abs(instru.isi_carriers[mosa]) <= 25E6)
                assert np.all(np.abs(instru.isi_usbs[mosa]) <= 25E6)
                assert np.all(np.abs(instru.rfi_carriers[mosa]) <= 25E6)
                assert np.all(np.abs(instru.rfi_usbs[mosa]) <= 25E6)

def test_constant_equal_fplan():
    """Test a user-defined constant equal fplan."""

    # Check fplan initialization
    instru = Instrument(size=100, fplan=42.0)
    for mosa in instru.MOSAS:
        assert instru.fplan[mosa] == 42.0

def test_constant_unequal_fplan():
    """Test a user-defined constant unequal fplan."""

    # Check fplan initialization
    fplan = {
        '12': 8.1E6, '23': 9.2E6, '31': 10.3E6,
        '13': 1.4E6, '32': -11.6E6, '21': -9.5E6,
    }
    instru = Instrument(size=100, lock='N1-12', fplan=fplan)
    for mosa in instru.MOSAS:
        assert instru.fplan[mosa] == fplan[mosa]

    # Check locking beatnotes
    instru = Instrument(size=100, lock='N1-12', fplan=fplan)
    instru.simulate()
    instru.write(mode='w')
    assert _consistent_locking_beatnotes(instru, fplan)
    instru = Instrument(size=100, lock='N1-21', fplan=fplan)
    instru.simulate()
    instru.write(mode='w')
    assert _consistent_locking_beatnotes(instru, fplan)
    instru = Instrument(size=100, lock='N4-12', fplan=fplan)
    instru.simulate()
    instru.write(mode='w')
    assert _consistent_locking_beatnotes(instru, fplan)

def test_varying_equal_fplan():
    """Test a user-defined time-varying equal fplan."""

    # Check fplan initialization
    fplan = np.random.uniform(5E6, 25E6, size=400)
    instru = Instrument(size=100, fplan=fplan)
    for mosa in instru.MOSAS:
        assert np.all(instru.fplan[mosa] == fplan)

    # Check locking beatnotes
    fplan = {mosa: fplan for mosa in Instrument.MOSAS}
    instru = Instrument(size=100, lock='N1-12', fplan=fplan)
    instru.simulate()
    instru.write(mode='w')
    assert _consistent_locking_beatnotes(instru, fplan)
    instru = Instrument(size=100, lock='N1-21', fplan=fplan)
    instru.simulate()
    instru.write(mode='w')
    assert _consistent_locking_beatnotes(instru, fplan)
    instru = Instrument(size=100, lock='N4-12', fplan=fplan)
    instru.simulate()
    instru.write(mode='w')
    assert _consistent_locking_beatnotes(instru, fplan)

def test_varying_unequal_fplan():
    """Test a user-defined time-varying unequal fplan."""

    # Check fplan initialization
    fplan = {
        mosa: np.random.uniform(5E6, 25E6, size=400)
        for mosa in Instrument.MOSAS
    }
    instru = Instrument(size=100, fplan=fplan)
    for mosa in instru.MOSAS:
        assert np.all(instru.fplan[mosa] == fplan[mosa])

    # Check locking beatnotes
    instru = Instrument(size=100, lock='N1-12', fplan=fplan)
    instru.simulate()
    instru.write(mode='w')
    assert _consistent_locking_beatnotes(instru, fplan)
    instru = Instrument(size=100, lock='N1-21', fplan=fplan)
    instru.simulate()
    instru.write(mode='w')
    assert _consistent_locking_beatnotes(instru, fplan)
    instru = Instrument(size=100, lock='N4-12', fplan=fplan)
    instru.simulate()
    instru.write(mode='w')
    assert _consistent_locking_beatnotes(instru, fplan)

def test_keplerian_fplan_1_1():
    """Test standard Keplerian fplan file v1.1."""

    # Check fplan file with standard lock configs
    for primary in Instrument.MOSAS:
        for topology in Instrument.LOCK_TOPOLOGIES:
            instru = Instrument(size=100, lock=f'{topology}-{primary}', fplan='tests/keplerian-fplan-1-1.h5')

    # Should raise an error for non-standard lock config
    with pytest.raises(ValueError):
        Instrument(size=100, lock='six', fplan='tests/keplerian-fplan-1-1.h5')
    with pytest.raises(ValueError):
        lock = {'12': 'cavity', '13': 'cavity', '21': 'distant', '31': 'distant', '23': 'adjacent', '32': 'adjacent'}
        Instrument(size=100, lock=lock, fplan='tests/keplerian-fplan-1-1.h5')

    # Check locking beatnotes
    instru = Instrument(size=100, lock='N1-12', fplan='tests/keplerian-fplan-1-1.h5')
    instru.simulate()
    instru.write(mode='w')
    assert _consistent_locking_beatnotes(instru)
    instru = Instrument(size=100, lock='N1-21', fplan='tests/keplerian-fplan-1-1.h5')
    instru.simulate()
    instru.write(mode='w')
    assert _consistent_locking_beatnotes(instru)
    instru = Instrument(size=100, lock='N4-12', fplan='tests/keplerian-fplan-1-1.h5')
    instru.simulate()
    instru.write(mode='w')
    assert _consistent_locking_beatnotes(instru)

def test_esa_trailing_fplan_1_1():
    """Test standard ESA trailing fplan file v1.1."""

    # Check fplan file with standard lock configs
    for primary in Instrument.MOSAS:
        for topology in Instrument.LOCK_TOPOLOGIES:
            instru = Instrument(size=100, lock=f'{topology}-{primary}', fplan='tests/esa-trailing-fplan-1-1.h5')

    # Should raise an error for non-standard lock config
    with pytest.raises(ValueError):
        Instrument(size=100, lock='six', fplan='tests/esa-trailing-fplan-1-1.h5')
    with pytest.raises(ValueError):
        lock = {'12': 'cavity', '13': 'cavity', '21': 'distant', '31': 'distant', '23': 'adjacent', '32': 'adjacent'}
        Instrument(size=100, lock=lock, fplan='tests/esa-trailing-fplan-1-1.h5')

    # Check locking beatnotes
    instru = Instrument(size=100, lock='N1-12', fplan='tests/esa-trailing-fplan-1-1.h5')
    instru.simulate()
    instru.write(mode='w')
    assert _consistent_locking_beatnotes(instru)
    instru = Instrument(size=100, lock='N1-21', fplan='tests/esa-trailing-fplan-1-1.h5')
    instru.simulate()
    instru.write(mode='w')
    assert _consistent_locking_beatnotes(instru)
    instru = Instrument(size=100, lock='N4-12', fplan='tests/esa-trailing-fplan-1-1.h5')
    instru.simulate()
    instru.write(mode='w')
    assert _consistent_locking_beatnotes(instru)

def test_offset_freqs():
    """Test that offset frequencies are correctly set for unlocked lasers."""

    # Check that default set works for 'six' lock config
    instru = Instrument(size=100, lock='six', offset_freqs='default')
    instru.disable_all_noises()
    instru.simulate()
    instru.write(mode='w')
    for mosa in instru.MOSAS:
        assert np.all(5E6 <= np.abs(instru.isi_carriers[mosa]))
        assert np.all(5E6 <= np.abs(instru.isi_usbs[mosa]))
        assert np.all(5E6 <= np.abs(instru.rfi_carriers[mosa]))
        assert np.all(5E6 <= np.abs(instru.rfi_usbs[mosa]))
        assert np.all(np.abs(instru.isi_carriers[mosa]) <= 25E6)
        assert np.all(np.abs(instru.isi_usbs[mosa]) <= 25E6)
        assert np.all(np.abs(instru.rfi_carriers[mosa]) <= 25E6)
        assert np.all(np.abs(instru.rfi_usbs[mosa]) <= 25E6)

    # Check that unlocked laser frequency offsets are correctly set
    offset_freqs = {
        '12': 8.1E6, '23': 9.2E6, '31': 10.3E6,
        '13': 1.4E6, '32': -11.6E6, '21': -9.5E6,
    }
    instru = Instrument(size=100, lock='six', offset_freqs=offset_freqs)
    instru.simulate()
    instru.write(mode='w')
    for mosa in instru.MOSAS:
        assert instru.local_carrier_offsets[mosa] == offset_freqs[mosa]

    # Check that frequency offsets are only set on unlocked lasers
    instru = Instrument(size=100, lock='N1-12', offset_freqs=offset_freqs)
    instru.disable_all_noises()
    instru.simulate()
    instru.write(mode='w')
    assert instru.local_carrier_offsets['12'] == offset_freqs['12']
    instru = Instrument(size=100, lock='N1-23', offset_freqs=offset_freqs)
    instru.disable_all_noises()
    instru.simulate()
    instru.write(mode='w')
    assert instru.local_carrier_offsets['23'] == offset_freqs['23']
