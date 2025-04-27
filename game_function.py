# game_logic.py

import random

# 多玩家积分，结构是一个列表：每个元素是一个玩家的积分字典
player_points_list = []

def init_players(n):
    global player_points_list
    player_points_list = []
    for _ in range(n):
        player_points_list.append({
            "Capital": 0,
            "Inspiration": 0,
            "Experiment": 0,
            "Literature": 0
        })

def get_player_points(player_index):
    return player_points_list[player_index]
def apply_points(player_index, choice, amount):
    player_points_list[player_index][choice] += amount
def roll_two_dice(player_index):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    print(f"玩家{player_index + 1} 骰子结果: {die1} + {die2} = {total}")
    points = player_points_list[player_index]

    # 需要界面上做出选择的情况
    if total == 2:
        return total, ["Capital", "Inspiration"], 2
    elif total in [3, 4]:
        points["Capital"] += 1
        points["Inspiration"] += 1
    elif total in [5, 6]:
        points["Experiment"] += 1
        points["Literature"] += 1
    elif total in [7, 8]:
        return total, ["Experiment", "Literature"], 2
    elif total in [9, 10]:
        points["Capital"] += 1
        points["Experiment"] += 1
    elif total in [11, 12]:
        points["Inspiration"] += 1
        points["Literature"] += 1

    return total, None, None
