"""LangChain Agent Tool Calling Demo

Demonstrates how an agent can autonomously select and execute tools
based on user queries, using a domestic LLM via OpenAI-compatible interface.
"""

import os
import sys
from datetime import datetime

from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

# ---- Tools ----


@tool
def get_current_time(query: str = "") -> str:
    """Returns the current date and time. `query` is for agent routing only."""
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


@tool
def calculator(expression: str) -> str:
    """Evaluates a math expression and returns the result.

    Args:
        expression: A math expression, e.g. "2 + 3 * 4"
    """
    try:
        result = eval(expression, {"__builtins__": {}}, {})  # noqa: S307
        return str(result)
    except Exception as e:
        return f"Error: {e}"


# ---- Agent Setup ----


def build_agent():
    """Creates and returns a tool-calling agent."""
    llm = ChatOpenAI(
        base_url=os.getenv("OPENAI_BASE_URL", ""),
        api_key=os.getenv("OPENAI_API_KEY", ""),
        model=os.getenv("MODEL_NAME", ""),
    )
    tools = [get_current_time, calculator]
    return create_agent(model=llm, tools=tools)


# ---- Main ----


def main():
    """Interactive loop: user asks questions, agent selects tools and responds."""
    print("=== LangChain Agent Demo ===")
    print("Agent tools: get_current_time, calculator")
    print("Type 'quit' to exit\n")

    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY environment variable not set.")
        sys.exit(1)

    agent = build_agent()

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ("quit", "exit"):
            print("Goodbye!")
            break
        if not user_input:
            continue

        print("\nAgent thinking...")
        result = agent.invoke({"messages": [HumanMessage(content=user_input)]})
        # The last message in the result is the agent's final response
        agent_reply = result["messages"][-1].content
        print(f"\nAgent: {agent_reply}\n")


if __name__ == "__main__":
    main()
