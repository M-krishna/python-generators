def ship_control():
    while True:
        value = yield
        if value == "UP":
            yield "Going UP"
        elif value == "DOWN":
            yield "Going DOWN"
        elif value == "LEFT":
            yield "Going LEFT"
        elif value == "RIGHT":
            yield "Going RIGHT"
        else:
            yield "Invalid"

# Initialize the generator
control = ship_control()

# Start the generator
next(control)

while True:
    user_input = input("Where to do go? ")
    if user_input == "EXIT":
        control.close()
        break
    else:
        msg = control.send(user_input)
        print(msg)
        next(control)