def generate_report(report_name):

    try:

        if not report_name:
            raise ValueError("Report name is required.")

        print("Generating report:", report_name)

        return "Report generated successfully."

    except Exception as error:

        return f"Task failed: {error}"
