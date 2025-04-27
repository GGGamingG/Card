# character.py

from Skills import skills_dict

class Role:
    def __init__(self, name: str, skill_names: list[str], traits: list[str]):
        self.name = name
        self.skills = [skills_dict[name] for name in skill_names]
        self.traits = traits
        self.cooldowns = {skill.name: 0 for skill in self.skills}  # 技能冷却时间管理

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

    def reduce_cooldowns(self):
        for skill in self.cooldowns:
            if self.cooldowns[skill] > 0:
                self.cooldowns[skill] -= 1

    def __str__(self):
        skills_str = "，".join([skill.name for skill in self.skills])
        traits_str = "，".join(self.traits)
        return f"🎭 {self.name}：\n技能：{skills_str}\n特点：{traits_str}"

# 示例角色创建
if __name__ == "__main__":
    zhangheng = Role(
        "张衡",
        ["天象推演", "超级计算"],
        ["睿智", "守纪", "天文大师"]
    )

    print(zhangheng)

    # 使用技能
    zhangheng.use_skill("天象推演")
    zhangheng.use_skill("超级计算")
    # 尝试连续使用触发冷却
    zhangheng.use_skill("天象推演")

    # 减少冷却回合
    zhangheng.reduce_cooldowns()
    zhangheng.reduce_cooldowns()

    # 冷却完成后再次使用
    zhangheng.use_skill("天象推演")
roles_list = [
    Role("天文大师", ["天象推演", "超级计算"], "完成3个天文事件"),
    Role("医学专家", ["放射研究", "灵感闪现"], "治疗2个灾害"),
]
roles_dict = {role.name: role for role in roles_list}