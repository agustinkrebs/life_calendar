from datetime import datetime

import pytest

from get_row_column_and_remainder_days import get_row_column_and_remainder_days


@pytest.mark.parametrize(
    "date, expected",
    [
        (datetime(1997, 8, 22), (1, 0, 1)),
        (datetime(2024, 8, 12), (27, 51, 0)),
        (datetime(2024, 8, 19), (27, 52, 0)),
        (datetime(2024, 8, 20), (27, 52, 1)),
        (datetime(2024, 8, 21), (28, 0, 0)),
        (datetime(2024, 8, 28), (28, 1, 0)),
        (datetime(2024, 8, 29), (28, 1, 1)),
        (datetime(2025, 8, 20), (28, 52, 0)),
        (datetime(2025, 8, 21), (29, 0, 0)),
        (datetime(2025, 8, 22), (29, 0, 1)),
        (datetime(2025, 8, 28), (29, 1, 0)),
        (datetime(2026, 8, 28), (30, 1, 0)),
        (datetime(2027, 8, 28), (31, 1, 0)),
    ],
)
def test_get_row_column_and_remainder_days(date, expected):
    assert get_row_column_and_remainder_days(date) == expected
