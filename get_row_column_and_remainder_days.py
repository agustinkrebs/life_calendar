from datetime import datetime

BIRTHDAY = datetime(1997, 8, 21)


def get_row_column_and_remainder_days(
    date: datetime | None = None,
) -> tuple[int, int, int]:
    """
    Get the row, column, and remainder days from the BIRTHDAY to the target `date`.

    Args:
        date: The target date.
    """
    # If target_date is not given, use today's date
    target_date = date if date is not None else datetime.now()

    years_passed = target_date.year - BIRTHDAY.year
    current_year_birthday = BIRTHDAY.replace(year=target_date.year)
    if target_date < current_year_birthday:
        years_passed -= 1
        current_year_birthday = BIRTHDAY.replace(year=target_date.year - 1)

    days_in_current_year = (target_date - current_year_birthday).days
    # Calculate the row based on the years passed
    row = years_passed + 1
    # Calculate the column and remainder days
    column = days_in_current_year // 7
    remainder_days = days_in_current_year % 7

    return row, column, remainder_days
