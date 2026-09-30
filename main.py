import json
import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse
from prompts import system_prompt
from call_function import available_functions, call_function
from config import MAX_ITERS

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
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
    final_response_received: bool = False

    for _ in range(MAX_ITERS):
        try:
            final_response: str | None = generate_content(client, messages, args.verbose)
            if final_response:
                final_response_received  = True
                print(f"Final Response: {final_response}")
                return
        except Exception as e:
            print(f"Error generating content: {e}")
    if not final_response_received:
        print(f"Max iterations of {MAX_ITERS} reached without final response")
        exit(1)

def generate_content(client: OpenAI, messages: list, verbose: bool) -> str | None:
    response = client.chat.completions.create( messages=messages, model="openrouter/free", tools=available_functions,)
    if not response.usage:
        raise RuntimeError("API reponse appears to be malformed")
    if verbose:
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")
    message = response.choices[0].message
    messages.append(message)
    if not message.tool_calls:
        return message.content
    
    for tool_call in message.tool_calls:
        result_message = call_function(tool_call)
        if not result_message.get("content"):
            raise RuntimeError(f"Empty function response for {tool_call.function.name}")
        if verbose:
            print(f"-> {result_message['content']}")
        messages.append(result_message)
    return None
        


if __name__ == "__main__":
    main()
