import pytest

input = [{u'source_team': u'TBFH1TB89', u'text': u'<@UBG138J2D> test01', u'ts': u'1530383263.000053', u'user': u'UBFH1TBG9', u'team': u'TBFH1TB89', u'type': u'message', u'channel': u'DBGMAKJQ5'}]

@pytest.fixture
def slackIM():
    from mySlackBot import slackIM
    return slackIM()


@pytest.fixture
def mainFunc():
    from mySlackBot import mainFunc
    return mainFunc()


#@pytest.mark.skip(reason = "completed test")
def test_slackConnect(slackIM):
    assert slackIM.slackConnect() == True

def test_inputParse(slackIM):
    assert slackIM.inputParse(input, "UBG138J2D") == ["UBFH1TBG9", "test01", "DBGMAKJQ5"]

def test_extractBotID(slackIM):
    assert slackIM.extractBotID("jeevesbot") == "UBG138J2D"

def test_writeBack(slackIM):
    assert slackIM.writeBack("UBFH1TBG9", "test write")["ok"] == True

#@pytest.mark.skip(reason = "not pertinent right now")
def test_slackRead(slackIM):
    slackIM.slackConnect()
    print slackIM.slackRead()

def test_takeAction_empty(mainFunc):
    input = ["UBFH1TBG9", "test01", "DBGMAKJQ5"]
    assert mainFunc.takeAction(input)

def test_takeAction_content(mainFunc):
    input = [None, None, None]
    assert mainFunc.takeAction(input)
