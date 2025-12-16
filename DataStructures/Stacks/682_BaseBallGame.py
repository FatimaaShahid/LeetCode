class Solution:
    def calPoints(self, operations: List[str]) -> int:

        record = []
        for operand in operations:
            if operand == "D":
                record.append(2*record[-1])
            elif operand == "C":
                record.pop(-1)
            elif operand == "+":
                record.append(record[-1]+record[-2])
            else:
                record.append(int(operand))
        return sum(record)


        