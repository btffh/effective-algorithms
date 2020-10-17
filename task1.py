# Необходимо реализовать эффективный механизм обнаружения закономерностей в заданной последовательности 'S'.
# Пусть имеется последовательность 'S': "купить Amazon, купить Yahoo, купить eBay, купить Yahoo, купить Yahoo, купить Oracle".
# Необходимо определить, содержится ли в последовательности 'S' подпоследовательность 's' с возможностью разбиения подпоследовательности, но с сохранением порядка элементов.
# Пожпоследовательность 's': "купить Yahoo, купить eBay, купить Yahoo, купить Oracle".
# Временная сложность алгоритма - O(n + m), где n, m - длина последовательностей 'S' и 's'.


def checkSubsequence(sequence: str, subsequence: str) -> bool:
    """
    Функция проверки вхождения подпоследовательности в последовательность.
    Временная сложность работы алгоритма в худшем случае - O(n), где n - длина последовательности.
    Временная сложность алгоритма в лучшем случае - O(x), где x - время разбиения строки на массив и сравнения целых чисел.

    :param sequence: исходная последовательность
    :type sequence: str
    :param subsequence: подпоследовательность для проверки
    :type subsequence: str
    :return: подпоследовательность есть в последовательности
    :rtype: bool
    """
    seq = sequence.split(", ")
    subseq = subsequence.split(", ")

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


# run program if it was called directly
if __name__ == "__main__":
    sequence = "Yahoo, Amazon, Yahoo, Yahoo, eBay, Yahoo, Oracle"
    subsequence = "Yahoo, eBay, Yahoo, Oracle"
    print(checkSubsequence(sequence, subsequence))  # returns True

    subsequence = "Yahoo, eBay, Yahoo, Oracle, Amazon"
    print(checkSubsequence(sequence, subsequence))  # return False (does not contain)

    subsequence = (
        "Yahoo, eBay, Yahoo, Oracle, Amazon, Yahoo, eBay, Yahoo, Oracle, Amazon"
    )
    print(
        checkSubsequence(sequence, subsequence)
    )  # return False (subsequence is bigger than sequence)
