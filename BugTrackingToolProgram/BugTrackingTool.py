# Here are my instructions for this project, so I dont have to flip through documents to check.
# What It Does:
#•	Allows a user to add bug reports with fields like: title, description, severity, status.
#•	Lists all reported bugs.
#•	Optionally allows updating status (open, resolved).
#Skills Demonstrated:
#•	Documentation of errors (core QA skill)
#•	Working with structured data
#•	Logical thinking
#•	Basic user interface handling (console or simple GUI)
#How to Approach It:
#1.	Start with console input/output.
#2.	Store bugs in a list or dictionary.
#3.	Implement commands: Add bug, view bug, change status.
#4.	Optional: Save to CSV or JSON for persistence.

def main():
    title = "none"#variables cannot be empty so I have a placeholder.
    description = "none"
    severity = "none"
    status = "none"
    userSelection = "none"
    print("Hello this is a Bug Tracking Tool Simulation.")
    while userSelection.lower() != "exit":
        userSelection = input("Type \"Add\" to add a bug report, type \"View Bug\" to view the current bug reports, and type \"change status\" to change the contents of a bug report.\n")
        if userSelection.lower() == "add":
            title = input("type the title of the bug report.")
            description = input("enter the description of the bug")
            severity = input("enter the severity of the bug")
            status = input("enter the status of the bug report")
        elif userSelection.lower() == "view bug":
            pass#since I cant type #temp without having an error saying: Expected indented block, I have to use pass instead as a placeholder.
        elif userSelection.lower() == "change status":
            pass

main()