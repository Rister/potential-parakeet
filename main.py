import rich
from rich.prompt import Prompt


def mainloop() -> None:
    while True:
        user_input = Prompt.ask(default="quickhelp").lower()
        if user_input in ["quit", "exit"]:
            break
        elif user_input in ["quickhelp", "qhelp"]:
            rich.print("Quick Help not implemented.")
        else:
            rich.print("Command not recognized...")
            rich.print(f"What is '{user_input}'?")
    rich.print("Bye!")


if __name__ == "__main__":
    mainloop()
