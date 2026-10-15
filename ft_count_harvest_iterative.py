def ft_count_harvest_iterative():
    days_until_harvest = input("Days until harvest: ")
    for i in range(1, int(days_until_harvest) + 1):
        print("Day " + str(i))
    print("Harvest time!")
