from time import sleep


class Hero():
    def __init__(self, name, health, armor, power, weapon, crit_chance):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon
        self.crit_chance = crit_chance

    def print_info(self):
        print("имя:", self.name,
              "\nздоровье", self.health,
              "\nброня", self.armor,
              "\nсила", self.power,
              "\nоружие", self.weapon,
              "\nкритичиский урон", self.crit_chance)

    def strike(self, enemy):
        print(self.name, ' наносит', self.power - enemy.armor,
              ' урона', enemy.name)
        enemy.health -= self.power - enemy.armor
        print(self.health)

    def fight(self, enemy):
        while self.health > 0 and enemy.health > 0:
            self.strike(enemy)
            sleep(1)
            enemy.strike(self)
            sleep(1)
        print('Бой окончен')


knight = Hero('Артур', 100, 15, 25, 'булава', 10)
knight.print_info()
print('\n')
murder = Hero('Злоба', 25, 5, 25, 'кинжал', 10)
murder.print_info()
knight.fight(murder)