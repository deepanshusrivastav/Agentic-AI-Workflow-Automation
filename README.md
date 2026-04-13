# Agentic-AI-Workflow-Automation
AI agent that:  Takes a task (e.g., “test login page”) Breaks it into steps Executes steps using tools (LLM + functions).

#Architecture(Simple Version)

User Input → LLM (Planner) → Task List
                   ↓
              Executor (Python functions)
                   ↓
              Final Output


#Tech Stack:
Python
OpenAI API (or any LLM API)
Simple CLI (no need UI)
Optional: LangChain (only if you want)

#Project Structure
agentic-ai-workflow/
│── main.py
│── agent.py
│── tools.py
│── prompts.py
│── requirements.txt
│── README.md
