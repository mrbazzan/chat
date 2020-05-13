import re


def countEachMessage(path, name):

    count = 0
    with open(path, 'r', encoding="utf8") as file:
        timeRegex = re.compile(
            r'((\d/|\d{2}/)+(\d/|\d{2}/)+(\d{2})+, (\d|\d{2})+:(\d{2})+ (AM|PM)+)|(\d{2}/\d{2}/\d{4}, '
            r'\d{2}:\d{2})')

        for eachLine in file:
            search = timeRegex.search(eachLine)
            if search is None:
                pass
            else:
                if name in eachLine[:len(name) + len(search.group()) + 5]:
                    count += 1
        file.seek(0)
    return count


# theName = "Bazzan"
# answer = countEachMessage("text.txt", theName)
# print(f'{theName} sent {answer} messages')


def countTotalMessage(*args):
    count = 0
    path = args[0]
    with open(path, 'r', encoding="utf8") as file:
        file.seek(0)
        for eachLine in file:
            if args[1] in str(eachLine) or args[2] in str(eachLine):
                count += 1
            else:
                pass
    return count


# total = countTotalMessage("text.txt", "Samuel Millimeter", "Bazzan")
# print(f'The total number of messages is {total}')
