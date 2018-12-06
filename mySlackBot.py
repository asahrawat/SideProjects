from slackclient import SlackClient
from yelpSample import clientResponse, extractArgs, parseResponse, request, search, get_business, query_api
import time


class slackIM(object):

    def __init__(self):
        self.slackClient = SlackClient("xoxb-389579929281-390037290081-hDWG97V7SAEbdP8zkALj9t2Q")
        self.realBotName = "jeevesbot"

    def slackConnect(self):
        return self.slackClient.rtm_connect()

    def slackRead(self):
        #while True:
            return self.slackClient.rtm_read()
        #    time.sleep(1)

    def inputParse(self, input, bot_id):
        formattedID = "<@"+ bot_id +">"
        if input and len(input) > 0:
            inputDict = input[0]
            if "text" in inputDict and formattedID in inputDict["text"]:
                content = inputDict["text"]
                content = content.split(formattedID)[1]
                content = content.strip(" ")
                user = inputDict["user"]
                channel = inputDict["channel"]
                return [str(user), str(content), str(channel)]
            else:
                return [None, None, None]

    def extractBotID(self, botRealName):
        userInfo = self.slackClient.api_call("users.list")
        allUsers = userInfo["members"]
        for user in allUsers:
            if "name" in user and botRealName in user.get("name") and not user.get("deleted"):
                return user.get("id")


    def writeBack(self, channel, content):
        return self.slackClient.api_call("chat.postMessage", channel = channel, text = content, as_user = True)

#extractBotID("jeevesbot")

class mainFunc(slackIM):

    def __init__(self):
        super(mainFunc, self).__init__()

    yelpRes = staticmethod(clientResponse)

    def takeAction(self, input):
        if input:
            [user, content, channel] = input
            print(content)
            #print(clientResponse(content))
            if content != None:
                resList = self.yelpRes(content)
                for business in resList:
                     self.writeBack(channel,business)

    def runBot(self):
        self.slackConnect()
        botID = self.extractBotID(self.realBotName)
        while True:
            self.takeAction(self.inputParse(self.slackRead(), botID))
            time.sleep(1)

if __name__ == "__main__":
    mainInst = mainFunc()
    #print(clientResponse('-term= "bars" --location= "San Francisco, CA"'))
    mainInst.runBot()
