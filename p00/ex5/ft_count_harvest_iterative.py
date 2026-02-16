def ft_count_harvest_iterative():
    days_until_harvest = int(input("Days until harvest: "))
    for day in range(days_until_harvest):
        print(f"Day {day + 1}")
    print("Harvest time!")
