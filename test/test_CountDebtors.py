# -*- coding: utf-8 -*-
import pytest
from src.Types import DataType
from src.CountDebtors import CountDebtors


class TestCountDebtors:
    @pytest.fixture()
    def dataset(self) -> tuple[DataType, int]:
        data: DataType = {
            "Студент1": [
                ("математика", 60),        # долг
                ("русский язык", 55),      # долг
                ("программирование", 90)
            ],
            "Студент2": [
                ("математика", 30),        # долг
                ("русский язык", 40),      # долг
                ("программирование", 20),  # долг
                ("литература", 100)
            ],
            "Студент3": [
                ("математика", 61),        # не долг (>= 61)
                ("русский язык", 60),      # долг
                ("программирование", 80)
            ],
            "Студент4": [
                ("математика", 100),
                ("русский язык", 90)
            ]
        }
        expected_count = 1
        return data, expected_count

    def test_init(self, dataset: tuple[DataType, int]) -> None:
        counter = CountDebtors(dataset[0])
        assert dataset[0] == counter.data

    def test_calc(self, dataset: tuple[DataType, int]) -> None:
        result = CountDebtors(dataset[0]).calc()
        assert result == dataset[1]

    def test_empty(self) -> None:
        result = CountDebtors({}).calc()
        assert result == 0
