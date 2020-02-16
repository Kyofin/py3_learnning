"""
python3
学习迭代法
"""
import numpy

# 计算米粒
def lesson_3_1(number):
    if number == 1:
        return 1
    return 2 * lesson_3_1(number - 1)


# 使用二分法算平方根（求方程的精确或近似值）
def lesson_3_2(target, left, right, maxTry):
    mid = (left + right) / 2
    # 计算中间值的平方
    midSquare = numpy.square(mid)

    # 没有尝试次数就结束
    if (maxTry == 0):
        return mid;

    if (midSquare > target):
        return lesson_3_2(target, left, mid, maxTry - 1)
    elif (midSquare < target):
        return lesson_3_2(target, mid, right, maxTry - 1)
    elif (midSquare == target):
        return mid;


if __name__ == '__main__':
    print(lesson_3_1(64))

    print(4.25 / 2)
    # numpy平方
    print(numpy.square(3.109375) )
    # numpy平方根
    print(numpy.sqrt(10))
    print(lesson_3_2(10, 1, 10, 20))
