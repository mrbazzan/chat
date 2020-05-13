from time import strptime, strftime
import re
import pprint

"""
    This .py file is for text file with '1/3/20, 3:43 PM' format
"""


# TODO
# Find a way to get the dictionary that will give each day and
# the maximum message sent in hourPattern()


def hourPattern(path):
    """ Returns a dictionary of the number of message(s) sent per hour everyday"""

    with open(path, 'r', encoding="utf8") as file:
        timeRegex = re.compile(r'((\d/|\d{2}/)+(\d/|\d{2}/)+(\d{2})+, (\d|\d{2})+:(\d{2})+ (AM|PM)+)')
        timeDict = {}

        for line in file:
            modLine = line.split(" - ")
            # To find a pattern that suites the date and time
            search = timeRegex.search(line)
            if search is None:
                continue
            elif line.startswith(search.group()):
                timeStruct = strptime(modLine[0], '%m/%d/%y, %I:%M %p')  # , '%m/%D/%Y, %H:%M'
                hourFormat = strftime('%m/%d/%y: around %I %p', timeStruct)
                if hourFormat in timeDict:
                    timeDict[hourFormat] += 1
                else:
                    timeDict.setdefault(hourFormat, 0)
                    timeDict[hourFormat] += 1

    for date, number in timeDict.items():
        print(f'{date} -- {number} message(s)')


# hourPattern()


def dayPattern(path):
    """ Returns a dictionary of the number of messages sent everyday"""
    with open(path, 'r', encoding="utf8") as file:
        timeRegex = re.compile(r'((\d/|\d{2}/)+(\d/|\d{2}/)+(\d{2})+, (\d|\d{2})+:(\d{2})+ (AM|PM)+)')
        timeDict = {}

        for line in file:
            modLine = line.split(" - ")
            # To find a pattern that suites the date and time
            search = timeRegex.search(line)
            if search is None:
                continue
            elif str(line).startswith(search.group()):
                timeStruct = strptime(modLine[0], '%m/%d/%y, %I:%M %p')
                weekFormat = strftime('%m/%d/%y:', timeStruct)

                if weekFormat in timeDict:
                    timeDict[weekFormat] += 1
                else:
                    timeDict.setdefault(weekFormat, 0)
                    timeDict[weekFormat] += 1
    return timeDict


# value = dayPattern()
# for k, i in value.items():
#     print(k, i)


def monthPattern(path):
    """ Returns a dictionary of the number of messages sent per month"""
    with open(path, 'r', encoding="utf8") as file:
        timeRegex = re.compile(r'((\d/|\d{2}/)+(\d/|\d{2}/)+(\d{2})+, (\d|\d{2})+:(\d{2})+ (AM|PM)+)')
        timeDict = {}
        for line in file:
            modLine = line.split(" - ")
            # To find a pattern that suites the date and time
            search = timeRegex.search(line)
            if search is None:
                continue
            elif str(line).startswith(search.group()):
                timeStruct = strptime(modLine[0], '%m/%d/%y, %I:%M %p')
                monthFormat = strftime('%m/%y:', timeStruct)
                if monthFormat in timeDict:
                    timeDict[monthFormat] += 1
                else:
                    timeDict.setdefault(monthFormat, 0)
                    timeDict[monthFormat] += 1
    return timeDict


# pprint.pprint(monthPattern(''))


def firstMessage(path, name):
    """ Print the number of first message sent by each party in the chat."""
    with open(path, 'r', encoding="utf8") as file:
        timeRegex = re.compile(r'((\d/|\d{2}/)+(\d/|\d{2}/)+(\d{2})+, (\d|\d{2})+:(\d{2})+ (AM|PM)+)')
        timeList = []
        initiateList = []
        for line in file:
            modLine = line.split(" - ")
            search = timeRegex.search(line)
            if search is None:
                continue
            elif str(line).startswith(search.group()):
                timeStruct = strptime(modLine[0][:6], '%m/%d/%y')  # '%d/%m/%Y, %H:%M' or , %I:%M %p
                if name.startswith(modLine[-1][:len(name)]):
                    if timeStruct not in timeList:
                        timeList.append(timeStruct)
                        initiateList.append(modLine[-1])
                    elif timeStruct in timeList:
                        continue
                else:
                    timeList.append(timeStruct)
                    continue
    return initiateList


count = 0
for i in firstMessage('', ""):
    print(i)
    count += 1
print(count)
