# This function represents one automation task.
def generate_report(report_name):

    # Show which report is being generated.
    print("Generating report:", report_name)

    # Send the result back to the caller.
    return "Report generated successfully"


# Call the function and pass an argument.
result = generate_report("Sales Report")


# Display the value returned by the function.
print(result)



# /*Answer 
# Generating report: Sales Report
# Report generated successfully
# */


# -----------------------------------------------------------------------------

# This function represents one automation task.
def generate_report2(report_name):

    # Show which report is being generated.
    print("Generating report:", report_name)

    # Send the result back to the caller.
    return report_name


# Call the function and pass an argument.
result2 = generate_report2("Sales Report")


# Display the value returned by the function.
print(result2)


# Answer
# Generating report: Sales Report
# Sales Report


# -----------------------------------------------------------------------------------------------

def generate_report3(report_name):

    # Show which report is being generated.
    print("Generating report:", report_name)

    # Send the result back to the caller.
    return f"Report generated successfully: {report_name}"


# Call the function and pass an argument.
result3 = generate_report3("Sales Report")


# Display the value returned by the function.
print(result3)
