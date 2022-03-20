from typing import List, Dict, Type
import random


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
        print(f'Сгенерирован предмет {self.name}. Жизнь:{self.value_hp}; Атака: {self.value_atk}; Процент защиты {self.percent_def:.3f}.')

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
        print(f'Паладин {name} родился. Жизни:{basic_hp}, {basic_atk}, {basic_percent_def:.3f}')

class Warrior(Person):
    '''Класс воина'''
    def __init__(self,
                 name: str, 
                 basic_hp: int,
                 basic_atk: int,
                 basic_percent_def: float) -> None:
        super().__init__(name, basic_hp, basic_atk, basic_percent_def)
        basic_atk *= 2
        print(f'Воин {name} родился. Жизни:{basic_hp}, {basic_atk}, {basic_percent_def:.3f}')

def generate_things(count_thing: int) -> None:
    '''Генерирует вещи до 20 штук'''
    #Позже можно дописать проверку на количество вещей принимаемых вещей
    DATA_NAME_THINGS: List[str] = ['Элексир бесмертия', 'Меч святого',
                                   'Наплечники удачи', 'Броня старого вояки',
                                   'Кольцо подмены', 'Кольцо золота',
                                   'Кольцо жизненной силы', 'Кольцо маны',
                                   'Многоразовое зелье жизни', 'Плащ следопыта',
                                   'Сапоги строго вояки', 'Перчатки стрелка',
                                   'Легкий арбалет', 'Книга огненого шара',
                                   'Говорящая шляпа','Свиток красной руки',
                                   'Шипастый щит','Яд смерти',
                                   'Молот тысячи гномов','Кольцо Намиры']
    percent_def =[]
    for k in range(0, count_thing): 
        percent_def.append(random.uniform(0, 0.1))
    percent_def.sort()
    for i in range(0, count_thing):
        value_atk: int = random.randint(0, 10)
        value_hp: int = random.randint(1, 5)
        Thing(DATA_NAME_THINGS[i], percent_def[i], value_atk, value_hp)

def generate_persons(сount_person:int) -> None:
    '''Создает персонажей до 20 штук'''
    DATA_NAME_PERSONS: List[str] = ['Анакин', 'Джоффри',
                       'Гэндальф', 'Хан Соло',
                       'Саурон', 'Джарет',
                       'Гаюс', 'Эмметт',
                       'Фокс', 'Ронан',
                       'Септимус', 'Спок',
                       'Тирион', 'Зак',
                       'Райлан','Роуэн',
                       'Рори','Северус',
                       'Салазар','Фродо']
    DATA_CLASS_PERSON: Dict[str, Type(Person)] = {
        0: Paladin,
        1: Warrior
    }
    for i in range(0, сount_person):#генерирование данных персонажа
        name = random.choice(DATA_NAME_PERSONS)
        DATA_NAME_PERSONS.remove(name)
        basic_hp = random.randint(50, 150)
        basic_atk = random.randint(5, 15)
        basic_percent_def = random.uniform(0, 0.1)
        DATA_CLASS_PERSON[random.randint(0, 1)](name, basic_hp, basic_atk, basic_percent_def)
    
generate_things(10)
generate_persons(10)