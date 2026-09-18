class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for op in operations:
            if op == "C":
                record.pop()
            elif op == "D":
                score = record[-1]
                record.append(int(score * 2))
            elif op == "+":
                prev_1 = record.pop()
                prev_2 = record.pop()
                record.append(prev_2)
                record.append(prev_1)
                record.append(int(prev_1 + prev_2))
            else:
                record.append(int(op))
        
        return sum(record)
        