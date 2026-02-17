def helper_function(days_until_harvest):
    if days_until_harvest != 1:
        helper_function(days_until_harvest - 1)
    print(f"Day {days_until_harvest}")


def ft_count_harvest_recursive():
    days_until_harvest = int(input("Days until harvest: "))
    helper_function(days_until_harvest)
    print("Harvest time!")
