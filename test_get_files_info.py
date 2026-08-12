
from functions.get_files_info import get_files_info

class TestGetFilesFunction():
    def current_directory() -> None:
        print(get_files_info("calculator", "."))

    def pkg_directory() -> None:
        print(get_files_info("calculator", "pkg"))

    def folder_not_present() -> None:
        print(get_files_info("calculator", "/bin"))

    def outside_working_directory() -> None:
        print(get_files_info("calculator", "../"))

def main() -> None:
      TestGetFilesFunction.current_directory()
      TestGetFilesFunction.pkg_directory()
      TestGetFilesFunction.folder_not_present()
      TestGetFilesFunction.outside_working_directory()


if __name__ == "__main__":
    main()