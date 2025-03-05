import random

class Pokemon:
    def __init__(self, name, type, max_hp, attack_power):
        self.name = name
        self.type = type
        self.hp = max_hp
        self.max_hp = max_hp
        self.attack_power = attack_power
    
    def attack(self, other_pokemon):
        damage = self.calculate_damage(other_pokemon)
        print(f"{self.name} 對 {other_pokemon.name} 造成 {damage} 點傷害！")
        other_pokemon.take_damage(damage)
    
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            print(f"{self.name} 倒下了！")
        else:
            print(f"{self.name} 剩餘 HP: {self.hp}")
    
    def is_fainted(self):
        return self.hp <= 0
    
    def calculate_damage(self, other_pokemon):
        type_effectiveness = {
            ('電', '水'): 2,
            ('水', '火'): 2,
            ('火', '草'): 2,
            ('草', '水'): 2
        }
        multiplier = type_effectiveness.get((self.type, other_pokemon.type), 1)
        return self.attack_power * multiplier

def catch_pokemon(pokemon, base_catch_rate):
    if pokemon.is_fainted():
        print(f"無法捕捉 {pokemon.name}，因為它已經倒下！")
        return False
    if pokemon.hp == pokemon.max_hp:
        print(f"{pokemon.name} 的 HP 滿格，難以捕捉！")
        return False
    
    hp_factor = (pokemon.max_hp - pokemon.hp) / pokemon.max_hp
    final_catch_rate = base_catch_rate + (hp_factor * (1 - base_catch_rate))
    if pokemon.hp < 10:
        final_catch_rate += 0.1  # HP 太低，捕捉率提高 10%
    
    if random.random() < final_catch_rate:
        print(f"成功捕捉 {pokemon.name}！")
        return True
    else:
        print(f"捕捉 {pokemon.name} 失敗，它逃走了！")
        return False

# 創建兩隻寶可夢
pikachu = Pokemon("皮卡丘", "電", 100, 20)
charmander = Pokemon("小火龍", "火", 120, 15)

def battle_and_capture(player, wild_pokemon, ball_type):
    poke_ball_rates = {"Poke Ball": 0.3, "Great Ball": 0.5, "Ultra Ball": 0.7}
    if ball_type not in poke_ball_rates:
        print("無效的精靈球類型！")
        return False
    
    print(f"野生的 {wild_pokemon.name} 出現了！")
    while not wild_pokemon.is_fainted():
        player.attack(wild_pokemon)
        if wild_pokemon.is_fainted():
            break
        
        action = input("要攻擊(A) 還是丟精靈球(C)？").strip().upper()
        if action == "C":
            if catch_pokemon(wild_pokemon, poke_ball_rates[ball_type]):
                return True
    return False

# 進行戰鬥並嘗試捕捉
battle_and_capture(pikachu, charmander, "Great Ball")
