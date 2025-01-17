from loguru import logger


class Weapon(object):

    def __init__(self, name, attack, denfense):
        self.name = name
        self.attack = attack
        self.denfense = denfense


class Player(object):

    def __init__(self, name, health=100, gold=100, defense=100, attack=100, level=1, weapon_list=[]):
        self.name = name
        self.health = health
        self.gold = gold
        self.defense_val = defense
        self.attack_val = attack
        self.level = level
        self.weapon_list = weapon_list

    def attack(self, defenser, weapon_index=None):

        if weapon_index is None:
            damage = int(self.attack_val - defenser.defense_val / 10)
        else:
            damage = int((self.weapon_list[weapon_index].attack - defenser.defense_val) / 10)

        if damage > 0:
            defenser.health -= damage
            logger.info(f"{self.name}成功攻击了{defenser.name}，造成了{damage}点伤害。")
        else:
            logger.info(f"{self.name}的攻击被{defenser.name}防御了。")

    def buy_weapon(self, weapon):
        self.weapon_list.append(weapon)
        logger.info(f"{self.name}购买装备{weapon.name}!")

    def level_up(self):
        self.level += 1
        self.gold += 100
        logger.info(f"{self.name}升级了，奖励金币100！")


yuan = Player("yuan")
alex = Player("alex")

w1 = Weapon("屠龙刀", 250, 90)
w2 = Weapon("倚天剑", 350, 120)

yuan.buy_weapon(w1)
yuan.buy_weapon(w2)

yuan.attack(alex, 0)
print(alex.health)
yuan.attack(alex, 1)
print(alex.health)
alex.attack(yuan)
