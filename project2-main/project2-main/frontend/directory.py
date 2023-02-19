import os


def folder_list(file_path_list):
    # directory path where files are located
    directory = "E:\/file_detection\my kadya\media"

# get the list of files in the directory
    files = os.listdir(directory)


# loop through each file in the directory
    for file in files:
        # get the file path
        file_path_list.append(os.path.join(directory, file))

    # print(file_path_list)
