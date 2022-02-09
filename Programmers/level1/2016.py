a, b = 5, 24

weeks = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

days = sum(months[:a - 1]) + b
_, week = divmod(days, 7)

answer = weeks[week - 1]
print(answer)