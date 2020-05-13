
import re

# Beware of ''.split() and ''.split(" ")


class MainWord:

    def __init__(self, path):
        self.path = path

    def eachWord(self, name):
        with open(self.path, 'r', encoding="utf8") as file:
            # regex for format like "05/09/2019, 21:02" or '1/3/20, 3:43 PM'
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

    def totalWord(self, *thing):
        count = 0
        value = ''
        with open(self.path, 'r', encoding="utf8") as file:
            # regex for format like "05/09/2019, 21:02 or '1/3/20, 3:43 PM'
            timeRegex = re.compile(
                r'((\d/|\d{2}/)+(\d/|\d{2}/)+(\d{2})+, (\d|\d{2})+:(\d{2})+ (AM|PM)+)|(\d{2}/\d{2}/\d{4}, '
                r'\d{2}:\d{2})')

            for eachLine in file:
                search = timeRegex.search(eachLine)
                if search is None:
                    new2 = eachLine.split()
                    if value == thing[1]:
                        count += len(new2)
                    else:
                        count += len(new2)
                else:
                    if thing[0] in eachLine[:len(thing[0]) + len(search.group()) + 5]:
                        new = eachLine[len(thing[0]) + len(search.group()) + 5:].split()
                        count += len(new)
                        value = thing[0]

                    elif thing[1] in eachLine[:len(thing[1]) + len(search.group()) + 5]:
                        new1 = eachLine[len(thing[1]) + len(search.group()) + 5:].split()
                        count += len(new1)
                        value = thing[1]

        return count


if __name__ == '__main__':
    theName = 'Samuel Millimeter'
    answer = MainWord('mytest.txt').eachWord(theName)
    print(f'{theName} sent {answer} words')

    total = MainWord('mytest.txt').totalWord("Samuel Millimeter", "Bazzan")
    print(f'The total number of words is {total}')
