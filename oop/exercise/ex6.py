from random import randrange

class Player:
    def __init__(self, name):
        self.__name = str(name)
        self.__health = 10
        self.__potion = 2
    
    @property
    def name(self):
        return self.__name
    
    @property
    def health(self):
        return self.__health
    
    @property
    def potion(self):
        return self.__potion

    def __str__(self):
        text = f"{self.name} (Health: {self.health}, Potions Left: {self.potion})"
        return text

    def __repr__(self):
        return self.__str__()
    
    def update(self, value, heal=False):
        if heal and (0 < self.health < 10):
            if self.__health + value > 10:
                self.__health = 10
            else:
                self.__health += value
            return self.health
        else:
            if self.health - value <= 0:
                self.__health = 0
                return 0
            else:
                self.__health = self.health - value
                return self.health
    
    def attack(self, other):
        other_health = other.update(1)
        if other_health > 0:
            return False
        else:
            return True
    
    def risk(self, other):
        success = randrange(1, 11) == 10
        if success:
            other_health = other.update(5)
            if other_health > 0:
                return False
            else:
                return True
        else:
            return False
    
    def heal(self):
        if self.potion <= 0:
            return False
        else:
            self.__potion -= 1
            pot = randrange(1,5)
            if self.health + pot >= 10:
                self.__health = 10
            else:
                self.__health += pot
            return True

class Enemy(Player):
    def move(self, other):
        option = randrange(1,4)
        if option == 1:
            print(f"{self.name} attacked.")
            return self.attack(other)
        elif option == 2:
            print(f"{self.name} took a risk.")
            return self.risk(other)
        else:
            print(f"{self.name} healed.")
            return self.heal()

p1 = Player("Player 1")
e1 = Enemy("Enemy 1")
print(p1)
print(e1)

turn = 0
while True:
    turn += 1
    print(f"Turn {turn}.\n -- {p1}\n -- {e1}")
    
    options = f"""{p1.name}'s options:
    1. Attack
    2. Risk
    3. Heal
    """
    print(options)
    user_input = int(input("Enter optons (1/2/3):"))
    if user_input == 1:
        p1.attack(e1)
    elif user_input == 2:
        p1.risk(e1)
    else:
        p1.heal()
    
    e1.move(p1)
