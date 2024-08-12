import logging
from lightspeed_lint.linter import Linter
from lightspeed_lint.logger import setup_logging

def main():
    setup_logging('logs/lightspeed_lint.log')
    linter = Linter('/path/to/directory')  # Update path as needed
    linter.run()

    with open('logs/lightspeed_lint.log', 'r') as log_file:
        log_content = log_file.read()
        if "ERROR" in log_content:
            print("Errors found during linting. Here are the details:\n")
            print(log_content)
        else:
            print("Lint checks passed successfully.")

if __name__ == "__main__":
    main()
