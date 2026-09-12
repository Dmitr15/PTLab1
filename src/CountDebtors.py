# -*- coding: utf-8 -*-
from Types import DataType


class CountDebtors:
    def __init__(self, data: DataType) -> None:
        self.data: DataType = data

    def calc(self) -> int:
        count = 0
        for student in self.data:
            debts = 0
            for _, score in self.data[student]:
                if score < 61:
                    debts += 1
            if debts == 2:
                count += 1
        return count
