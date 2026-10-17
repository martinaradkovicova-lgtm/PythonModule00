def ft_count_harvest_recursive():
    days_until_harvest = input("Days until harvest: ")

    def print_days(i, days_until_harvest):
        if int(i) > int(days_until_harvest):
            print("Harvest time!")
            return
        print(f"Day {i}")
        print_days(int(i + 1), days_until_harvest)

    print_days(1, days_until_harvest)
