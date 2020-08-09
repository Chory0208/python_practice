"""
一个多回合制游戏，每个角色都有hp 和power，
hp代表血量，power代表攻击力，hp的初始值为1000，
power的初始值为200。打斗多个回合
定义一个fight方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
谁的hp先为0，那么谁就输了
"""

import random
import time


def fight():
    my_hp = 1000
    my_power = random.randint(1, 100)
    enemy_hp = 1000
    enemy_power = random.randint(1, 100)
    print(f'我的攻击力是{my_power}')
    print(f'我的攻击力是{enemy_power}')
    count = 1
    while True:
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power
        if (my_hp > 0) & (enemy_hp > 0):
            print(f'第{count}回合')
            print(f'我的血量是{my_hp}')
            print(f'敌人的血量是{enemy_hp}')
            print("==========")
            time.sleep(1)
            count += 1
        if my_hp <= 0:
            print("你赢了")
            break
        elif enemy_hp <= 0:
            print("我赢了")
            break


fight()
