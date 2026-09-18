from abc import ABC, abstractmethod


class Creature:
    def __init__(self, attack, health):
        self.attack = attack
        self.health = health
        # Temporary damage jaoks peame meeles ka olendi algset elupunkti
        self.max_health = health


class CardGame(ABC):
    def __init__(self, creatures):
        self.creatures = creatures

    # See on üldine raam-meetod (Template Method)
    def combat(self, c1_index, c2_index):
        c1 = self.creatures[c1_index]
        c2 = self.creatures[c2_index]

        # Mõlemad olendid ründavad üheaegselt teineteist
        c1_alive = self.hit(attacker=c2, defender=c1)
        c2_alive = self.hit(attacker=c1, defender=c2)

        # Tagastatava väärtuse loogika kontroll
        if (c1_alive and c2_alive) or (not c1_alive and not c2_alive):
            return -1
        elif c1_alive:
            return c1_index
        else:
            return c2_index

    @abstractmethod
    def hit(self, attacker, defender):
        pass


class TemporaryDamageCardGame(CardGame):
    def hit(self, attacker, defender):
        # Vähendame kaitsja elusid ründaja rünnakutugevuse võrra
        defender.health -= attacker.attack

        # Kontrollime, kas kaitsja jäi ellu
        if defender.health > 0:
            # Kuna tegu on ajutise kahjuga, taastuvad elud algväärtusele
            defender.health = defender.max_health
            return True
        else:
            return False


class PermanentDamageCardGame(CardGame):
    def hit(self, attacker, defender):
        # Vähendame kaitsja elusid ründaja rünnakutugevuse võrra
        defender.health -= attacker.attack

        # Püsiva kahju korral me elusid ei taasta, vaid vaatame otse tulemust
        return defender.health > 0