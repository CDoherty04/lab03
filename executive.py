from history import History


def get_commands():
    """Takes user input for the input file and converts it into a list of commands"""

    while True:
        # Repeats the prompt until a valid file is given

        try:
            file_name = input("Name of the input file: ")

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

    def run(self):
        """Acts as the main method"""
        pass
