# Яким Алексей ПИ17-1
#
# Требуется проанализировать информацию из двух разных баз данных. Каждая база данных
# содержит n числовых значений (так что общее количество значений равно 2n); будем
# считать, что одинаковых значений нет. Требуется вычислить медиану этого множества из
# 2n значений, которую мы определим как n-е значение в порядке возрастания. Однако доступ
# к информации затруднен — ее можно получить только при помощи запросов к базам данных.
# В одном запросе указывается значение k для одной из двух баз данных, и выбранная база
# данных возвращает k-е значение в порядке возрастания, содержащееся в этой базе. Так как
# обращения к базам занимают много времени, медиану хотелось бы вычислить с минимальным
# количеством запросов. Приведите алгоритм вычисления медианы с количеством запросов
# не более O(log n).

from typing import List, Tuple, Dict
import itertools


def getMedianFlatten(db1: List[int], db2: List[int]) -> Tuple[int, Dict[str, int]]:
    """
    Функция создает из двух отсортированных массивов один при помощи перебора
    элементов и вставки значений:
        1. i, j -индексы первого и второго массивов соответственно
        2. пока i < длина массива 1 и j < длина массива 2:
            2.1. если i-й элемент первого массива меньше j-го элемента второго
                массива, то вставялем его в результирующий массив и увеличиваем
                индекс i на 1
            2.2. если j-й элемент второго массива меньше i-го элемента первого
                массива, то вставялем его в результирующий массив и увеличиваем
                индекс j на 1
        3. возвращаем медиану
    Сложность работы алгоритма - не более O(2n) - время перебораобоих массивов.

    :param db1: массив
    :type db1: List[int]
    :param db2: массив
    :type db2: List[int]
    :raises ValueError: длина массивов не равна
    :return: (медиана, статистика)
    :rtype: Tuple[int, Dict[str, int]]
    """
    if len(db1) != len(db2):
        raise ValueError

    stats: Dict[str, int] = {"comparisons": 0, "insertions": 0}
    i, j = 0, 0
    entire: List[int] = []
    while i < len(db1) and j < len(db1):
        stats["comparisons"] += 1
        stats["insertions"] += 1
        if db1[i] < db2[j]:
            entire.append(db1[i])
            i += 1
        else:
            entire.append(db2[j])
            j += 1

    if i < len(db1):
        stats["comparisons"] += 1
        stats["insertions"] += len(db1) - i
        entire.extend(db1[i:])
    if j < len(db2):
        stats["comparisons"] += 1
        stats["insertions"] += len(db2) - j
        entire.extend(db2[j:])

    if len(entire) % 2 == 1:
        stats["comparisons"] += 1
        return entire[len(entire) // 2], stats
    return 0.5 * (entire[len(entire) // 2 - 1] + entire[len(entire) // 2]), stats


def incSingleStat(a: int, stats: Dict[str, int]) -> bool:
    stats["insertions"] += 1
    stats["comparisons"] += 1
    return a


def getMedianFlattenSort(db1: List[int], db2: List[int]) -> Tuple[int, Dict[str, int]]:
    """
    Функция создает из двух массивов один, а затем сортирует его и возвращает
    медианное значение. Сложность O(2n + n*log(n))

    :param db1: массив
    :type db1: List[int]
    :param db2: массив
    :type db2: List[int]
    :raises ValueError: длина массивов не равна
    :return: (медиана, статистика)
    :rtype: Tuple[int, Dict[str, int]]
    """
    if len(db1) != len(db2):
        raise ValueError

    stats: Dict[str, int] = {"comparisons": 0, "insertions": 0}
    stats["insertions"] = len(db1) * 2
    entire: List[int] = sorted(
        itertools.chain(db1, db2), key=lambda a: incSingleStat(a, stats)
    )
    stats["comparisons"] += 1
    if len(entire) % 2 == 1:
        return entire[len(entire) // 2], stats
    return 0.5 * (entire[len(entire) // 2 - 1] + entire[len(entire) // 2]), stats


if __name__ == "__main__":
    # Исходя из условия задачи мы получаем k-е по возрастанию число, то есть мы можем
    # оперировать двумя возрастающими массивами и каждый раз брать элемент с индексом k,
    # что и будет соответствовать k-му значению в порядке возрастания.

    print("--- Length 17 * 2 ---")
    # length == 17
    db1 = [0, 1, 6, 7, 9, 10, 12, 12, 17, 26, 28, 37, 42, 44, 46, 49, 50]
    # length == 17
    db2 = [1, 4, 7, 14, 14, 15, 16, 18, 20, 20, 24, 24, 29, 33, 39, 39, 46]
    res = getMedianFlattenSort(db1, db2)
    print(f"flattenSort: {res}")
    res = getMedianFlatten(db1, db2)
    print(f"flatten: {res}")
