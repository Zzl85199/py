import random

def catch_pokemon(pokemon_name, current_hp, max_hp, base_catch_rate):
    hp_factor = (max_hp - current_hp) / max_hp  # HP 越低，捕捉機率越高
    final_catch_rate = base_catch_rate + (hp_factor * (1 - base_catch_rate))
    
    if random.random() < final_catch_rate:
        print(f"成功捕捉 {pokemon_name}！")
        return True
    else:
        print(f"捕捉 {pokemon_name} 失敗，它逃走了！")
        return False

# 範例使用
pokemon_name = "噴火龍"
current_hp = 20
max_hp = 150
base_catch_rate = 0.3  # 基礎捕捉率 30%

catch_pokemon(pokemon_name, current_hp, max_hp, base_catch_rate)
