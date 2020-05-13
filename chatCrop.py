
# run only once

def chatCrop(path):
    with open(path, 'r', encoding="utf-8") as file:
        newFile = file.readlines()
        del newFile[0]

    with open(path, 'w', encoding="utf8") as writer:
        for file in newFile:
            writer.write(file)


# chatCrop("text.txt")
