def greet(name):
    print(f"Hello, {name}!")

name = input("Enter your name (or press Enter for default): ") or "User"
greet(name)