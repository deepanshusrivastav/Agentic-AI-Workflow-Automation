Project Title: Agentic AI Workflow Automation

What it does:

Converts user intent into actionable steps
Uses LLM for planning
Executes tasks via modular tools

Key Concepts:

Agentic AI
Task decomposition
Tool-based execution
Prompt engineering


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
<img width="611" height="172" alt="Screenshot 2026-04-13 at 10 45 23 PM" src="https://github.com/user-attachments/assets/57370ef0-28c3-46e7-b3fc-fe19b1141704" />
