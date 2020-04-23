import pytest

def test_zero_pad():
    records = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ans = zero_pad(records)
    assert len(ans) == 16
