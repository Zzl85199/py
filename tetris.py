import random, time, pygame, sys
from pygame.locals import *

FPS = 25
視窗寬度 = 640  
視窗高度 = 480
格子大小 = 20
格子寬度 = 10
格子高度 = 20
BLANK = '.'

左右移動變化頻率 = 0.15
向下移動變化頻率 = 0.1

中央對齊 = int((視窗寬度 - 格子寬度 * 格子大小) / 2)
頂端對齊 = 視窗高度 - (格子高度 * 格子大小) - 5

#               R    G    B
白        = (255, 255, 255)
灰        = (185, 185, 185)
黑        = (  0,   0,   0)
紅        = (155,   0,   0)
亮紅      = (175,  20,  20)
綠        = (  0, 155,   0)
亮綠      = ( 20, 175,  20)
藍        = (  0,   0, 155)
亮藍      = ( 20,  20, 175)
黃        = (155, 155,   0)
亮黃      = (175, 175,  20)

格子顏色 = 藍
背景顏色 = 黑
文字顏色 = 白
文字底部顏色 = 灰
顏色      = (     藍,      綠,      紅,      黃)
亮顏色 = (亮藍, 亮綠, 亮紅, 亮黃)
assert len(顏色) == len(亮顏色) # each color must have 亮 color

方塊寬度 = 5
方塊高度 = 5

F形塊      = [['.....',
               '..OO.',
               '.OO..',
               '..O..',
               '.....'],
              ['.....',
               '..O..',
               '.OOO.',
               '...O.',
               '.....'],
              ['.....',
               '..O..',
               '..OO.',
               '.OO..',
               '.....'],
              ['.....',
               '.O...',
               '.OOO.',
               '..O..',
               '.....']]
反F形塊     = [['.....',
                '.OO..',
                '..OO.',
                '..O..',
                '.....'],
               ['.....',
                '...O.',
                '.OOO.',
                '..O..',
                '.....'],
               ['.....',
                '..O..',
                '.OO..',
                '..OO.',
                '.....'],
               ['.....',
                '..O..',
                '.OOO.',
                '.O...',
                '.....']]
I形塊      = [['..O..',
               '..O..',
               '..O..',
               '..O..',
               '..O..'],
              ['.....',
               '.....',
               'OOOOO',
               '.....',
               '.....']]
L形塊      = [['..O..',
               '..O..',
               '..O..',
               '..OO.',
               '.....'],
              ['.....',
               '.....',
               '.OOOO',
               '.O...',
               '.....'],
              ['.....',
               '.OO..',
               '..O..',
               '..O..',
               '..O..'],
              ['.....',
               '...O.',
               'OOOO.',
               '.....',
               '.....']]
J形塊 =      [['..O..',
               '..O..',
               '..O..',
               '.OO..',
               '.....'],
              ['.....',
               '.O...',
               '.OOOO',
               '.....',
               '.....'],
              ['.....',
               '..OO.',
               '..O..',
               '..O..',
               '..O..'],
              ['.....',
               '.....',
               'OOOO.',
               '...O.',
               '.....']]
N形塊 =      [['.....',
               '.OO..',
               '..OOO',
               '.....',
               '.....'],
              ['.....',
               '...O.',
               '..OO.',
               '..O..',
               '..O..'],
              ['.....',
               '.....',
               'OOO..',
               '..OO.',
               '.....'],
              ['..O..',
               '..O..',
               '.OO..',
               '.O...',
               '.....']]
反N形塊 =     [['.....',
                '..OO.',
                'OOO..',
                '.....',
                '.....'],
               ['..O..',
                '..O..',
                '..OO.',
                '...O.',
                '.....'],
               ['.....',
                '.....',
                '..OOO',
                '.OO..',
                '.....'],
               ['.....',
                '.O...',
                '.OO..',
                '..O..',
                '..O..']]
P形塊 =      [['.....',
               '..OO.',
               '..OO.',
               '..O..',
               '.....'],
              ['.....',
               '.....',
               '.OOO.',
               '..OO.',
               '.....'],
              ['.....',
               '..O..',
               '.OO..',
               '.OO..',
               '.....'],
              ['.....',
               '.OO..',
               '.OOO.',
               '.....',
               '.....']]
反P形塊 =     [['.....',
                '.OO..',
                '.OO..',
                '..O..',
                '.....'],
               ['.....',
                '..OO.',
                '.OOO.',
                '.....',
                '.....'],
               ['.....',
                '..O..',
                '..OO.',
                '..OO.',
                '.....'],
               ['.....',
                '.....',
                '.OOO.',
                '.OO..',
                '.....']]
T形塊 =      [['.....',
               '.OOO.',
               '..O..',
               '..O..',
               '.....'],
              ['.....',
               '...O.',
               '.OOO.',
               '...O.',
               '.....'],
              ['.....',
               '..O..',
               '..O..',
               '.OOO.',
               '.....'],
              ['.....',
               '.O...',
               '.OOO.',
               '.O...',
               '.....']]
U形塊 =       [['.....',
               '.O.O.',
               '.OOO.',
               '.....',
               '.....'],
              ['.....',
               '..OO.',
               '..O..',
               '..OO.',
               '.....'],
              ['.....',
               '.....',
               '.OOO.',
               '.O.O.',
               '.....'],
              ['.....',
               '.OO..',
               '..O..',
               '.OO..',
               '.....']]
V形塊 =      [['..O..',
               '..O..',
               '..OOO',
               '.....',
               '.....'],
              ['.....',
               '.....',
               '..OOO',
               '..O..',
               '..O..'],
              ['.....',
               '.....',
               'OOO..',
               '..O..',
               '..O..'],
              ['..O..',
               '..O..',
               'OOO..',
               '.....',
               '.....']]
W形塊 =      [['.....',
               '.O...',
               '.OO..',
               '..OO.',
               '.....'],
              ['.....',
               '..OO.',
               '.OO..',
               '.O...',
               '.....'],
              ['.....',
               '.OO..',
               '..OO.',
               '...O.',
               '.....'],
              ['.....',
               '...O.',
               '..OO.',
               '.OO..',
               '.....']]
X形塊 =      [['.....',
               '..O..',
               '.OOO.',
               '..O..',
               '.....']]
Y形塊 =      [['.....',
               '..O..',
               'OOOO.',
               '.....',
               '.....'],
              ['..O..',
               '..O..',
               '..OO.',
               '..O..',
               '.....'],
              ['.....',
               '.....',
               '.OOOO',
               '..O..',
               '.....'],
              ['.....',
               '..O..',
               '.OO..',
               '..O..',
               '..O..']]
反Y形塊 =     [['.....',
                '..O..',
                'OOOO.',
                '.....',
                '.....'],
               ['..O..',
                '..O..',
                '..OO.',
                '..O..',
                '.....'],
               ['.....',
                '.....',
                '.OOOO',
                '..O..',
                '.....'],
               ['.....',
                '..O..',
                '.OO..',
                '..O..',
                '..O..']]
Z形塊 =      [['.....',
               '.OO..',
               '..O..',
               '..OO.',
               '.....'],
              ['.....',
               '...O.',
               '.OOO.',
               '.O...',
               '.....']]
反Z形塊 =     [['.....',
                '..OO.',
                '..O..',
                '.OO..',
                '.....'],
               ['.....',
                '.O...',
                '.OOO.',
                '...O.',
                '.....']]



PIECES = {'F': F形塊,
          'RF': 反F形塊,
          'I': I形塊,
          'L': L形塊,
          'J': J形塊,
          'N': N形塊,
          'RN': 反N形塊,
          'P': P形塊,
          'RP': 反P形塊,
          'T': T形塊,
          'U': U形塊,
          'V': V形塊,
          'W': W形塊,
          'X': X形塊,
          'Y': Y形塊,
          'RY': 反Y形塊,
          'Z': Z形塊,
          'RZ': 反Z形塊}


def main():
    global FPS計時, 顯示介面, 基本字型, 放大字型
    pygame.init()
    FPS計時 = pygame.time.Clock()
    顯示介面 = pygame.display.set_mode((視窗寬度, 視窗高度))
    基本字型 = pygame.font.Font('freesansbold.ttf', 18)
    放大字型 = pygame.font.Font('freesansbold.ttf', 100)
    pygame.display.set_caption('DO NOT CRY')

    顯示文字螢幕('DO NOT CRY')
    while True: # game loop
        跑遊戲()
        顯示文字螢幕("Don't cry~~~")


def 跑遊戲():
    # setup variables for the start of the game
    板子 = getBlankBoard()
    最後落下時間 = time.time()
    最後平移時間 = time.time()
    最後下落時間 = time.time()
    下移 = False
    左移 = False
    右移 = False
    分數 = 0
    等級, 下落頻率 = 計算關卡與下落頻率(分數)

    下落方塊 = 取得新的一塊()
    下一個方塊 = 取得新的一塊()
    暫存方塊 = None  # 新增：暫存方塊
    已暫存 = False  # 新增：每回合只能暫存一次

    while True:  # 遊戲的迴圈
        if 下落方塊 is None:
            # 沒有下落方塊時，生成新的方塊
            下落方塊 = 下一個方塊
            下一個方塊 = 取得新的一塊()
            最後下落時間 = time.time()

            if not 判斷(板子, 下落方塊):
                return  # 遊戲結束

        點選離開()
        for event in pygame.event.get():  # 事件處理
            if event.type == KEYUP:
                if event.key == K_p:
                    顯示介面.fill(背景顏色)
                    pygame.mixer.music.stop()
                    顯示文字螢幕('Paused')
                    pygame.mixer.music.play(-1, 0.0)
                    最後下落時間 = time.time()
                    最後落下時間 = time.time()
                    最後平移時間 = time.time()
                elif event.key in (K_LEFT, K_a):
                    左移 = False
                elif event.key in (K_RIGHT, K_d):
                    右移 = False
                elif event.key in (K_DOWN, K_s):
                    下移 = False

            elif event.type == KEYDOWN:
                if (event.key == K_LEFT or event.key == K_a) and 判斷(板子, 下落方塊, adjX=-1):
                    下落方塊['x'] -= 1
                    左移 = True
                    右移 = False
                    最後平移時間 = time.time()

                elif (event.key == K_RIGHT or event.key == K_d) and 判斷(板子, 下落方塊, adjX=1):
                    下落方塊['x'] += 1
                    右移 = True
                    左移 = False
                    最後平移時間 = time.time()

                elif event.key == K_UP or event.key == K_w:
                    下落方塊['rotation'] = (下落方塊['rotation'] + 1) % len(PIECES[下落方塊['shape']])
                    if not 判斷(板子, 下落方塊):
                        下落方塊['rotation'] = (下落方塊['rotation'] - 1) % len(PIECES[下落方塊['shape']])

                elif event.key == K_q:
                    下落方塊['rotation'] = (下落方塊['rotation'] - 1) % len(PIECES[下落方塊['shape']])
                    if not 判斷(板子, 下落方塊):
                        下落方塊['rotation'] = (下落方塊['rotation'] + 1) % len(PIECES[下落方塊['shape']])

                elif event.key == K_DOWN or event.key == K_s:
                    下移 = True
                    if 判斷(板子, 下落方塊, adjY=1):
                        下落方塊['y'] += 1
                    最後落下時間 = time.time()

                elif event.key == K_SPACE:
                    下移 = False
                    左移 = False
                    右移 = False
                    for i in range(1, 格子高度):
                        if not 判斷(板子, 下落方塊, adjY=i):
                            break
                    下落方塊['y'] += i - 1

                elif event.key == K_c or event.key == K_LSHIFT:  # 加入Keep功能
                    if not 已暫存:  # 每回合只能暫存一次
                        if 暫存方塊 is None:
                            暫存方塊 = 下落方塊
                            下落方塊 = 下一個方塊
                            下一個方塊 = 取得新的一塊()
                        else:
                            暫存方塊, 下落方塊 = 下落方塊, 暫存方塊  # 交換
                        下落方塊['x'] = int(格子寬度 / 2) - int(方塊寬度 / 2)
                        下落方塊['y'] = -2  # 重置位置
                        已暫存 = True  # 本回合已暫存

        if not 判斷(板子, 下落方塊, adjY=1):
            增加分數(板子, 下落方塊)
            分數 += 消除完成的一條線(板子)
            等級, 下落頻率 = 計算關卡與下落頻率(分數)
            下落方塊 = None
            已暫存 = False  # 允許下一回合使用 Keep

        顯示介面.fill(背景顏色)
        畫板子(板子)
        畫狀態(分數, 等級)
        畫新的一塊(下一個方塊)
        if 暫存方塊:
            畫方塊(暫存方塊, X像素=視窗寬度-120, Y像素=180)  # 顯示暫存方塊
        if 下落方塊 is not None:
            畫方塊(下落方塊)

        pygame.display.update()
        FPS計時.tick(FPS)



def makeTextObjs(text, font, color):
    surf = font.render(text, True, color)
    return surf, surf.get_rect()


def 終止():
    pygame.quit()
    sys.exit()


def checkForKeyPress():
    # Go through event queue looking for a KEYUP event.
    # Grab KEYDOWN events to remove them from the event queue.
    點選離開()

    for event in pygame.event.get([KEYDOWN, KEYUP]):
        if event.type == KEYDOWN:
            continue
        return event.key
    return None


def 顯示文字螢幕(text):
    # This function displays large text in the
    # center of the screen until a key is pressed.
    # Draw the text drop shadow
    titleSurf, titleRect = makeTextObjs(text, 放大字型, 文字底部顏色)
    titleRect.center = (int(視窗寬度 / 2), int(視窗高度 / 2))
    顯示介面.blit(titleSurf, titleRect)

    # Draw the text
    titleSurf, titleRect = makeTextObjs(text, 放大字型, 文字顏色)
    titleRect.center = (int(視窗寬度 / 2) - 3, int(視窗高度 / 2) - 3)
    顯示介面.blit(titleSurf, titleRect)

    # Draw the additional "Press a key to play." text.
    pressKeySurf, pressKeyRect = makeTextObjs('Press a key to play.', 基本字型, 文字顏色)
    pressKeyRect.center = (int(視窗寬度 / 2), int(視窗高度 / 2) + 100)
    顯示介面.blit(pressKeySurf, pressKeyRect)

    while checkForKeyPress() == None:
        pygame.display.update()
        FPS計時.tick()


def 點選離開():
    for event in pygame.event.get(QUIT): # get all the QUIT events
        終止() # 終止 if any QUIT events are present
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            終止() # 終止 if the KEYUP event was for the Esc key
        pygame.event.post(event) # put the other KEYUP event objects back


def 計算關卡與下落頻率(分數):
    # Based on the 分數, return the 等級 the player is on and
    # how many seconds pass until a falling 方塊 falls one space.
    等級 = int(分數 / 10) + 1
    下落頻率 = 0.27 - (等級 * 0.02)
    return 等級, 下落頻率

def 取得新的一塊():
    # return a random new 方塊 in a random rotation and color
    形狀 = random.choice(list(PIECES.keys()))
    新的一塊 = {'shape': 形狀,
                'rotation': random.randint(0, len(PIECES[形狀]) - 1),
                'x': int(格子寬度 / 2) - int(方塊寬度 / 2),
                'y': -2, # start it above the 板子 (i.e. less than 0)
                'color': random.randint(0, len(顏色)-1)}
    return 新的一塊


def 增加分數(板子, 方塊):
    # fill in the 板子 based on 方塊's location, shape, and rotation
    for x in range(方塊寬度):
        for y in range(方塊高度):
            if PIECES[方塊['shape']][方塊['rotation']][y][x] != BLANK:
                板子[x + 方塊['x']][y + 方塊['y']] = 方塊['color']


def getBlankBoard():
    # create and return a new blank 板子 data structure
    板子 = []
    for i in range(格子寬度):
        板子.append([BLANK] * 格子高度)
    return 板子


def isOnBoard(x, y):
    return x >= 0 and x < 格子寬度 and y < 格子高度


def 判斷(板子, 方塊, adjX=0, adjY=0):
    # Return True if the 方塊 is within the 板子 and not 碰撞
    for x in range(方塊寬度):
        for y in range(方塊高度):
            isAboveBoard = y + 方塊['y'] + adjY < 0
            if isAboveBoard or PIECES[方塊['shape']][方塊['rotation']][y][x] == BLANK:
                continue
            if not isOnBoard(x + 方塊['x'] + adjX, y + 方塊['y'] + adjY):
                return False
            if 板子[x + 方塊['x'] + adjX][y + 方塊['y'] + adjY] != BLANK:
                return False
    return True

def 是否已完成一行(板子, y):
    # Return True 如果完成一直行沒有空格.
    for x in range(格子寬度):
        if 板子[x][y] == BLANK:
            return False
    return True


def 消除完成的一條線(板子):
    # Remove any completed lines on the 板子, 將上面的方塊下移, and 並回傳完成行數的數量.
    已完成要移除的那一行 = 0
    y = 格子高度 - 1 # start y at the bottom of the 板子
    while y >= 0:
        if 是否已完成一行(板子, y):
            # Remove the line and pull boxes down by one line.
            for pullDownY in range(y, 0, -1):
                for x in range(格子寬度):
                    板子[x][pullDownY] = 板子[x][pullDownY-1]
            # Set very top line to blank.
            for x in range(格子寬度):
                板子[x][0] = BLANK
            已完成要移除的那一行 += 1
            # Note on the next iteration of the loop, y is the same.
            # This is so that if the line that was pulled down is also
            # complete, it will be removed.
        else:
            y -= 1 # move on to check next row up
    return 已完成要移除的那一行


def 變換像素作標(boxx, boxy):
    # Convert the given xy coordinates of the 板子 to xy
    # coordinates of the location on the screen.
    return (中央對齊 + (boxx * 格子大小)), (頂端對齊 + (boxy * 格子大小))


def 畫格子(boxx, boxy, color, X像素=None, Y像素=None):
    # draw a single box (each DO NOT CRY 方塊 has four boxes)
    # at xy coordinates on the 板子. Or, if X像素 & Y像素
    # are specified, draw to the pixel coordinates sto紅 in
    # X像素 & Y像素 (this is used for the "Next" 方塊).
    if color == BLANK:
        return
    if X像素 == None and Y像素 == None:
        X像素, Y像素 = 變換像素作標(boxx, boxy)
    pygame.draw.rect(顯示介面, 顏色[color], (X像素 + 1, Y像素 + 1, 格子大小 - 1, 格子大小 - 1))
    pygame.draw.rect(顯示介面, 亮顏色[color], (X像素 + 1, Y像素 + 1, 格子大小 - 4, 格子大小 - 4))


def 畫板子(板子):
    # draw the border around the 板子
    pygame.draw.rect(顯示介面, 格子顏色, (中央對齊 - 3, 頂端對齊 - 7, (格子寬度 * 格子大小) + 8, (格子高度 * 格子大小) + 8), 5)

    # fill the background of the 板子
    pygame.draw.rect(顯示介面, 背景顏色, (中央對齊, 頂端對齊, 格子大小 * 格子寬度, 格子大小 * 格子高度))
    # draw the individual boxes on the 板子
    for x in range(格子寬度):
        for y in range(格子高度):
            畫格子(x, y, 板子[x][y])


def 畫狀態(分數, 等級):
    # draw the 分數 text
    分數介面 = 基本字型.render('Score: %s' % 分數, True, 文字顏色)
    分數反應 = 分數介面.get_rect()
    分數反應.topleft = (視窗寬度 - 150, 20)
    顯示介面.blit(分數介面, 分數反應)

    # draw the 等級 text
    等級介面 = 基本字型.render('Level: %s' % 等級, True, 文字顏色)
    等級反應 = 等級介面.get_rect()
    等級反應.topleft = (視窗寬度 - 150, 50)
    顯示介面.blit(等級介面, 等級反應)


def 畫方塊(方塊, X像素=None, Y像素=None):
    畫出形狀 = PIECES[方塊['shape']][方塊['rotation']]
    if X像素 == None and Y像素 == None:
        # if X像素 & Y像素 hasn't been specified, use the location sto紅 in the 方塊 data structure
        X像素, Y像素 = 變換像素作標(方塊['x'], 方塊['y'])

    # draw each of the boxes that make up the 方塊
    for x in range(方塊寬度):
        for y in range(方塊高度):
            if 畫出形狀[y][x] != BLANK:
                畫格子(None, None, 方塊['color'], X像素 + (x * 格子大小), Y像素 + (y * 格子大小))


def 畫新的一塊(方塊):
    # draw the "next" text
    新的介面 = 基本字型.render('Next:', True, 文字顏色)
    新的反應 = 新的介面.get_rect()
    新的反應.topleft = (視窗寬度 - 120, 80)
    顯示介面.blit(新的介面, 新的反應)
    # draw the "next" 方塊
    畫方塊(方塊, X像素=視窗寬度-120, Y像素=100)


if __name__ == '__main__':
    main()