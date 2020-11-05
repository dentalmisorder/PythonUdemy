class Item():
    
    def __init__(self, name, hp_restore, mp_restore, attack, sell_cost, description, is_poisoned):
        self.name = name
        self.description = description
        self.sell_cost = sell_cost
        self.attack = attack
        self.is_poisoned = is_poisoned

        if self.is_poisoned:
            self.hp_restore = -hp_restore
            self.mp_restore = -mp_restore
            self.is_poisoned = '☢☢☢☢☢☢☢☢'
        else:
            self.hp_restore = abs(hp_restore)
            self.mp_restore = abs(mp_restore)
            self.is_poisoned = '☯☯☯☯☯☯☯☯'

    def __str__(self):
        return f"""
        ✦ {self.name} stats ✦
        ❤ HP: {self.hp_restore} ❤
        ❖ MP: {self.mp_restore} ❖
        ☠ ATK: {self.attack} ☠
        {self.is_poisoned}

                                Sell for: {self.sell_cost} ◎
        """

    def __len__(self):
        return self.sell_cost

Infinity_Edge = Item("Infinity Edge", 0, 0, 80, 2340, "UNIQUE: Increase Critical Strike Damage by 25%.", False)

print(Infinity_Edge)
        