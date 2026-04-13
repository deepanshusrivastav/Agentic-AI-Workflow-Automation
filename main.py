from agent import execute_task

task_plan = [
    "Generate test cases for login page",
    "Debug login API failure"
]

result = execute_task(task_plan)

for r in result:
    print(r)
