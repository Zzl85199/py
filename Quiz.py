import random

# 遊戲初始化
number_to_guess = random.randint(1, 100)
attempts = 0
guesses = []

print("歡迎來到猜數字遊戲！")
print("我已經選擇了一個 1 到 100 之間的數字。來猜猜看是什麼數字吧！")

# 開始遊戲
while True:
    try:
        guess = int(input("請輸入你猜的數字： "))
        attempts += 1
        guesses.append(guess)

        # 判斷玩家的猜測
        if guess < number_to_guess:
            print("太小了，再試一次！")
        elif guess > number_to_guess:
            print("太大了，再試一次！")
        else:
            print(f"恭喜你！你在第 {attempts} 次猜對了數字 {number_to_guess}！")
            break  # 猜對了，結束遊戲
    except ValueError:
        print("請輸入一個有效的數字。")

# 顯示歷史猜測
print("\n你猜過的數字是：")
for i, g in enumerate(guesses, start=1):
    print(f"第 {i} 次猜：{g}")

print("遊戲結束，感謝你的遊玩！")
