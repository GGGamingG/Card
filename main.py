# main.py

import pygame
from game_function import init_players, get_player_points, roll_two_dice, apply_points
from Game_start import start_game
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("多人骰子卡牌游戏")
#FONT = pygame.font.Font("fonts/simsunb.ttf", 36)
FONT = pygame.font.SysFont("simhei.ttf", 36)
WHITE, BLACK = (255, 255, 255), (0, 0, 0)

dice_button = pygame.Rect(100, 100, 100, 50)
end_turn_button = pygame.Rect(100, 200, 100, 50)

# 用于选择资源的按钮（初始化时隐藏）
choice_buttons = []
choice_pending = None  # (options_list, amount)
waiting_for_choice = False

# 初始化玩家数量
NUM_PLAYERS = 3
init_players(NUM_PLAYERS)

current_player = 0
dice_result = None
has_rolled = False  # 限制每轮只能投一次

def draw_scores():
    points = get_player_points(current_player)
    y = 200
    for key, value in points.items():
        text = FONT.render(f"{key}: {value}", True, BLACK)
        screen.blit(text, (500, y))
        y += 40

def show_choice_buttons(options, amount):
    global choice_buttons, waiting_for_choice, choice_pending
    waiting_for_choice = True
    choice_pending = (options, amount)
    choice_buttons.clear()
    x = 100
    for opt in options:
        rect = pygame.Rect(x, 400, 180, 50)
        choice_buttons.append((rect, opt))
        x += 200

def draw_choice_buttons():
    for rect, label in choice_buttons:
        pygame.draw.rect(screen, (200, 220, 255), rect)
        text = FONT.render(label, True, BLACK)
        screen.blit(text, (rect.x + 20, rect.y + 10))

# 主循环
running = True
while running:
    screen.fill(WHITE)

    pygame.draw.rect(screen, (180, 180, 180), dice_button)
    pygame.draw.rect(screen, (150, 180, 200), end_turn_button)

    screen.blit(FONT.render("Dice", True, BLACK), (dice_button.x + 10, dice_button.y + 10))
    screen.blit(FONT.render("Rond over", True, BLACK), (end_turn_button.x + 10, end_turn_button.y + 10))
    screen.blit(FONT.render(f"Play {current_player + 1} operation", True, BLACK), (100, 40))

    if dice_result:
        screen.blit(FONT.render(f"Dice: {dice_result}", True, BLACK), (500, 150))

    draw_scores()

    if waiting_for_choice:
        screen.blit(FONT.render("Choose resource：", True, BLACK), (100, 350))
        draw_choice_buttons()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos

            # 投骰子按钮
            if dice_button.collidepoint(pos) and not has_rolled and not waiting_for_choice:
                dice_result, options, amount = roll_two_dice(current_player)
                has_rolled = True
                if options:
                    show_choice_buttons(options, amount)

            # 结束回合按钮
            elif end_turn_button.collidepoint(pos) and not waiting_for_choice:
                current_player = (current_player + 1) % NUM_PLAYERS
                has_rolled = False
                dice_result = None

            # 点击了某个资源按钮
            if waiting_for_choice:
                for rect, label in choice_buttons:
                    if rect.collidepoint(pos):
                        apply_points(current_player, label, choice_pending[1])
                        waiting_for_choice = False
                        choice_buttons.clear()
                        break

    pygame.display.flip()

pygame.quit()