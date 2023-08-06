import random
from abc import ABCMeta, abstractmethod

from wargame.gameuniterror import HealthMeterException
from wargame.gameutils import weighted_random_selection, print_bold


class AbstractGameUnit(metaclass=ABCMeta):
    def __init__(self, name=''):
        self.max_hp = 0
        self.health_meter = 0
        self.name = name
        self.enemy = None
        self.unit_type = None

    @abstractmethod
    def info(self):
        pass

    def attack(self, enemy):
        injured_unit = weighted_random_selection(self, enemy)
        injury = random.randint(10, 15)
        injured_unit.health_meter = max(injured_unit.health_meter - injury, 0)
        print("ATTACK! ", end='')
        self.show_health(end=' ')
        enemy.show_health(end=' ')

    def heal(self, heal_by=2, full_healing=True):
        if self.health_meter == self.max_hp:
            return
        if full_healing:
            self.health_meter = self.max_hp
        else:
            self.health_meter += heal_by
            # assert (self.health_meter + heal_by <= self.max_hp)

        if self.health_meter > self.max_hp:
            raise HealthMeterException("health_meter > max_hp!")

        print_bold("You are HEALED!", end=' ')
        self.show_health(bold=True)

    def reset_health_meter(self):
        self.health_meter = self.max_hp

    def show_health(self, bold=False, end='\n'):
        msg = "Health: %s: %d" % (self.name, self.health_meter)

        if bold:
            print_bold(msg, end=end)
        else:
            print(msg, end=end)