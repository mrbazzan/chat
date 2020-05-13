
from chatMessage import Main
from chatWord import MainWord


class AvgLength:

    def __init__(self, path):
        self.path = path

    def eachAvgLengthMessage(self, name):
        """This function gives the average length of message by each person in a private chat."""

        eachMessage = Main(self.path).countEachMessage(name)
        everyWord = MainWord(self.path).eachWord(name)

        avgLength = everyWord / eachMessage
        return f"Average Length of message by {name} is {everyWord}/" \
               f"{eachMessage} = {avgLength}"

    def totalAvgLengthMessage(self, *name):
        """This function gives the total average length of message by the two parties in a private chat."""

        eachMessage = Main(self.path).countTotalMessage(name[0], name[1])
        everyWord = MainWord(self.path).totalWord(name[0], name[1])

        avgLength = everyWord / eachMessage
        return f"The total Average Length of message is {everyWord}/" \
               f"{eachMessage} = {avgLength}"

    def __str__(self):
        return 'This is the Average Length class.'


if __name__ == '__main__':

    theName = "Samuel Millimeter"
    avg = AvgLength('mytest.txt').eachAvgLengthMessage(theName)
    print(avg)

    print(AvgLength('mytest.txt').totalAvgLengthMessage("Samuel Millimeter", "Bazzan"))
