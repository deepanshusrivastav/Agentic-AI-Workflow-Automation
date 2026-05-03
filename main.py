from agent import run_agent

if __name__ == "__main__":
    user_input = input("Enter your task: ")

    results = run_agent(user_input)

    print("\n✅ Final Output:\n")
    for r in results:
        print(r)
        print("-" * 50)
