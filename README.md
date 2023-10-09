# AirBnB Console

The AirBnB Console is a command-line interface (CLI) designed to manage objects for a simplified version of the AirBnB website. It serves as the foundation for subsequent steps in the project, including HTML/CSS templating, database storage, API development, and front-end integration.

## Command Interpreter

The command interpreter allows users to perform various operations on objects within the project, including creating, retrieving, updating, and deleting instances. It mimics the functionality of a shell but is tailored to our specific use-case.

### Basic Commands

- **create**: Creates a new instance of a specified class, saves it to the JSON file, and prints its unique identifier.

- **show**: Displays the string representation of an instance based on the class name and ID.

- **destroy**: Deletes an instance based on the class name and ID, saving the change to the JSON file.

- **all**: Prints string representations of all instances, filtered by class name if specified.

- **update**: Updates an instance based on the class name and ID, adding or modifying an attribute.

## Execution

### Interactive Mode

To run the AirBnB Console in interactive mode, use the following command:

```bash
$ ./console.py
(hbnb) 

In this mode, you can enter commands directly and receive immediate feedback.

Non-Interactive Mode
The console can also be used in non-interactive mode, where commands are provided through input streams. For example:

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 

Supported Commands
The AirBnB Console supports the following commands:

EOF: Exit the program.
help: Display help information.
quit: Exit the program.
Getting Started
Clone this repository to your local machine.
Ensure you have Python 3.8.5 or higher installed.
Navigate to the project directory.
Run the console using ./console.py.


