<b> РАСЧЕТНО-ПРАКТИЧЕСКАЯ РАБОТА </b>

<b> ТЕМА: "АЛГОРИТМЫ НА ГРАФАХ" </b>

<b> Цель работы: </b>

Изучение алгоритмов перебора вершин графа и использование этих алгоритмов при программировании задач на графах.

<b> Задание: </b>

Построить остов графа с помощью алгоритма «поиск в ширину».

<b> Решение: </b>

Для решения поставленной задачи был выбран язык Python 3.5, т.к. он имеет лёгкий и простой синтаксис, а также включает в себя ряд универсальных функций, например - очередь (применяется в данной задаче).

В Питоне с целью осуществления обхода в ширину исходный граф G удобно представлять в памяти ЭВМ списком смежности adj, храня для каждой вершины графа v список adj[v] смежных с ней вершин. Список used, исполняющий роль булевского массива размерности N, служит для отметки о том, стала вершина v посещенной в процессе обхода в ширину или еще нет. При этом если used[v] = True, то вершина v является посещенной, если used[v] = False, то нет. Процедура использует очередь queue.Queue() для хранения еще не посещенных вершин, достижимых из текущей обрабатываемой вершины в обходе. Чтобы использовать очередь в Питоне, необходимо импортировать её командой: import queue. 

Как это выглядит в программе:

import queue  # импорт очереди

adj = [[] for i in range(n)] #список смежности

used = [False for i in range(n)] #инфо о пройденных и не пройденных вершинах

queue.Queue() #очередь для добавления вершин при обходе в ширину

В качестве списка смежности для представления графа на языке 
Python 3.5 удобно использовать список списков adj. В приведенной ниже реализации входные данные считываются из файла graf.txt, а результат работы программы выводится в консоли.

<b> Контрольный пример: </b>

Рассмотрим работу алгоритма на графе G, изображенном на рисунке:

![example](https://raw.githubusercontent.com/aksenof/vsuet-projects/master/discrete-mathematics/pract-work/example.png)

Начальная вершина обхода в ширину - вершина с номером 1. После завершения работы алгоритма будет построено дерево поиска в ширину Gπ. Ребра исходного графа G, которые входят в дерево поиска в ширину Gπ изображены на рисунке жирной линией.

<b> Входные данные: </b>

![graf](https://raw.githubusercontent.com/aksenof/vsuet-projects/master/discrete-mathematics/pract-work/graf.png)

<b> Результат работы программы: </b>

![rpr](https://raw.githubusercontent.com/aksenof/vsuet-projects/master/discrete-mathematics/pract-work/rpr.png)

<b> Вывод: </b>

В данной работе была представлена реализация алгоритма поиска в ширину для построения остова на языке Python 3.5. Проверка программы осуществлена на контрольном примере, приведенном выше. Исходя из ручного решения и графического представления построенного дерева, программа работает верно.
