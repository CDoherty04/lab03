from history import History


def get_commands():
    """Takes user input for the input file and converts it into a list of commands"""

    while True:
        # Repeats the prompt until a valid file is given

        try:
            file_name = input("Name of the input file: ")
            print()

            with open(file_name, "r") as file:
                lines = file.readlines()
            break

        except FileNotFoundError:
            print("Not a valid file, try again")

    # Removes newlines
    lines = [line.strip() for line in lines]
    return lines


class Executive:
    """The class that handles files and function calls"""

    def __init__(self):
        """Initializes the Exec object by getting file input"""

        self._commands = get_commands()
        self.history = History()

    def run(self):
        """Acts as the main method"""

        for command in self._commands:

            match command.split(" ")[0]:

                # Navigates to the given URL
                case "NAVIGATE":
                    self.history.navigate_to(command.split(" ")[1])

                # Reads history
                case "HISTORY":
                    print(self.history.history())

                # Goes forward in the history
                case "FORWARD":
                    self.history.forward()

                # Goes backwards in the history
                case "BACK":
                    self.history.back()

                # Default case
                case _:
                    print("Invalid input, continuing...")
