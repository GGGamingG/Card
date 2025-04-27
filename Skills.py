'''
class Skill:
    def __init__(self, name: str, effect: str):
        self.name = name
        self.effect = effect

    def use(self):
        print(f"✨ 触发技能：{self.name} → {self.effect}")
    def __str__(self):
        return f"{self.name}（效果：{self.effect}）"

skills_list = [
    Skill("1", "123"),
    Skill("2", "123+1"),
    Skill("3", "123，可抵消一次伤害"),
    Skill("4", "234+2分"),
    Skill("5", "234"),
    Skill("6", "234"),
    # ……后面随便加1000个技能也行
]
skills_dict = {skill.name: skill for skill in skills_list}

'''
class Skill:
    def __init__(self, name: str, effect_desc: str, effect_func=None):
        self.name = name
        self.effect_desc = effect_desc
        self.effect_func = effect_func  #技能真正执行的函数

    def use(self, user=None):
        print(f"✨ 触发技能：{self.name} → {self.effect_desc}")
        if self.effect_func:
            self.effect_func(user)

    def __str__(self):
        return f"{self.name}（效果：{self.effect_desc}）"

def predict_future_dice(user):
    print(f"🔮 {user.name} 预知了未来两次投骰子的结果！")

def block_penalty(user):
    print(f"🛡️ {user.name} 抵消了一次资源惩罚！")

def extra_dice_roll(user):
    print(f"🎲 {user.name} 额外投掷了一组骰子！")
skills_list = [
    Skill("天象推演", "查看未来两回合的骰子结果", predict_future_dice),
    Skill("放射研究", "抵消一次资源惩罚", block_penalty),
    Skill("超级计算", "额外投掷一组骰子", extra_dice_roll),
    # 后面继续加更多技能
]
skills_dict = {skill.name: skill for skill in skills_list}
# 以后新增技能，只需在 skills_list 添加即可，无需改别的地方！
