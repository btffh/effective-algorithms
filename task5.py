# Яким Алексей ПИ17-1
#
# Наибольшей возрастающей подпоследовательностью в массиве из n элементов называется самая
# длинная последовательность элементов массива, простирающаяся слева направо и такая, что
# каждый следующий элемент больше предыдущего.

from typing import List, Tuple


class Node(object):
    def __init__(
        self,
        val: int,
    ) -> None:
        self.val: int = val
        self.prevNodes: List[Node] = []

    def __str__(self) -> str:
        s = ""
        if len(self.prevNodes) == 0:
            s = "None"
        else:
            s = " | ".join([str(prev) for prev in self.prevNodes])
        return f"val: {self.val}, prevNodes: ({s})"


def getNodeSeqLen(node: Node) -> Tuple[List[int], int]:
    def helper(curNode: Node, curSeq: List[int], depth: int) -> Tuple[List[int], int]:
        # print(f"depth {depth}, curSeq {curSeq}, Node {curNode}")
        curSeqC = curSeq[:]
        curSeqC.append(curNode.val)
        depthC = depth + 1
        if len(curNode.prevNodes) == 0:
            return curSeqC, depthC

        maxSeq, maxDepth = [], 0
        for prev in curNode.prevNodes:
            s, d = helper(prev, curSeqC, depthC)
            if d > maxDepth:
                maxSeq, maxDepth = s, d

        return maxSeq, maxDepth

    return helper(node, [], 0)


def maxSeqSpaces(seq: List[int]) -> Tuple[int, List[int]]:
    """
    Функция поиска наибольшей возрастающей подпоследовательности в исходном направлении
    в массиве с учетом пропусков:

        input: [1, 2, 3, 1, 4, 5, 6, 1, 2, 7, 3, 4]
        result: [1, 2, 3, 4, 5, 6, 7]

    :param seq: исходная последовательность для поиска максимальной подпоследовательности
    :type seq: List[int]
    :return: максимальная длина овзрастающей подпоследовательности и сама подпоследовательность
    :rtype: Tuple[int, List[int]]
    """
    nodes: List[Node] = []
    nodes.append(Node(seq[0]))
    for val in seq[1:]:
        curNode = Node(val)
        for node in nodes:
            if node.val < val:
                curNode.prevNodes.append(node)
        nodes.append(curNode)

    maxSeq, maxLen = [], 0
    for node in nodes:
        s, l = getNodeSeqLen(node)
        if l > maxLen:
            maxSeq, maxLen = s, l
    maxSeq.reverse()
    return maxLen, maxSeq


if __name__ == "__main__":
    arr = [1, 2, 3, 1, 4, 5, 6, 1, 2, 7, 3, 4]
    countMax, analyticLongestSeq = maxSeqSpaces(arr)
    print(f"{countMax}: {str(analyticLongestSeq)}")
    # output >>>
    # 7: [1, 2, 3, 4, 5, 6, 7]

    arr = [6, 2, 5, 1, 7, 4, 8, 3]
    countMax, analyticLongestSeq = maxSeqSpaces(arr)
    print(f"{countMax}: {str(analyticLongestSeq)}")
    # output >>>
    # 4: [2, 5, 7, 8]
