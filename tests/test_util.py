import pytest
from wordle.util import get_info, hard_most_consistent

def test_get_info():
    assert get_info('crane', 'stain') == [0,0,1,0,2]
    assert get_info('aaaaa', 'aaaaa') == [1,1,1,1,1]
    assert get_info('aaaaa', 'bbbbb') == [0,0,0,0,0]
    assert get_info('abcde', 'edcba') == [2,2,1,2,2]
    assert get_info('abcde', 'abcdf') == [1,1,1,1,0]
    
def test_hard_mode_consistent():
    word = 'crane'
    previous_guess = 'brain'
    assert hard_most_consistent(word, 'crabs', previous_guess)==False
    assert hard_most_consistent(word, 'trane', previous_guess)==True