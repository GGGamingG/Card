from Cards_Model import Card,EventCard,ExperimentCard,InspirationCard,ScientistCard
from Skills import skills_dict
# 事件卡
P1 = EventCard(
    1, "金字塔建造", "公元前2600", "古代",
    {"Capital": 3, "Experiment": 2}, 3,
    "完成后解锁建筑类实验卡", "古埃及工程数学"
)
P2 = EventCard(
    2, "浑天仪诞生", "公元125", "古代",
    {"Literature": 2, "Inspiration": 1}, 2,
    "获得1次免费骰子重投机会",
    "张衡的地动仪原理"
)
P3 = EventCard(
    3, "雅典学园创立", "公元前387", "古代",
    {"Literature": 3, "Capital": 1}, 4,
    "所有玩家获得1灵感",
    "柏拉图与西方哲学起源"
)
P4 = EventCard(
    4, "造纸术革新", "公元105", "古代",
    {"Experiment": 2, "Literature": 2}, 3,
    "后续文献需求永久-1",
    "蔡伦改进造纸工艺流程"
)
P5 = EventCard(
    5, "阿基米德浮力", "公元前250", "古代",
    {"Inspiration": 2, "Experiment": 1}, 2,
    "立即从弃牌堆回收1张卡",
    "\"尤里卡\"时刻的发现过程"
)
P6 = EventCard(
    6, "本草纲目编撰", "1593", "古代",
    {"Literature": 3, "Experiment": 3}, 5,
    "治疗类事件需求降低1级",
    "李时珍的药物分类体系"
)
#近代卡
P7 = EventCard(
    19, "牛顿定律", "1687", "近代",
    {"Inspiration": 3, "Experiment": 4}, 6,
    "永久解锁“经典物理”标签加成"
)
P8 = EventCard(
    20, "蒸汽机车", "1814", "近代",
    {"Capital": 5, "Experiment": 3}, 5,
    "所有实验卡维护费 -1"
)
P9 = EventCard(
    21, "物种起源", "1859", "近代",
    {"Literature": 4, "Inspiration": 2}, 5,
    "弃置对手1张实验卡"
)
P10 = EventCard(
    22, "元素周期表", "1869", "近代",
    {"Experiment": 4, "Literature": 2}, 4,
    "随机获得2个化学元素标记"
)
P11= EventCard(
    23, "电报发明", "1837", "近代",
    {"Capital": 3, "Inspiration": 3}, 4,
    "查看其他玩家手牌"
)
P12 = EventCard(
    24, "电磁感应", "1831", "近代",
    {"Experiment": 3, "Inspiration": 2}, 4,
    "将1个实验转化为2个资金"
)
    #现代卡
P18 = EventCard(
    37, "相对论发表", "1905", "现代",
    {"Inspiration": 5, "Literature": 3}, 8,
    "重构时间轴顺序"
)
P19 = EventCard(
    38, "DNA双螺旋", "1953", "现代",
    {"Experiment": 5, "Literature": 4}, 7,
    "获得基因编辑标记"
)
P20 = EventCard(
    39, "登月计划", "1969", "现代",
    {"Capital": 6, "Experiment": 5}, 7,
    "所有太空类事件分数+1"
)
P21 = EventCard(
    40, "互联网诞生", "1983", "现代",
    {"Literature": 4, "Inspiration": 4}, 6,
    "手牌上限+2"
)
P22= EventCard(
    41, "克隆羊多利", "1996", "现代",
    {"Experiment": 4, "Capital": 4}, 6,
    "复制1个已有实验卡"
)
P23= EventCard(
    42, "希格斯玻色子", "2012", "现代",
    {"Inspiration": 6, "Experiment": 6}, 9,
    "立即获胜（若在回合结束时）"
)
#实验卡
E1 = ExperimentCard(
    7, "天文观测台", "古代",
    {"Capital": 1}, "解决天文事件时额外+1实验资源"
)
E2 = ExperimentCard(
    8, "冶金工坊", "古代",
    {"Capital": 2},
    "每回合自动产生1资金"
)

E3 = ExperimentCard(
    9, "数学研究所", "古代",
    {"Literature": 1},
    "可将任意2资源转换为1灵感"
)

E4 = ExperimentCard(
    10, "航海制图室", "古代",
    {"Experiment": 1},
    "移动时代时保留此卡"
)
    #近代卡
E5 = ExperimentCard(
    25, "粒子加速器", "近代",
    {"Capital": 3},
    "现代物理事件需求 -2"
)

E6 = ExperimentCard(
    26, "进化实验室", "近代",
    {"Literature": 2},
    "每解决生物事件得1额外分"
)
E7 = ExperimentCard(
    27, "化学分析仪", "近代",
    {"Experiment": 2},
    "可拆分资源需求（如5=3+2）"
)
E8 = ExperimentCard(
    28, "蒸汽动力厂", "近代",
    {"Capital": 2},
    "每回合额外获得1骰子"
)
  #现代卡
E9 = ExperimentCard(
    43, "量子对撞机", "现代",
    {"Capital": 4},
    "现代物理事件可重复结算"
)
E10= ExperimentCard(
    44, "基因编辑台", "现代",
    {"Experiment": 3},
    "每回合可修改1个资源类型"
)
E11= ExperimentCard(
    45, "太空望远镜", "现代",
    {"Capital": 5},
    "解决事件时可借用对手资源"
)
E12= ExperimentCard(
    46, "AI计算中心", "现代",
    {"Literature": 3},
    "自动完成≤3资源需求的事件"
)
##灵感卡
I1 = InspirationCard(
    11, "星图启示",
    "查看未来3张事件卡并调整顺序",
    "古代"
)

I2 = InspirationCard(
    12, "丝绸之贸易",
    "将资金转换为其他资源1:1",
    "古代"
)
I3 = InspirationCard(
    13, "易经推演",
    "下回合骰子结果+1修正",
    "古代"
)

I4 = InspirationCard(
    14, "文艺复兴浪潮",
    "立即推进到近代时代",
    "古代"
)
I5 = InspirationCard(
    29, "专利制度", "近代",
    "复制对手1张非科学家卡"
)
I6 = InspirationCard(
    30, "大陆漂移说", "近代",
    "强制更换公共区所有卡牌"
)
I7 = InspirationCard(
    31, "工业标准化", "近代",
    "本回合资源可共享使用"
)
I8 = InspirationCard(
    32, "孟德尔豌豆", "近代",
    "将2个文献转化为实验"
)
  # 现代
I9 = InspirationCard(
    47, "大数据革命", "现代",
    "抽取等同于现存文献数量的卡"
)
I10 = InspirationCard(
    48, "碳中和倡议", "现代",
    "所有资金消耗减半"
)
I11 = InspirationCard(
    49, "CRISPR突破", "现代",
    "移除1个负面效果标记"
)
I12 = InspirationCard(
    50, "量子隧穿", "现代",
    "本回合可穿越时代使用卡牌"
)
##科学家卡
S1 = ScientistCard(
    15, "张衡",
    "地震预测 - 免除1次资源惩罚",
    "完成3个工程事件 +2分",
    "古代"
)


S2= ScientistCard(
    16, "亚里士多德",
    "逻辑学 - 事件卡文献需求 -1",
    "每存留2文献 +1分",
    "古代"
)
S3 = ScientistCard(
    17, "毕昇",
    "印刷术 - 购买文献卡费用减半",
    "拥有4文献时 +3分",
    "古代"
)
S4 = ScientistCard(
    18, "伽利略",
    "望远镜观测 - 天文事件分数 +1",
    "每解决1个跨时代事件 +1分",
    "古代"
)
S5 = ScientistCard(
    33, "达尔文", "近代",
    "环球考察 - 生物事件少需1文献",
    "每有1进化标记 +2分"
)
S6  = ScientistCard(
    34, "特斯拉", "近代",
    "交流电 - 电力事件分数 ×1.5",
    "建造3个实验设备 +4分"
)
S7 = ScientistCard(
    35, "居里夫人", "近代",
    "放射性研究 - 无视1个有害标记",
    "每处理2个危险事件 +3分"
)
S8 = ScientistCard(
    36, "门捷列夫", "近代",
    "元素预测 - 提前知晓化学事件需求",
    "集齐4元素 +5分"
)
  #现代
S9  = ScientistCard(
    51, "爱因斯坦", "现代",
    "时空扭曲 - 跳过1个事件需求",
    "每有1个理论事件 +2分"
)


# 调用方法,之后读取当前玩家的资源并判断（鼠标放在该卡牌上就计算，若是不满足则无法点击）
print(P1.is_playable({"Capital": 3, "Experiment": 3}))  # False
print(P1)  # 打印美化过的字符串

# 自动收集所有 EventCard 类型的对象
event_cards = [obj for obj in globals().values() if isinstance(obj, EventCard)]
experiment_cards = [obj for obj in globals().values() if isinstance(obj, ExperimentCard)]
inspiration_cards = [obj for obj in globals().values() if isinstance(obj, InspirationCard)]
scientist_cards = [obj for obj in globals().values() if isinstance(obj, ScientistCard)]

all_cards = event_cards + experiment_cards + inspiration_cards + scientist_cards

#for c in all_cards:
#    print(c)

# 使用卡牌技能
P1.use_skill(id=1)  # 传入当前角色