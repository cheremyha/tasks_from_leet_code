"""
This code measure execution time
and used memory by max_altitude methods.
"""

from highest_altitude.highest_altitude import Solution
from auxiliary_decorators.measuring_execution_time import get_execution_time
from auxiliary_decorators.measuring_used_memory import get_used_memory


@get_execution_time
@get_used_memory
def get_execution_time_auxiliary():
    # Create Solution entity.
    solution_entity = Solution()
    # Set gain list.
    gain_list = [-4, -3, -2, -1, 4, 3, 2]
    # Get result from method.
    result = solution_entity.max_altitude(gain=gain_list)
    return result


# Call the auxiliary function.
inner_funct_result = get_execution_time_auxiliary()

# Get data from decorators.
inner_funct_result_value = inner_funct_result['inner_funct_result']['inner_funct_result']
inner_funct_used_memory = inner_funct_result['inner_funct_result']['memory_used']
inner_funct_execution_time = inner_funct_result['execution_time']

info_message_str = (
    'Inner funct result value is {0}, program execution time is {1} microseconds' 
    ' and used memory is {2} Mb'
)

info_message_str_for = info_message_str.format(
    inner_funct_result_value,
    inner_funct_execution_time,
    inner_funct_used_memory
)

print(info_message_str_for)

