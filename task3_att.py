from typing import List, Dict


def analyzeQueue(queue: List[Dict[str, int]]) -> Dict[str, int]:
    length = 0
    latestTaskcompleteTime = 0
    for task in queue:
        length += task["p"]
        taskCompleteTime = length + task["f"]
        if latestTaskcompleteTime < taskCompleteTime:
            latestTaskcompleteTime = taskCompleteTime
    return {"p_time": length, "f_time": latestTaskcompleteTime}


def sortByF(tasks: List[Dict[str, int]], reverse: bool = True) -> List[Dict[str, int]]:
    return sorted(tasks, key=lambda x: x["f"], reverse=reverse)


def sortByP(tasks: List[Dict[str, int]], reverse: bool = True) -> List[Dict[str, int]]:
    return sorted(tasks, key=lambda x: x["p"], reverse=reverse)


def sortBySum(
    tasks: List[Dict[str, int]], reverse: bool = True
) -> List[Dict[str, int]]:
    return sorted(tasks, key=lambda x: x["p"] + x["f"], reverse=reverse)


def sortByCoefSum(
    tasks: List[Dict[str, int]], p: float = 0.1, f: float = 0.9, reverse: bool = True
) -> List[Dict[str, int]]:
    if p + f != 1:
        if 0 <= f <= 1:
            p = 1 - f
        elif 0 <= p <= 1:
            f = 1 - p
        else:
            p, f = 0.1, 0.9
    return sorted(tasks, key=lambda x: x["p"] * p + x["f"] * f, reverse=reverse)


def showQueue(queue: List[Dict[str, int]]) -> str:
    res = ["["]
    res.extend(["\t" + str(task) for task in queue])
    res.append("]")
    return "\n".join(res)


if __name__ == "__main__":
    tasks = [
        {"p": 10, "f": 20},
        {"p": 5, "f": 10},
        {"p": 3, "f": 29},
        {"p": 15, "f": 10},
        {"p": 12, "f": 12},
        {"p": 11, "f": 11},
        {"p": 15, "f": 8},
        {"p": 13, "f": 15},
        {"p": 9, "f": 9},
    ]

    print("--- F Sort ---")
    queue = sortByF(tasks)
    print(showQueue(queue))
    print(analyzeQueue(queue))

    print("--- P Sort ---")
    queue = sortByP(tasks)
    print(showQueue(queue))
    print(analyzeQueue(queue))

    print("--- Sum Sort ---")
    queue = sortBySum(tasks)
    print(showQueue(queue))
    print(analyzeQueue(queue))

    print("--- Coef Sum Sort ---")
    for i in range(1, 10):
        coef = i / 10
        print(f"sorting with coef: p={coef}, f={1 - coef}")
        queue = sortByCoefSum(tasks, coef, 1 - coef)
        print(showQueue(queue))
        print(analyzeQueue(queue))

    # в результате трех экспериментов и эксперимента с интервалами
    # видно, что время работы суперкомпьютера
    # никак не изменялось (что вполне логично, ведь все задания выолняются
    # последовательно, а суммарное время заданий никак не менялось), в то время
    # как результирующее время индексирования зависело от метода сортировки:
    # по времени выполнения заданий на суперкомпьютере, по времени выполнения
    # заданий на рабочих станций, по суммарному времени выполнения заданий как
    # на суперкомпьютере, так и на рабочей станции

    # так же рассматривал такой вариант: коэффициент для сортировки есть
    # отношение параметров `coef = p/f`, тогда сортируем по убыванию коэффициента,
    # однако такой вариант не выдаёт минимальное время всего индексирования.
    # если же добавить дополнительное условие (f задачи больше, чем p+f второй
    # задачи, тогда первая обрабатывается раньше), то в случае, когда у нас есть
    # две задачи с времязатратами 8+8 и 16+16 мы получим общее время индексирования,
    # равное 40, а не 32, что является в данном случае решением задачи

    # временная сложность встроенного алгоритма сортировки - O(n*log(n)) в
    # лучшем случае и O(n^2) в худшем случае
