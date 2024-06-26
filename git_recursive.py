import os
import subprocess
import sys

def run_git_command_in_subdirs():
    git_command = input("Type your Git command: ") # Get the user input for the git command
    print('*' * 75)
    
    current_directory = os.getcwd() # Get the current working directory

    # Collect only directories
    directories = [os.path.join(current_directory, item) for item in os.listdir(current_directory) if os.path.isdir(os.path.join(current_directory, item))]
    multiple_dirs = len(directories) > 1

    # Iterate over directories
    for path in directories:
        print(f'"{path}"')

        os.chdir(path) # Change to the directory

        print('-' * 75)
        print(git_command)

        # Execute the git command and capture the output
        try:
            result = subprocess.run(['git'] + git_command.split(), check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(result.stdout) # Print the standard output

            # Check if there is any error output
            if result.stderr:
                print("Error Output:", file=sys.stderr)
                print(result.stderr, file=sys.stderr)  # Print the standard error to the error stream
        except subprocess.CalledProcessError as e:
            print(f'Error executing Git command: {e}', file=sys.stderr)
            print("Git error output:", file=sys.stderr)
            print(e.stderr, file=sys.stderr)

        # Conditional print based on the number of directories
        if multiple_dirs:
            print('-' * 75)
            print('*' * 75)

        os.chdir(current_directory) # Return to the original directory

if __name__ == '__main__':
    run_git_command_in_subdirs()
