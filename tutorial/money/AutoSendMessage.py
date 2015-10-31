__author__ = 'bj'
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
import  re
device = MonkeyRunner.waitForConnection()
ACTION_CLICK = "DOWN_AND_UP"
GREEN_COLOR = [-1, 69, 192, 26]
WHITE_COLOR = [-1, 255, 255, 255]
BUTTON_GREEN= [-1, 69, 192, 26]
menu_x_2 = 456
menu_y_2 = 291
width = 720;
ACTIVITY_CHATROOMINFO="com.tencent.mm.plugin.chatroom.ui.ChatroomInfoUI";
ACTIVITY_SAY_HI="com.tencent.mm.plugin.profile.ui.SayHiWithSnsPermissionUI";
ACTIVITY_SNS_USER_INFO="com.tencent.mm.plugin.profile.sns.SnsUserUi";
ACTIVITY_QQ_TROPMEMBER="com.tencent.mobileqq.activity.TroopMemberListActivity"

def click(x, y):
    print('click ('+str(x)+','+str(y)+')')
    device.touch(x, y, "DOWN_AND_UP")
    MonkeyRunner.sleep(2)

def longClick(x, y):
    device.touch(x, y, "DOWN")
    MonkeyRunner.sleep(2)
    device.touch(x, y, "UP")
    MonkeyRunner.sleep(1)

def toMain():
    runComponent = "com.tencent.mm/com.tencent.mm.ui.LauncherUI"
    device.startActivity(component=runComponent, flags=0x00008000)
    MonkeyRunner.sleep(3)


def clickMenu():
    print("click menu")
    device.press('KEYCODE_MENU', ACTION_CLICK)
    MonkeyRunner.sleep(2)


def clickRightCorner():
    print('click right corner')
    click(680, 90)
    MonkeyRunner.sleep(2)


def clickFirstMenu():
    device.touch(456, 240, ACTION_CLICK)
    MonkeyRunner.sleep(2)


def clickThirdMenu():
    device.touch(456, 340, ACTION_CLICK)
    MonkeyRunner.sleep(2)


def clickSecondMenu():
    device.touch(456, 290, ACTION_CLICK)
    MonkeyRunner.sleep(2)


def toQrod():
    toMain()
    clickMenu()
    clickThirdMenu()


def moveVertify(y):
    print("moveVertify "+str(y))
    if y > 10:
        while y > 800:
            start = (100, 800 + 300)
            end = (100, 300)
            device.drag(start, end, 0.5, 10)
            y -= 800
        start = (100, y + 300)
        end = (100, 300)
        device.drag(start, end, 0.5, 10)


def clickBack():
    print('click back button')
    device.press('KEYCODE_BACK', ACTION_CLICK)
    MonkeyRunner.sleep(1)


def scanQrode(start_x, start_y, per_x, move_y_dis, startI, endI):
    for i in range(startI, endI):
        toQrod()
        clickMenu()
        clickSecondMenu()
        moveVertify((i / 3) * move_y_dis)
        device.touch(start_x + (i % 3) * per_x, start_y, ACTION_CLICK)
        MonkeyRunner.sleep(5)
        clickBack()


def sendMessage(idx):
    clickMenu()
    clickFirstMenu()
    clickX = 360
    click_y = 475
    num_conv = 9
    height_conv = 110
    maxY = 1240
    if (idx < num_conv):
        click(clickX,
              (click_y + height_conv * idx) if (click_y + height_conv * idx) < maxY else maxY);
    else:
        while idx >= num_conv:
            moveVertify(height_conv)
            idx = idx - 1;
        click(clickX,maxY)
    MonkeyRunner.sleep(3)
    device.touch(550, 840, ACTION_CLICK)
    MonkeyRunner.sleep(5)


def isSomeColor(x, y, basepixe):
    newimage = device.takeSnapshot()
    pixel = newimage.getRawPixel(x, y)
    newimage=None
    gateValue = 10
    for i in range(1, 4):
        if abs(basepixe[i] - pixel[i]) > gateValue:
            return False
    return True

def isSomeColor(newimage,x, y, basepixe):
    pixel = newimage.getRawPixel(x, y)
    gateValue = 10
    for i in range(1, 4):
        if abs(basepixe[i] - pixel[i]) > gateValue:
            return False
    return True

def getPixelSub(newimage,x,y):
    pixel = newimage.getRawPixel(x, y)
    return pixel

def getPixel(x,y):
    newimage = device.takeSnapshot()
    res =  getPixelSub(newimage,x,y)
    newimage  = None
    return re

def getFrontActivityName():
    shell = device.shell("dumpsys activity | grep \"mFocusedActivity\"").encode('utf-8','ingore')
    pattern = re.compile(r'[A-Za-z.]+/[A-Za-z.]+')
    match = pattern.findall(shell)
    if match:
        name= match[0].replace("/","")
        print('current activity name '+str(name))
        return name
    return ""

def addFriendInChatroom(idx):
    print("add friend " + str(idx))
    if idx == 20 :
        moveVertify(60)
    if (idx / 4 >= 5 and idx %4 == 0):
        moveVertify(215)
    click(115 + (idx % 4) * 160, 270 + (idx / 4 if idx/4<4 else 4) * 200)
    name = getFrontActivityName()
    if ( name == ACTIVITY_CHATROOMINFO ):
        print(' add friend finish ')
        clickBack()
        return False
    newimage = device.takeSnapshot();
    startY = [486,650,716,830, 900]
    for y in startY:
        if (isSomeColor(newimage,200, y, BUTTON_GREEN)):
            isNeedAdd=False
            for textX in range(0,10):
                if (isSomeColor(newimage,250+textX,y,WHITE_COLOR)):
                    isNeedAdd = True
            if isNeedAdd == False:
                continue
            click(width / 2, y)
            sayHiActivity=getFrontActivityName()
            if sayHiActivity==ACTIVITY_SAY_HI:
                clickRightCorner()
                break
            if sayHiActivity == ACTIVITY_SNS_USER_INFO:
                clickBack()
                clickBack()
                newimage = None
                return True
    newimage = None
    clickBack()
    return True




def isGroupChat():
    clickRightCorner()
    name = getFrontActivityName()
    res = ( name == ACTIVITY_CHATROOMINFO )
    clickBack()
    return res

def run():
    clickX = 360
    click_y = 215
    num_conv = 8
    height_conv = 130
    for idx in range(0,20):
        print("go Chatroom "+str(idx))
        if (idx < num_conv):
            click(clickX,click_y + height_conv * idx)
        else:
            moveVertify(height_conv)
            MonkeyRunner.sleep(1)
            click(clickX,1080)
        MonkeyRunner.sleep(3)
        clickRightCorner()
        name = getFrontActivityName()
        if (name == ACTIVITY_CHATROOMINFO ):
            clickRightCorner()
            for i in range(0,120):
                if addFriendInChatroom(i) == False:
                    break
        else:
            print("Activity name unfit ")
            clickBack()
        print('exit Chatroom')
        clickBack()
def getQQNum():
    getFrontActivityName()

    # for i in range(1,2):
    # toQrod()
    # clickMenu()
    # clickSecondMenu()
    # MonkeyRunner.sleep(3)
    # for i in range(1,3):
    # toQrod()
    # clickMenu()
    # clickSecondMenu()
    # for i in range(1,10):
    # i = 1
    # device.touch(start_x + (i % 3) * per_x, start_y, ACTION_CLICK)
    # idx = 0
    # addGroupOwner(idx)
    # addFriendInChatroom(6)
    # print(isSomeColor(256,830,WHITE_COLOR))
    # print(isSomeColor(682, 79,GREEN_COLOR))
    # newimage = device.takeSnapshot()
    # pixel = newimage.getRawPixel(682, 79)
    # print(pixel)
    # for i in range(3,10):
    # addFriendInChatroom(10)
    # p2 = newimage.getRawPixel(255,104)
    # p3 = newimage.getRawPixel(221,106)
    # print(p1)
    #
    # print(p2)
    # print(p3)

    # clickRightCorner()
# for y in range(680,780):
#     pixel = newimage.getRawPixel(256,y)
#     if (pixel[1]  == 255 and pixel[2] == 255):
#         print(y)
#         break
# print('end')

# print (isSomeColor(newimage,615,110, GREEN_COLOR))
# for i in range(10,15):
#     addFriendInChatroom(i)
# MonkeyRunner.sleep(3)  # device.touch(start_x + (i % 3) * per_x, start_y + (i / 3) * per_y, "MOVE")
# device.touch(start_x + (i % 3) * per_x, start_y + (i / 3) * per_y+100, "MOVE")
# addFriendInChatroom(14)
# getFrontActivityName()
# run()
# addFriendInChatroom(18)
# for i in range(10,30):
#     sendMessage(i)
# addFriendInChatroom(36)
# longClick(307,848)
# newim
# age = device.takeSnapshot()
# print(isSomeColor(newimage,615,110, GREEN_COLOR))
# getFrontActivityName()
