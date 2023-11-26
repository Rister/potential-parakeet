import rich
from rich.prompt import Prompt

def mainloop() -> None:
	while True:
		user_input = Prompt.ask(">",default="quickhelp")
		if user_input == "quit":
			break
		elif user_input == "quickhelp":
			rich.print("Quick Help not implemented.")
		else:
			rich.print("Command not recognized...")
	rich.print("Bye!")

if __name__ == "__main__":
	mainloop()