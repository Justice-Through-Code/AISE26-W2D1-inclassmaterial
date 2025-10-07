# Simple command line interface

while True:
    user_input = input("Talk to me! (or say q to quit) ")
    if user_input == 'q':
        break
    print(f"You said: {user_input}")