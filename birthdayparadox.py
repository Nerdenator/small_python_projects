import datetime
from iteration_utilities import duplicates
import random


def generate_birthdays():
    birthday_count = int(input("How many birthdays shall I generate? (Max 100)"))
    if birthday_count > 100:
        print("Please enter a valid number.")
        generate_birthdays()
    else:
        birthday_list = build_birthday_list(birthday_count)
        print(f"Here are {birthday_count} birthdays: ")
        for x in birthday_list:
            s = x.strftime("%b %-d")
            print(s)
        dupes = list(duplicates(birthday_list))  # work smarter, not harder, using someone else's hard work
        for x in dupes:
            s = x.strftime("%b %-d")
            print(f"In this simulation, multiple people have a birthday on {s}.")
        print(f"Generating {birthday_count} random birthdays 100,000 times...")
        if input() == '':
            i = 0
            birthday_lists_list = []
            while i < 100000:
                birthday_lists_list.append(build_birthday_list(birthday_count))
                if i % 10000 == 0:
                    print(f"{i} simulations run...")
                i += 1
            duplicate_birthday_counter = 0
            for birthday_list_item in birthday_lists_list:
                dupes = list(duplicates(birthday_list_item))
                if len(dupes) != 0:
                    duplicate_birthday_counter += 1
                percentage = (duplicate_birthday_counter / 100000) * 100
            print(f"Out of 100,000 simulations of {birthday_count} people, there was a matching birthday in that group "
                  f"{duplicate_birthday_counter} times. This means that {birthday_count} people have"
                  f" a {percentage} % chance of"
                  f"having a matching birthday in their group. That's probably more than you would think!")


def build_birthday_list(birthday_count):
    birthday_list = []
    start = datetime.date(2021, 1, 1)
    end = datetime.date(2021, 12, 31)
    time_between_dates = end - start
    days_between_dates = time_between_dates.days
    i = 0
    while i < birthday_count:
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start + datetime.timedelta(days=random_number_of_days)
        birthday_list.append(random_date)
        i += 1
    return birthday_list


generate_birthdays()
