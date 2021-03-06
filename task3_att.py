# Яким Алексей ПИ17-1, вариант 1 (номер по списку 15)
#
# Задание:
# 1. Невероятно популярная испаноязычная поисковая система Goog проводит огромный объем
# вычислений при каждом пересчете индекса. К счастью, в распоряжении компании имеется
# один суперкомпьютер с практически неограниченным запасом мощных рабочих станций.
# Вычисления разбиты на n заданий J1, J2, ..., Jn, которые могут выполняться полностью
# независимо друг от друга. Каждое задание состоит из двух фаз: сначала оно проходит
# предварительную обработку на суперкомпьютере, а затем завершается на одной из рабочих
# станций. Допустим, обработка задания Ji требует pi секунд на суперкомпьютере, а затем
# fi секунд на рабочей станции. На площадке доступны как минимум n рабочих станций,
# поэтому завершающая фаза обработки всех заданий может проходить параллельно — все
# задания будут выполняться одновременно. Однако суперкомпьютер может работать только с
# одним заданием, поэтому администратор должен определить порядок передачи заданий
# суперкомпьютеру. Как только первое задание в этом порядке будет обработано на
# суперкомпьютере, оно передается на рабочую станцию для завершения; после обработки на
# суперкомпьютере второе задание передается на рабочую станцию независимо от того,
# завершилось первое задание или нет (так как рабочие станции работают параллельно), и
# т. д. Допустим, расписание представляет собой упорядоченный список заданий для
# суперкомпьютера, а время завершения расписания определяется самым ранним временем
# завершения всех заданий на рабочих станциях. Очень важно свести к минимуму эту
# характеристику, так как она определяет, насколько быстро El Goog сможет построить
# новый индекс.
#
# Предложите алгоритм с полиномиальным временем, который находит расписание с минимальным
# временем завершения.
#
# Примечание: словесное описание подходов к решению задачи и алгоритма представлены ниже,
# в блоке `if __name__ == "__main__":`, который является входной точкой в программу.

from typing import List, Dict, Tuple


def analyzeQueue(queue: List[Dict[str, int]]) -> Dict[str, int]:
    length = 0
    latestTaskcompleteTime = 0
    for task in queue:
        length += task["p"]
        taskCompleteTime = length + task["f"]
        if latestTaskcompleteTime < taskCompleteTime:
            latestTaskcompleteTime = taskCompleteTime
    return {"p_time": length, "f_time": latestTaskcompleteTime}


def sortByKey(
    tasks: List[Dict[str, int]], sortKey: str = "f", reverse: bool = True
) -> List[Dict[str, int]]:
    return sorted(tasks, key=lambda x: x[sortKey], reverse=reverse)


def sortByCoefSum(
    tasks: List[Dict[str, int]], p: float = 0.1, f: float = 0.9, reverse: bool = True
) -> List[Dict[str, int]]:
    # если сумма коэффициентов не равна 1, нормализуем коэффициенты
    if p + f != 1:
        p = p / (p + f)
        f = 1 - p
    return sorted(tasks, key=lambda x: x["p"] * p + x["f"] * f, reverse=reverse)


def sortByAttitude(
    tasks: List[Dict[str, int]],
    attitudeKeys: Tuple[str, str] = ("p", "f"),
    reverse: bool = True,
) -> List[Dict[str, int]]:
    return sorted(
        tasks, key=lambda x: x[attitudeKeys[0]] / x[attitudeKeys[1]], reverse=reverse
    )


def showQueue(queue: List[Dict[str, int]]) -> str:
    res = ["["]
    res.extend(["\t" + str(task) for task in queue])
    res.append("]")
    return "\n".join(res)


def runExperiment(
    tasks: List[Dict[str, int]],
    expName: str = "",
    printExperimentNames: bool = True,
    printResultedQueue: bool = False,
    printAnalyticStats: bool = True,
) -> Dict[str, Dict[str, int]]:
    analytics = {}

    if printExperimentNames:
        print(f"-- Experiment: {expName} --")

    queue = sortByKey(tasks)
    queueAnalyzeStats = analyzeQueue(queue)
    analytics["f_sort"] = queueAnalyzeStats
    if printExperimentNames:
        print("--- F Sort ---")
    if printResultedQueue:
        print(showQueue(queue))
    if printAnalyticStats:
        print(f"\t{queueAnalyzeStats}")

    queue = sortByKey(tasks, "p")
    queueAnalyzeStats = analyzeQueue(queue)
    analytics["p_sort"] = queueAnalyzeStats
    if printExperimentNames:
        print("--- P Sort ---")
    if printResultedQueue:
        print(showQueue(queue))
    if printAnalyticStats:
        print(f"\t{queueAnalyzeStats}")

    queue = sortByAttitude(tasks, ("p", "f"))
    queueAnalyzeStats = analyzeQueue(queue)
    analytics["attitude_sort"] = queueAnalyzeStats
    if printExperimentNames:
        print("--- Attitude Sort ---")
    if printResultedQueue:
        print(showQueue(queue))
    if printAnalyticStats:
        print(f"\t{queueAnalyzeStats}")

    if printExperimentNames:
        print("--- Coef Sum Sort ---")
    for i in range(1, 10):
        coef = i / 10
        if printExperimentNames:
            print(f"\t-- sorting with coef: p={coef}, f={1 - coef}")

        queue = sortByCoefSum(tasks, coef, 1 - coef)
        queueAnalyzeStats = analyzeQueue(queue)
        analytics[f"coef_sort_{coef}"] = queueAnalyzeStats
        if printResultedQueue:
            print(showQueue(queue))
        if printAnalyticStats:
            print(f"\t\t{queueAnalyzeStats}")

    return analytics


if __name__ == "__main__":
    # исходя из условия задачи, все операции p на суперкомпьютере выполняются последовательно,
    # что означает константное время выполнения операций на суперкомпьютере, равное сумме всех p.
    # так же, по условию задачи все операции f могут выполняться параллельно и независимо друг
    # от друга, даже если мы запускаем все N операций одновременно, однако операции f не могут
    # быть запущены до выполнения соответствующей им операции p. таким образом, поиск минимального
    # времени работы всего процесса индексации сводится к поиску минимального остаточного
    # времени - времени, необходимого для окончания самой поздней (с точки зрения завершения)
    # операции f.

    # рассмотрим следующие варианты сортировки:
    # 1. сортировка заданий по убыванию времени операций f
    # 2. сортировка заданий по убыванию времени операций p
    # 3. сортировка заданий по убыванию суммы `coef * p + (1-coef) * f`, где coef - коэффициент из
    #    диапазона [0.1, 0.9] с шагом 0.1
    # 4. сортировка заданий по убыванию отношения параметров `p/f`

    # теоретические выводы по поставленным вариантам
    # 1. так как мы сортируем по убываю f, то после завершения последней операции p начнется
    #    операция f минимальной продолжительности, что гарантирует минимальное остаточное время
    # 2. сортировка по параметру p не имеет смысла, так как все операции p выполняются последовательно,
    #    соответственно суммарное время, затраченное на операции p, будет константно, а поседняя
    #    операция p может запускать не самую короткую операцию f, что не гарантирует минимального
    #    остаточного времени
    # 3. данный вариант представляет собой некоторый компромисс между решениями 1 и 2, вводя
    #    коэффициент значимости параметров p и f, однако, исходя из вывода к решению 2, сортировать
    #    по параметру p не имеет смысла
    # 4. отношение параметров p и f представляет собой коэффициент относительной продолжительности
    #    выполнения операций самого задания и никак не учитывает их продолжительность, то есть
    #    коэффициент задания с `p = 10, f = 5` будет равен коэффициенту задания с `p = 100, f = 50`,
    #    однако очевидно, что порядок заданий должен быть [2, 1], а суммарное время будет равно 150,
    #    в то время как алгоритм может вернуть последовательность [1, 2], при этом суммарное время
    #    будет равно 160, то есть равные коэффициенты дают различные решения

    # так же был предложен вариант решения, когда мы ищем такие задания, у которых сумма
    # продолжительности выполнрения операций f нескольких заданий будет меньше или равна
    # продолжительности оперции p любого другого задания. данный вариант может быть оптимален только
    # в том случае, когда мы имеем только два параллельных потока выполнения, предназначенных отдельно
    # для операций p и f, при этом для выполнения оперций f предварительно должны быть выполнены все
    # операции p соответствующих заданий. однако по условию мы обладаем ресурсами для параллельного
    # выполнения всех операций f, то есть у нас `1+n` параллельных потоков, где n - число заданий.
    # следовательно, данное решение не является оптимальным, так как просто не имеет смысла пытаться
    # выполнить несколько операций f в период выполнения одной операции p (ведь это также приводит
    # к поиску оптимальной очереди для предвыполнения оперций p соответствующих заданиям искомых
    # операций f)

    # исходя из четырех рассмотренных решений, мы упираемся в оптимальный алгоритм сортировки
    # во всех четырех решениях, поэтому следует оптимизировать алгоритм сортировки.
    #
    # для удобства возьмем встроенную в язык программирования Python функцию sorted, которая
    # возвращает отсортированный массив в соответствии с переданным ключом.
    #
    # временная сложность встроенного алгоритма сортировки - O(n*log(n)) в лучшем случае, что
    # так же соответствует временной сложности в общем случае, и O(n^2) в худшем случае.
    #
    # это соответствует алгоритму быстрой сортировки, который является жадным алгоритмом:
    # 1. случайным образом выбирается опорный элемент массива (обычно - середина массива)
    # 2. остальные элементы массива сравниваются с опорным и, если они меньше опорного,
    #    помещаются в левую часть массива, иначе - в правую
    # 3. рекурсивно повторить алгоритм для обоих отрезков (отрезки "меньших" и "больших"
    #    элементов), если отрезок имеет длину не более двух - вернуть отсортированный отрезок,
    #    метод сортировки в данном случае - сравнение обоих элементов отрезка

    # для чистоты эксперимента реализуем все 4 рассмотренных решения для различных наборов данных:
    basic_random_case = [
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

    p_gt_f_case = [
        {"p": 16, "f": 10},
        {"p": 8, "f": 4},
        {"p": 27, "f": 17},
        {"p": 28, "f": 23},
        {"p": 19, "f": 8},
        {"p": 24, "f": 16},
        {"p": 21, "f": 4},
        {"p": 9, "f": 1},
        {"p": 21, "f": 2},
        {"p": 28, "f": 25},
    ]

    f_gt_p_case = [
        {"p": 4, "f": 14},
        {"p": 8, "f": 9},
        {"p": 2, "f": 2},
        {"p": 19, "f": 30},
        {"p": 17, "f": 17},
        {"p": 12, "f": 27},
        {"p": 7, "f": 10},
        {"p": 2, "f": 11},
        {"p": 14, "f": 21},
        {"p": 7, "f": 27},
    ]

    mixed_case = [
        {"p": 26, "f": 9},
        {"p": 26, "f": 9},
        {"p": 9, "f": 9},
        {"p": 28, "f": 20},
        {"p": 16, "f": 6},
        {"p": 1, "f": 30},
        {"p": 2, "f": 21},
        {"p": 3, "f": 6},
        {"p": 4, "f": 9},
        {"p": 8, "f": 14},
    ]

    # небольшое пояснение к выводимым данным: 'p_time' - время окончания работы последнего
    # процесса p, 'f_time' - время окончания работы последнего процесса f. таким образом,
    # искомое остаточное время равно `f_time - p_time`

    runExperiment(basic_random_case, "Basic")
    # output >>>
    # --- F Sort ---
    #         {'p_time': 93, 'f_time': 101}
    # --- P Sort ---
    #         {'p_time': 93, 'f_time': 122}
    # --- Attitude Sort ---
    #         {'p_time': 93, 'f_time': 122}
    # --- Coef Sum Sort ---
    #         -- sorting with coef: p=0.1, f=0.9
    #                 {'p_time': 93, 'f_time': 101}
    #         -- sorting with coef: p=0.2, f=0.8
    #                 {'p_time': 93, 'f_time': 102}
    #         -- sorting with coef: p=0.3, f=0.7
    #                 {'p_time': 93, 'f_time': 103}
    #         -- sorting with coef: p=0.4, f=0.6
    #                 {'p_time': 93, 'f_time': 103}
    #         -- sorting with coef: p=0.5, f=0.5
    #                 {'p_time': 93, 'f_time': 103}
    #         -- sorting with coef: p=0.6, f=0.4
    #                 {'p_time': 93, 'f_time': 103}
    #         -- sorting with coef: p=0.7, f=0.30000000000000004
    #                 {'p_time': 93, 'f_time': 108}
    #         -- sorting with coef: p=0.8, f=0.19999999999999996
    #                 {'p_time': 93, 'f_time': 117}
    #         -- sorting with coef: p=0.9, f=0.09999999999999998
    #                 {'p_time': 93, 'f_time': 117}

    runExperiment(f_gt_p_case, "All 'f' are greater than 'p'")
    # output >>>
    # --- F Sort ---
    #         {'p_time': 92, 'f_time': 99}
    # --- P Sort ---
    #         {'p_time': 92, 'f_time': 111}
    # --- Attitude Sort ---
    #         {'p_time': 92, 'f_time': 117}
    # --- Coef Sum Sort ---
    #         -- sorting with coef: p=0.1, f=0.9
    #                 {'p_time': 92, 'f_time': 99}
    #         -- sorting with coef: p=0.2, f=0.8
    #                 {'p_time': 92, 'f_time': 99}
    #         -- sorting with coef: p=0.3, f=0.7
    #                 {'p_time': 92, 'f_time': 101}
    #         -- sorting with coef: p=0.4, f=0.6
    #                 {'p_time': 92, 'f_time': 101}
    #         -- sorting with coef: p=0.5, f=0.5
    #                 {'p_time': 92, 'f_time': 101}
    #         -- sorting with coef: p=0.6, f=0.4
    #                 {'p_time': 92, 'f_time': 102}
    #         -- sorting with coef: p=0.7, f=0.30000000000000004
    #                 {'p_time': 92, 'f_time': 102}
    #         -- sorting with coef: p=0.8, f=0.19999999999999996
    #                 {'p_time': 92, 'f_time': 102}
    #         -- sorting with coef: p=0.9, f=0.09999999999999998
    #                 {'p_time': 92, 'f_time': 102}

    runExperiment(p_gt_f_case, "All 'p' are greater than 'f'")
    # output >>>
    # --- F Sort ---
    #         {'p_time': 201, 'f_time': 202}
    # --- P Sort ---
    #         {'p_time': 201, 'f_time': 205}
    # --- Attitude Sort ---
    #         {'p_time': 201, 'f_time': 226}
    # --- Coef Sum Sort ---
    #         -- sorting with coef: p=0.1, f=0.9
    #                 {'p_time': 201, 'f_time': 202}
    #         -- sorting with coef: p=0.2, f=0.8
    #                 {'p_time': 201, 'f_time': 202}
    #         -- sorting with coef: p=0.3, f=0.7
    #                 {'p_time': 201, 'f_time': 202}
    #         -- sorting with coef: p=0.4, f=0.6
    #                 {'p_time': 201, 'f_time': 202}
    #         -- sorting with coef: p=0.5, f=0.5
    #                 {'p_time': 201, 'f_time': 202}
    #         -- sorting with coef: p=0.6, f=0.4
    #                 {'p_time': 201, 'f_time': 202}
    #         -- sorting with coef: p=0.7, f=0.30000000000000004
    #                 {'p_time': 201, 'f_time': 202}
    #         -- sorting with coef: p=0.8, f=0.19999999999999996
    #                 {'p_time': 201, 'f_time': 205}
    #         -- sorting with coef: p=0.9, f=0.09999999999999998
    #                 {'p_time': 201, 'f_time': 205}

    runExperiment(mixed_case, "Mixed case: both f > p and p > f")
    # output >>>
    # --- F Sort ---
    #         {'p_time': 123, 'f_time': 129}
    # --- P Sort ---
    #         {'p_time': 123, 'f_time': 153}
    # --- Attitude Sort ---
    #         {'p_time': 123, 'f_time': 153}
    # --- Coef Sum Sort ---
    #         -- sorting with coef: p=0.1, f=0.9
    #                 {'p_time': 123, 'f_time': 129}
    #         -- sorting with coef: p=0.2, f=0.8
    #                 {'p_time': 123, 'f_time': 129}
    #         -- sorting with coef: p=0.3, f=0.7
    #                 {'p_time': 123, 'f_time': 129}
    #         -- sorting with coef: p=0.4, f=0.6
    #                 {'p_time': 123, 'f_time': 129}
    #         -- sorting with coef: p=0.5, f=0.5
    #                 {'p_time': 123, 'f_time': 129}
    #         -- sorting with coef: p=0.6, f=0.4
    #                 {'p_time': 123, 'f_time': 129}
    #         -- sorting with coef: p=0.7, f=0.30000000000000004
    #                 {'p_time': 123, 'f_time': 137}
    #         -- sorting with coef: p=0.8, f=0.19999999999999996
    #                 {'p_time': 123, 'f_time': 144}
    #         -- sorting with coef: p=0.9, f=0.09999999999999998
    #                 {'p_time': 123, 'f_time': 150}

    # в результате четырех экспериментов и эксперимента с интервалами видно, что время работы
    # суперкомпьютера, как и предполагалось, константно и не меняется от решения к решению,
    # в то время как результирующее время индексирования зависело от способа сортировки:
    # сортировка по продолжительности операций f стабильно выдает лучший результат, при этом
    # коэффициентная сортировка всегда выдает схожий результат при маленькой значимести
    # критерия p, однако коэффициент зависит от входных данных, что позволяет предположить
    # о незначимости учета продолжительности операций p при оптимизации времени индексации

    # итог: оптимизация достигается за счет сортировки заданий по параметру f, сортировка
    # производится при помощи жадного алгоритма - быстрая сортировка, - действующего по
    # принципу "разделяй и властвуй", временная сложность алгоритма быстрой сортировки в общем
    # случае равна O(n*log(n)), что является наилучшим результатом для всех известных алгоритмов
    # сортировки
