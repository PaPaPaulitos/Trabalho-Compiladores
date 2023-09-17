import sys
import re

class Readfile:
    def __init__(self) -> None:
        pass

    def __file_exists(self) -> str:
        try:
            if len(sys.argv) > 1:
                arquivo = sys.argv[1]

                return arquivo
            else:
                raise Exception("No file")
        except Exception as e:
            print(e)

    def __verify_file_name(self) -> str:
        pattern = r'^[a-zA-Z0-9]+\.paulitos$'

        try:
            filename = self.__file_exists()
            is_dot_paulitos = re.search(pattern, filename)
            if is_dot_paulitos:
                return filename
            else:
                raise Exception("Invalid file name")
        except Exception as e:
            print(e)


    def source_code(self) -> str:
        file = self.__verify_file_name()
        try:
            with open(file, 'r') as source_code:
                input = source_code.readline()

                if input.strip():
                    expr = input
                else:
                    raise Exception(f"Empty file")
        except FileNotFoundError:
            print(f"File not found: {file}")
        except Exception as e:
            print(e)

        return expr