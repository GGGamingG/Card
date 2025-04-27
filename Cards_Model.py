from Skills import skills_dict

class Card:
    def __init__(self, id, name, period, type_):
        self.id = id
        self.name = name
        self.period = period
        self.type = type_

class EventCard(Card):
    def __init__(self, id, name, year, period, require, score, skill_name=None, knowledge=""):
        super().__init__(id, name, period, "事件卡")
        self.year = year
        self.require = require  # 例如 {"Capital": 3, "Experiment": 2}
        self.score = score
        self.knowledge = knowledge

        if skill_name:
            self.skill = skills_dict.get(skill_name)
        else:
            self.skill = None
    def use_skill(self, user=None):
        if self.skill:
            self.skill.use(user)
        else:
            print(f"📜 {self.name} 没有绑定技能。")
    def is_playable(self, player_resources):
        for res, val in self.require.items():
            if player_resources.get(res, 0) < val:
                print("不能打出")
                return False
        return print("可以打出")

    def __str__(self):
        return f"[{self.name}]（{self.year}，{self.period} - 事件卡）\n需求: {self.require} | 分数: {self.score}\n效果: {self.effect}\n知识点: {self.knowledge}"
class ExperimentCard(Card):
    def __init__(self, id, name, period, upkeep, effect):
        super().__init__(id, name, period, "实验卡")
        self.upkeep = upkeep
        self.effect = effect

    def __str__(self):
        return f"[{self.name}]（{self.period} - 实验卡）\n维持费: {self.upkeep}\n效果: {self.effect}"


class InspirationCard(Card):
    def __init__(self, id, name, period,effect=""):
        super().__init__(id, name, period, "灵感卡")
        self.effect = effect

    def __str__(self):
        return f"[{self.name}]（灵感卡）\n效果: {self.effect}"

class ScientistCard(Card):
    def __init__(self, id, name, ability, end_score, period=""):
        super().__init__(id, name, period, "科学家卡")
        self.ability = ability
        self.end_score = end_score

    def __str__(self):
        return f"[{self.name}]（{self.period} - 科学家卡）\n能力: {self.ability}\n终局分: {self.end_score}"

