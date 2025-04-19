from abc import ABC, abstractmethod

from formatter.utils import (
    create_dir, 
    get_dir_path,
    get_file_name, 
    join_paths, 
    print_error, print_msg, 
    print_warning
)

class BaseFormatter(ABC):
    def __init__(self, filepath: str):
        self.filepath = filepath

    @abstractmethod
    def _serialize(self, content: str, indent: int = 4,  separators=(", ", ":")):
        pass

    @abstractmethod
    def _deserialize(self, file) -> str:
        pass

    @abstractmethod
    def get_format_name(self) -> str:
        return self.extension_name

    @abstractmethod
    def get_format_extension(self) -> str:
        return self.extension


    def check(self):
        print_msg(f"Checking {self.get_format_name()}...")

        try:
            with open(self.filepath, "r", encoding="utf-8") as file:
                content_original = file.read()
            with open(self.filepath, "r", encoding="utf-8") as file:
                content = self._deserialize(file)
        except Exception as e:
            print_error(f"Invalid {self.get_format_name()}: {e}")

        default_comma = ", "
        default_colon = " : "

        preview = self._serialize(content, indent=4, separators=(default_comma, default_colon))
        if (content_original != preview):
            print_warning(f"{self.get_format_name()} is not correct formatted. But syntax is OK.")
            return False
        
        print_msg(f"{self.get_format_name()} is already formatted.", True)
        return True


    def dry_run(self):
        print_msg(f"{self.get_format_name()} Preview:")

        try:
            with open(self.filepath, "r", encoding="utf-8") as file:
                content = self._deserialize(file)
        except Exception as e:
            print_error(f"Invalid {self.get_format_name()}: {e}")
            
        default_comma = ", "
        default_colon = " : "

        try:
            print_msg(self._serialize(content, indent=4, separators=(default_comma, default_colon)))
        except TypeError as e:
            print_error(f"Unable to serialize data to {self.get_format_name()}: {e}")
        
        return True
        

    def format(self, dir_output, in_place):
        print_msg(f"Formatting {self.get_format_name()}...")

        try:
            with open(self.filepath, "r", encoding="utf-8") as file:
                content = self._deserialize(file)
        except Exception as e:
            print_error(f"Invalid {self.get_format_name()}: {e}")
            
        print_msg(f"Deserialized {self.get_format_name()} file.")
        default_comma = ", "
        default_colon = " : "

        if (in_place):
            output = self.filepath
        else:
            if (dir_output != None):
                output = dir_output
                create_dir(output)
                print_msg(f"Created output folder {output}")
            else:
                output = get_dir_path(self.filepath)
                output = join_paths(output, "output")
                create_dir(output)
                print_msg(f"Created output folder {output}")
            
            output = join_paths(output, get_file_name(self.filepath) + "_formatted" + self.get_format_extension())

        try:
            with open(output, "w", encoding="utf-8") as file:
                file.write(self._serialize(content, indent=4, separators=(default_comma, default_colon)))
        except TypeError as e:
            print_error(f"Unable to serialize data to {self.get_format_name()}: {e}")

        print_msg(f"{self.get_format_name()} completed.", True)
        
        return True

