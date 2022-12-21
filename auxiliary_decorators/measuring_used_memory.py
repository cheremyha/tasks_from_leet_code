"""
Use this decorator to measuring used memory by program.
"""

import resource


def get_used_memory(inner_funct):
    def wrapper(*args, **kwargs) -> dict:
        """
        This wrapper measure used memory by inner function
        and return this quantity memory and result inner function.
        :return: dictionary with two keys:
        inner_funct_result - Result inner function
        memory_used - Quantity memory used by inner function.
        """
        # Run inner function and return its function result.
        inner_funct_result = inner_funct(*args, **kwargs)

        # Get quantity used memory
        memory_used = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        # Cast bytes into Megabytes.
        memory_used /= 1024 ** 2

        return {
            'inner_funct_result': inner_funct_result,
            'memory_used': memory_used
        }

    return wrapper

