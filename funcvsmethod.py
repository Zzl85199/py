'''Function講解'''
#獨立的計算函數
#def add(a, b):
#    return a + b
#result = add(3, 4)
#print(result)  

'''Method講解'''
#class Person:
#    def __init__(self, name):
#        self.name = name  # self.name 指的是物件自己的 name 屬性
#
#    def greet(self):
#        return f"Hello, my name is {self.name}"  # self.name 取當前物件的 name 屬性
#
# 創建物件實例
#person1 = Person("Alice")
#person2 = Person("Bob")
#
# 調用greet方法
#print(person1.greet())  
#print(person2.greet())  





'''用來講解參數傳遞的錯誤程式碼'''
#class Person:
#    def __init__(name):  # 沒有self
#        name = name  # 這裡沒有將name屬性賦值給self
#
#    def greet(obj):  #()內一定要加入一個參數，因為下面物件呼叫greet()時會自動傳遞1個參數，即物件本身（person）。
#        return f"Hello, my name is {obj}"  # 如果在is後面加入{name}變數，其中{name}不屬於物件，所以call不到
# 創建物件
#person = Person()
#print(person.greet())



'''案例演練-汽車 Method'''
#class Car:
#    def __init__(self, name, hp, speed):
#        self.name = name
#        self.hp = hp
#        self.speed = speed
#
#    def show(obj):
#        return f"我的{obj.name}有{obj.hp}馬力，極限車速大約是{obj.speed}公里"  #1
#        #print(f"我的{obj.name}有{obj.hp}馬力，極限車速大約是{obj.speed}公里")  #2
#
#Tesla = Car("modelX", 1000, 240)
#Toyota = Car("camry", 200, 180)
#
#print(Tesla.show())  #1
#print(Toyota.show()) #1
##Tesla.show()  #2
##Toyota.show() #2

'''Function實作Car範例'''
#def create_car(name, speed): # 定義一個函數來創建車輛（模擬類別的初始化）
#    return {'name': name, 'speed': speed} # 返回一個包含車輛信息的字典
#def describe_car(car): # 定義一個函數來描述車輛
#    return f"{car['name']} can go up to {car['speed']} km/h"
#
# 創建車輛
#my_car = create_car("Tesla", 250)
#another_car = create_car("Toyota", 180)
#print(describe_car(my_car))       # 輸出：Tesla can go up to 250 km/h
#print(describe_car(another_car))  # 輸出：Toyota can go up to 180 km/h

#'''list vs dict vs tuple'''
#my_car_list = ['Tesla', 250]
#print(my_car_list)
#my_car_list[0] = 'Toyota'
#print(my_car_list)
#
#my_car_dict = {'name':'Tesla', 'speed':250}
#print(my_car_dict)
#my_car_dict[0] = 'Toyota' # dict是鍵-值配對，沒有0這個鍵
#print(my_car_dict)
#my_car_dict['name'] = 'Toyota'
#print(my_car_dict)
#
#my_car_tuple = ('Tesla', 250)
#print(my_car_tuple)
#my_car_tuple(0) = 'Toyota' #錯誤
#my_car_tuple[0] = 'Toyota' #TypeError: 'tuple' object does not support item assignment

#print('計算平均')
#total = int(input('總和'))
#count = int(input('個數'))
#if count>0:
#    print('答案是', total/count)
#else:
#    print('無法計算-個數為0')

#a = 33
#b = 200
#if a>b :
#    print('a大')
#else :
#    print('b大')

#print('我要買電影票')
#identity = input('請輸入身分')
#count = int(input('請輸入人數'))
#
#price = 320*count
#
#if identity == '學生':
#    price *=0.8
#
#print('總價', price)

#Score = int(input('分數'))
#if 80 <= Score <= 100:
#    print('A')
#elif 60<=Score<=79:
#    print('B')
#elif 0<=Score<=59:
#    print('F')
#else:
#    print('不在設定範圍內')
#
#
#
#x = float(input("請輸入 x 座標: "))
#y = float(input("請輸入 y 座標: "))
#
#
#if x > 0 and y > 0:
#    print("該點位於第一象限")
#elif x < 0 and y > 0:
#    print("該點位於第二象限")
#elif x < 0 and y < 0:
#    print("該點位於第三象限")
#elif x > 0 and y < 0:
#    print("該點位於第四象限")
#elif x == 0 and y != 0:
#    print("該點位於y軸上")
#elif y == 0 and x != 0:
#    print("該點位於x軸上")
#else:
#    print("該點位於原點")


#x=5
#if x<=5:
#    pass
#else:
#    print('Hi')

#for j in range(1, 10):
#    for i in range(1, 10):
#        print(j, '*', i, '=', i*j, sep='', end=' ')
#    print()

#for i in range(5):
#    print("A", end=' ')
#    for j in range(3):
#        print("*", end='')
#        if j == 2:
#            break
#    print()

#x=0
#n=5
#for i in range(1, n+1):
#    for j in range(1, n+1):
#        if i+j==2:
#            x+=2
#        if i+j==3:
#            x+=3
#        if i+j==4:
#            x+=4
#print(x)

'''a005. Eva 的回家作業'''
#t = input()
#for i in range(1, int(t)+1):
#    list1 = [int(x) for x in input().split()]
#
#    if (list1[1]-list1[0] == list1[2]-list1[1]):
#        list1.append(list1[3] + (list1[1]-list1[0]))
#
#    elif (list1[1]/list1[0] == list1[2]/list1[1]):
#        list1.append(int(list1[3]*(list1[1]/list1[0])))
#
#    print(*list1)

'''a215. 明明愛數數'''
#while True:
#    try:
#        a,b=map(int,input().split())
#        c=a
#    except:
#        break
#    sum=0
#    while True:
#        sum+=a
#        a+=1
#        if sum>b:
#            break
#    print(a-c)

'''d071. 格瑞哥里的煩惱 (EOF 版)'''
#while(True):
#    try:
#        i=int(input())
#    except:
#        break
#    if i%4==0 and i%100!=0 or i%400==0:
#        print("a leap year")
#    else:
#        print("a normal year")

#x='variable'
#for var in x,'red',1,'green',2,'blue':
#    print(var)

#A,B,C = input().split()
#print(A)
#
#a,b,c = map(int,input().split())
#print(a+b+c) 

#for i in list(range(3)):
#    print(i)

#'''RPG剪刀石頭布遊戲'''
#import random
#
#'''定義角色的初始屬性'''
#class Player:
#    def __init__(self, name):
#        self.name = name
#        self.hp = 100
#
#    def take_damage(self, damage):
#        self.hp -= damage
#        if self.hp < 0:
#            self.hp = 0
#
#    def is_alive(self):
#        return self.hp > 0
#
#choices = ["剪刀", "石頭", "布"]
#
#'''判斷勝負的函數'''
#def determine_winner(player_choice, computer_choice):
#    if player_choice == computer_choice:
#        return "平手"
#    elif (player_choice == "剪刀" and computer_choice == "布") or \
#         (player_choice == "布" and computer_choice == "石頭") or \
#         (player_choice == "石頭" and computer_choice == "剪刀"):
#        return "玩家"
#    else:
#        return "電腦"
#'''遊戲主函數'''
#def game():
#    player_name = input("請輸入你的名字: ")
#    player = Player(player_name)
#    computer = Player("電腦")
#
#    print(f"歡迎來到剪刀石頭布對戰, {player.name}!")
#
#    while player.is_alive() and computer.is_alive():
#        print(f"\n{player.name} 的HP: {player.hp} | 電腦的HP: {computer.hp}")
#        
#        # 玩家選擇
#        player_choice = input("請選擇 (剪刀, 石頭, 布): ")
#        while player_choice not in choices:
#            print("無效的選擇，請重新選擇")
#            player_choice = input("請選擇 (剪刀, 石頭, 布): ")
#
#        # 電腦隨機選擇
#        computer_choice = random.choice(choices)
#        print(f"電腦選擇了: {computer_choice}")
#
#        # 判斷勝負
#        result = determine_winner(player_choice, computer_choice)
#
#        if result == "玩家":
#            print(f"{player.name} 勝利！")
#            computer.take_damage(20)
#        elif result == "電腦":
#            print("電腦勝利！")
#            player.take_damage(20)
#        else:
#            print("這局平手！")
#
#    # 遊戲結束
#    if player.is_alive():
#        print(f"\n{player.name} 獲勝了！")
#    else:
#        print("\n電腦獲勝了！")
#
## 開始遊戲
#game()

#for i in 'red', 'green', 'blue':
#    print(i)

import random

# 定義地圖上的地點，每個地點可以購買或者交租金
class Place:
    def __init__(self, name, price, rent):
        self.name = name
        self.price = price
        self.rent = rent
        self.owner = None

# 定義玩家
class Player:
    def __init__(self, name):
        self.name = name
        self.money = 1500  # 初始金額
        self.position = 0  # 起始位置
        self.properties = []  # 擁有的房地產

    def move(self, steps, board_size):
        self.position = (self.position + steps) % board_size

    def buy_property(self, place):
        if self.money >= place.price:
            self.money -= place.price
            place.owner = self
            self.properties.append(place)
            print(f"{self.name} 購買了 {place.name}")
        else:
            print(f"{self.name} 資金不足，無法購買 {place.name}")

    def pay_rent(self, owner, rent):
        if self.money >= rent:
            self.money -= rent
            owner.money += rent
            print(f"{self.name} 向 {owner.name} 支付了 {rent} 的租金")
        else:
            print(f"{self.name} 無法支付租金，破產！")
            self.money = 0

# 遊戲地圖
def create_board():
    return [
        Place("起點", 0, 0),
        Place("公園", 200, 50),
        Place("商店街", 300, 80),
        Place("學校", 250, 60),
        Place("超市", 400, 100),
        Place("醫院", 350, 90),
        Place("圖書館", 150, 40),
        Place("遊樂場", 500, 120)
    ]

# 擲骰子
def roll_dice():
    return random.randint(1, 6)

# 遊戲主函數
def game():
    board = create_board()
    board_size = len(board)

    # 初始化兩名玩家
    player1 = Player("玩家1")
    player2 = Player("玩家2")
    players = [player1, player2]
    
    turn = 0

    while player1.money > 0 and player2.money > 0:
        current_player = players[turn % 2]
        print(f"\n{current_player.name} 的回合!")

        # 擲骰子並移動
        steps = roll_dice()
        print(f"{current_player.name} 擲出了 {steps}")
        current_player.move(steps, board_size)

        current_place = board[current_player.position]
        print(f"{current_player.name} 來到了 {current_place.name}")

        # 如果該地點有主人
        if current_place.owner is None:
            if current_place.price > 0:
                print(f"{current_place.name} 的價格是 {current_place.price}，租金是 {current_place.rent}")
                buy_choice = input("你想購買這個地點嗎？(y/n): ").lower()
                if buy_choice == 'y':
                    current_player.buy_property(current_place)
        else:
            if current_place.owner != current_player:
                print(f"{current_place.name} 已經被 {current_place.owner.name} 擁有，需支付租金 {current_place.rent}")
                current_player.pay_rent(current_place.owner, current_place.rent)

        # 顯示玩家狀態
        print(f"{player1.name} 的餘額: {player1.money}，擁有資產: {[p.name for p in player1.properties]}")
        print(f"{player2.name} 的餘額: {player2.money}，擁有資產: {[p.name for p in player2.properties]}")

        # 回合結束
        turn += 1

    # 判斷勝負
    if player1.money > 0:
        print(f"{player1.name} 獲勝！")
    else:
        print(f"{player2.name} 獲勝！")

# 開始遊戲
game()
