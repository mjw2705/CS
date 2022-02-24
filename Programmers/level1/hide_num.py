phone_numbers = "01033334444", "027778888"

for phone_number in phone_numbers:
    number = '*' * len(phone_number[:-4])
    answer = number + phone_number[-4:]
    print(answer)