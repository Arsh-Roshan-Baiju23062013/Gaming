import random

shape_data = {
    "a": ("Circle", "Red"),
    "b": ("Square", "Blue"),
    "c": ("Triangle", "Green")
}

def generate_random_event(key):
    if key in shape_data:
        position = (random.randint(0, 500), random.randint(0, 500))
        shape_info = shape_data[key]
        
        print(f"Key '{key}' pressed!")
        print(f"Drawing a {shape_info[1]} {shape_info[0]} at coordinates {position}.")
        print(f"Tuple data point: {position[0]}x, {position[1]}y\n")
    else:
        print("Key not assigned!")

for _ in range(3):
    random_key = random.choice(["a", "b", "c"])
    generate_random_event(random_key)