import os
import config

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        if not os.path.isdir(working_directory):
            return f'Error: "{working_directory}" is not a directory'
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        if not valid_target_file:
             return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(target_file):
             return f'Error: Cannot write to "{file_path}" as it is a directory'
        os.makedirs(os.path.dirname(target_file),exist_ok=True)
        with open(target_file, "w") as f:
            f.write(content)            
        if os.path.isfile(target_file):
             return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        else:
             return f'Error: Failed to write to "{file_path}"'
    except ValueError as inst:
            return f'Error: Value Error - {inst}'
    except RuntimeError as inst:
            return f'Error: Runtime Error - {inst}'
    except TypeError as inst:
            return f'Error: Type Error - {inst}'
    except NameError as inst:
        return f'Error: Name Error - {inst}'
    except NotADirectoryError:
        return f'Error: Not a Directory Error - {working_directory} is not a directory'
    except FileNotFoundError:
        return f'Error: File Not Found Error - {file_path} not found'
    except Exception as inst:
        return f'Error: Unknown Error - {inst}'