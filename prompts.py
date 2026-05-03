def format_execution_prompt(step):
    return f"""
    Execute the following step:
    {step}

    Provide a clear and helpful output.
    """
