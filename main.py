from agent import agent


def print_ai_response(messages):
    """
    Prints only the AI's final response.
    """

    for message in reversed(messages):
        if message.type == "ai" and message.content:
            print("\n🤖 Assistant:")
            print(message.content)
            return


def print_tool_calls(messages):
    """
    Prints any tool calls made by the LLM.
    """

    for message in messages:

        if message.type == "ai" and message.tool_calls:

            for tool_call in message.tool_calls:

                print("\n🔧 Tool Called:")
                print(f"Tool : {tool_call['name']}")

                if "query" in tool_call["args"]:
                    print("Generated SQL:")
                    print(tool_call["args"]["query"])


def chat():

    print("=" * 60)
    print("      SQL Agent")
    print("=" * 60)

    print("Type 'exit' to quit.\n")

    while True:

        question = input("You: ")

        if question.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        try:

            response = agent.invoke(
                {
                    "messages": [
                        {
                            "role": "user",
                            "content": question
                        }
                    ]
                }
            )

            messages = response["messages"]

            print_tool_calls(messages)

            print_ai_response(messages)

        except Exception as e:
            print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    chat()