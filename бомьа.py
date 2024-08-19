from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from random import randint
from kivy.clock import Clock

last_chance = False

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        layout = FloatLayout()
        self.button = Button(text='Продовжити', size_hint=(.4,.2), pos_hint={'center_x': .5, 'center_y': .2})
        label2 = Label(text=f'Вікно №{int(self.name)}', markup = True, pos_hint= {"center_x": .5,"center_y": .85}, size_hint=(.4, .2))
        self.a = True
        if self.name == "0":
            self.label1 = Label(text='Вітаю в "[i]ШАЛЕНІ 50 СЛАЙДІВ[/i]"! Натисни "Продовжити"', markup = True, pos_hint= {"center_x": .5,"center_y": .7}, size_hint=(.4, .2))
        elif self.name == "3":
            self.label1 = Label(text='Не надоїло?', markup = True, pos_hint= {"center_x": 0.5,"center_y": 0.7}, size_hint=(0.4, 0.2))
        elif self.name == "4":
            self.label1 = Label(text='Ну ти й зануда..', markup = True, pos_hint= {"center_x": 0.5,"center_y": 0.7}, size_hint=(0.4, 0.2))
        elif self.name == "6":
            self.label1 = Label(text='Ти ужасна людина. Натисни продовжити.', markup = True, pos_hint= {"center_x": 0.5,"center_y": 0.7}, size_hint=(0.4, 0.2))
        elif self.name == "7":
            self.label1 = Label(text='√(x) + 1 = 0. Найдіть х', markup = True, pos_hint= {"center_x": 0.5,"center_y": 0.7}, size_hint=(0.4, 0.2))
            self.button = Button(text='x = ±i', size_hint=(.4,.2), pos_hint={'center_x': .5, 'center_y': .2})
        elif self.name == "12":
            self.label1 = Label(text='Якщо ви натиснете кнопку "Продовжити" ви погоджуєтесь з нашою політикою конфіденційності', markup = True, pos_hint= {"center_x": 0.5,"center_y": 0.7}, size_hint=(0.4, 0.2))
        elif self.name == "13":
            self.label1 = Label(text='Я вас вітаю! Тепер індійський хлопчик знає номер, термін дії та СVC2 вашої кредитної картки. ', markup = True, pos_hint= {"center_x": 0.5,"center_y": 0.7}, size_hint=(0.4, 0.2))
            self.button = Button(text='Ура!', size_hint=(.4,.2), pos_hint={'center_x': .5, 'center_y': .4})
        elif self.name == "15":
            self.label1 = Label(text='Обережно, не пропусти 17-те вікно! Там буде важлива інформація (І числа також враховуються)', markup = True, pos_hint= {"center_x": 0.5,"center_y": 0.7}, size_hint=(0.4, 0.2))
            self.a = False
        elif self.name == "16":
            self.label1 = Label(text='Нічого інтересного. Натисни "Я люблю їсти собак"', markup = True, pos_hint= {"center_x": 0.5,"center_y": 0.7}, size_hint=(0.4, 0.2))
            self.button = Button(text='Я люблю їсти собак', size_hint=(.4,.2), pos_hint={'center_x': .5, 'center_y': .2})
        elif self.name == "30":
            self.label1 = Label(text='Залишилось 20 слайдів. Відтепер, питання будуть значно складнішими.', markup = True, pos_hint= {"center_x": 0.5,"center_y": 0.7}, size_hint=(0.4, 0.2))
        elif self.name == "40":
            self.label1 = Label(text='4242424242424242424242424242424242424242424242424242424242424242424242424242424242', markup = True, pos_hint= {"center_x": 0.5,"center_y": 0.7}, size_hint=(0.6, 0.4))
            self.button = Button(text='42424242424242424242424242424242424242', size_hint=(.4,.2), pos_hint={'center_x': .5, 'center_y': .2})
        else:
            self.label1 = Label(text='Нічого інтересного. Натисни "Продовжити"', markup = True, pos_hint= {"center_x": 0.5,"center_y": 0.7}, size_hint=(0.4, 0.2))
        if self.a:
            self.button.bind(on_press=self.switch_to_anotha_screen)
        else:
            self.button.bind(on_press=self.move_lol)
            self.new_text= "Ти читаєш шо я там написав?!! На 17-му вікні буде важлива інформація."
            self.change_button_position = True
            self.new_button_position = {'center_x': .2, 'center_y': .2}
            self.second = False
        
        layout.add_widget(self.button)
        layout.add_widget(self.label1)
        layout.add_widget(label2)
        self.add_widget(layout)
        
    def switch_to_anotha_screen(self, instance):
        self.layout = None
        
        self.manager.current = str(int(self.name) + 1)
        
        
    def move_lol(self, instance):
        if not self.second:
            self.label1.text = self.new_text
            self.button.pos_hint = self.new_button_position
            self.second = True
        else:
            self.label1.text = "Я маю бути впевнений що ти пройдеш вікно #30, тому зауваж 17-те вікно."
            self.button.pos_hint = {'center_x': .8, 'center_y': .2}
            self.button.text = "ТА ПРОПУСТИ МЕНЕ ВЖЕ"
            self.button.bind(on_press = self.switch_to_anotha_screen)
        
left_trys = True
class DoubleButtonScreen(Screen):
    def __init__(self, **kwargs):
        super(DoubleButtonScreen, self).__init__(**kwargs)
        self.layout = FloatLayout()
        self.label2 = Label(text=f'Вікно №{int(self.name)}', markup = True, pos_hint= {"center_x": .5,"center_y": .85}, size_hint=(.4, .2))
        global left_trys
        if self.name == "0":
            self.label1 = Label(text='Вітаю в ХрестикиНолики3000! Увійдіть, або створіть новий аккаунт.', markup = True, pos_hint= {"center_x": .5,"center_y": .7}, size_hint=(.4, .2))
            self.button2 = Button(text='Створити новий аккаунт', size_hint=(.4,.2), pos_hint={'center_x': .75, 'center_y': .2})
            self.button1 = Button(text='Увійти', size_hint=(.4,.2), pos_hint={'center_x': .25, 'center_y': .2})
            self.button1.bind(on_press=self.switch_to_alternative_route)
            self.button2.bind(on_press=self.switch_to_anotha_screen)
        elif self.name == "34":
            self.label1 = Label(text='Як задумувався ChatGPT на початку?', markup = True, pos_hint= {"center_x": .5,"center_y": .7}, size_hint=(.4, .2))
            self.button1 = Button(text='Як покращений Т9', size_hint=(.4,.2), pos_hint={'center_x': .25, 'center_y': .2})
            self.button2 = Button(text='Як помічник з ідеями', size_hint=(.4,.2), pos_hint={'center_x': .75, 'center_y': .2})
            self.button1.bind(on_press=self.correct)
            self.button2.bind(on_press=self.incorrect)
        elif self.name == "38":
            self.label1 = Label(text='До другої світової війни в пілоти ВВС США не брали \n дальтоників, але в 1941 їм почали надавати перевагу. Ізза чого?', markup = True, pos_hint= {"center_x": .5,"center_y": .7}, size_hint=(.4, .2))
            self.button1 = Button(text="Бо дальтоники зачасту \n не розрізняють зелений колір.", size_hint=(.4,.2), pos_hint={'center_x': .25, 'center_y': .2})
            self.button2 = Button(text='Бо дальтоники бачуть дальше, \n що дає значну перевагу в морі.', size_hint=(.4,.2), pos_hint={'center_x': .75, 'center_y': .2})
            self.button1.bind(on_press=self.correct)
            self.button2.bind(on_press=self.incorrect)
        elif self.name == "40":
            self.label1 = Label(text='Що таке світло?', markup = True, pos_hint= {"center_x": .5,"center_y": .7}, size_hint=(.4, .2))
            self.button1 = Button(text="Хвиля", size_hint=(.4,.2), pos_hint={'center_x': .25, 'center_y': .2})
            self.button2 = Button(text='Частиця', size_hint=(.4,.2), pos_hint={'center_x': .75, 'center_y': .2})
            self.button1.bind(on_press=self.no_answer)
            self.button2.bind(on_press=self.no_answer)
        elif self.name == "43":
            self.label1 = Label(text='Яка найдовша ріка в азії?', markup = True, pos_hint= {"center_x": .5,"center_y": .7}, size_hint=(.4, .2))
            self.button1 = Button(text="Хуанхе", size_hint=(.4,.2), pos_hint={'center_x': .25, 'center_y': .2})
            self.button2 = Button(text='Янцзи', size_hint=(.4,.2), pos_hint={'center_x': .75, 'center_y': .2})
            self.button1.bind(on_press=self.incorrect)
            self.button2.bind(on_press=self.correct)
        elif self.name == "44":
            self.label1 = Label(text='Ти готовий до фінального питання?', markup = True, pos_hint= {"center_x": .5,"center_y": .7}, size_hint=(.4, .2))
            self.button1 = Button(text="Так", size_hint=(.4,.2), pos_hint={'center_x': .25, 'center_y': .2})
            self.button2 = Button(text='Ні', size_hint=(.4,.2), pos_hint={'center_x': .75, 'center_y': .2})
            self.button1.bind(on_press=self.jokeyes)
            self.button2.bind(on_press=self.jokeno)
        elif self.name == "48":
            self.label1 = Label(text='Ти готовий до фінального питання?', markup = True, pos_hint= {"center_x": .5,"center_y": .7}, size_hint=(.4, .2))
            self.button1 = Button(text="Так", size_hint=(.4,.2), pos_hint={'center_x': .25, 'center_y': .2})
            self.button2 = Button(text='Ні', size_hint=(.4,.2), pos_hint={'center_x': .75, 'center_y': .2})
            self.button1.bind(on_press=self.switch_to_anotha_screen)
            self.button2.bind(on_press=self.agressiveno)
        self.layout.add_widget(self.label1)
        self.layout.add_widget(self.button1)
        self.layout.add_widget(self.button2)
        self.layout.add_widget(self.label2)
        self.add_widget(self.layout)
    def incorrect(self, instance):
        self.label1.text = "Невірно. Відправляйся на перший слайд!"
        self.button1.opacity = 0
        self.button1.disabled = True
        self.button2.opacity = 0
        self.button3.disabled = True
        Clock.schedule_once(self.go_to_first_screen, 5)
    def correct(self,instance):
        self.label1.text = "Вірно!"
        self.button1.opacity = 0
        self.button1.disabled = True
        self.button2.opacity = 0
        self.button2.disabled = True
        Clock.schedule_once(self.switch_to_anotha_screen, 5)
    def no_answer(self,instance):
        self.label1.text = "Насправді, ніхто не знає)"
        self.button1.opacity = 0
        self.button1.disabled = True
        self.button2.opacity = 0
        self.button2.disabled = True
        Clock.schedule_once(self.switch_to_anotha_screen, 5)
    def go_to_first_screen(self, dt):
        raise Exception("Closing..")
        
    def switch_to_anotha_screen(self, instance):
        self.manager.current = str(int(self.name) + 1)
        self.layout = None
        
    def switch_to_alternative_route(self,instance):
        self.manager.current = "Alternative route"
    def jokeno(self, instance):
        self.label1.text = "Я також"
        self.button1.opacity = 0
        self.button1.disabled = True
        self.button2.opacity = 0
        self.button2.disabled = True
        Clock.schedule_once(self.switch_to_anotha_screen, 5)
    def jokeyes(self,instance):
        self.label1.text = "А я ні"
        self.button1.opacity = 0
        self.button1.disabled = True
        self.button2.opacity = 0
        self.button2.disabled = True
        Clock.schedule_once(self.switch_to_anotha_screen, 5)
    def agressiveno(self,instance):
        self.label1.text = "Ух який, будеш таке казати на робочому столі."
        self.button1.opacity = 0
        self.button1.disabled = True
        self.button2.opacity = 0
        self.button2.disabled = True
        Clock.schedule_once(self.go_to_first_screen, 5)
class ImageScreen(Screen):
    def __init__(self, **kwargs):
        super(ImageScreen, self).__init__(**kwargs)
        self.layout = FloatLayout()
        self.button = Button(text='Продовжити', size_hint=(.4,.2), pos_hint={'center_x': .5, 'center_y': .2}, background_color = (0,0,0,.5))
        self.label1 = Label(text='БУ!!', markup = True, pos_hint= {"center_x": .5,"center_y": .7}, size_hint=(.4, .2))
        self.image = Image(source = "лол.png", size_hint = (1,1), pos_hint = {"center_x": .5,"center_y": .5})
        self.label2 = Label(text=f'Вікно №{int(self.name) }', markup = True, pos_hint= {"center_x": .5,"center_y": .85}, size_hint=(.4, .2))
        if self.name == "41":
            self.label1.text = "Шрек вернувся! Хаха)"
        if self.name == "5" or self.name == "41":
            self.new_text= "Не так швидко!"
            self.change_button_position = True
            self.new_button_position = {'center_x': .7, 'center_y': .2}
            self.button.bind(on_press = self.change_label1_name)
        else:
            self.button.bind(on_press=self.switch_to_anotha_screen)
        self.layout.add_widget(self.image)
        self.layout.add_widget(self.button)
        self.layout.add_widget(self.label1)
        self.layout.add_widget(self.label2)
        self.add_widget(self.layout)
    def change_label1_name(self,instance):
        self.label1.text = "Не так швидко!"
        self.button.pos_hint = {'center_x': .8, 'center_y': .2}
        self.button.bind(on_press=self.switch_to_anotha_screen)
    def switch_to_anotha_screen(self, instance):

        self.manager.current = str(int(self.name) + 1)
class RadioScreen(Screen):
    def __init__(self, **kwargs):
        super(RadioScreen, self).__init__(**kwargs)
        self.layout = FloatLayout()
        self.button = Button(text='Ввести', size_hint=(.4,.2), pos_hint={'center_x': .5, 'center_y': .2})
        self.text_input = TextInput(pos_hint={'center_x': .5, 'center_y': .5}, size_hint=(.4, .1),multiline=False)
        try:
            self.label2 = Label(text=f'Вікно №{int(self.name)}', markup = True, pos_hint= {"center_x": .5,"center_y": .85}, size_hint=(.4, .2))
        except:
            self.label2 = Label(text='Реєстрація', markup = True, pos_hint= {"center_x": .5,"center_y": .85}, size_hint=(.4, .2))
        self.last_chance= False
        if self.name == "14":
            self.a = randint(1,9)
            self.b = randint(1,9)
            self.label1 = Label(text= f'Прекрасно! Вот новий тип - з строкою вводу. Давай щось легке: {self.a} + {self.b} = ?', markup = True, pos_hint= {"center_x": .5,"center_y": .7}, size_hint=(.1, .01))
        elif self.name == "Alternative route":
            self.label1 = Label(text= f'Введіть ваш нікнейм:', markup = True, pos_hint= {"center_x": .5,"center_y": .7}, size_hint=(.1, .01))
            self.skibidi = 0
        elif self.name == "17":
            self.label1 = Label(text= f'я так і знаW! тоді скільки буде 1 * 1?', markup = True, pos_hint= {"center_x": .5,"center_y": .7}, size_hint=(.1, .01))
        elif self.name == "25":
            self.label1 = Label(text= f'Хм. Ви вчили корні? Давайте просто - √(4)', markup = True, pos_hint= {"center_x": .5,"center_y": .7}, size_hint=(.1, .01))
        elif self.name == "26":
            self.label1 = Label(text= f'Скільки долларів можна було купити на 100 гривень в лютому 2005? \n (Округли до цілого). Це складне запитання, тому в тебе нескінченість спроб', markup = True, pos_hint= {"center_x": .5,"center_y": .7}, size_hint=(.1, .01))
        elif self.name == "29":
            self.label1 = Label(text= f"Який найшвидший автомобіль Mercedes? (Не обов'язково легальний на дорогах)", markup = True, pos_hint= {"center_x": .5,"center_y": .7}, size_hint=(.1, .01))
        elif self.name == "39":
            self.a = randint(1000,10000)
            self.b = randint(1000,10000)
            self.label1 = Label(text= f'Скільки буде {self.a} + {self.b} = ?', markup = True, pos_hint= {"center_x": .5,"center_y": .7}, size_hint=(.1, .01))
        elif self.name == "44":
            self.label1 = Label(text= f'Імя правителя, який вбив від 40 до 80 мілліона людей? (3 букви)', markup = True, pos_hint= {"center_x": .5,"center_y": .7}, size_hint=(.1, .01))
        elif self.name == "49":
            self.label1 = Label(text= 'Цезарь сказав: "WlfWdfWrh з паролем +3". Що він мав на увазі? (англ. алфавіт)', markup = True, pos_hint= {"center_x": .5,"center_y": .7}, size_hint=(.1, .01))
        elif self.name == "50":
            self.label1 = Label(text= f'Вітаємо! Введіть ваш нікнейм, і ми пустимо вас, щоби грати', markup = True, pos_hint= {"center_x": .5,"center_y": .7}, size_hint=(.1, .01))
        self.layout.add_widget(self.button)
        self.layout.add_widget(self.label1)
        self.layout.add_widget(self.text_input)
        self.layout.add_widget(self.label2)
        self.add_widget(self.layout)
        self.button.bind(on_press=self.check)
    def check(self, instance):
        if self.name == "14" or self.name == "39":
            answer = str(int(self.a) + int(self.b))
            if self.text_input.text == answer:
                self.manager.current = str(int(self.name) + 1)
                self.last_chance = False
            elif not self.last_chance:
                self.label1.text = f"Спробуй ще раз! {self.a} + {self.b}"
                self.last_chance = True
            else:
                self.label1.text = "У тебе був другий шанс, ти його втратив. Тепер ця програма закриється"
                self.last_chance = False
                self.button.opacity = 0
                self.button.disabled = True
                Clock.schedule_once(self.go_to_first_screen, 5)
        elif self.name == "44":
            answer = "мао"
            if self.text_input.text.lower() == answer:
                self.manager.current = str(int(self.name) + 1)
                self.last_chance = False
            elif not self.last_chance:
                self.label1.text = "Спробуй ще раз!"
                self.last_chance = True
            else:
                self.label1.text = "У тебе був другий шанс, ти його втратив. Тепер ця програма закриється"
                self.last_chance = False
                self.button.opacity = 0
                self.button.disabled = True
                Clock.schedule_once(self.go_to_first_screen, 5)
        elif self.name == "49":
            answer = "tictactoe"
            if self.text_input.text.lower() == answer:
                self.manager.current = str(int(self.name) + 1)
                self.last_chance = False
            elif not self.last_chance:
                self.label1.text = "Спробуй ще раз!"
                self.last_chance = True
            else:
                self.label1.text = "У тебе був другий шанс, ти його втратив. Тепер ця програма закриється.. Круто таке чути на останьому слайді?"
                self.last_chance = False
                self.button.opacity = 0
                self.button.disabled = True
                Clock.schedule_once(self.go_to_first_screen, 5)
        elif self.name == "50":
            self.manager.current = "End"
        elif self.name == "Alternative route":
            if self.skibidi < 2:
                if self.skibidi < 1:
                    self.label1.text = "Нікнейм не знайдено!"
                else:
                    self.label1.text = "Нікнейм не знайдено! У вас ще одна спроба."
                self.skibidi += 1
            else:
                self.label1.text = "Нажаль, ви вичерпали всі спроби."
                self.button.text = "Вернутись"
                self.button.bind(on_press=self.REALLY_go_to_first_screen)
        elif self.name == "17":
            if self.text_input.text == "1":
                self.manager.current = str(int(self.name) + 1)
                self.last_chance = False
            elif not self.last_chance:
                self.label1.text = f"СпWобуй ще раз! 1 * 1"
                self.last_chance = True
            else:
                self.label1.text = "У тебе був другий шанс, ти його втратив. Тепер ця програма закриється"
                self.last_chance = False
                self.button.opacity = 0
                self.button.disabled = True
                Clock.schedule_once(self.go_to_first_screen, 5)
        elif self.name == "25":
            if self.text_input.text == "2":
                self.manager.current = str(int(self.name) + 1)
                self.last_chance = False
            elif not self.last_chance:
                self.label1.text = f"Ну добре, тобі треба найти яке число треба перемножити саме на себе,\n щоб получити 4. Приклад: Корінь з 9 = 3, тому що 3*3 = 9"
                self.last_chance = True
            else:
                self.label1.text = "Нє, ну може і не знаєш шо таке корні і не розумієш як вони працюють. \n Все окей! Йди на наступне вікно!"
                self.button.text = "Ура!"
                self.last_chance = False
                self.button.bind(on_press = self.switch_to_anotha_screen)
        elif self.name == "26":
            try:
                if self.text_input.text == "20":
                    self.label1.text = "От би я купив доляри тоді, але мені тоді було лиш -7 років."
                    self.button.opacity = 0
                    self.button.disabled = True
                    self.last_chance = False
                    Clock.schedule_once(self.switch_to_anotha_screen, 5)
                elif int(self.text_input.text) > 20:
                    self.label1.text = "Меньше!"
                else:
                    self.label1.text = "Більше!"
            except:
                self.label1.text = f"Я не думаю що {self.text_input.text} є числом."
        elif self.name == "29":
            if self.text_input.text.lower() == "w11":
                self.label1.text = "Це болід Formula-1!"
                self.button.opacity = 0
                self.button.disabled = True
                Clock.schedule_once(self.switch_to_anotha_screen,5)
                self.last_chance = False
            elif not self.last_chance:
                self.last_chance = True
                self.label1.text = "Використай підсказку яка була на 17-ому слайді!"
            else:
                self.label1.text = "Забув, чи шо? Ну нічо, згадаєш коли програма закриється"
                Clock.schedule_once(self.go_to_first_screen , 5)
                
                
            
    def go_to_first_screen(self, dt):
        raise Exception("Closing..")
    def REALLY_go_to_first_screen(self,instance):
        self.manager.current = "0"
        
    def switch_to_anotha_screen(self, instance):
        self.manager.current = str(int(self.name) + 1)
        self.layout = None
        
class TicTacToe(Screen):
    def __init__(self,**kwargs):
        super(TicTacToe, self).__init__(**kwargs)
        self.side = "хрестиків"
        self.begin_side = "хрестиків"
        self.x_score = 0
        self.o_score = 0
        self.label1 = Label(text= f'Хід {self.side}', markup = True, pos_hint= {"center_x": .5,"center_y": .9}, size_hint=(.1, .01))
        self.buttonA1 = Button(text='', size_hint=(.2,.2), pos_hint={'center_x': .30, 'center_y': .7})
        self.buttonA2 = Button(text='', size_hint=(.2,.2), pos_hint={'center_x': .50, 'center_y': .7})
        self.buttonA3 = Button(text='', size_hint=(.2,.2), pos_hint={'center_x': .70, 'center_y': .7})
        self.buttonB1 = Button(text='', size_hint=(.2,.2), pos_hint={'center_x': .30, 'center_y': .5})
        self.buttonB2 = Button(text='', size_hint=(.2,.2), pos_hint={'center_x': .50, 'center_y': .5})
        self.buttonB3 = Button(text='', size_hint=(.2,.2), pos_hint={'center_x': .70, 'center_y': .5})
        self.buttonC1 = Button(text='', size_hint=(.2,.2), pos_hint={'center_x': .30, 'center_y': .3})
        self.buttonC2 = Button(text='', size_hint=(.2,.2), pos_hint={'center_x': .50, 'center_y': .3})
        self.buttonC3 = Button(text='', size_hint=(.2,.2), pos_hint={'center_x': .70, 'center_y': .3})
        self.label2 = Label(text= f'Xрестики {self.x_score}:{self.o_score} Круги', markup = True, pos_hint= {"center_x": .1,"center_y": .98}, size_hint=(.1, .01))
        self.resetbutton = Button(text='Перезапустити', size_hint=(.15,.1), pos_hint={'center_x': .9, 'center_y': .9})
        self.layout = FloatLayout()
        self.layout.add_widget(self.buttonA1)
        self.layout.add_widget(self.buttonA2)
        self.layout.add_widget(self.buttonA3)
        self.layout.add_widget(self.buttonB1)
        self.layout.add_widget(self.buttonB2)
        self.layout.add_widget(self.buttonB3)
        self.layout.add_widget(self.buttonC1)
        self.layout.add_widget(self.buttonC2)
        self.layout.add_widget(self.buttonC3)
        self.layout.add_widget(self.resetbutton)
        self.layout.add_widget(self.label1)
        self.add_widget(self.layout)
        self.a = ["","",""]
        self.b = ["","",""]
        self.c = ["","",""]
        self.buttonA1.bind(on_press = self.a1_pressed)
        self.buttonA2.bind(on_press = self.a2_pressed)
        self.buttonA3.bind(on_press = self.a3_pressed)
        self.buttonB1.bind(on_press = self.b1_pressed)
        self.buttonB2.bind(on_press = self.b2_pressed)
        self.buttonB3.bind(on_press = self.b3_pressed)
        self.buttonC1.bind(on_press = self.c1_pressed)
        self.buttonC2.bind(on_press = self.c2_pressed)
        self.buttonC3.bind(on_press = self.c3_pressed)
        self.resetbutton.bind(on_press =self.reload)
        self.layout.add_widget(self.label2)
        
        #A1 A2 A3
        #B1 B2 B3
        #C1 C2 C3
    def a1_pressed(self, instance):
        if self.a[0] == "":
            if self.side == "хрестиків":
                self.a[0] = "Х"
                self.buttonA1.text = 'X'
                self.side = "кругів"
            else:
                self.a[0] = "О"
                self.buttonA1.text = 'O'
                self.side = "хрестиків"
            self.label1.text = f'Хід {self.side}'
            self.check_win()
    def a2_pressed(self, instance):
        if self.a[1] == "":
            if self.side == "хрестиків":
                self.a[1] = "Х"
                self.buttonA2.text = 'X'
                self.side = "кругів"
            else:
                self.a[1] = "О"
                self.buttonA2.text = 'O'
                self.side = "хрестиків"
            self.label1.text = f'Хід {self.side}'
            self.check_win()
    def a3_pressed(self, instance):
        if self.a[2] == "":
            if self.side == "хрестиків":
                self.a[2] = "Х"
                self.buttonA3.text = 'X'
                self.side = "кругів"
            else:
                self.a[2] = "О"
                self.buttonA3.text = 'O'
                self.side = "хрестиків"
            self.label1.text = f'Хід {self.side}'
            self.check_win()
    def b1_pressed(self, instance):
        if self.b[0] == "":
            if self.side == "хрестиків":
                self.b[0]= "Х"
                self.buttonB1.text = "Х"
                self.side = "кругів"
            else:
                self.b[0] = "О"
                self.buttonB1.text = "О"
                self.side = "хрестиків"
            self.label1.text = f'Хід {self.side}'
            self.check_win()
    def b2_pressed(self, instance):
        if self.b[1] == "":
            if self.side == "хрестиків":
                self.b[1]= "Х"
                self.buttonB2.text = "Х"
                self.side = "кругів"
            else:
                self.b[1] = "О"
                self.buttonB2.text = "О"
                self.side = "хрестиків"
            self.label1.text = f'Хід {self.side}'
            self.check_win()
    def b3_pressed(self, instance):
        if self.b[2] == "":
            if self.side == "хрестиків":
                self.b[2]= "Х"
                self.buttonB3.text = "Х"
                self.side = "кругів"
            else:
                self.b[2] = "О"
                self.buttonB3.text = "О"
                self.side = "хрестиків"
            self.label1.text = f'Хід {self.side}'
            self.check_win()
    def c1_pressed(self, instance):
        if self.c[0] == "":
            if self.side == "хрестиків":
                self.c[0]= "Х"
                self.buttonC1.text = "Х"
                self.side = "кругів"
            else:
                self.c[0] = "О"
                self.buttonC1.text = "О"
                self.side = "хрестиків"
            self.label1.text = f'Хід {self.side}'
            self.check_win()
    def c2_pressed(self, instance):
        if self.c[1] == "":
            if self.side == "хрестиків":
                self.c[1]= "Х"
                self.buttonC2.text = "Х"
                self.side = "кругів"
            else:
                self.c[1] = "О"
                self.buttonC2.text = "О"
                self.side = "хрестиків"
            self.label1.text = f'Хід {self.side}'
            self.check_win()
    def c3_pressed(self, instance):
        if self.c[2] == "":
            if self.side == "хрестиків":
                self.c[2]= "Х"
                self.buttonC3.text = "Х"
                self.side = "кругів"
            else:
                self.c[2] = "О"
                self.buttonC3.text = "О"
                self.side = "хрестиків"
            self.label1.text = f'Хід {self.side}'
            self.check_win()
    def reload(self,instance):
        self.a = ["","",""]
        self.b = ["","",""]
        self.c = ["","",""]
        self.buttonA1.text = ""
        self.buttonA2.text = ""
        self.buttonA3.text = ""
        self.buttonB1.text = ""
        self.buttonB2.text = ""
        self.buttonB3.text = ""
        self.buttonC1.text = ""
        self.buttonC2.text = ""
        self.buttonC3.text = ""
        if self.begin_side == "хрестиків":
            self.begin_side = "кругів"
            self.side = "кругів"
        self.label1.text = f'Хід {self.side}'
    def check_win(self,instance = None):
        if self.begin_side == "хрестиків":
            shpare = ["Х","О"]
        else:
            shpare = ["О","Х"]
        for i in shpare:
            if self.a[0] == i and self.a[1] == i and self.a[2] == i:
                if i == "Х":
                    self.x_win()
                else:
                    self.o_win()
            elif self.a[0] == i and self.b[1] == i and self.c[2] == i:
                if i == "Х":
                    self.x_win()
                else:
                    self.o_win()
            elif self.a[2] == i and self.b[1] == i and self.c[0] == i:
                if i == "Х":
                    self.x_win()
                else:
                    self.o_win()
            elif self.b[0] == i and self.b[1] == i and self.b[2] == i:
                if i == "Х":
                    self.x_win()
                else:
                    self.o_win()
            elif self.c[0] == i and self.c[1] == i and self.c[2] == i:
                if i == "Х":
                    self.x_win()
                else:
                    self.o_win()
            elif self.a[0] == i and self.b[0] == i and self.c[0] == i:
                if i == "Х":
                    self.x_win()
                else:
                    self.o_win()
            elif self.a[1] == i and self.b[1] == i and self.c[1] == i:
                if i == "Х":
                    self.x_win()
                else:
                    self.o_win()
            elif self.a[2] == i and self.b[2] == i and self.c[2] == i:
                if i == "Х":
                    self.x_win()
                else:
                    self.o_win()
            elif self.a[0] != "" and self.b[0] != "" and self.c[0] != "" and self.a[1] != "" and self.b[1] != "" and self.c[1] != "" and self.a[2] != "" and self.b[2] != "" and self.c[2] != "":
                self.draw()
    def x_win(self,instance=None):
        self.label1.text = "Виграли хрестики. Перезагрузка дошки через 3 секунди."
        self.x_score += 1
        self.label2.text = f'Xрестики {self.x_score}:{self.o_score} Круги'
        Clock.schedule_once(self.reload, 3)
    def o_win(self,instance=None):
        self.label1.text = f"Виграли круги. Перезагрузка дошки через 3 секунди."
        self.o_score += 1
        self.label2.text = f'Xрестики {self.x_score}:{self.o_score} Круги'
        Clock.schedule_once(self.reload, 3)
    def draw(self,instance=None):
        self.label1.text = "Нічия. Перезагрузка дошки через 3 секунди."
        self.x_score += 1
        self.o_score += 1
        self.label2.text = f'Xрестики {self.x_score}:{self.o_score} Круги'
        Clock.schedule_once(self.reload, 3)
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(DoubleButtonScreen(name="0"))
        sm.add_widget(RadioScreen(name="Alternative route"))
        for i in range(4):
            sm.add_widget(MainScreen(name=str(i + 1)))
        sm.add_widget(ImageScreen(name="5"))
        for i in range(8):
            sm.add_widget(MainScreen(name=str(i + 6)))
        sm.add_widget(RadioScreen(name="14"))
        sm.add_widget(MainScreen(name = "15"))
        sm.add_widget(MainScreen(name = "16"))
        sm.add_widget(RadioScreen(name = "17"))
        for i in range(7):
            sm.add_widget(MainScreen(name=str(i + 18)))
        sm.add_widget(RadioScreen(name="25"))
        sm.add_widget(RadioScreen(name="26"))
        for i in range(2):
            sm.add_widget(MainScreen(name=str(i+27)))
        sm.add_widget(RadioScreen(name="29"))
        for i in range(4):
            sm.add_widget(MainScreen(name=str(i+30)))
        sm.add_widget(DoubleButtonScreen(name= "34"))
        for i in range(3):
            sm.add_widget(MainScreen(name=str(i+35)))
        sm.add_widget(DoubleButtonScreen(name = "38"))
        sm.add_widget(RadioScreen(name= "39"))
        sm.add_widget(DoubleButtonScreen(name="40"))
        sm.add_widget(ImageScreen(name="41"))
        sm.add_widget(MainScreen(name="42"))
        sm.add_widget(DoubleButtonScreen(name="43"))
        sm.add_widget(DoubleButtonScreen(name= "44"))
        for i in range(3):
            sm.add_widget(MainScreen(name=str(i + 45)))
        sm.add_widget(DoubleButtonScreen(name="48"))
        sm.add_widget(RadioScreen(name = "49"))
        sm.add_widget(RadioScreen(name= "50"))
        sm.add_widget(TicTacToe(name="End"))
        return sm

if __name__ == '__main__':
    MyApp().run()