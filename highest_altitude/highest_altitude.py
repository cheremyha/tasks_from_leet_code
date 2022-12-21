"""
Solution for task:
https://leetcode.com/problems/find-the-highest-altitude/
"""

from typing import List


class Solution(object):
    def max_altitude(self, gain: List[int]) -> int:
        """
        We don't use @staticmethod but create
        entity to use this method
        :param gain: List[int]
        :return: int
        """
        altitude = 0
        max_altitude = altitude

        for difference in gain:
            altitude += difference
            if altitude > max_altitude:
                max_altitude = altitude
            print('Logger: current max_altitude == {}'.format(max_altitude))

        print('Logger: Result max_altitude == {}'.format(max_altitude))
        return max_altitude


