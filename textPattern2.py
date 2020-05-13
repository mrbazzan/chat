import re
from time import strptime, strftime

"""
    This .py file is for text file with "05/09/2019, 21:02" format
"""


def hourPattern(path):
    """ Returns a dictionary of the number of message(s) sent per hour everyday"""
    with open(path, 'r', encoding="utf8") as file:
        timeRegex = re.compile(r'\d{2}/\d{2}/\d{4}, \d{2}:\d{2}')
        timeDict = {}
        for line in file:
            modLine = line.split(" - ")
            # To find a pattern that suits the date and time
            search = timeRegex.search(line)
            if search is None:
                continue
            elif line.startswith(search.group()):
                timeStruct = strptime(modLine[0], '%d/%m/%Y, %H:%M')
                hourFormat = strftime('%d/%m/%Y: around %H', timeStruct)
                if hourFormat in timeDict:
                    timeDict[hourFormat] += 1
                else:
                    timeDict.setdefault(hourFormat, 0)
                    timeDict[hourFormat] += 1
    for date, number in timeDict.items():
        print(f'{date}:00 -- {number} message(s)')


# hourPattern("text.txt")


def dayPattern(path):
    """ Returns a dictionary of the number of messages sent everyday"""
    with open(path, 'r', encoding="utf8") as file:
        timeRegex = re.compile(r'\d{2}/\d{2}/\d{4}, \d{2}:\d{2}')
        timeDict = {}

        for line in file:
            modLine = line.split(" - ")
            # To find a pattern that suites the date and time
            search = timeRegex.search(line)
            if search is None:
                continue
            elif str(line).startswith(search.group()):
                timeStruct = strptime(modLine[0][:14], '%d/%m/%Y, %H')  # :%M
                weekFormat = strftime('%d/%m/%Y:', timeStruct)

                if weekFormat in timeDict:
                    timeDict[weekFormat] += 1
                else:
                    timeDict.setdefault(weekFormat, 0)
                    timeDict[weekFormat] += 1
    return timeDict


# value = dayPattern("text.txt")
# for k,i in value.items():
#     print(k,i)


def monthPattern(path):
    """ Returns a dictionary of the number of messages sent per month"""
    with open(path, 'r', encoding="utf8") as file:
        timeRegex = re.compile(r'\d{2}/\d{2}/\d{4}, \d{2}:\d{2}')
        timeDict = {}
        for line in file:
            modLine = line.split(" - ")
            # To find a pattern that suites the date and time
            search = timeRegex.search(line)
            if search is None:
                continue
            elif str(line).startswith(search.group()):
                timeStruct = strptime(modLine[0][:14], '%d/%m/%Y, %H')  # :%M
                monthFormat = strftime('%m/%Y:', timeStruct)

                if monthFormat in timeDict:
                    timeDict[monthFormat] += 1
                else:
                    timeDict.setdefault(monthFormat, 0)
                    timeDict[monthFormat] += 1
    return timeDict


# pprint.pprint(monthPattern("text.txt"))


def firstMessage(path, name):
    """ Print the number of first message sent by the person passed as the second arguement."""
    with open(path, 'r', encoding="utf8") as file:
        timeRegex = re.compile(
            r'((\d/|\d{2}/)+(\d/|\d{2}/)+(\d{2})+, (\d|\d{2})+:(\d{2})+ (AM|PM)+)|(\d{2}/\d{2}/\d{4}, '
            r'\d{2}:\d{2})')
        timeList = []
        initiateList = []
        for line in file:
            modLine = line.split(" - ")
            search = timeRegex.search(line)
            if search is None:
                continue
            elif str(line).startswith(search.group()):
                timeStruct = strptime(modLine[0][:10], '%d/%m/%Y')  # %H:%M
                if name in modLine[-1][:len(name)]:
                    if timeStruct not in timeList:
                        timeList.append(timeStruct)
                        initiateList.append(modLine[-1])
                    elif timeStruct in timeList:
                        continue
                else:
                    timeList.append(timeStruct)
                    continue
    return initiateList

#
# count = 0
# for i in firstMessage("text.txt", "Bazzan"):
#     print(i)
#     count += 1
# print(count)
