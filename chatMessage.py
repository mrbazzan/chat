import re

"""
    This class helps to;
    - count the total number of messages sent by each party in a whatsapp private chat
    - and the overall total message contained in the chat

"""


class Main:

    def __init__(self, path):
        self.path = path

    def countEachMessage(self, name):
        count = 0
        with open(self.path, 'r', encoding="utf8") as file:
            # regex for '18/12/2019, 11:20' or '1/3/20, 3:43 PM'
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

    def countTotalMessage(self, *args):
        count = 0
        with open(self.path, 'r', encoding="utf8") as file:
            file.seek(0)
            for eachLine in file:
                if args[0] in str(eachLine) or args[1] in str(eachLine):
                    count += 1
                else:
                    pass
        return count


if __name__ == '__main__':
    theName = "Bazzan"  # or 'Samuel Millimeter'
    answer = Main('mytest.txt').countEachMessage(theName)
    print(f'{theName} sent {answer} messages')

    total = Main('mytest.txt').countTotalMessage("Samuel Millimeter", "Bazzan")
    print(f'The total number of messages is {total}')
