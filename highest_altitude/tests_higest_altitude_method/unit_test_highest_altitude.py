"""
This code implements unit tests for max_altitude method.
Unit test consist of (???) test.
"""


import unittest
from highest_altitude.highest_altitude import Solution


class TestsMaxAltitudeMethod(unittest.TestCase):
    def setUp(self):
        """
        Set gain value from:
        https://leetcode.com/problems/find-the-highest-altitude/
        in attributes.
        """

        # Create Solution entity.
        self.solution_entity = Solution()
        # Set first gain list.
        self.gain_list_first = [-4, -3, -2, -1, 4, 3, 2]
        # Set second gain list.
        self.gain_list_second = [-5, 1, 5, 0, -7]
        # Set second gain list with one broken second element.
        self.gain_list_broken = [-5, '1', 5, 0, -7]
        # Set empty gain.
        self.gain_list_empty = []

    def test_max_altitude_on_leet_code_gains(self):
        """
        This unit tests check max_altitude method on
        two gains from Leetcode.
        We check methods on two true values and
        two borderline values for each.
        For example for 0 value two borderline values
        are -1 and 1.
        """

        # Check left borderline case for gain_list_first.
        self.assertNotEqual(self.solution_entity.max_altitude(gain=self.gain_list_first), -1)
        # Check true value for gain_list_first.
        self.assertEqual(self.solution_entity.max_altitude(gain=self.gain_list_first), 0)
        # Check right borderline case for gain_list_first.
        self.assertNotEqual(self.solution_entity.max_altitude(gain=self.gain_list_first), 1)
        # Check left borderline case for gain_list_second.
        self.assertNotEqual(self.solution_entity.max_altitude(gain=self.gain_list_second), 0)
        # Check true value for gain_list_second.
        self.assertEqual(self.solution_entity.max_altitude(gain=self.gain_list_second), 1)
        # Check right borderline case for gain_list_second.
        self.assertNotEqual(self.solution_entity.max_altitude(gain=self.gain_list_second), 2)

    def test_max_altitude_on_broken_gains(self):
        """
        max_altitude must be raised an exception if
        in put gain_list_second consist not from int
        but consist from str.
        """
        with self.assertRaises(TypeError):
            # Call the max_altitude method, we must get TypeError.
            self.solution_entity.max_altitude(gain=self.gain_list_broken)

    def test_max_altitude_on_empty_gains(self):
        """
        max_altitude must be raised an exception if
        in put gain_list_second is empty.
        """
        with self.assertRaises(ValueError):
            # Call the max_altitude method, we must get ValueError.
            self.solution_entity.max_altitude(gain=self.gain_list_empty)


if __name__ == '__main__':
    unittest.main()
