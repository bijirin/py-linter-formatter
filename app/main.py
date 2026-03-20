def format_linter_error(error: dict) -> dict:
    new_error = {}

    new_error["line"] = error["line_number"]
    new_error["column"] = error["column_number"]
    new_error["message"] = error["text"]
    new_error["name"] = error["code"]
    new_error["source"] = "flake8"

    return new_error


def format_single_linter_file(file_path: str, errors: list) -> dict:
    new_file = {}

    new_file["errors"] = [format_linter_error(error) for error in errors]
    new_file["path"] = file_path

    if new_file["errors"] == []:
        new_file["status"] = "passed"
    else:
        new_file["status"] = "failed"

    return new_file

def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(file, linter_report[file]) for file in linter_report]
