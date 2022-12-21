"""
Use this decorator to measuring execution program time.
"""

import datetime


def get_execution_time(inner_funct):
    def wrapper(*args, **kwargs) -> dict:
        """
        This wrapper measure inner program execution time
        and return this time and result inner function.
        :return: dictionary with two keys:
        inner_funct_result - Result inner function
        execution_time Inner function execution time
        in microseconds.
        """

        # Create program start time timestamp.
        start_time = datetime.datetime.now()

        # Run inner function and return its function result.
        inner_funct_result = inner_funct(*args, **kwargs)

        # Get program end time timestamp.
        end_time = datetime.datetime.now()
        execution_time = end_time - start_time

        # Get quantity microsecond from execution_time.
        execution_time = execution_time.microseconds

        return {
            'inner_funct_result': inner_funct_result,
            'execution_time': execution_time
        }

    return wrapper

