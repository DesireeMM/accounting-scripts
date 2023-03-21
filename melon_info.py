"""Print out all the melons in our inventory."""


from melons import melon_dict 


def print_melon_data(melon_dict):
    """Print each melon with corresponding attribute information."""

    for name, values in melon_dict.items():
        print(name.upper())

        for trait, value in values.items():
            print(f'{trait}: {value}')