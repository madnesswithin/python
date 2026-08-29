def ft_count_harvest_recursive():
    def count_day(day, total):
        if day > total:
            print("Harvest time!")
            return
        print(f"Day {day}")
        count_day(day + 1, total)

    days = int(input("Days until harvest: "))
    count_day(1, days)
