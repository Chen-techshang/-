#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
题目描述：
    一球从 100 米的高度自由落体（忽略空气阻力），每次落地后反跳回原高度的一半，再落下。
    要求：
    （1）求第 10 次掉下并反弹到最高点时（即完成 10 次落下和反弹上升）的反弹高度、
         此时球一共经过的距离以及运动所用的总时间。
    （2）求第 n 次掉下并反弹到最高点时的反弹高度、经过的总距离和运动时间。

算法说明：
    - 初始高度 H0 = 100 米。
    - 每次落下后，反弹高度为原高度的一半，即第 n 次反弹高度 H_n = H0 / (2^n)。
    - 总运动距离：
        初次下落 100 米 +
        对于第 1 到 n-1 次，每次经历：上升（H0/2^i）+下落（H0/2^i），共 2*(H0/2^i)；
        最后一次（第 n 次）仅计算上升距离（到达最高点时，尚未下落）。
        故： D(n) = H0 + ∑[i=1 to n-1] 2*(H0/2^i) + (H0/2^n)。
    - 时间计算（忽略空气阻力，使用自由落体运动公式 t = √(2h/g)，其中 g = 9.8 m/s²）：
        初次下落时间： √(2*H0/g)；
        对于第 1 到 n-1 次：每次有上升和下落（时间相等），即 2*√(2*(H0/2^i)/g)；
        第 n 次仅计算上升时间： √(2*(H0/2^n)/g)。
        故： T(n) = √(2*H0/g) + ∑[i=1 to n-1] 2*√(2*(H0/2^i)/g) + √(2*(H0/2^n)/g)。

程序中定义了函数 compute_values(n, H0, g) 来计算第 n 次反弹时的反弹高度、累计距离和运动时间，
并在 main() 函数中先计算 n = 10 的情况，然后允许用户输入任意正整数 n 进行计算。
"""

import math


def compute_values(n, H0=100, g=9.8):
    """
    计算第 n 次落下并反弹到最高点时：
    - 反弹高度（bounce_height）
    - 累计运动距离（total_distance）
    - 总运动时间（total_time）

    参数：
        n   : 反弹次数（落下次数）为正整数
        H0  : 初始高度（默认为 100 米）
        g   : 重力加速度（默认为 9.8 m/s^2）

    返回：
        bounce_height, total_distance, total_time
    """
    # 反弹高度：第 n 次反弹时，达到的最高点
    bounce_height = H0 / (2 ** n)

    # 计算累计运动距离：
    # 初次下落距离
    total_distance = H0
    # 对于第 1 到 n-1 次，每次先反弹上升，再落下
    for i in range(1, n):
        total_distance += 2 * (H0 / (2 ** i))
    # 第 n 次只计算上升距离（达到最高点时停止运动）
    total_distance += H0 / (2 ** n)

    # 计算累计运动时间：
    # 初次下落时间
    total_time = math.sqrt(2 * H0 / g)
    # 对于第 1 到 n-1 次，每次经历上升和下落（时间相等）
    for i in range(1, n):
        t = math.sqrt(2 * (H0 / (2 ** i)) / g)
        total_time += 2 * t
    # 第 n 次仅计算上升时间
    total_time += math.sqrt(2 * (H0 / (2 ** n)) / g)

    return bounce_height, total_distance, total_time


def main():
    # 计算 n = 10 时的各项指标
    n = 10
    bounce_height, total_distance, total_time = compute_values(n)
    print("第 10 次落下并反弹到最高点时：")
    print("反弹高度 (m): {:.6f}".format(bounce_height))
    print("累计运动距离 (m): {:.6f}".format(total_distance))
    print("累计运动时间 (s): {:.6f}".format(total_time))
    print("\n------------------------------------\n")

    # 允许用户输入任意正整数 n 进行计算
    try:
        n_input = int(input("请输入反弹次数 n (正整数)："))
        if n_input <= 0:
            print("n 必须为正整数。")
        else:
            bh, td, tt = compute_values(n_input)
            print("当 n = {} 时：".format(n_input))
            print("反弹高度 (m): {:.6f}".format(bh))
            print("累计运动距离 (m): {:.6f}".format(td))
            print("累计运动时间 (s): {:.6f}".format(tt))
    except ValueError:
        print("输入无效，请输入正整数。")


if __name__ == "__main__":
    main()
