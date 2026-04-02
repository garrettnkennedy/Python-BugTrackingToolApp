import json
import os
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
def save_to_json(bugReports):
    with open("bugReports.json", "w") as file:#w means write mode which creates the file if it doesnt exist and overwrites it if it does, this line of code also closes the file automatically when done 
        json.dump(bugReports, file, indent=4)#this code saves the python data in bugReports to a JSON file and indent=4 is just for formatting to make it look better

def load_from_json():
    try:
        with open("bugReports.json", "r") as file:#r means read mode
            return json.load(file)#the difference between the load here and the .dump above is the direction, .dump is from python to the file and .load is from the file to python.
    except FileNotFoundError:
        return []

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

def find_bug_by_title(bugReports, title):
    return next((bug for bug in bugReports if bug["title"] == title), None) #None is the default value if nothing is found.

def main():
    title = "none"#variables cannot be empty so I have a placeholder.
    description = "none"
    severity = "none"
    status = "none"
    if os.path.exists("bugReports.json"):
        bugReports = load_from_json()
        reset = input("bugReports.json already exists, you can type \"reset\" to clear all previously existing data or press Enter to continue: ")
        
        if reset.lower() == "reset":
            bugReports = []
            save_to_json(bugReports)
    else:
        bugReports = []#if the bugReports.json exists and the user did not enter reset then it skils both the if reset == "reset": and the else: allowing the bugReports = load_from_json() below to run.

    bugReports = load_from_json()
    userSelection = "none"
    viewBugSelection = "none"
    print("Hello this is a Bug Tracking Tool Simulation.")
    while userSelection.lower() != "exit":
        userSelection = input("Type \"Add\" to add a bug report, type \"View Bug\" to view the current bug reports, and type \"Change Status\" to change the contents of a bug report. Type \"Exit\" to end the program.\n")
        if userSelection.lower() == "add":
            bug = get_bug_info(bugReports)
            bugReports.append(bug)
            save_to_json(bugReports)
            print("bug report added")
        elif userSelection.lower() == "view bug":
            if has_bug_reports(bugReports):
                display_bug_titles(bugReports)
                viewBugSelection = input("Please select a bug report to display.")
                matching_bug = find_bug_by_title(bugReports, viewBugSelection)
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

                title_of_bug_report_to_change = input("Enter the title of the bug report whose status you want to change.")

                matching_bug = find_bug_by_title(bugReports, title_of_bug_report_to_change)#matching_bug points to the same bug report in bugReports, so changes to it can change the status of the bug report in bugReports
                new_status = get_valid_input("Enter new status: ")
                matching_bug["status"] = new_status
                save_to_json(bugReports)
                print("Status changed successfully")
                    
main()