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

        # Check gain isn't empty, else raise exception.
        if not gain:
            raise ValueError('The in put gain list is empty but should be empty')

        # The way starts from this altitude by task's condition.
        altitude = 0
        max_altitude = altitude

        for difference in gain:
            altitude += difference
            if altitude > max_altitude:
                max_altitude = altitude
            print('Logger: current max_altitude == {}'.format(max_altitude))

        print('Logger: Result max_altitude == {}'.format(max_altitude))

        return max_altitude


