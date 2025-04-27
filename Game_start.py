import random
import pygame
from Cards import all_cards,EventCard,ExperimentCard,InspirationCard,ScientistCard
# 1. 卡牌分堆并洗牌
def prepare_decks():
    def by_period(cards):
        return {
            "古代": [c for c in all_cards if c.period == "古代"],
            "近代": [c for c in all_cards if c.period == "近代"],
            "现代": [c for c in all_cards if c.period == "现代"],
        }

    # 分堆
    exp_decks = by_period(EventCard)
    insp_decks = by_period(ExperimentCard)
    sci_decks = by_period(ScientistCard)

    # 洗牌
    for deck in [exp_decks, insp_decks, sci_decks]:
        for era in deck:
            random.shuffle(deck[era])

    return exp_decks, insp_decks, sci_decks

# 2. 玩家初始化资源与手牌,牌库中牌减少
def create_players(num_players, exp_deck, insp_deck, sci_deck):
    players = []
    for i in range(num_players):
        player = {
            "id": i + 1,
            "resources": {
                "Capital": 3,
                "Inspiration": 2,
                "Experiment": 1,
                "Literature": 1
            },
            "hand": []
        }

        # 从每个卡堆中各抽 1 张，并移除该卡（确保唯一）
        if exp_deck:
            player["hand"].append(exp_deck.pop(0))
        if insp_deck:
            player["hand"].append(insp_deck.pop(0))
        if sci_deck:
            player["hand"].append(sci_deck.pop(0))

        players.append(player)
    return players

# 游戏开始函数
def start_game(num_players=3):
    # 当前时代标记
    current_period = "古代"

    # 分堆 + 洗牌
    exp_decks, insp_decks, sci_decks = prepare_decks()

    # 从当前时代堆中取出卡堆
    exp = exp_decks[current_period]
    insp = insp_decks[current_period]
    sci = sci_decks[current_period]

    # 初始化玩家
    players = create_players(num_players, exp, insp, sci)

    return {
        "players": players,
        "current_period": current_period,
        "decks": {
            "experiment": exp_decks,
            "inspiration": insp_decks,
            "scientist": sci_decks
        }
    }
