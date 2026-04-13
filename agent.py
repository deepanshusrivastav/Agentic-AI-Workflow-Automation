from tools import generate_test_cases, debug_code

def execute_task(task_plan):
    results = []
    for step in task_plan:
        if "test" in step.lower():
            results.append(generate_test_cases(step))
        elif "debug" in step.lower():
            results.append(debug_code(step))
    return results
