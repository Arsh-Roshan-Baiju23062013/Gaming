destinations = (
    ("Tokyo", ("Cool & Sunny", "$800", "Shibuya Crossing")),
    ("Paris", ("Romantic & Breezy", "$650", "Eiffel Tower")),
    ("New York", ("Busy & Bright", "$400", "Times Square")),
    ("Dubai", ("Hot & Golden", "$550", "Burj Khalifa"))
)

def travel_game():
    print(" Welcome to the Bahubali Travel Planner, Arsh!")
    
    while True:
        print("\nAvailable Destinations:")
        for i, city in enumerate(destinations, 1):
            print(f"{i}. {city[0]}")
        print("5. Exit Game")

        choice = input("\nWhere would you like to go? (Enter 1-5): ")

        if choice == '5':
            print("Safe travels!")
            break
        if choice.isdigit() and 1 <= int(choice) <= 4:
            index = int(choice) - 1
            city_data = destinations[index]
            city_name = city_data[0]
            weather, cost, spot = city_data[1]

            print(f"\n Trip Details for {city_name}")
            print(f" Weather: {weather}")
            print(f" Flight:  {cost}")
            print(f" Must-See: {spot}")
            print("-" * 30)
        else:
            print("only take a choice from the menu please.")

travel_game()