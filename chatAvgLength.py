
from chatMessage import countEachMessage, countTotalMessage
from chatWord import eachWord, totalWord


def eachAvgLengthMessage(path, name):
    """This function gives the average length of message by each person in a private chat."""

    with open(path, 'r'):
        eachMessage = countEachMessage(path, name)
        everyWord = eachWord(path, name)
    avgLength = everyWord / eachMessage
    return f"Average Length of message by {name} is {everyWord}/" \
           f"{eachMessage} = {avgLength}"


# theName = "Samuel Millimeter"
# avg = eachAvgLengthMessage("text.txt", theName)
# print(avg)


def totalAvgLengthMessage(*name):
    """This function gives the total average length of message by the two parties in a private chat."""
    path = name[0]

    with open(path, 'r'):
        eachMessage = countTotalMessage(path, name[1], name[2])
        everyWord = totalWord(path, name[1], name[2])
    avgLength = everyWord / eachMessage
    return f"The total Average Length of message is {everyWord}/" \
           f"{eachMessage} = {avgLength}"


# print(totalAvgLengthMessage("text.txt", "Samuel Millimeter", "Bazzan"))
