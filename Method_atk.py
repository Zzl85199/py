class Pokemon:
    def __init__(self, name, type, hp, attack_power):
        self.name = name
        self.type = type
        self.hp = hp
        self.attack_power = attack_power
    
    def attack(self, other_pokemon):
        print(f"{self.name} 使用攻擊對 {other_pokemon.name} 造成 {self.attack_power} 點傷害！")
        other_pokemon.take_damage(self.attack_power)
    
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            print(f"{self.name} 倒下了！")
        else:
            print(f"{self.name} 剩餘 HP: {self.hp}")

pikachu = Pokemon("皮卡丘", "電", 100, 20)
bulbasaur = Pokemon("妙蛙種子", "草", 120, 15)

pikachu.attack(bulbasaur)

bulbasaur.attack(pikachu)
