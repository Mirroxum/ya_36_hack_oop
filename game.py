from typing import List, Dict, Type
import random


class Thing:
    
    '''Класс содержит все вещи для игры'''
    def __init__(self,
                 name_thing: str,
                 percent_def: float,
                 value_atk: int,
                 value_hp: int,
                 ) -> None:
        self.name_thing = name_thing
        self.percent_def = percent_def
        self.value_atk = value_atk
        self.value_hp = value_hp
        print(f'Сгенерирован предмет {self.name_thing}. Жизнь:{self.value_hp}; Атака: {self.value_atk}; Процент защиты {self.percent_def:.3f}.')

class Person:
    '''Базовый класс персонажа'''
    def __init__(self,
                 name_person: str,
                 basic_hp: int,
                 basic_atk: int,
                 basic_percent_def: float,
                 ) -> None:
        self.name_person = name_person
        self.basic_hp = basic_hp
        self.basic_atk = basic_atk
        self.basic_percent_def = basic_percent_def
    
    def set_things(self, things):
        '''Получаем все предметы из судука, возвращаем предметы, которые взяли'''
        if len(things) >= 4:
            count_things = random.randint(0, 4)    
        else:
            count_things = random.randint(0, len(things))
        if count_things == 0:
            print(f'{self.name_person} не получает предметов')
            return None
        else:
            received_items = []
            received_items_name = [] #имена полученных предметов
            for i in range(0, count_things):
                get_thing = random.choice(things) #получили предмет
                received_items_name.append(get_thing.name_thing) #записали в список
                received_items.append(get_thing)
                things.remove(get_thing) #удалили элемент
            print(f'{self.name_person} получает {count_things} предмет(а): {", ".join(received_items_name)}')
            return received_items

    def count_items():
        return count_items

    def subtraction_hp():
        '''Вычитание жизней на основе полученной атаки'''
        pass

class Paladin(Person):
    '''Класс Паладина'''
    def __init__(self,
                 name_person: str, 
                 basic_hp: int,
                 basic_atk: int,
                 basic_percent_def: float) -> None:
        super().__init__(name_person, basic_hp, basic_atk, basic_percent_def)
        basic_hp *= 2
        basic_percent_def *= 2
        print(f'Паладин {name_person} родился. Жизни:{basic_hp}, атака:{basic_atk}, процент защиты:{basic_percent_def:.3f}')

class Warrior(Person):
    '''Класс воина'''
    def __init__(self,
                 name_person: str, 
                 basic_hp: int,
                 basic_atk: int,
                 basic_percent_def: float) -> None:
        super().__init__(name_person, basic_hp, basic_atk, basic_percent_def)
        basic_atk *= 2
        print(f'Воин {name_person} родился. Жизни:{basic_hp}, атака:{basic_atk}, процент защиты:{basic_percent_def:.3f}')


def generate_things(count_thing: int) -> List:
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
    things =[]
    for i in range(0, count_thing):
        value_atk: int = random.randint(0, 10)
        value_hp: int = random.randint(1, 5)
        things.append(Thing(DATA_NAME_THINGS[i], percent_def[i], value_atk, value_hp))
    return things

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
    persons =[]
    for i in range(0, сount_person):#генерирование данных персонажа
        name = random.choice(DATA_NAME_PERSONS)
        DATA_NAME_PERSONS.remove(name)
        basic_hp = random.randint(50, 150)
        basic_atk = random.randint(5, 15)
        basic_percent_def = random.uniform(0, 0.1)
        persons.append(DATA_CLASS_PERSON[random.randint(0, 1)](name, basic_hp, basic_atk, basic_percent_def))
    return persons

def del_things_from_chest(things, del_things=None):
    '''Удаление использованных предметов из сундука'''
    if del_things == None:
        return things
    else:
        for i in things:
            for k in del_things:
                if i == k:
                    things.remove(i)
        return things

things = generate_things(20)
persons = generate_persons(10)

for i in persons:
    del_things = i.set_things(things)
    things = del_things_from_chest(things, del_things)
