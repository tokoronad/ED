import arcade
import arcade.gui

SCREEN_WIDTH = 1980
SCREEN_HEIGHT = 1080
SCREEN_TITLE = "Эволюционный защитник"

COLOR_WHITE = arcade.color.WHITE
COLOR_GRAY = arcade.color.GRAY
COLOR_LIGHT_GRAY = arcade.color.LIGHT_GRAY
COLOR_TRANSPARENT = (0, 0, 0, 0)
COLOR_BLACK_TRANSPARENT = (0, 0, 0, 180)
created_mobs = []

class MobSelectView(arcade.View):
    def __init__(self):
        super().__init__()
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        layout = arcade.gui.UIBoxLayout(vertical=False, space_between=100)

        self.list1 = self._create_list("Моб 1")
        self.list2 = self._create_list("Моб 2")

        layout.add(self.list1)
        layout.add(self.list2)

        anchor = arcade.gui.UIAnchorLayout()
        anchor.add(layout, anchor_x="center", anchor_y="center")
        self.manager.add(anchor)

    def _create_list(self, title):
        vbox = arcade.gui.UIBoxLayout(vertical=True, space_between=10)

        vbox.add(arcade.gui.UILabel(text=title, font_size=24))

        for i, mob in enumerate(created_mobs):
            btn = arcade.gui.UIFlatButton(text=f"Моб #{i+1}", width=200)

            @btn.event("on_click")
            def select(event, m=mob):
                print("Выбран моб", m)

            vbox.add(btn)

        add_btn = arcade.gui.UIFlatButton(text="+", width=200, height=50)

        @add_btn.event("on_click")
        def add(event):
            from game import MobEditorView
            self.window.show_view(
                MobEditorView(self._save_mob)
            )

        vbox.add(add_btn)
        return vbox

    def _save_mob(self, mob):
        created_mobs.append(mob)

    def on_draw(self):
        self.clear((30, 30, 30))
        self.manager.draw()

    def on_hide_view(self):
        self.manager.disable()

class MenuButton(arcade.gui.UIFlatButton):
    def __init__(self, text):
        style = {
            "normal": {
                "font_name": "Arial",
                "font_size": 24,
                "font_color": COLOR_WHITE,
                "bg": COLOR_TRANSPARENT,
                "border_width": 0
            },
            "hover": {
                "font_name": "Arial",
                "font_size": 24,
                "font_color": COLOR_WHITE,
                "bg": COLOR_BLACK_TRANSPARENT,
                "border_width": 0
            },
            "press": {
                "font_name": "Arial",
                "font_size": 24,
                "font_color": COLOR_WHITE,
                "bg": COLOR_BLACK_TRANSPARENT,
                "border_width": 0
            }
        }
        super().__init__(text=text, width=420, height=60, style=style)


class HelpView(arcade.View):
    def __init__(self):
        super().__init__()
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        help_text = (
            "ЭВОЛЮЦИОННЫЙ ЗАЩИТНИК\n\n"
            "Вы создаёте моба, состоящего из частей тела.\n"
            "Моб автоматически обучается и защищает ваш Куб жизни.\n\n"
            "ЦЕЛЬ ИГРЫ:\n"
            "- Защитить свой Куб жизни\n"
            "- Уничтожить Куб противника\n\n"
            "ЧАСТИ МОБА:\n"
            "- Ноги — скорость\n"
            "- Руки — атака\n"
            "- Защита — броня\n"
            "- Сенсоры — радиус обнаружения\n\n"
            "Управление:\n"
            "ESC — назад в меню"
        )

        text_area = arcade.gui.UITextArea(
            text=help_text,
            width=900,
            height=500,
            font_size=18,
            text_color=COLOR_WHITE,
            multiline=True
        )

        back_button = MenuButton("Назад")

        @back_button.event("on_click")
        def back(event):
            self.window.show_view(MainMenuView())

        v_box = arcade.gui.UIBoxLayout(vertical=True, space_between=20)
        v_box.add(text_area)
        v_box.add(back_button)

        anchor = arcade.gui.UIAnchorLayout()
        anchor.add(v_box, anchor_x="center", anchor_y="center")
        self.manager.add(anchor)

    def on_draw(self):
        self.clear((30, 30, 30))
        self.manager.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            self.window.show_view(MainMenuView())

    def on_hide_view(self):
        self.manager.disable()


class LeaderboardView(arcade.View):
    def __init__(self):
        super().__init__()
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        leaders = (
            "1. Игрок1 — 1000\n"
            "2. Игрок2 — 950\n"
            "3. Игрок3 — 900\n"
            "4. Игрок4 — 850\n"
            "5. Игрок5 — 800\n"
        )

        leaderboard_text = arcade.gui.UITextArea(
            text=leaders,
            width=600,
            height=300,
            font_size=20,
            text_color=COLOR_LIGHT_GRAY,
            multiline=True
        )

        back_button = MenuButton("Назад")

        @back_button.event("on_click")
        def back(event):
            self.window.show_view(MainMenuView())

        v_box = arcade.gui.UIBoxLayout(vertical=True, space_between=20)
        v_box.add(leaderboard_text)
        v_box.add(back_button)

        anchor = arcade.gui.UIAnchorLayout()
        anchor.add(v_box, anchor_x="center", anchor_y="center")
        self.manager.add(anchor)

    def on_draw(self):
        self.clear((25, 25, 25))
        self.manager.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            self.window.show_view(MainMenuView())

    def on_hide_view(self):
        self.manager.disable()


class MainMenuView(arcade.View):
    def __init__(self):
        super().__init__()
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.build_ui()

    def build_ui(self):
        self.manager.clear()

        start_button = MenuButton("Начать игру")
        help_button = MenuButton("Справка")
        leaderboard_button = MenuButton("Лучшие результаты")
        exit_button = MenuButton("Выйти")

        @start_button.event("on_click")
        def start(event):
            self.window.show_view(MobSelectView())


        @help_button.event("on_click")
        def help_view(event):
            self.window.show_view(HelpView())

        @leaderboard_button.event("on_click")
        def leaderboard(event):
            self.window.show_view(LeaderboardView())

        @exit_button.event("on_click")
        def exit_game(event):
            arcade.exit()

        v_box = arcade.gui.UIBoxLayout(vertical=True, space_between=20)
        v_box.add(start_button)
        v_box.add(help_button)
        v_box.add(leaderboard_button)
        v_box.add(exit_button)

        anchor = arcade.gui.UIAnchorLayout()
        anchor.add(v_box, anchor_x="center", anchor_y="center")
        self.manager.add(anchor)

    def on_draw(self):
        self.clear((40, 40, 40))
        self.manager.draw()

        arcade.draw_text(
            "ЭВОЛЮЦИОННЫЙ ЗАЩИТНИК",
            SCREEN_WIDTH // 2,
            SCREEN_HEIGHT - 150,
            COLOR_WHITE,
            64,
            anchor_x="center",
            font_name="Arial",
            bold=True
        )

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            arcade.exit()

        if key == arcade.key.F10:
            self.window.set_fullscreen(not self.window.fullscreen)

    def on_hide_view(self):
        self.manager.disable()
