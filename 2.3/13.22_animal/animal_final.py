from tkinter import *
import time


class Condition_hunger:
    __very_hungry = 1
    __normal = 2
    __chunky = 3

    @property
    def very_hungry(self):
        return self.__very_hungry

    @property
    def normal(self):
        return self.__normal

    @property
    def chunky(self):
        return self.__chunky


class Condition_mood:
    __bad = 1
    __good = 2
    __happy = 3

    @property
    def bad(self):
        return self.__bad

    @property
    def good(self):
        return self.__good

    @property
    def happy(self):
        return self.__happy


class Animal(Condition_mood, Condition_hunger):
    __feeding = 1
    __playing = 1
    __timer_play_eat = 10

    def __init__(self, name, mood=2, hunger=3):
        self.__name = name
        self.__mood = mood
        self.__hunger = hunger
        self.__time = time.time()

    @property
    def name(self):
        return self.__name

    @name.setter
    def change_name(self, name):
        self.__name = name

    @name.deleter
    def del_name(self):
        del self.__name

    def down_health(self):
        if time.time()-self.__time >= self.__timer_play_eat:
            self.__time = time.time()
            self.down_mood()
            self.down_hunger()

    def up_mood(self):
        self.__mood += self.__playing

    def down_mood(self):
        self.__mood -= self.__playing

    def up_hunger(self):
        self.__hunger += self.__feeding

    def down_hunger(self):
        self.__hunger -= self.__feeding

    def print_condition_mood(self):
        match self.__mood:
            case self.bad:
                return "Мне скучно"
            case self.good:
                return "Я доволен"
            case self.happy:
                return "Я счастлив"

    def print_hunger_mood(self):
        match self.__hunger:
            case self.very_hungry:
                return "Я очень голоден"
            case self.normal:
                return "Я сыт"
            case self.chunky:
                return "Я уже полненький"

    def warning_condition(self):
        if self.__mood == self.bad:
            print("Поиграй со мной или я уйду")
        if self.__hunger == self.very_hungry:
            print("Накорми меня или я умру")

    def button_condition_mood(self, button):
        if self.__mood == self.happy:
            button['state'] = 'disabled'
        else:
            button['state'] = 'normal'

    def button_condition_hunger(self, button):
        if self.__hunger == self.chunky:
            button['state'] = 'disabled'
        else:
            button['state'] = 'normal'

    def game_lose(self, window):
        if self.__mood < self.bad:
            print(animal.name,"ушёл от вас")
            window.destroy()
        if self.__hunger < self.very_hungry:
            print(animal.name,"умер от голода")
            window.destroy()


animal = Animal('pes')

animal.change_name = 'Tom'


def print_condition_mood_btn():
    print(animal.print_condition_mood())


def print_condition_hunger_btn():
    print(animal.print_hunger_mood())


def up_mood_btn():
    animal.up_mood()


def up_hunger_btn():
    animal.up_hunger()


def repeated():
    animal.down_health()
    animal.button_condition_mood(btn)
    animal.button_condition_hunger(btn4)
    animal.warning_condition()
    animal.game_lose(window)

    window.after(500, repeated)


window = Tk()

window.title(animal.name)
window.geometry('450x450')

btn = Button(window, text="Поиграть", command=up_mood_btn)
btn.grid(column=0, row=0)
btn2 = Button(window, text="Узнать настроение",
              command=print_condition_mood_btn)
btn2.grid(column=1, row=0)

btn3 = Button(window, text="Узнать состояние голода",
              command=print_condition_hunger_btn)
btn3.grid(column=2, row=0)

btn4 = Button(window, text="Покормить", command=up_hunger_btn)
btn4.grid(column=3, row=0)

window.after(0, repeated)
window.mainloop()
