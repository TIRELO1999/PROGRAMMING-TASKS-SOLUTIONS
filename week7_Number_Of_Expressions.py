"""

***************************** PROBLEM **********************************************************
Given a list of integers and a target result, count the number of ways in
which we can add + or - operators between the integers such that the
expression that is formed is equal to the target result.
Example:
Given numbers [1, 2, 2, 3, 1] and target result 3, we can form three expressions:
• 1 + 2 + 2 - 3 + 1 = 3
• 1 + 2 - 2 + 3 - 1 = 3
• 1 - 2 + 2 + 3 - 1 = 3
Therefore the answer is 3.
************************************************************************************************

=================================== Clarification questions ======================================
Q: What result should be returned if the list contains a single number?
A: No operators can be added in this case, so the only expression that can be formed is the
given number itself. Return 1 if the number is equal to the result, 0 otherwise.
Q: What result should be returned if the list contains no numbers?
A: The result should be zero, since no expressions can be formed.
Q: How long can the list be?
A: It may contain up to 30 numbers.
==================================================================================================

=============================== CODING WITH CLIFFORD =============================================

"""

def main():
    numbers = [1, 2, 2, 3, 1]
    target_sum = 3
    print("With the set of integers ' {0} ', we can operate {1} times using operations '+' and '-' to optain the sum {2}"
          " ".format(numbers,count_expressions(numbers,target_sum),target_sum))
def count_expressions(numbers, target_result):
    def count(index, partial_result):
        """
        Counts the number of expressions equal to `target_result`,
        given that the first `index` operators have been assigned,
        thus the left part of the expression is equal to `partial_result`.
        """
        if index == len(numbers):
            # We formed a full expression. Count it if we hit the target.
            if partial_result == target_result:
                return 1
            return 0
        # For the operator before `numbers[index]`, we have two options:
        # Add the `+` sign:
        count_add = count(index + 1, partial_result + numbers[index])
        # Add the `- `sign:

        count_sub = count(index + 1, partial_result-numbers[index])
        # Each option may yield some valid expressions. Sum up the counters.
        return count_add + count_sub
    first_index = 1
    partial_result = numbers[0]
    return count(first_index, partial_result)

main()



















# ========================================================== CODING WITH CLIFFORD =============================================================