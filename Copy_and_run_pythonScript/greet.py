# File: greet.py
import os

def main():
    # Retrieve the USER_NAME from an environment variable, defaulting to "World"
    user_name = os.getenv("USER_NAME", "World")
    # Print a customized greeting message
    print(f"Hello, {user_name}!")

if __name__ == "__main__":
    main()
