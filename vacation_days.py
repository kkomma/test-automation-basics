def count_vacation_weeks(year, A, B, W):
    # Define the number of days in each month
    days_in_month = {
        'January': 31, 'February': 28, 'March': 31, 'April': 30,
        'May': 31, 'June': 30, 'July': 31, 'August': 31,
        'September': 30, 'October': 31, 'November': 30, 'December': 31
    }
    # Adjust for leap years
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month['February'] = 29

    # Define the order of days in a week
    days_in_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Generate a list of all days in the year with their respective day names
    all_days = []
    idx = days_in_week.index(W)
    for month in days_in_month:
        for day in range(1, days_in_month[month] + 1):
            all_days.append((month, day, days_in_week[idx]))
            idx = (idx + 1) % 7

    # Find the start and end indices
    start_index = None
    end_index = None

    for i, (month, day, week_day) in enumerate(all_days):
        if month == A and week_day == 'Monday' and start_index is None:
            start_index = i
        if month == B and week_day == 'Sunday':
            end_index = i

    if start_index is None or end_index is None:
        return 0

    # Count the number of full weeks between the start and end dates
    total_days = end_index - start_index + 1
    total_weeks = total_days // 7

    return total_weeks

# Example usage:
year = 2014
A = 'May'
B = 'June'
W = 'Wednesday'
print(count_vacation_weeks(year, A, B, W))  # Should return 7

year = 2015
A = 'January'
B = 'June'
W = 'Thursday'
print(count_vacation_weeks(year, A, B, W))  

year = 2024
A = 'January'
B = 'June'
W = 'Monday'
print(count_vacation_weeks(year, A, B, W))  