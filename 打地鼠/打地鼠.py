import pygame
import time
from random import randint
#視窗大小
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
#常用顏色
GREEN = (73,188,11)
WHITE = (255,255,255)
#地鼠座標 / 分數 /遊戲時間 / 開始時間 / 狀態
x,y = None,None
score = 0
game_time = 20
start_time = 0
state = 0 #首頁0 遊戲中1 結束2
#建立視窗及頻率鐘
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('打地鼠')
clock = pygame.time.Clock()
#載入遊戲圖片
mallet = pygame.image.load('mallet.png') 
down_mallet = pygame.image.load('down-mallet.png')
mole = pygame.image.load('mole.png') 
grass = pygame.image.load('grass.png') 
#隱藏滑鼠座標顯示及初始化文字模組
pygame.mouse.set_visible(False)
pygame.font.init()

def welcome_screen():
    screen.fill(GREEN)
    font = pygame.font.SysFont('corbel',48)
    text = font.render('Press ENTER to start',False,WHITE)
    screen.blit(text,((SCREEN_WIDTH - text.get_width()) / 2, 185 ) )
    screen.blit(mallet,(200,350))
    screen.blit(mole,(120,50))
    # 取得槌子的矩形範圍
    mallet_position = mallet.get_rect()
    # 將槌子的中心點設在滑鼠點的位置
    mallet_position.center = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
         screen.blit(down_mallet, mallet_position)
    else:
         screen.blit(mallet, mallet_position)

    
def play():
   # 取用遊戲狀態、分數及開始時間資訊
   global state, score, start_time
   # 設定遊戲開始時間 time.time() 會取得目前的時間
   start_time = time.time()
   # 將分數歸 0 且狀態設定為 1 遊玩中
   score = 0
   state = 1
   # 產生新的老鼠（這邊先立一個函式之後完成）
   new_mole()
   # 產生瞬間先檢查是否有被打到（這邊先立一個函式之後完成）
   whack()
 
def end():
   # 狀態改為 2 結束遊戲
   global state
   state = 2
 
def new_mole():
   # 隨機決定下一個老鼠產生的位置
   global x, y
   # x 從螢幕最左到右邊扣掉老鼠的寬都能取, y 則向下移 30 到底部扣掉老鼠的高都能取
   x = randint(0, SCREEN_WIDTH - mole.get_width())
   y = randint(30, SCREEN_HEIGHT - mole.get_height())
 
def whack():
   global score
   # 取得滑鼠當前的位置
   mx, my = pygame.mouse.get_pos()
   # 取得老鼠的寬及高
   width, height = mole.get_size()
   # 將座標計算是不是點擊在老鼠的圖片上, 如果有的話要加分和產生下一隻新的
   if abs(mx - x - width / 2) <= width / 2 and abs(my - y - height / 2) <= height / 2:
       score += 1
       new_mole()


def play_screen():
    screen.blit(grass,(0,0))
    font = pygame.font.SysFont('corbel',30)
    text_sc = font.render(str(score),False,WHITE)
    current = game_time - (time.time() - start_time)
    if current <= 0:
          end()
    text_time = font.render(str(int(current)),False,WHITE)
    if pygame.mouse.get_pressed()[0]:
        screen.blit(down_mallet, pygame.mouse.get_pos())
    else:
        screen.blit(mallet,pygame.mouse.get_pos())
    screen.blit(text_sc,(10,0))
    screen.blit(text_time,(370,0))
    screen.blit(mole,(x,y))
        
def end_screen():
    # 背景填滿綠色
    screen.fill(GREEN)
    # 設定字體樣板分別顯示遊戲結束、分數及重新開始按鈕
    font = pygame.font.Font(None, 30)
    game_over = font.render("GAME OVER", False, WHITE)
    font = pygame.font.Font(None, 25)
    points = font.render("Score: " + str(score), False, WHITE)
    font = pygame.font.Font(None, 22)
    restart = font.render("Press ENTER to play again", False, WHITE)
    # 將上述資訊顯示到螢幕上
    screen.blit(game_over, (SCREEN_WIDTH / 2 - game_over.get_width() / 2, 100))
    screen.blit(points, (SCREEN_WIDTH / 2 - points.get_width() / 2, 200))
    screen.blit(restart, (SCREEN_WIDTH / 2 - restart.get_width() / 2, 300))

    
#遊戲執行
running=True
while running:
    #事件處理
    for event in pygame.event.get():
        #當遊戲視窗被關閉
        if event.type==pygame.QUIT:#當遊戲視窗被關閉
            running=False
        elif state == 0:#遊戲還沒開始的事件
           if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    play()
        elif state == 1:#遊戲中的事件
           if event.type == pygame.MOUSEBUTTONDOWN:
               whack()
        elif state == 2:#遊戲結束的事件
             if event.type == pygame.KEYDOWN and event.key ==pygame.K_RETURN:
                   play()
        if state == 0:#還沒開始的畫面
            welcome_screen()
        elif state == 1:#遊戲中的畫面
            play_screen()
        elif state == 2:#遊戲結束的畫面
            end_screen()
        clock.tick(60)#限制畫面最高更新 60 FPS
        pygame.display.update()#更新畫面      
pygame.quit()

# pip install auto-py-to-exe
# auto-py-to-exe