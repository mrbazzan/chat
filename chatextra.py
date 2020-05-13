import re
import tabulate
import pprint


class Extra:

    def __init__(self, path):
        self.path = path

    """Returns a dictionary of each of the object in a chat file"""

    def eachLetter(self, name):

        with open(self.path, 'r', encoding="utf-8") as file:

            # regex for format like "05/09/2019, 21:02" or '1/3/20, 3:43 PM'
            timeRegex = re.compile(
                r'((\d/|\d{2}/)+(\d/|\d{2}/)+(\d{2})+, (\d|\d{2})+:(\d{2})+ (AM|PM)+)|(\d{2}/\d{2}/\d{4}, '
                r'\d{2}:\d{2})')
            newList = []
            wordDict = {}
            for eachLine in file:
                search = timeRegex.search(str(eachLine))
                if search is None:
                    if name in newList[-1]:
                        lineSplit2 = str(eachLine)
                        for word in lineSplit2:
                            wordDict.setdefault(word, 0)
                            wordDict[word] += 1
                        del newList[-1]
                        continue
                else:
                    if name in str(eachLine):
                        lineSplit = str(eachLine)[len(name) + len(search.group()) + 5:]
                        for word in lineSplit:
                            wordDict.setdefault(word, 0)
                            wordDict[word] += 1
                        newList.append(str(eachLine))
                    else:
                        newList.append(str(eachLine))
        return wordDict

    """This returns a dictionary of the most word used in the private chat"""

    def mostWord(self, name):

        with open(self.path, 'r', encoding="utf-8") as file:
            # regex for format like "05/09/2019, 21:02" or '1/3/20, 3:43 PM'
            timeRegex = re.compile(
                r'((\d/|\d{2}/)+(\d/|\d{2}/)+(\d{2})+, (\d|\d{2})+:(\d{2})+ (AM|PM)+)|(\d{2}/\d{2}/\d{4}, '
                r'\d{2}:\d{2})')
            newList = []
            wordDict = {}
            for eachLine in file:
                search = timeRegex.search(str(eachLine))
                if search is None:
                    if name in newList[-1]:
                        lineSplit2 = str(eachLine).split()
                        for word in lineSplit2:
                            wordDict.setdefault(word, 0)
                            wordDict[word] += 1
                        del newList[-1]
                        continue
                else:
                    if name in str(eachLine):
                        lineSplit = str(eachLine)[len(name) + len(search.group()) + 5:].split()
                        for word in lineSplit:
                            wordDict.setdefault(word, 0)
                            wordDict[word] += 1
                        newList.append(str(eachLine))
                    else:
                        newList.append(str(eachLine))
        return wordDict

    """This returns the number of link sent by a all party in a private chat"""

    def totalSharedLink(self):

        count = 0
        with open(self.path, 'r', encoding="utf8") as file:

            # regex for website-like format(http:www.livescores.com)"
            linkRegex = re.compile(r'((http:// | https:// )+ (([\w.%-?=+]+ /*) (([\w.%-+?=]+)? /*)?))', re.VERBOSE)
            for eachLine in file:
                search = linkRegex.findall(str(eachLine))
                for group in search:
                    if group[2] is None:
                        continue
                    else:
                        # print(group[2])
                        count += 1
            return count

    """This returns the number of link sent by a specific party in a private chat"""

    def eachSharedLink(self, name):

        with open(self.path, 'r', encoding="utf8") as file:
            newList = []
            count = 0
            # regex for website-like format"
            linkRegex = re.compile(r'((http:// | https:// )+ (([\w.%-?=+]+ /*) (([\w.%-+?=]+)? /*)?))', re.VERBOSE)
            # regex for format like "05/09/2019, 21:02"
            timeRegex = re.compile(
                r'((\d/|\d{2}/)+(\d/|\d{2}/)+(\d{2})+, (\d|\d{2})+:(\d{2})+ (AM|PM)+)|(\d{2}/\d{2}/\d{4}, '
                r'\d{2}:\d{2})')
            for eachLine in file:
                timeSearch = timeRegex.search(eachLine)
                search = linkRegex.findall(str(eachLine))
                if timeSearch is None:
                    if name in newList[-1]:
                        newList.append(str(eachLine))
                        for group in search:
                            if group[2]:
                                count += 1
                            else:
                                del newList[-1]
                                continue
                        del newList[-1]

                else:
                    if name in eachLine:
                        newList.append(str(eachLine))
                        for group in search:
                            if group[2]:
                                count += 1
                            else:
                                continue
                    else:
                        newList.append(str(eachLine))

        return count


def tabularForm(wordDict, occurrence=0):
    """
        This is a fancy grid table which prints a word and the number of
        time(s) it appears.

        OCCURRENCE: This is the number of time(s) a particular
        object or word appears
        """

    newList = [("WORD", "NO. OF TIME(S)")]
    for value in wordDict:
        if wordDict[value] >= occurrence:
            newList.append((value, wordDict[value]))
    return tabulate.tabulate(newList, tablefmt="fancy_grid", headers="firstrow")


if __name__ == '__main__':

    # print(Extra('mytest.txt').eachLetter("Bazzan"))
    #
    # theName = "Samuel Millimeter"
    # link = Extra('mytest.txt').eachSharedLink(theName)
    # print(f'Number of link(s) sent by {theName} is {link}')
    #
    # pprint.pprint(Extra('mytest.txt').mostWord("Bazzan"))
    #
    theName = "Bazzan"
    most_dict = Extra('mytest.txt').mostWord(theName)
    table = tabularForm(most_dict, 10)
    print(f'''
        TABLE SHOWING MOST WORDS USED BY {theName}
{table}
    ''')
    #
    # link = Extra('mytest.txt').totalSharedLink()
    # print(f'Total shared link in conversation is {link}')
