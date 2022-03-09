
def display(message, is_warning=False):
    if is_warning:
        print("WARNING:", message)
    else:
        print("INFO:", message)


def say_hello():
    print("Hello")


def print_text(text: str) -> str:
    return 1

print_text(1)