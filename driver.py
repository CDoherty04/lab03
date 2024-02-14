"""
Author: Charlie Doherty
KUID: 3115329
Date: 2/13/24
Lab: 03
Last modified: 02/13/24
Purpose: Create linked lists to simulate a browser history

Run driver to execute the program and modify commands.txt to change the terminal's output
"""
import linkedlist
from executive import Executive


def main():
    """Hands the process over to an Executive object"""

    my_exec = Executive()
    my_exec.run()


if __name__ == "__main__":
    """Call stack begins here"""
    main()