import arcade
import math

SCREEN_WIDTH = 1980
SCREEN_HEIGHT = 1080

ATTACK = "attack"
MOVE = "move"

PARALLELOGRAM = "parallelogram"
CIRCLE = "circle"
TRIANGLE = "triangle"

class MobData:
    def __init__(self, parts):
        self.parts = parts

class ConnectionPoint:
    def __init__(self, offset_x, offset_y):
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.occupied = False

    def world_pos(self, part):
        return (
            part.center_x + self.offset_x,
            part.center_y + self.offset_y
        )


class Part:
    def __init__(self, x, y, shape, part_type):
        self.center_x = x
        self.center_y = y
        self.shape = shape
        self.part_type = part_type
        self.attached_to = None
        self.children = []

        self.connection_points = self.create_points()

    def create_points(self):
        points = [ConnectionPoint(0, 0)]

        if self.shape == PARALLELOGRAM:
            points += [
                ConnectionPoint(30, 30),
                ConnectionPoint(-30, 30),
                ConnectionPoint(30, -30),
                ConnectionPoint(-30, -30)
            ]

        if self.shape == CIRCLE:
            points += [
                ConnectionPoint(40, 0),
                ConnectionPoint(-40, 0),
                ConnectionPoint(0, 40),
                ConnectionPoint(0, -40)
            ]

        if self.shape == TRIANGLE:
            points += [
                ConnectionPoint(30, -30),
                ConnectionPoint(-30, -30),
                ConnectionPoint(0, 40)
            ]

        return points

    def draw(self):
        color = arcade.color.RED if self.part_type == ATTACK else arcade.color.BLUE

        if self.shape == CIRCLE:
            arcade.draw_circle_filled(
                self.center_x,
                self.center_y,
                40,
                color
            )

        if self.shape == PARALLELOGRAM:
            arcade.draw_lbwh_rectangle_filled(
                self.center_x - 40,
                self.center_y - 30,
                80,
                60,
                color
            )

        if self.shape == TRIANGLE:
            arcade.draw_triangle_filled(
                self.center_x, self.center_y + 40,
                self.center_x - 40, self.center_y - 40,
                self.center_x + 40, self.center_y - 40,
                color
            )

        for p in self.connection_points:
            if not p.occupied:
                x, y = p.world_pos(self)
                arcade.draw_circle_outline(
                    x,
                    y,
                    6,
                    arcade.color.YELLOW
                )


class GhostPart(Part):
    def draw(self):
        arcade.draw_circle_filled(
            self.center_x,
            self.center_y,
            40,
            (255, 255, 255, 120)
        )


class MobEditorView(arcade.View):
    def __init__(self, on_save_callback):
        super().__init__()
        self.on_save_callback = on_save_callback
        self.parts = []

        self.core = Part(
            SCREEN_WIDTH // 2,
            SCREEN_HEIGHT // 2,
            PARALLELOGRAM,
            ATTACK
        )
        self.parts.append(self.core)

        self.selected_shape = None
        self.selected_type = None
        self.ghost = None

    def on_draw(self):
        self.clear((25, 25, 25))

        for part in self.parts:
            part.draw()

        if self.ghost:
            self.ghost.draw()

        arcade.draw_text("1 – атакующая", 20, SCREEN_HEIGHT - 40, arcade.color.WHITE, 18)
        arcade.draw_text("2 – двигающаяся", 20, SCREEN_HEIGHT - 70, arcade.color.WHITE, 18)
        arcade.draw_text("Q – параллелограмм", 20, SCREEN_HEIGHT - 110, arcade.color.WHITE, 18)
        arcade.draw_text("W – круг", 20, SCREEN_HEIGHT - 140, arcade.color.WHITE, 18)
        arcade.draw_text("E – треугольник", 20, SCREEN_HEIGHT - 170, arcade.color.WHITE, 18)

    def on_mouse_motion(self, x, y, dx, dy):
        if self.ghost:
            self.ghost.center_x = x
            self.ghost.center_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        if not self.ghost:
            return

        for part in self.parts:
            for p1 in self.ghost.connection_points:
                gx, gy = p1.world_pos(self.ghost)

                for p2 in part.connection_points:
                    if p2.occupied:
                        continue

                    px, py = p2.world_pos(part)
                    if math.dist((gx, gy), (px, py)) < 15:
                        p1.occupied = True
                        p2.occupied = True

                        self.ghost.center_x = px - p1.offset_x
                        self.ghost.center_y = py - p1.offset_y

                        self.parts.append(self.ghost)
                        self.ghost = None
                        return

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            from menu import MobSelectView
            self.window.show_view(MobSelectView())

        if key == arcade.key.ENTER:
            mob = MobData(self.parts.copy())
            self.on_save_callback(mob)
            from menu import MobSelectView
            self.window.show_view(MobSelectView())

        if key == arcade.key.KEY_1:
            self.selected_type = ATTACK

        if key == arcade.key.KEY_2:
            self.selected_type = MOVE

        if key == arcade.key.Q:
            self.selected_shape = PARALLELOGRAM

        if key == arcade.key.W:
            self.selected_shape = CIRCLE

        if key == arcade.key.E:
            self.selected_shape = TRIANGLE

        if self.selected_shape and self.selected_type:
            self.ghost = Part(0, 0, self.selected_shape, self.selected_type)
