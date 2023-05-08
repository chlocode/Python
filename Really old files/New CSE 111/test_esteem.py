import pytest
from esteem import positive_score, negative_score

def test_positive_score():
    assert positive_score("a", "b")

pytest.main(["-v", "--tb=line", "-rN", __file__])