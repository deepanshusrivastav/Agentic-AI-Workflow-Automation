from llm import get_task_plan
from tools import generate_test_cases, debug_issue

def decide_tool(step):
    step_lower = step.lower()

    if "test" in step_lower:
        return generate_test_cases(step)
    elif "debug" in step_lower or "error" in step_lower:
        return debug_issue(step)
    else:
        return f"[General Execution] {step}"


def run_agent(user_input):
    print("\n🔹 Generating Plan...\n")

    plan = get_task_plan(user_input)
    print("📌 Plan:\n", plan)

    print("\n🔹 Executing Steps...\n")

    steps = plan.split("\n")
    results = []

    for step in steps:
        if step.strip():
            result = decide_tool(step)
            results.append(result)

    return results
