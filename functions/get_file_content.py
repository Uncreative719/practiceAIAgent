import os
import config

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        if not os.path.isdir(working_directory):
            return f'Error: "{working_directory}" is not a directory'
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        if not valid_target_file or not os.path.isfile(target_file):
             return f'Error: File not found or is not a regular file: "{file_path}"'
        file_content_string: str = ''
        with open(target_file, "r") as f:
            file_content_string = f.read(config.MAX_CHARS)
            if f.read(1):
                file_content_string += f'[...File "{file_path}" truncated at {config.MAX_CHARS} characters]'
        return file_content_string
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