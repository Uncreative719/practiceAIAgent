import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        if not os.path.isdir(working_directory):
            return f'Error: "{working_directory}" is not a directory'
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        result: str = ''
        if directory == '.':
            result = 'Result for current directory:'
        else:
            result = f"Result for '{directory}' directory:"
        if not valid_target_dir:
            result += (f'\n    Error: Cannot list "{directory}" as it is outside the permitted working directory')
            return result
        else:
            file_list: list[str, str, str] = []
            iter_list: list[str] = os.listdir(target_dir)
            for item in iter_list:
                if not item.startswith("__"):
                    item_path = target_dir+"/"+item
                    file_list.append((item, os.path.getsize(item_path), os.path.isdir(item_path)))
            for name, size, isdir in file_list:
                result += (f"\n  - {name}: file_size={size} bytes, is_dir={isdir}")
            return result
    except ValueError as inst:
        return f'Error: Value Error - {inst}'
    except RuntimeError as inst:
        return f'Error: Runtime Error - {inst}'
    except TypeError as inst:
        return f'Error: Type Error - {inst}'
    except NameError as inst:
        return f'Error: Name Error - {inst}'
    except NotADirectoryError:
        return f'Error: Not a Directory Error - {directory} is not a directory'
    except FileNotFoundError:
        return f'Error: File Not Found Error - {directory} not found'
    except Exception as inst:
        return f'Error: Unknown Error - {inst}'