import pygame
from random import *

# 래벨 설정
def setup(level):
    number_count = (level // 3) + 5
    number_count = min(number_count, 20)

    suffle_grid(number_count)

def suffle_grid(number_count):
    rows = 5
    columns = 9

    cell_size = 130
    button_size = 110
    screen_left_margin = 55
    screen_top_margin = 20

    grid = [[0 for col in range(columns)] for row in range(rows)]

    number = 1
    while number <= number_count:
        row_index = randrange(0, rows)
        columns_index = randrange(0, columns)
        if grid[row_index][columns_index] == 0:
            grid[row_index][columns_index] = number
            number += 1

            center_x = screen_left_margin + columns_index * cell_size + cell_size / 2
            center_y = screen_top_margin + row_index * cell_size + cell_size / 2

            button = pygame.Rect(0, 0, button_size, button_size)
            button.center = (center_x, center_y)

            number_buttons.append(button)

    for i in grid:
        print(i)


# 시작 화면 보여줌
def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)

# 게임 화면 보여줌
def display_game_screen():
    for idx, rect in enumerate(number_buttons, start=1):
        if hidden:
            # 사각
            pygame.draw.rect(screen, WHITE, rect)
        else:
            # 숫자
            cell_text = game_font.render(str(idx), True, WHITE)
            text_rect = cell_text.get_rect(center=rect.center)
            screen.blit(cell_text, text_rect)



def check_number_buttons(pos):
    global hidden
    for button in number_buttons:
        if button.collidepoint(pos):
            if button == number_buttons[0]:
                del number_buttons[0]
                if not hidden:
                    hidden = True
            else:
                print('wrong')
            break

# pos에 해당하는 버튼 확인
def check_buttons(pos):
    global start
    
    if start:
        check_number_buttons(pos)    
    elif start_button.collidepoint(pos):
        start = True



# 초기화
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory game")
game_font = pygame.font.Font(None, 120)

# 시작 버튼
start_button = pygame.Rect(0, 0, 120, 120)
start_button.center = (120, screen_height - 120)

# 색
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)

# 버튼
number_buttons = []

# 게임 시작 여부
start = False
# 숫자 숨김 여부
hidden = False

# 게임 설정
setup(1)

# 게임 루프
running = True
while running:
    click_pos = None

    # 이벤트 루프
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            click_pos = pygame.mouse.get_pos()

    # 화면
    screen.fill(BLACK)

    if start:
        display_game_screen()       # 게임 화면
    else:
        display_start_screen()      # 시작 화면

    if click_pos:
        check_buttons(click_pos)

    # 화면 업데이트
    pygame.display.update()

# 게임 종료
pygame.quit()