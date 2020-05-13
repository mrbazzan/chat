
"""
    This function takes a .txt whatsapp file and returns a file with the first line deleted.
    Note: The first line contains "Messages to this chat and calls are now secured with end-to-end encryption.
                                   Tap for more info.", which is not needed for the analysis
    Hence, why it was deleted.
"""


def chatCrop(path, newpath):
    # opens the .txt file
    with open(path, 'r', encoding="utf-8") as file:
        newFile = file.readlines()
        del newFile[0]  # delete the first line

    # open a new file in writer mode, and save the old file sin it.
    with open(newpath, 'w', encoding="utf8") as writer:
        for file in newFile:
            writer.write(file)


if __name__ == '__main__':
    chatCrop("text.txt", 'mytest.txt')
