from typing import List


class Thing:
    '''Класс содержит все вещи для игры'''
    def __init__(self,
                 name: str,
                 percent_def: float,
                 value_atk: int,
                 value_hp: int,
                 ) -> None:
        self.name = name
        self.percent_def = percent_def
        self.value_atk = value_atk
        self.value_hp = value_hp

class Person:
    '''Базовый класс персонажа'''
    def __init__(self,
                 name: str,
                 basic_hp: int,
                 basic_atk: int,
                 basic_percent_def: float,
                 ) -> None:
        self.name = name
        self.basic_hp = basic_hp
        self.basic_atk = basic_atk
        self.basic_percent_def = basic_percent_def

    def set_things(things: List[str]):
        '''Метод принимающий список вещей'''
        pass

    def subtraction_hp():
        '''Вычитание жизней на основе полученной атаки'''
        pass

class Paladin(Person):
    '''Класс Паладина'''
    def __init__(self,
                 name: str, 
                 basic_hp: int,
                 basic_atk: int,
                 basic_percent_def: float) -> None:
        super().__init__(name, basic_hp, basic_atk, basic_percent_def)
        basic_hp *= 2
        basic_percent_def *= 2

class Warrior(Person):
    '''Класс воина'''
    def __init__(self,
                 name: str, 
                 basic_hp: int,
                 basic_atk: int,
                 basic_percent_def: float) -> None:
        super().__init__(name, basic_hp, basic_atk, basic_percent_def)
        basic_atk *= 2

class Battle: