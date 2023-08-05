#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=missing-module-docstring

import os
import numpy as np
from pytest import raises
from h5py import File
from lisainstrument.containers import ForEachObject, ForEachSC, ForEachMOSA


class ForEachAB(ForEachObject):
    """Concrete implementation of ForEachObject for tests."""
    @classmethod
    def indices(cls):
        return ['A', 'B']


def test_init_dictionary():
    """Test that one can initialize a ForEachObject with a dictionary."""

    my_object = ForEachAB({'A': 1, 'B': 2})
    assert my_object['A'] == 1
    assert my_object['B'] == 2

    with raises(KeyError):
        ForEachAB({'A': 1})


def test_init_callable():
    """Test that one can initialize a ForEachObject with a function."""

    my_object = ForEachAB(lambda index: index.lower())
    assert my_object['A'] == 'a'
    assert my_object['B'] == 'b'


def test_init_dataset():
    """Test that one can initialize a ForEachObject with an HDF5 dataset."""

    try:
        with File('test-temp.h5', 'x') as h5file:
            dtype = np.dtype({'names': ['A', 'B'], 'formats': [np.float64, np.float64]})
            h5file.create_dataset('test-dataset', (1, ), dtype=dtype)
            h5file['test-dataset']['A'] = 1
            h5file['test-dataset']['B'] = 2

        with File('test-temp.h5', 'r') as h5file:
            my_object = ForEachAB(h5file['test-dataset'])
            assert my_object['A'] == [1]
            assert my_object['B'] == [2]
    finally:
        os.remove('test-temp.h5')

    try:
        with File('test-temp.h5', 'x') as h5file:
            dtype = np.dtype({'names': ['A'], 'formats': [np.float64]})
            h5file.create_dataset('test-dataset', (1, ), dtype=dtype)
            h5file['test-dataset']['A'] = 1

        with File('test-temp.h5', 'r') as h5file:
            with raises(ValueError):
                my_object = ForEachAB(h5file['test-dataset'])
    finally:
        os.remove('test-temp.h5')


def test_init_scalar():
    """Test that one can initialize a ForEachObject with a scalar."""

    my_object = ForEachAB(42)
    assert my_object['A'] == 42
    assert my_object['B'] == 42


def test_access_item():
    """Test that one can get and set items."""

    my_object = ForEachAB(0)

    my_object['A'] = 1
    assert my_object['A'] == 1
    assert my_object['B'] == 0

    my_object['B'] = 42
    assert my_object['A'] == 1
    assert my_object['B'] == 42


def test_len():
    """Test that one can retreive the length of values."""

    my_object = ForEachAB(0)
    assert len(my_object) == 1

    my_object = ForEachAB({
        'A': range(10),
        'B': range(42),
    })
    assert len(my_object) == 42

    my_object = ForEachAB({
        'A': range(42),
        'B': 1,
    })
    assert len(my_object) == 42


def test_equality():
    """Check that ForEachObject instances are equal when containing identical values."""

    object_1 = ForEachAB({'A': 1, 'B': 2})
    object_2 = ForEachAB({'A': 1, 'B': 2})
    assert object_1 == object_2

    object_2['A'] = 3
    assert object_1 != object_2

    object_1['A'] = 3
    assert object_1 == object_2


def test_addition():
    """Check that we can add two ForEachObject subclasses of the same type, or a scalar."""

    object_1 = ForEachAB({'A': 1, 'B': 2})
    object_2 = ForEachAB({'A': 3, 'B': -4})
    object_3 = ForEachMOSA(0)

    result = object_1 + object_2
    assert result['A'] == 4
    assert result['B'] == -2

    result = object_1 + 10
    assert result['A'] == 11
    assert result['B'] == 12

    result = -5 + object_2
    assert result['A'] == -2
    assert result['B'] == -9

    with raises(TypeError):
        result = object_1 + object_3
    with raises(TypeError):
        result = object_2 + object_3


def test_subtraction():
    """Check that we can subtract two ForEachObject subclasses of the same type, or a scalar."""

    object_1 = ForEachAB({'A': 1, 'B': 2})
    object_2 = ForEachAB({'A': 3, 'B': -4})
    object_3 = ForEachMOSA(0)

    result = object_1 - object_2
    assert result['A'] == -2
    assert result['B'] == 6

    result = object_1 - 10
    assert result['A'] == -9
    assert result['B'] == -8

    result = 10 - object_2
    assert result['A'] == 7
    assert result['B'] == 14

    with raises(TypeError):
        result = object_1 - object_3
    with raises(TypeError):
        result = object_2 - object_3


def test_multiplication():
    """Check that we can multiply two ForEachObject subclasses of the same type, or a scalar."""

    object_1 = ForEachAB({'A': 1, 'B': 2})
    object_2 = ForEachAB({'A': 3, 'B': -4})
    object_3 = ForEachMOSA(0)

    result = object_1 * object_2
    assert result['A'] == 3
    assert result['B'] == -8

    result = object_1 * 2
    assert result['A'] == 2
    assert result['B'] == 4

    result = 10 * object_2
    assert result['A'] == 30
    assert result['B'] == -40

    with raises(TypeError):
        result = object_1 * object_3
    with raises(TypeError):
        result = object_2 * object_3


def test_floor_division():
    """Check that we can apply floor division on two ForEachObject subclasses, or a scalar."""

    object_1 = ForEachAB({'A': 1, 'B': 2})
    object_2 = ForEachAB({'A': 3, 'B': -4})
    object_3 = ForEachMOSA(0)

    result = object_2 // object_1
    assert result['A'] == 3
    assert result['B'] == -2

    result = object_2 // 2
    assert result['A'] == 1
    assert result['B'] == -2

    with raises(TypeError):
        result = object_1 // object_3
    with raises(TypeError):
        result = 20 // object_1


def test_real_division():
    """Check that we can divide two ForEachObject subclasses of the same type, or a scalar."""

    object_1 = ForEachAB({'A': 1, 'B': 2})
    object_2 = ForEachAB({'A': 3, 'B': -4})
    object_3 = ForEachMOSA(0)

    result = object_1 / object_2
    assert result['A'] == 1/3
    assert result['B'] == -1/2

    result = object_1 / 5
    assert result['A'] == 1/5
    assert result['B'] == 2/5

    result = 10 / object_2
    assert result['A'] == 10/3
    assert result['B'] == -10/4

    with raises(TypeError):
        result = object_1 / object_3
    with raises(TypeError):
        result = object_2 / object_3


def test_power():
    """Check that we take the power of a ForEachObject instance."""

    object_1 = ForEachAB({'A': 1, 'B': -2})

    result = object_1**1
    assert result['A'] == 1
    assert result['B'] == -2

    result = object_1**2
    assert result['A'] == 1
    assert result['B'] == 4


def test_transformed():
    """Check that we transformation is correctly applied to ForEachObject instances."""

    my_object = ForEachAB({'A': 1, 'B': 2})
    my_object = my_object.transformed(lambda index, x: 2 * x)
    assert my_object['A'] == 2
    assert my_object['B'] == 4

    my_object = my_object.transformed(lambda index, x: index.lower())
    assert my_object['A'] == 'a'
    assert my_object['B'] == 'b'


def test_abs():
    """Check that we can take the absolute value of ForEachObject instances."""

    my_object = ForEachAB({'A': -1, 'B': 2})
    my_object = abs(my_object)
    assert my_object['A'] == 1
    assert my_object['B'] == 2


def test_neg():
    """Check that we can take the negative value of ForEachObject instances."""

    my_object = ForEachAB({'A': -1, 'B': 2})
    my_object = -my_object
    assert my_object['A'] == 1
    assert my_object['B'] == -2


def test_write():
    """Check that we can write a ForEachObject instance."""

    my_object = ForEachAB({'A': 1, 'B': 2})

    try:
        with File('test-temp.h5', 'x') as h5file:
            my_object.write(h5file, 'test_dataset')

        with File('test-temp.h5', 'r') as h5file:
            assert h5file['test_dataset']['A'] == [1]
            assert h5file['test_dataset']['B'] == [2]
    finally:
        os.remove('test-temp.h5')


def test_sc_indices():
    """Test spacecraft indices."""

    assert ForEachSC.indices() == ['1', '2', '3']

    assert ForEachSC.distant_left_sc('1') == '2'
    assert ForEachSC.distant_left_sc('2') == '3'
    assert ForEachSC.distant_left_sc('3') == '1'

    assert ForEachSC.distant_right_sc('1') == '3'
    assert ForEachSC.distant_right_sc('2') == '1'
    assert ForEachSC.distant_right_sc('3') == '2'

    assert ForEachSC.left_mosa('1') == '12'
    assert ForEachSC.left_mosa('2') == '23'
    assert ForEachSC.left_mosa('3') == '31'

    assert ForEachSC.right_mosa('1') == '13'
    assert ForEachSC.right_mosa('2') == '21'
    assert ForEachSC.right_mosa('3') == '32'


def test_mosa_indices():
    """Test MOSA indices."""

    assert ForEachMOSA.indices() == ['12', '23', '31', '13', '32', '21']

    assert ForEachMOSA.sc('12') == '1'
    assert ForEachMOSA.sc('23') == '2'
    assert ForEachMOSA.sc('31') == '3'
    assert ForEachMOSA.sc('13') == '1'
    assert ForEachMOSA.sc('32') == '3'
    assert ForEachMOSA.sc('21') == '2'

    assert ForEachMOSA.distant_mosa('12') == '21'
    assert ForEachMOSA.distant_mosa('23') == '32'
    assert ForEachMOSA.distant_mosa('31') == '13'
    assert ForEachMOSA.distant_mosa('13') == '31'
    assert ForEachMOSA.distant_mosa('32') == '23'
    assert ForEachMOSA.distant_mosa('21') == '12'

    assert ForEachMOSA.adjacent_mosa('12') == '13'
    assert ForEachMOSA.adjacent_mosa('23') == '21'
    assert ForEachMOSA.adjacent_mosa('31') == '32'
    assert ForEachMOSA.adjacent_mosa('13') == '12'
    assert ForEachMOSA.adjacent_mosa('32') == '31'
    assert ForEachMOSA.adjacent_mosa('21') == '23'


def test_foreachsc_to_foreachmosa():
    """Test that one can turn a ForEachSC instance to a ForEachMOSA instance."""

    my_sc = ForEachSC(lambda sc: 10 * int(sc))
    assert my_sc['1'] == 10
    assert my_sc['2'] == 20
    assert my_sc['3'] == 30

    my_mosa = my_sc.for_each_mosa()
    assert my_mosa['12'] == 10
    assert my_mosa['13'] == 10
    assert my_mosa['21'] == 20
    assert my_mosa['23'] == 20
    assert my_mosa['31'] == 30
    assert my_mosa['32'] == 30


def test_auto_foreachsc_to_foreachmosa():
    """Test that ForEachSC turn automatically into ForEachMOSA during operations."""

    my_sc = ForEachSC(int)
    my_mosa = ForEachMOSA(int)

    my_add_1 = my_sc + my_mosa
    my_add_2 = my_mosa + my_sc
    assert my_add_1 == my_sc.for_each_mosa() + my_mosa
    assert my_add_1 == my_add_2

    my_sub_1 = my_sc - my_mosa
    my_sub_2 = my_mosa - my_sc
    assert my_sub_1 == my_sc.for_each_mosa() - my_mosa
    assert my_sub_1 == -my_sub_2

    my_mult_1 = my_sc * my_mosa
    my_mult_2 = my_mosa * my_sc
    assert my_mult_1 == my_sc.for_each_mosa() * my_mosa
    assert my_mult_1 == my_mult_2


def test_foreachmosa_distant():
    """Test that one can generate a ForEachMOSA instant for distant MOSAs."""

    my_mosa = ForEachMOSA(int)
    assert my_mosa['12'] == 12
    assert my_mosa['13'] == 13
    assert my_mosa['21'] == 21
    assert my_mosa['23'] == 23
    assert my_mosa['31'] == 31
    assert my_mosa['32'] == 32

    distant_mosa = my_mosa.distant()
    assert distant_mosa['12'] == 21
    assert distant_mosa['13'] == 31
    assert distant_mosa['21'] == 12
    assert distant_mosa['23'] == 32
    assert distant_mosa['31'] == 13
    assert distant_mosa['32'] == 23


def test_foreachmosa_adjacent():
    """Test that one can generate a ForEachMOSA instant for adjacent MOSAs."""

    my_mosa = ForEachMOSA(int)
    assert my_mosa['12'] == 12
    assert my_mosa['13'] == 13
    assert my_mosa['21'] == 21
    assert my_mosa['23'] == 23
    assert my_mosa['31'] == 31
    assert my_mosa['32'] == 32

    adjacent_mosa = my_mosa.adjacent()
    assert adjacent_mosa['12'] == 13
    assert adjacent_mosa['13'] == 12
    assert adjacent_mosa['21'] == 23
    assert adjacent_mosa['23'] == 21
    assert adjacent_mosa['31'] == 32
    assert adjacent_mosa['32'] == 31
