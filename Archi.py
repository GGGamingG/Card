from abc import ABC, abstractmethod
from typing import List
from enum import Enum, auto
import random
from GameCharacter import roles_dict
class Croupier:
    # 游戏荷官，负责整局游戏的流程、计分等
    
    def __init__(self, players: List["Player"], deck: "Deck"):
        self.players = players  # 游戏中的玩家列表
        self.deck = deck        # 卡堆
        self.current_player_index = 0  # 当前轮到的玩家索引

    def run_game(self):
        """启动游戏，分发初始手牌，并开始回合循环"""
        self._initialize_players()
        self.assign_roles()
        while not self._is_game_over():
            self._play_turn()
            self.check_victory()
        self._end_game()
        
    def assign_roles(self):
        """分配身份"""
        roles = []   # 【【【以三国杀为例的话  ["主公", "忠臣", "反贼", "反贼", "内奸"  # 身份往往和技能绑定，可以抽象出来?]】】】
        random.shuffle(roles)
        for player, role in zip(self.players, roles):
            self.roles[player] = role
            player.set_role(role)
            
    def _initialize_players(self):
        """初始化玩家，发放初始手牌"""
        for player in self.players:
            player.draw_cards(self.deck, 4)  # 默认每人摸4张牌
 
    def _play_turn(self):
        """每个玩家、每一轮的核心流程"""
        
        current_player = self.players[self.current_player_index]  # 判断当前轮的玩家
        current_player.before_turn()        # 轮前结算
        current_player.draw_cards(self.deck, 2)          # 摸牌
        current_player.play_turn(self)        # 出牌阶段
        current_player.after_turn()        # 轮后结算
        
        self.current_player_index = (self.current_player_index + 1) % len(self.players)        # 切换到下一个玩家
 
    def _is_game_over(self) -> bool:
        return any(player.is_defeated() for player in self.players)        # 判断游戏是否结束
    def show_scores(self):
        print("\n=== 当前得分 ===")
        for record in self.records:
            print(record)
    def _end_game(self):
        # print("Game Over")         # 游戏结束时的处理
        self.records.sort(key=lambda r: r.score, reverse=True)
        for idx, record in enumerate(self.records, start=1):
            print(f"🏆 第{idx}名：\n{record}\n")
    def check_victory(self):
        """检查胜负条件"""
        return False
    
 
class Player(ABC):
    def __init__(self, name: str, role_name: str):
        self.name = name
        self.hand = []  # 手牌
        self.health = 4  # 初始生命值
        self.role =  roles_dict[role_name]  # 玩家身份
        self.skills = self.role.skills    # 输入玩家身份后自动匹配角色技能
        self.goal = self.role.goal        # 输入玩家身份后自动匹配角色目标
    #def set_role(self, role: Role):
    def set_role(self, role: str):
        """设置玩家身份"""
        self.role = role
    def use_skill(self, skill_name: str):
        if skill_name not in self.cooldowns:
            print(f"❌ {self.name} 没有技能：{skill_name}")
            return

        if self.cooldowns[skill_name] > 0:
            print(f"⌛ 技能 {skill_name} 冷却中，还需 {self.cooldowns[skill_name]} 回合")
            return

        for skill in self.skills:
            if skill.name == skill_name:
                skill.use(user=self)
                # 使用后技能进入冷却，可以根据技能类型设定不同冷却时间，这里统一冷却2回合
                self.cooldowns[skill_name] = 2
                return
'''        
    def use_skill(self, skill_name: str, game: "Croupier"):
        """使用技能"""
        for skill in self.skills:
            if skill.name == skill_name:
                skill.activate(self, game)
                return
        print(f"{self.name} 没有技能 {skill_name}")
 
    def respond_to_card(self, card: "Card") -> bool:
        """响应卡牌的逻辑"""
        for response_card in self.hand:
            if response_card.can_counter(card):  # 假设有能反制的逻辑
                self.hand.remove(response_card)
                print(f"{self.name} 使用 {response_card} 响应 {card}")
                return True
        print(f"{self.name} 无法响应 {card}")
        return False
'''
'''
class Card(ABC):
    @abstractmethod
    def play(self, player: "Player", game: "Croupier", targets: List["Player"]):
        """卡牌被打出时的行为"""
        pass
 
    def process_responses(self, game: "Croupier", targets: List["Player"]):
        """处理多个目标玩家的响应逻辑"""
        for target in targets:
            if self.requires_response():
                responded = target.respond_to_card(self)
                if not responded:
                    self.apply_effect(target)
 
    @abstractmethod
    def apply_effect(self, target: "Player"):
        """对目标玩家应用卡牌效果"""
        pass
 
    @abstractmethod
    def requires_response(self) -> bool:
        """是否需要其他玩家响应"""
        return False
 
    
 
class Skill(ABC):
    def __init__(self, name: str):
        self.name = name
 
    @abstractmethod
    def activate(self, player: "Player", game: "Croupier"):
        """技能的具体效果"""
        pass
'''
class Deck:
    def __init__(self, cards: List["Card"]):
        '''
        self.cards = cards
        random.shuffle(self.cards)
        '''
        self.unused = all_cards.copy()  # 未使用牌堆
        self.used = []  # 已使用牌堆
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.unused)

    '''
    def draw(self) -> "Card":
        """从卡堆顶抽取一张卡牌"""
        if self.cards:
            return self.cards.pop()
        return None
    '''

    def draw(self, n=1):
        drawn_cards = []
        for _ in range(n):
            if self.unused:
                drawn_cards.append(self.unused.pop(0))
            else:
                print("⚠️ 未使用牌堆为空，无法抽牌！")
                # 此处也可以讲used洗牌引入unesed
                break
        return drawn_cards


    def add_to_discard_pile(self, card: "Card"):
        """将卡牌放入弃牌堆"""
        # 如果需要弃牌堆，可以在这里实现
        pass
    
    def show_top(self, K):
        """展示牌顶的几张"""
        pass

class Record: # 每个 Player 就可以有一个 Record 作为自己的记分板
    def __init__(self, player_id: int, player_name: str):
        self.player_id = player_id
        self.player_name = player_name
        self.score = 0
        self.details = []  # 详细得分记录，如完成事件、达成目标等

    def add_points(self, points: int, reason: str = ""):
        self.score += points
        if reason:
            self.details.append(f"+{points}：{reason}")
        else:
            self.details.append(f"+{points}")

    def reduce_points(self, points: int, reason: str = ""):
        self.score -= points
        if reason:
            self.details.append(f"-{points}：{reason}")
        else:
            self.details.append(f"-{points}")

    def __str__(self):
        details_str = "\\n  ".join(self.details)
        return (f"🎯 玩家 {self.player_id}：{self.player_name}\\n"
                f"总分：{self.score}\\n"
                f"详细记录：\\n  {details_str if details_str else '暂无记录'}")