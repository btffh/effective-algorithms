# Яким Алексей ПИ17-1
#
# Пусть имеется множество номиналов монет coins = {c1, c2, …, ck} и денежная сумма n.
# Задача заключается в том, чтобы разменять сумму n, использовав как можно меньше монет.
# Количество монет одного номинала не ограничено. Например, если coins = {1, 2, 5} и
# n = 12, то оптимальное решение 5 + 5 + 2 = 12, так что достаточно трех монет.

from typing import List


def getCoinsArray(total: int, coins: List[int]) -> List[int]:
    sortedCoins = sorted(coins, reverse=True)
    result = []
    balance = total
    for coin in sortedCoins:
        amount, balance = balance // coin, balance % coin
        result.extend([coin] * amount)
        if balance == 0:
            break
    return result


if __name__ == "__main__":
    # алгоритм заключается в переборе списка монет, отсортированного по убыванию.
    # для каждой монеты:
    # 1. находим целое число от деления текущего баланса на номинал текущей монеты
    # 2. добавляем монеты текущего номинала в результирующий массив в количестве, равном
    #    найденному в пункте 1 числу
    # 3. изменяем текущий баланс: новый баланс равен остатку от деления старого баланса на
    #    номинал текущей монеты, если новый баланс равен 0, можно досрочно закончить
    #    перебор массива монет, так как искомая сумма достугнута

    coins = [1, 2, 5]
    total = 12
    print(getCoinsArray(total, coins))
    # output >>>
    # [5, 5, 2]

    coins = [1, 2, 5]
    total = 11
    print(getCoinsArray(total, coins))
    # output >>>
    # [5, 5, 1]

    total = 23
    print(getCoinsArray(total, coins))
    # output >>>
    # [5, 5, 5, 5, 2, 1]

    coins = [1, 2, 5, 7]
    total = 23
    print(getCoinsArray(total, coins))
    # output >>>
    # [7, 7, 7, 2]

    coins = [1, 2, 5, 7, 10]
    total = 123
    print(getCoinsArray(total, coins))
    # output >>>
    # [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 2, 1]
