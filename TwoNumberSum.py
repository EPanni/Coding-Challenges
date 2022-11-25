""" Two Number Sum Challenge"""


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
