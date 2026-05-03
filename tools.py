def generate_test_cases(task):
    return f"""
    [Test Cases Generated]
    - Validate input fields
    - Check error handling
    - Verify successful flow
    Task: {task}
    """

def debug_issue(task):
    return f"""
    [Debug Suggestions]
    - Check API response codes
    - Validate request payload
    - Inspect logs for errors
    Issue: {task}
    """
