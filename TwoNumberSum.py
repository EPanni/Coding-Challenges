""" Two Number Sum Challenge


  Write a function that takes in a non-empty array of distinct integers and an
  integer representing a target sum. If any two numbers in the input array sum
  up to the target sum, the function should return them in an array, in any
  order. If no two numbers sum up to the target sum, the function should return
  an empty array.


  Note that the target sum has to be obtained by summing two different integers
  in the array; you can't add a single integer to itself in order to obtain the
  target sum.


  You can assume that there will be at most one pair of numbers summing up to
  the target sum.

 Sample Input = [3, 5, -4, 8, 11, 1, -1, 6]
 
 Target Sum  = 10



"""


class TwoNumberSum:
    def __init__(self, array: list, targetSum: int) -> list:
        self.targetSum = targetSum
        self.conj = set(array)

    def two_mumber_sum(self):
        output = []

        for item in self.conj:
            aux = self.targetSum - item

            if aux in self.conj and aux != item:
                if aux not in output or item not in output:
                    output.append(item)
                    output.append(aux)

        return output


if __name__ == "__main__":

    array = [3, 5, -4, 8, 11, 1, -1, 6]
    target_sum = 10
    output = [-1, 11]

    check_condition = TwoNumberSum(array, target_sum).two_mumber_sum()

    print(check_condition.sort() is output.sort())
