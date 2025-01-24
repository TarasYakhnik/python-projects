import pygame as pg
import sys

pg.init()

WIDTH = 800
HEIGHT = 600

BLACK = ((0, 0, 0))
WHITE = ((255, 255, 255))
RED = ((255, 0, 0))
GREEN = ((34, 139, 34))
DARKGREEN = ((0, 100, 0))

num1 = ''
num2 = ''
operator = ''
typing_num1 = True
operator_is_input = False
result_is_ready = False
result_is_displayed = False
num1_list = []
num2_list = []

font = pg.font.Font(None, 36)
Font = pg.font.Font(None, 50)


class Button:
    def __init__(self, x, y, width, height, name):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.name = name

    def is_clicked(self, mouse_x, mouse_y):
        if self.x < mouse_x < self.x + self.width and self.y < mouse_y < self.y + self.height:
            return True
        return False


buttons = [
    Button(240, 200, 60, 60, '1'),
    Button(310, 200, 60, 60, '2'),
    Button(380, 200, 60, 60, '3'),
    Button(240, 270, 60, 60, '4'),
    Button(310, 270, 60, 60, '5'),
    Button(380, 270, 60, 60, '6'),
    Button(240, 340, 60, 60, '7'),
    Button(310, 340, 60, 60, '8'),
    Button(380, 340, 60, 60, '9'),
    Button(310, 410, 60, 60, '0'),
    Button(460, 270, 60, 60, '÷'),
    Button(460, 340, 60, 60, 'х'),
    Button(530, 270, 60, 60, '-'),
    Button(530, 340, 60, 60, '+'),
    Button(530, 410, 60, 60, '='),
    Button(380, 410, 60, 60, ','),
    Button(460, 410, 60, 60, 'AC')
]

chiffres = [buttons[9], buttons[0], buttons[1], buttons[2], buttons[3], buttons[4], buttons[5], buttons[6], buttons[7],
            buttons[8]]
operators = [buttons[10], buttons[11], buttons[12], buttons[13]]
buttons_clicked = []

screen = pg.display.set_mode((WIDTH, HEIGHT))

run = True

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = pg.mouse.get_pos()

            for button in buttons:
                if button.is_clicked(mouse_x, mouse_y):
                    buttons_clicked.append(button.name)

                    if result_is_ready and button.name != 'AC':
                        continue

                    if button.name in [cfr.name for cfr in chiffres]:
                        if typing_num1:
                            num1_list.append(button.name)
                            num1 = int(''.join(num1_list))
                        elif operator_is_input:
                            num2_list.append(button.name)
                            num2 = int(''.join(num2_list))

                    elif button.name in [op.name for op in operators]:
                        if num1:
                            operator = button.name
                            typing_num1 = False
                            operator_is_input = True

                    if button.name == 'AC':
                        buttons_clicked.clear()
                        num1_list.clear()
                        num2_list.clear()
                        result = 0
                        result_is_ready = False
                        typing_num1 = True
                        result_is_displayed = False
                        operator = ''
                        num1 = ''
                        num2 = ''
                        print(result)

                    elif button.name == '=':
                        if num1 and num2 and not result_is_displayed:
                            result_is_displayed = True
                            try:
                                num1 = int(num1)
                                num2 = int(num2)

                                print(f"num1: {num1}, num2: {num2}, operator: {operator}")

                                if operator == '÷' and num2 == 0:
                                    result = 'Error'
                                else:
                                    if operator == '+':
                                        result = num1 + num2
                                    elif operator == '-':
                                        result = num1 - num2
                                    elif operator == 'х':
                                        result = num1 * num2
                                    elif operator == '÷':
                                        result = float(num1 / num2)

                            except ZeroDivisionError:
                                result = 'Error'
                            except ValueError:
                                result = 'Error'

                            print(f"result: {result}")
                        else:
                            result = 'Error'

                        print(f"final result: {result}")

                        buttons_clicked.clear()
                        result_is_ready = True
                        Result = list(str(result))

    screen.fill(BLACK)

    if result_is_ready:
        pg.draw.rect(screen, GREEN, (120, 100, 470, 70))

        visible_text_symbols = ''.join(Result)
        visible_text = Font.render(visible_text_symbols, True, DARKGREEN)

        visible_text_x = 570 - (visible_text.get_width() // 2) - (10 * len(Result))
        visible_text_y = 100 + (70 // 2) - (visible_text.get_height() // 2)

        screen.blit(visible_text, (visible_text_x, visible_text_y))
    else:
        pg.draw.rect(screen, GREEN, (120, 100, 470, 70))

        visible_text_symbols = ''.join(buttons_clicked)
        visible_text = Font.render(visible_text_symbols, True, DARKGREEN)

        visible_text_x = 570 - (visible_text.get_width() // 2) - (10 * len(buttons_clicked))
        visible_text_y = 100 + (70 // 2) - (visible_text.get_height() // 2)

        screen.blit(visible_text, (visible_text_x, visible_text_y))

    for button in buttons:
        pg.draw.rect(screen, RED, (button.x, button.y, button.width, button.height))

        Button_symbol = font.render(button.name, True, WHITE)

        Button_symbol_x = button.x + (button.width // 2) - (Button_symbol.get_width() // 2)
        Button_symbol_y = button.y + (button.height // 2) - (Button_symbol.get_height() // 2)

        screen.blit(Button_symbol, (Button_symbol_x, Button_symbol_y))

    pg.display.flip()

pg.quit()
sys.exit()
