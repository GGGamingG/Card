import pygame
import random
from Game_start import start_game
from game_function import roll_two_dice, apply_points

# === 初始化 Pygame ===
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("多人骰子卡牌游戏")
FONT = pygame.font.SysFont("simhei.ttf", 28)
WHITE, BLACK = (255, 255, 255), (0, 0, 0)

# === 读取玩家人数 ===
try:
    NUM_PLAYERS = int(input("请输入玩家人数（建议2~4）："))
    if NUM_PLAYERS < 1:
        raise ValueError
except ValueError:
    print("⚠️ 输入无效，默认设置为 2 名玩家")
    NUM_PLAYERS = 2

# === 初始化游戏状态 ===
game_state = start_game(num_players=NUM_PLAYERS)
players = game_state["players"]
current_period = game_state["current_period"]

# === 游戏变量 ===
current_player = 0
dice_result = None
has_rolled = False

# === 按钮区域 ===
dice_button = pygame.Rect(100, 100, 100, 50)
end_turn_button = pygame.Rect(100, 200, 100, 50)

# === 资源选择 ===
choice_buttons = []
choice_pending = None
waiting_for_choice = False

# === 分数绘制 ===
def get_player_points(index):
    return players[index]["resources"]

def draw_scores():
    points = get_player_points(current_player)
    y = 200
    for key, value in points.items():
        text = FONT.render(f"{key}: {value}", True, BLACK)
        screen.blit(text, (500, y))
        y += 30

# === 手牌绘制 ===
def draw_hand(player_index):
    hand = players[player_index]["hand"]
    y = 400
    screen.blit(FONT.render("手牌：", True, BLACK), (500, y))
    for card in hand:
        y += 28
        screen.blit(FONT.render(f"{card.name}（{card.type}）", True, BLACK), (500, y))

# === 资源选择按钮 ===
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

# === 游戏主循环 ===
running = True
while running:
    screen.fill(WHITE)

    # 按钮
    pygame.draw.rect(screen, (180, 180, 180), dice_button)
    pygame.draw.rect(screen, (150, 180, 200), end_turn_button)
    screen.blit(FONT.render("Dice", True, BLACK), (dice_button.x + 10, dice_button.y + 10))
    screen.blit(FONT.render("Rond over", True, BLACK), (end_turn_button.x + 10, end_turn_button.y + 10))

    # 文本
    screen.blit(FONT.render(f"Play {current_player + 1} operation", True, BLACK), (100, 40))
    if dice_result:
        screen.blit(FONT.render(f"Dice: {dice_result}", True, BLACK), (500, 150))

    # 状态区
    draw_scores()
    draw_hand(current_player)

    if waiting_for_choice:
        screen.blit(FONT.render("Choose resource：", True, BLACK), (100, 350))
        draw_choice_buttons()

    # 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos

            if dice_button.collidepoint(pos) and not has_rolled and not waiting_for_choice:
                dice_result, options, amount = roll_two_dice(current_player)
                has_rolled = True
                if options:
                    show_choice_buttons(options, amount)

            elif end_turn_button.collidepoint(pos) and not waiting_for_choice:
                current_player = (current_player + 1) % NUM_PLAYERS
                has_rolled = False
                dice_result = None

            if waiting_for_choice:
                for rect, label in choice_buttons:
                    if rect.collidepoint(pos):
                        apply_points(current_player, label, choice_pending[1])
                        waiting_for_choice = False
                        choice_buttons.clear()
                        break

    pygame.display.flip()

pygame.quit()