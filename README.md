# Git Command Runner in Subdirectories
This Python script allows you to execute a Git command in all subdirectories within the current working directory. It captures and displays the output and errors of each command execution.

## Features
- Prompts the user for a Git command.
- Iterates through all subdirectories in the current directory.
- Executes the Git command in each subdirectory.
- Displays the standard output and error messages for each command execution.
- Returns to the original directory after processing each subdirectory.

## Requirements
- Python 3.x
- Git installed on your system

## Installation
1. Clone this repository or download the script file.
2. Ensure you have Python 3.x and Git installed on your system.

## Usage
1. Navigate to the directory containing the script.
2. Run the script using Python:
    ```sh
    python run_git_command_in_subdirs.py
    ```
3. When prompted, type your desired Git command (e.g., `status`, `pull`, `fetch`, etc.).

## Example
If you want to run `git status` in all subdirectories, you would proceed as follows:
1. Execute the script:
    ```sh
    python run_git_command_in_subdirs.py
    ```
2. When prompted, type:
    ```sh
    status
    ```
The script will then iterate through all subdirectories and run `git status`, displaying the output for each directory.
