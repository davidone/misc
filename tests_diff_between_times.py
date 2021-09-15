import pytest
import diff_between_times

def test_validate_date():
    val = ('2021-09-15 00:00:00')
    assert diff_between_times.validate_date(None, None, val) == val
    
    with pytest.raises(Exception):
        val = ('2021-09-15 00:')
        assert diff_between_times.validate_date(None, None, val)
    
    since_val = '2021-09-15 00:00:00'
    until_val = '2021-09-15 00:01:00'
    assert diff_between_times.dateDiff(since_val, until_val) == 1
