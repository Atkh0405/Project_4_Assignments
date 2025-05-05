DAYS_PER_YEAR= 365
HOURS_PER_DAY = 24
MIN_PER_HOUR= 60
SEC_PER_MIN= 60

def main():

    total_seconds = DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN

    print(f"There are {total_seconds} seconds in a year!")

main()