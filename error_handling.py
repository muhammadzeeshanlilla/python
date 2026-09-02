# This function represents one automation task.
def generate_report(report_name):

    # Try to perform the task.
    try:

        # Check whether a report name was provided.
        if not report_name:
            raise ValueError("Report name is required.")

        # Perform the task.
        print("Generating report:", report_name)

        # Return success result.
        return "Report generated successfully"

    # If an error happens, control it here.
    except Exception as error:

        # Return the error message.
        return f"Task failed: {error}"


# Call the task.
result = generate_report("Sales Report")


# Display task result.
print(result)


# Answer
# Generating report: Sales Report
# Report generated successfully

# -------------------------------------------------------------------------

def check_employee_age(age=None):
    
    try:
        if not age:
            raise ValueError("Age is required.")

        if age < 18:
            raise ValueError("Employee must be at least 18 years old.")

        return "Employee age is valid."

    except Exception as error:
        return f"Validation failed: {error}"

result2 = check_employee_age()

print(result2)