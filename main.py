import arcade
from arcade.gui.experimental import UIScrollArea

SCREEN_WIDTH = 1980
SCREEN_HEIGHT = 1080
SCREEN_TITLE = "Эволюционный защитник"

COLOR_WHITE = arcade.color.WHITE
COLOR_BLACK = arcade.color.BLACK
COLOR_GRAY = arcade.color.GRAY
COLOR_LIGHT_GRAY = arcade.color.LIGHT_GRAY
COLOR_TRANSPARENT = (0, 0, 0, 0)
COLOR_BLACK_TRANSPARENT = (0, 0, 0, 180)
COLOR_BLUE = arcade.color.BLUE
COLOR_RED = arcade.color.RED

class MenuButton(arcade.gui.UIFlatButton):
    def __init__(self, text: str, **kwargs):
        style = {
            "normal": {
                "font_name": "Arial",
                "font_size": 24,
                "font_color": COLOR_WHITE,
                "bg": COLOR_TRANSPARENT,
                "border_color": COLOR_TRANSPARENT,
                "border_width": 0
            },
            "hover": {
                "font_name": "Arial",
                "font_size": 24,
                "font_color": COLOR_WHITE,
                "bg": COLOR_BLACK_TRANSPARENT,
                "border_color": COLOR_TRANSPARENT,
                "border_width": 0
            },
            "press": {
                "font_name": "Arial",
                "font_size": 24,
                "font_color": COLOR_WHITE,
                "bg": COLOR_BLACK_TRANSPARENT,
                "border_color": COLOR_TRANSPARENT,
                "border_width": 0
            },
            "disabled": {
                "font_name": "Arial",
                "font_size": 24,
                "font_color": (200, 200, 200),
                "bg": COLOR_TRANSPARENT,
                "border_color": COLOR_TRANSPARENT,
                "border_width": 0
            }
        }
        
        super().__init__(
            text=text,
            width=400,
            height=60,
            style=style,
            **kwargs
        )

class HelpWindow(arcade.gui.UIMouseFilterMixin, arcade.gui.UIAnchorLayout):
    def __init__(self, main_view, width=800, height=600):
        super().__init__(size_hint=(1, 1))
        
        self.main_view = main_view
        self.width = width
        self.height = height
        
        bg = arcade.gui.UISpace(width=width, height=height).with_background(color=COLOR_BLACK_TRANSPARENT)
        
        help_text = """1. Общее описание
Игра "Эволюционный защитник" - это 2D-игра, разработанная на Python с использованием библиотеки Arcade. Игрок создаёт и кастомизирует моба, который автоматически обучается с помощью ИИ для защиты собственного "Куба жизни" и атаки вражеских мобов.

2. Основная механика
2.1. Цель игры
• Защитить свой "Куб жизни" от вражеских мобов
• Уничтожить вражеский "Куб жизни" с помощью созданного моба
• Выжить дольше противника

2.2. Ключевые элементы
• Куб жизни игрока - центральный объект, который необходимо защищать
• Моб игрока - создаваемое существо, состоящее из частей тела
• Очки жизни (HP) - ресурс для присоединения частей тела к мобу
• Вражеский куб жизни и моб - аналогичные объекты противника

3. Функциональные требования
3.1. Система создания моба
Игрок начинает с базового куба жизни.
С помощью очков жизни игрок может присоединять к мобу различные части тела:
• Типы частей: ноги (передвижение), руки (атака), защитные элементы, сенсоры
• Каждая часть имеет стоимость в очков жизни
• Части присоединяются к основному телу моба
• Визуальное отображение созданного моба

3.2. ИИ обучение моба
Моб обучается с помощью простого ИИ (нейронная сеть или алгоритм обучения с подкреплением).
Моб самостоятельно обучается:
• Навигации по игровому полю
• Обнаружению вражеского куба жизни и мобов
• Атаке вражеского куба жизни
• Уклонению от вражеских мобов
• ИИ учитывает присоединённые части тела при принятии решений

3.3. Игровой процесс
• Два моба (игрока и противника) находятся на одной арене
• При контакте моба игрока с вражеским кубом жизни наносится урон
• При контакте вражеского моба с кубом жизни игрока наносится урон
• Игра завершается когда уничтожен один из кубов жизни

3.4. Управление
• Создание и кастомизация моба через интерфейс
• Запуск симуляции боя
• Возможность перезапуска игры с новым мобом

4. Технические требования
4.1. Графика и интерфейс
• Чистый, минималистичный дизайн
• Визуальное представление:
  - Куб жизни игрока (синий) и противника (красный)
  - Созданный моб с видимыми частями тела
  - Отображение здоровья кубов жизни
• Интерфейс создания моба:
  - Панель доступных частей тела
  - Отображение оставшихся очков жизни
  - Кнопка запуска симуляции

4.2. Физика и коллизии
• Реализация обнаружения столкновений:
  - Между мобами и кубами жизни
  - Между мобами (опционально)
• Реализация простой физики движения мобов

4.3. ИИ система
• Реализация простой нейронной сети:
  - Входные данные: положение целей, здоровье, дистанции
  - Выходные данные: направление движения, атака
• Обучение с подкреплением или предварительно обученная модель"""
        
        text_area = arcade.gui.UITextArea(
            text=help_text,
            width=width - 40,
            height=height - 100,
            font_size=14,
            text_color=COLOR_WHITE,
            multiline=True
        )
        
        close_button = arcade.gui.UIFlatButton(
            text="Закрыть",
            width=200,
            height=40,
            style={
                "normal": {
                    "font_name": "Arial",
                    "font_size": 16,
                    "font_color": COLOR_WHITE,
                    "bg": (100, 100, 100),
                    "border_color": COLOR_TRANSPARENT,
                    "border_width": 0
                },
                "hover": {
                    "font_name": "Arial",
                    "font_size": 16,
                    "font_color": COLOR_WHITE,
                    "bg": (120, 120, 120),
                    "border_color": COLOR_TRANSPARENT,
                    "border_width": 0
                },
                "press": {
                    "font_name": "Arial",
                    "font_size": 16,
                    "font_color": COLOR_WHITE,
                    "bg": (150, 150, 150),
                    "border_color": COLOR_TRANSPARENT,
                    "border_width": 0
                }
            }
        )
        
        @close_button.event("on_click")
        def on_click_close(event):
            self.main_view.show_main_menu()
        
        v_box = arcade.gui.UIBoxLayout(vertical=True, align="center", space_between=10)
        v_box.add(text_area)
        v_box.add(close_button)
        
        self.add(bg)
        self.add(v_box)

class LeaderboardWindow(arcade.gui.UIMouseFilterMixin, arcade.gui.UIAnchorLayout):
    def __init__(self, main_view, width=800, height=600):
        super().__init__(size_hint=(1, 1))
        
        self.main_view = main_view
        self.width = width
        self.height = height
        
        bg = arcade.gui.UISpace(width=width, height=height).with_background(color=COLOR_BLACK_TRANSPARENT)
                
        headers_box = arcade.gui.UIBoxLayout(vertical=False, space_between=10)
        
        leaders_label = arcade.gui.UILabel(
            text="ЛИДЕРЫ",
            font_size=24,
            text_color=COLOR_WHITE,
            width=width // 2 - 20,
            align="center"
        )
        
        scores_label = arcade.gui.UILabel(
            text="РЕЗУЛЬТАТЫ",
            font_size=24,
            text_color=COLOR_WHITE,
            width=width // 2 - 20,
            align="center"
        )
        
        headers_box.add(leaders_label)
        headers_box.add(scores_label)
        
        leaders_text = """1. Игрок1
2. Игрок2
3. Игрок3
4. Игрок4
5. Игрок5
6. Игрок6
7. Игрок7
8. Игрок8
9. Игрок9
10. Игрок10
11. Игрок11
12. Игрок12
13. Игрок13
14. Игрок14
15. Игрок15"""
        
        scores_text = """1000
950
900
850
800
750
700
650
600
550
500
450
400
350
300"""
        
        leaders_widget = arcade.gui.UITextArea(
            text=leaders_text,
            width=width // 2 - 40,
            height=height - 200,
            text_color=COLOR_LIGHT_GRAY,
            font_size=16,
            align="center",
            multiline=True
        )
        
        scores_widget = arcade.gui.UITextArea(
            text=scores_text,
            width=width // 2 - 40,
            height=height - 200,
            text_color=COLOR_LIGHT_GRAY,
            font_size=16,
            align="center",
            multiline=True
        )
        
        data_box = arcade.gui.UIBoxLayout(vertical=False, space_between=10)
        data_box.add(leaders_widget)
        data_box.add(scores_widget)
        
        close_button = arcade.gui.UIFlatButton(
            text="Закрыть",
            width=200,
            height=40,
            style={
                "normal": {
                    "font_name": "Arial",
                    "font_size": 16,
                    "font_color": COLOR_WHITE,
                    "bg": (100, 100, 100),
                    "border_color": COLOR_TRANSPARENT,
                    "border_width": 0
                },
                "hover": {
                    "font_name": "Arial",
                    "font_size": 16,
                    "font_color": COLOR_WHITE,
                    "bg": (120, 120, 120),
                    "border_color": COLOR_TRANSPARENT,
                    "border_width": 0
                },
                "press": {
                    "font_name": "Arial",
                    "font_size": 16,
                    "font_color": COLOR_WHITE,
                    "bg": (150, 150, 150),
                    "border_color": COLOR_TRANSPARENT,
                    "border_width": 0
                }
            }
        )
        
        @close_button.event("on_click")
        def on_click_close(event):
            self.main_view.show_main_menu()
        
        main_vbox = arcade.gui.UIBoxLayout(vertical=True, align="center", space_between=20)
        main_vbox.add(headers_box)
        main_vbox.add(data_box)
        main_vbox.add(close_button)
        
        self.add(bg)
        self.add(main_vbox)

class MainMenuView(arcade.View):
    def __init__(self):
        super().__init__()
        
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        
        self.setup_ui()
    
    def setup_ui(self):
        self.manager.clear()
        
        self.v_box = arcade.gui.UIBoxLayout(vertical=True, space_between=20, align="center")
        
        buttons_data = [
            ("Начать игру", self.on_click_start),
            ("Справка", self.on_click_help),
            ("Лучшие результаты", self.on_click_leaderboard),
            ("Выйти из игры", self.on_click_exit)
        ]
        
        for text, callback in buttons_data:
            button = MenuButton(text=text)
            
            @button.event("on_click")
            def on_click(event, cb=callback):
                cb()
            
            self.v_box.add(button)
        
        anchor = arcade.gui.UIAnchorLayout()
        anchor.add(child=self.v_box, anchor_x="center", anchor_y="center")
        
        self.manager.add(anchor)
    
    def show_main_menu(self):
        self.setup_ui()
    
    def on_click_start(self):
        print("Кнопка 'Начать игру' нажата")
    
    def on_click_help(self):
        help_window = HelpWindow(self)
        self.manager.clear()
        self.manager.add(help_window)
    
    def on_click_leaderboard(self):
        leaderboard_window = LeaderboardWindow(self)
        self.manager.clear()
        self.manager.add(leaderboard_window)
    
    def on_click_exit(self):
        arcade.exit()
    
    def on_draw(self):
        self.clear((50, 50, 50))
        
        self.manager.draw()
        
        arcade.draw_text(
            "ЭВОЛЮЦИОННЫЙ ЗАЩИТНИК",
            SCREEN_WIDTH // 2,
            SCREEN_HEIGHT - 150,
            COLOR_WHITE,
            64,
            anchor_x="center",
            anchor_y="center",
            font_name="Arial",
            bold=True
        )
    
    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            arcade.exit()
        
        if key == arcade.key.F10:
            window = self.window
            window.set_fullscreen(not window.fullscreen)
    
    def on_show_view(self):
        self.manager.enable()
    
    def on_hide_view(self):
        self.manager.disable()

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, fullscreen=True)
    menu_view = MainMenuView()
    window.show_view(menu_view)
    arcade.run()

if __name__ == "__main__":
    main()