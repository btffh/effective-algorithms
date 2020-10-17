# Необходимо реализовать эффективный механизм обнаружения закономерностей в заданной последовательности 'S'.
# Пусть имеется последовательность 'S': "купить Amazon, купить Yahoo, купить eBay, купить Yahoo, купить Yahoo, купить Oracle".
# Необходимо определить, содержится ли в последовательности 'S' подпоследовательность 's' с возможностью разбиения подпоследовательности, но с сохранением порядка элементов.
# Пожпоследовательность 's': "купить Yahoo, купить eBay, купить Yahoo, купить Oracle".
# Временная сложность алгоритма - O(n + m), где n, m - длина последовательностей 'S' и 's'.
from typing import List


def checkSubsequence(seq: List[str], subseq: List[str]) -> bool:
    """
    Функция проверки вхождения подпоследовательности в последовательность.
    Временная сложность работы алгоритма в худшем случае - O(n), где n - длина последовательности.
    Временная сложность работы алгоритма в лучшем случае - O(1) - время сравнения двух целых чисел.

    :param sequence: исходная последовательность
    :type sequence: str
    :param subsequence: подпоследовательность для проверки
    :type subsequence: str
    :return: подпоследовательность есть в последовательности
    :rtype: bool
    """
    if len(seq) < len(subseq):
        return False

    indSeq, indSubseq = 0, 0
    while True:
        if seq[indSeq] == subseq[indSubseq]:
            indSubseq += 1
        indSeq += 1

        # exceeded end of subsequence -> it consists in sequence
        if indSubseq == len(subseq):
            return True

        if indSeq == len(seq):
            return False


def checkSubsequenceStr(sequence: str, subsequence: str, sep: str = ", ") -> bool:
    """
    Функция проверки вхождения подпоследовательности в последовательность.
    Временная сложность работы алгоритма в худшем случае - O(n), где n - длина последовательности.
    Временная сложность работы алгоритма в лучшем случае - O(1) - время сравнения двух целых чисел.

    :param sequence: исходная последовательность
    :type sequence: str
    :param subsequence: подпоследовательность для проверки
    :type subsequence: str
    :param sep: разделитель строк, defaults to ", "
    :type sep: str, optional
    :return: подпоследовательность есть в последовательности
    :rtype: bool
    """
    return checkSubsequence(sequence.split(sep), subsequence.split(sep))


# run program if it was called directly
if __name__ == "__main__":
    sequence = "Yahoo, Amazon, Yahoo, Yahoo, eBay, Yahoo, Oracle"
    subsequence = "Yahoo, eBay, Yahoo, Oracle"
    print(checkSubsequenceStr(sequence, subsequence))  # returns True

    subsequence = "Yahoo, eBay, Yahoo, Oracle, Amazon"
    print(checkSubsequenceStr(sequence, subsequence))  # return False (does not contain)

    subsequence = (
        "Yahoo, eBay, Yahoo, Oracle, Amazon, Yahoo, eBay, Yahoo, Oracle, Amazon"
    )
    print(
        checkSubsequenceStr(sequence, subsequence)
    )  # return False (subsequence is bigger than sequence)
