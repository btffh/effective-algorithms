# Яким Алексей ПИ17-1
#
# Наибольшей возрастающей подпоследовательностью в массиве из n элементов называется самая
# длинная последовательность элементов массива, простирающаяся слева направо и такая, что
# каждый следующий элемент больше предыдущего.

from typing import List, Tuple


def maxSeq(seq: List[int]) -> Tuple[int, List[int]]:
    # временная сложность алгоритма - O(n)
    # алгоритм заключается в переборе всей последовательности елементов и сравнении:
    # 1. на каждом этапе текущее число сравнивается с предыдущем
    #   1.1. если предыдущее число больше, то сравнивается длина предыдущей максимальной
    #        последовательности и если текущая последовательность длиннее, то она становится
    #        новой максимальной последовательностью
    #   1.2. если текущее число меньше, то увеличивается счетчик длины текущей последовательности,
    #        предыдущий элемент заменяется текущем, происходит переход к следующему элементу
    maxCount, count = 0, 1
    prev = seq[0]
    analyticLogestSeq = []
    analyticSeq = [seq[0]]
    for el in seq[1:]:
        if el > prev:
            count += 1
            analyticSeq.append(el)
        else:
            if count > maxCount:
                maxCount = count
                analyticLogestSeq = analyticSeq[:]
            count = 1
            analyticSeq = [el]
        prev = el

    return maxCount, analyticLogestSeq


def maxSeqSpaces(seq: List[int]) -> Tuple[int, List[int]]:
    minEl, minElInd = seq[0], 0
    for ind, el in enumerate(seq):
        if el < minEl:
            minEl, minElInd = el, ind

    countMax = 1
    prev = seq[minEl]
    analyticLongestSeq = [minEl]
    for el in seq[minElInd + 1 :]:
        if el > prev:
            countMax += 1
            analyticLongestSeq.append(el)
            prev = el

    return countMax, analyticLongestSeq


if __name__ == "__main__":
    arr = [1, 2, 3, 1, 4, 5, 6, 7, 1, 2, 3, 4]
    countMax, analyticLongestSeq = maxSeq(arr)
    print(f"{countMax}: {str(analyticLongestSeq)}")
    # output >>>
    # 5: [1, 4, 5, 6, 7]

    countMax, analyticLongestSeq = maxSeqSpaces(arr)
    print(f"{countMax}: {str(analyticLongestSeq)}")
    # output >>>
    # 6: [1, 3, 4, 5, 6, 7]

    arr = [6, 2, 5, 1, 7, 4, 8, 3]
    countMax, analyticLongestSeq = maxSeq(arr)
    print(f"{countMax}: {str(analyticLongestSeq)}")
    # output >>>
    # 5: [1, 4, 5, 6, 7]

    countMax, analyticLongestSeq = maxSeqSpaces(arr)
    print(f"{countMax}: {str(analyticLongestSeq)}")
    # output >>>
    # 5: [1, 4, 5, 6, 7]
