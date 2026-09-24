import json
import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse
from prompts import system_prompt
from call_function import available_functions, call_function

def main() -> None:
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError("API Key not found. OPENROUTER_API_KEY environment variable not set.")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages = [
     {"role": "system", "content": system_prompt},
     {"role": "user", "content": args.user_prompt},
    ]
    response = client.chat.completions.create( messages=messages, model="openrouter/free", tools=available_functions,)
    if not response.usage:
        raise RuntimeError("API reponse appears to be malformed")
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")
    message = response.choices[0].message
    if message.tool_calls:
        for tool_call in message.tool_calls:
            result_message = call_function(tool_call)
            if result_message['content'] == '':
                raise Exception("No content found.")
            if args.verbose:
                print(f"-> {result_message['content']}")
    else:
        print(f"Response: {message.content}")


if __name__ == "__main__":
    main()
