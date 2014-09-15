from nose.tools import assert_equal

from UnraidMediaHandler.BLL import lcm


def test_lcm():
	assert_equal(lcm.lcmm([10, 16, 24]), 240)
	assert_equal(lcm.lcmm([6, 13, 22, 24]), 0)
	assert_equal(lcm.lcmm([12, 15, 25]), 0)
