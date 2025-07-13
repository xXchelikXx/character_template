from jinja2 import Environment, FileSystemLoader, select_autoescape

import random


def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html'])
    )
    template = env.get_template('template.html')

    character_amount = int(input("Сколько персонажей создать? "))

    for num in range(character_amount):

        races = ['Орк', 'Человек']
        select_race = int(input("Выберите рассу: 1-Орк, 2-Человек "))
        character_race = races[select_race-1]

        classes = ['Охотник', 'Маг', 'Воин', 'Ассасин', 'Бард']
        select_class = int(input("Выберите класс: 1-Охотник, 2-Маг, 3-Воин, 4-Ассасин, 5-Бард "))
        character_class = classes[select_class-1]

        classes_base = {
            'Охотник': {
                'skills': ['Верный выстрел', 'Чародейский выстрел', 'Стенающая стрела', 'Стрелы ветра', 'Призыв питомца', 'Глаз зверя', 'Осветительная ракета', 'Приручение животного'],
                'strength': random.randint(1,3),
                'agility': 15,
                'intelligence': random.randint(1,3),
                'luck': random.randint(1,3),
                'temper': random.randint(1,3),
                'img': '../images/archer.png'
            },
            'Маг': {
                'skills': ['Стрела ледяного огня', 'Снятие проклятия', 'Огненный взрыв', 'Обледенение', 'Ледяное копье', 'Конус холода', 'Прилив сил', 'Морозный доспех'],
                'strength':random.randint(1,3),
                'agility':random.randint(1,3),
                'intelligence':15,
                'luck':random.randint(1,3),
                'temper':random.randint(1,3),
                'img': '../images/wizard.png'
                },
            'Воин': {
                'skills': ['Блок щитом', 'Казнь', 'Рывок', 'Боевой крик', 'Вихрь', 'Парирование', 'Мощный удар', 'Глубокие раны'],
                'strength':15,
                'agility':random.randint(1,3),
                'intelligence':random.randint(1,3),
                'luck':random.randint(1,3),
                'temper':random.randint(1,3),
                'img': '../images/varrior.png'
                },
            'Ассасин': {
                'skills': ['Отравление', 'Взлом замка', 'Подлый трюк', 'Исчезновение', 'Ложный выпад', 'Внезапный удар', 'Ошеломление', 'Спринт'],
                'strength':random.randint(1,3),
                'agility':random.randint(1,3),
                'intelligence':random.randint(1,3),
                'luck':15,
                'temper':random.randint(1,3),
                'img': '../images/assasin.png'
                },
            'Бард': {
                'skills': ['Аккорды ветра', 'Аккорды воды', 'Исцеление', 'Соната жизни', 'Пауза', 'Плач сирен', 'Песнь ветра', 'Реквием'],
                'strength':random.randint(1,3),
                'agility':random.randint(1,3),
                'intelligence':random.randint(1,3),
                'luck':random.randint(1,3),
                'temper':15,
                'img': '../images/bard.png'
                }
        }
        skills = random.sample(classes_base[character_class]['skills'], 3)
        rendered_page = template.render(
            name="Абунга",
            race=character_race,
            character_class=character_class,
            strength=classes_base[character_class]['strength'],
            agility=classes_base[character_class]['agility'],
            intelligence=classes_base[character_class]['intelligence'],
            luck=classes_base[character_class]['luck'],
            temper=classes_base[character_class]['temper'],
            image=classes_base[character_class]['img'],
            first_skill=skills[0],
            second_skill=skills[1],
            third_skill=skills[2]
        )

        with open(f'characters/index{num+1}.html', 'w', encoding="utf8") as file:
            file.write(rendered_page)


if __name__ == "__main__":
    main()