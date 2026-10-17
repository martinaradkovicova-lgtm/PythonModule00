def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    Seed_type = seed_type.capitalize()
    Seed_type += " seeds"
    if seed_type == "tomato":
        print(f"{Seed_type}: {quantity} {unit} available")
    elif seed_type == "carrot":
        print(f"{Seed_type}: {quantity} {unit} total")
    elif seed_type == "lettuce":
        print(f"Lettuce seeds: covers {quantity} square meters")
    else:
        print(f"{Seed_type}: {quantity} Unknown unit type")
