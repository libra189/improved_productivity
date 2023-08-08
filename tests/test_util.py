from ..app import util


def test_tax_rate():
    rate = util.tax_rate()
    assert rate == 0.1
