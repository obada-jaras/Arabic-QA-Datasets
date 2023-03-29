import os
import json


def merge_json_files(directory):
    merged_data = {"data": [], "version": ""}
    file_list = [file for file in os.listdir(
        directory) if file.endswith('.json')]

    for file in file_list:
        with open(os.path.join(directory, file), 'r', encoding="utf-8") as f:
            json_data = json.load(f)

        merged_data["data"].extend(json_data["data"])

        if not merged_data["version"]:
            merged_data["version"] = json_data["version"]

    return merged_data


def main():
    directory = os.path.join(os.getcwd(), "All Datasets")
    merged_data = merge_json_files(directory)

    with open("merged_dataset.json", "w", encoding="utf-8") as outfile:
        json.dump(merged_data, outfile, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
