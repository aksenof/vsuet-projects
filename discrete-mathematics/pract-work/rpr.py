import queue  # импорт очереди
file = open("graf.txt")  # открытие файла
data = list()  # список данных из файла 
new_graf = list()  # список для нового графа
q = queue.Queue() #очередь для добавления вершин при обходе в ширину
for line in file:  # построчный цикл по файлу
    data.append([int(line[0]), int(line[2])]) # добавление эл-тов в data
print("Данные из файла:")
def print_data(lst):  # функция печати данных
    for i in lst:
        print(i)
print_data(data)
all_points = list(set([i for n in data for i in n]))  # список вершин
n = len(all_points)  # кол-во вершин в графе
m = len(data)  # кол-во ребер в графе
print("Кол-во вершин в графе:", n)
print("Кол-во ребер  в графе:", m)
adj = [[] for i in range(n)]  # список смежности (инцидентности)
data_graf = [[] for i in range(n)] # список для заданного графа
used = [False for i in range(n)]  # инфо о пройденных и не пройденных вершинах
for i in data:  # прохождение по элементам в списке data
    v, w = i[0], i[1]
    v -= 1
    w -= 1
    adj[v].append(w)  # добавление эл-та в список смежности
    adj[w].append(v)  # добавление эл-та в список смежности
    data_graf[v].append(w+1)  # добавление эл-та для построения графа
    data_graf[w].append(v+1)  # добавление эл-та для построения графа  
def breadth(v):  # функция обхода в ширину
    if used[v]:  # если вершина пройдена не производим из нее вызов ф-ции
        return
    q.put(v);  # начинаем обход из вершины v
    used[v] = True  # начинаем обход из вершины v
    while(not q.empty()):  # пока в очереди есть хотя бы одна вершина
        v = q.get()  # извлекаем вершину из очереди
        for w in adj[v]:  # запускаем обход из всех вершин, смежных с вершиной v
            if used[w]:  # если вершина уже была посещена, то пропускаем ее  
                continue
            q.put(w)  # добавляем вершину в очередь обхода
            used[w] = True  # помечаем вершину как пройденную
            new_graf.append([v+1, w+1]) # добавляем в новый граф ребро (v, w)
def run():  # функция запуска breadth
    for v in range(n):
        breadth(v)
run()  # запуск breadth
print("Исходный граф:")
def print_graf(gg):  # функция печати графа
	for i in range(len(gg)):
		print(i+1, ":", gg[i])
print_graf(data_graf)  # печать графа
derevo = {i: [] for i,j in new_graf}  # создание пустого дерева
for i,j in new_graf:  
    derevo[i] = derevo[i] + [j]  # добавление эл-тов в дерево из списка new_graf
def print_derevo(dd):  # функция печати дерева
    for i in dd:
        print(i, ":", dd[i])
print("Остов:")
print_derevo(derevo) # печать дерева
