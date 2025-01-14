def say_hello(name):
    if not isinstance(name, str):
        raise ValueError("The name must be a string")
    print("Hello, " + name)


say_hello("VS Code")
