from functions.get_file_content import get_file_content

class TestGetFilesFunction():
    def happy_path() -> None:
        print("Testing on file 'lorem.txt'")
        result = get_file_content("calculator", "lorem.txt")
        print(f"lorem.txt length: {len(result)}")
        print(f"lorem.txt truncated: {'truncated' in result}")
        if not 'truncated' in result:
                    print(result)

    def using_main_as_file() -> None:
        print("Testing on file 'main.py'")
        result = get_file_content("calculator", "main.py")
        print(f"lorem.txt length: {len(result)}")
        print(f"lorem.txt truncated: {'truncated' in result}")
        if not 'truncated' in result:
            print(result)

    def using_file_in_pkg() -> None:
        print("Testing on file 'pkg/calculator.py'")
        result = get_file_content("calculator", "pkg/calculator.py")
        print(f"lorem.txt length: {len(result)}")
        print(f"lorem.txt truncated: {'truncated' in result}")
        if not 'truncated' in result:
                    print(result)

    def folder_not_file() -> None:
        print("Testing on folder '/bin/cat'")
        print(get_file_content("calculator", "/bin/cat"))

    def nonexistant_file() -> None:
        print("Testing on nonexistant file 'pkg/does_not_exist.py'")
        print(get_file_content("calculator", "pkg/does_not_exist.py"))

def main() -> None:
      TestGetFilesFunction.happy_path()
      TestGetFilesFunction.using_main_as_file()
      TestGetFilesFunction.using_file_in_pkg()
      TestGetFilesFunction.folder_not_file()
      TestGetFilesFunction.nonexistant_file()


if __name__ == "__main__":
    main()