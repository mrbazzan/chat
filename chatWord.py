
import re
import tabulate

# Beware of ''.split() and ''.split(" ")


def eachWord(path, name):
    with open(path, 'r', encoding="utf8") as file:
        # regex for format like "05/09/2019, 21:02 or 03/01/2020, 15:47"
        timeRegex = re.compile(
            r'((\d/|\d{2}/)+(\d/|\d{2}/)+(\d{2})+, (\d|\d{2})+:(\d{2})+ (AM|PM)+)|(\d{2}/\d{2}/\d{4}, '
            r'\d{2}:\d{2})')
        count = 0
        newList = []

        for eachLine in file:
            search = timeRegex.search(eachLine)
            if search is None:
                if name in newList[-1]:
                    newList.append(str(eachLine))
                    lineSplit2 = str(eachLine).split()
                    count += len(lineSplit2)
                    del newList[-1]
            else:
                if name in eachLine[:len(name) + len(search.group()) + 5]:
                    lineSplit = eachLine[len(name) + len(search.group()) + 5:].split()
                    count += len(lineSplit)
                    newList.append(str(eachLine[:len(name) + len(search.group()) + 5]))
                else:
                    newList.append(str(eachLine[:len(name) + len(search.group()) + 5]))
        return count


# theName = "Samuel Millimeter"
# answer = eachWord("text.txt", theName)
# print(f'{theName} sent {answer} words')


def totalWord(*thing):
    path = thing[0]
    count = 0
    value = ''
    with open(path, 'r', encoding="utf8") as file:
        timeRegex = re.compile(
            r'((\d/|\d{2}/)+(\d/|\d{2}/)+(\d{2})+, (\d|\d{2})+:(\d{2})+ (AM|PM)+)|(\d{2}/\d{2}/\d{4}, '
            r'\d{2}:\d{2})')

        for eachLine in file:
            search = timeRegex.search(eachLine)
            if search is None:
                new2 = eachLine.split()
                if value == thing[2]:
                    count += len(new2)
                else:
                    count += len(new2)
            else:
                if thing[1] in eachLine[:len(thing[1]) + len(search.group()) + 5]:
                    new = eachLine[len(thing[1]) + len(search.group()) + 5:].split()
                    count += len(new)
                    value = thing[1]

                elif thing[2] in eachLine[:len(thing[2]) + len(search.group()) + 5]:
                    new1 = eachLine[len(thing[2]) + len(search.group()) + 5:].split()
                    count += len(new1)
                    value = thing[2]

    return count


# total = totalWord("text.txt", "Samuel Millimeter", "Bazzan")
# print(f'The total number of words is {total}')
