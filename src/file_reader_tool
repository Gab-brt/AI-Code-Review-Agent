class FileReaderTool:
    """
    Tool responsible for reading a local Python source file.
    """

    def execute(self, file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()

            if not content.strip():
                return {
                    "success": False,
                    "content": "",
                    "error": "The file is empty."
                }

            return {
                "success": True,
                "content": content,
                "error": None
            }

        except FileNotFoundError:
            return {
                "success": False,
                "content": "",
                "error": "The file was not found."
            }

        except PermissionError:
            return {
                "success": False,
                "content": "",
                "error": "Permission denied while reading the file."
            }

        except UnicodeDecodeError:
            return {
                "success": False,
                "content": "",
                "error": "The file could not be decoded using UTF-8."
            }

        except Exception as error:
            return {
                "success": False,
                "content": "",
                "error": f"Unexpected file reading error: {error}"
            }
