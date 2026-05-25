"""Password stars"""
def main():
    password = get_password()

    display_password(password)


def display_password(password: str):
    print("*" * len(password))


def get_password() -> str:
    password = input("Enter a password: ")
    return password

main()