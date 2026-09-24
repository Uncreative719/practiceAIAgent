import json
from collections.abc import Callable

import functions.get_files_info
import functions.run_python_files
import functions.get_file_content
import functions.write_file

available_functions = [
    functions.get_files_info.schema_get_files_info,
    functions.run_python_files.schema_run_python_files,
    functions.get_file_content.schema_get_file_content,
    functions.write_file.schema_write_file
]

def call_function(tool_call, verbose: bool = False) -> dict:
    function_name: str = tool_call.function.name
    function_args: dict = json.loads(tool_call.function.arguments or "{}")
    default_working_directory = "./calculator"
    if verbose:
        print(f" - Calling function: {function_name}({function_args})")
    else:
        print(f" - Calling function: {function_name}")

    function_map: dict[str, Callable[...,str]] = {
        "get_file_content": functions.get_file_content.get_file_content,
        "run_python_files": functions.run_python_files.run_python_files,
        "get_files_info": functions.get_files_info.get_files_info,
        "write_file": functions.write_file.write_file,
    }

    if function_name not in function_map:
        return {
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": f"Error: Unknown function: {function_name}",
        }
    else:
        function_args['working_directory'] = default_working_directory
        result = function_map[function_name](**function_args)
        return {
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": result,
        }