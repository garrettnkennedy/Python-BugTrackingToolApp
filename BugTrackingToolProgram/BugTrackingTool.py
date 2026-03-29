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
def make_sure_titles_are_not_identical(title, bugReports):
    while any(bug["title"] == title for bug in bugReports):
        print("A bug with this title already exists.")
        title = get_valid_input("Please type the title again: ")#it says again in the message because title = get_valid_input("Type the title: ") was already successfully called first inside of def get_bug_info(bugReports): for it to have reached this code
    return title

def get_valid_input(message):
    while True:#loop until return is run.
        user_input = input(message)
        invalidInputChecker = " ".join(user_input.split())#.split seperates words but if there are no words it creates an empty list, while .join combines the elements of a list but if a list is empty it returns an empty string, and a empty string can be checked via the == symbol in the following if statement.

        if invalidInputChecker == "":
            print("Input cannot be empty or just spaces.")
        else:
            return invalidInputChecker
        
def get_bug_info(bugReports):
    title = get_valid_input("Type the title: ")
    title = make_sure_titles_are_not_identical(title, bugReports)

    return {
        "title": title,#since title calls two methods instead of one I cannot call the method within the return statment, instead of having to pass it to a variable called title and use that instead.
        "description": get_valid_input("Enter description: "),
        "severity": get_valid_input("Enter severity: "),
        "status": get_valid_input("Enter status: ")
        }

def display_bug_titles(bugReports):
    if len(bugReports) == 0:
        print("You have not entered any bug reports.")
    else:
        for i, bug in enumerate(bugReports, start=1):
            print(f"{i}. {bug['title']}")

def has_bug_reports(bugReports):
    if len(bugReports) == 0:
        print("You have not entered any bug reports.")
        return False#if it returns False this function/method will not continue and run return True
    return True

def main():
    title = "none"#variables cannot be empty so I have a placeholder.
    description = "none"
    severity = "none"
    status = "none"
    bugReports = []
    userSelection = "none"
    viewBugSelection = "none"
    print("Hello this is a Bug Tracking Tool Simulation.")
    while userSelection.lower() != "exit":
        userSelection = input("Type \"Add\" to add a bug report, type \"View Bug\" to view the current bug reports, and type \"change status\" to change the contents of a bug report.\n")
        if userSelection.lower() == "add":
            bug = get_bug_info(bugReports)
            bugReports.append(bug)
            print("bug report added")
        elif userSelection.lower() == "view bug":
            if has_bug_reports(bugReports):
                display_bug_titles(bugReports)
                viewBugSelection = input("Please select a bug report to display.")
                matching_bug = next((bug for bug in bugReports if bug["title"] == viewBugSelection), None)#None is the default value if nothing is found.
                if matching_bug:
                    print(f"Bug Report: {matching_bug["title"]}")
                    print(matching_bug["description"])
                    print(matching_bug["severity"])
                    print(matching_bug["status"])
                else:
                    print("There is no bug report with that title")
                
        elif userSelection.lower() == "change status":
            if has_bug_reports(bugReports):
                display_bug_titles(bugReports)

main()