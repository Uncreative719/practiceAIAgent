from functions.get_files_info import schema_get_files_info
from functions.run_python_files import schema_run_python_files
from functions.get_file_content import schema_get_file_content
from functions.write_file import schema_write_file
available_functions = [
    schema_get_files_info,
    schema_run_python_files,
    schema_get_file_content,
    schema_write_file
]