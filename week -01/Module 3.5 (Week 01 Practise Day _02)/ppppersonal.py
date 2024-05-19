import pyautogui

def draw_pyramid(levels):
    screen_width, screen_height = pyautogui.size()
    pyramid_width = levels * 2 - 1
    pyramid_height = levels

    brick_width = 20
    brick_height = 10

    start_x = (screen_width - pyramid_width * brick_width) // 2
    start_y = screen_height - pyramid_height * brick_height

    for i in range(pyramid_height):
        bricks_in_row = i * 2 + 1
        row_start_x = start_x + (pyramid_width - bricks_in_row) // 2 * brick_width
        row_y = start_y + i * brick_height

        for j in range(bricks_in_row):
            brick_x = row_start_x + j * brick_width
            pyautogui.drawRect(brick_x, row_y, brick_width, brick_height)

levels = int(input("Enter the number of levels for the pyramid: "))
draw_pyramid(levels)
