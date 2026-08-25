from functions.write_file import write_file

class TestGetFilesFunction():
    def writing_to_existing_file() -> None:
        print("Testing writing to file 'lorem.txt'")
        print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

    def writing_to_new_file() -> None:
        print("Testing writing to file 'pkg/morelorem.txt'")
        print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

    def prevent_writing_out_of_working_directory() -> None:
        print("Testing writing to file '/tmp/temp.txt'")
        print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

def main() -> None:
      TestGetFilesFunction.writing_to_existing_file()
      TestGetFilesFunction.writing_to_new_file()
      TestGetFilesFunction.prevent_writing_out_of_working_directory()


if __name__ == "__main__":
    main()