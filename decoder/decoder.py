import os


FILE_PATH = "files"


file_list = os.listdir(FILE_PATH)


def group_files(files: list) -> list:
    grouped_files = {
        "first": [],
        "second": [],
        "last": {},
    }
    for file in files:
        if file.endswith("=="):
            grouped_files["first"].append(file)
        elif file.endswith("="):
            grouped_files["second"].append(file)
        else:
            if not grouped_files["last"].get(file[:3]):
               grouped_files["last"][file[:3]] = [] 
            grouped_files["last"][file[:3]].append(file)

    return grouped_files


def sort_group_names(names_list: list):
    after_items = "wxyz"
    names_list = sorted(names_list)
    indexes = []
    for i in range(len(names_list)):
        name = names_list[i]
        if name[-1].isalpha():
            indexes.append(i)
    indexed_list = names_list[indexes[0]::]
    names_list[indexes[0]::] = []
    for item in reversed(indexed_list):
        names_list.insert(0, item) 
    return names_list
    
def sort_last(files: dict) -> dict:
    group_names = files.keys()
    sorted_last_dict = dict()
    for group_name in sorted(group_names):
        sorted_last_dict[group_name] = sort_group_names(files[group_name])

    return sorted_last_dict


dict_files = group_files(file_list) 
sorted_first = sorted(dict_files["first"])
sorted_second = sorted(dict_files["second"])
sorted_last = sort_last(dict_files["last"])


all_binaries = ""


for file in sorted_first:
    with open(f"{FILE_PATH}/{file}", "r") as binary_file:
        all_binaries += " " + binary_file.read()


for file in sorted_second:
    with open(f"{FILE_PATH}/{file}", "r") as binary_file:
        all_binaries += " " + binary_file.read()


for file in sorted_last.values():
    for file_item in file:
        with open(f"{FILE_PATH}/{file_item}", "r") as binary_file:
            all_binaries += " " + binary_file.read()


with open("all-binaries.txt", "w+") as write_file:
    write_file.write(all_binaries)
