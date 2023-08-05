import json


def write_to_json_file(data, file_path, indent=None):
    json_dump = json.dumps(data, indent=indent)
    json_file = open(file_path, "w")
    json_file.write(json_dump)
    json_file.close()


def read_from_json_file(file_path):
    json_file = open(file_path, "r")
    data = json.load(json_file)
    json_file.close()
    return data


def write_to_text_file(lines, file_path, line_end_character="\n"):
    text_file = open(file_path, "w")
    for line in lines:
        text_file.write(line + line_end_character)
    text_file.close()


def read_from_text_file(file_path):
    text_file = open(file_path, "r")
    lines = [line.rstrip() for line in text_file.readlines()]
    text_file.close()
    return lines
