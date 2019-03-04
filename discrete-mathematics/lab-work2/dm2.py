def rule(n, i, m, j):  # правило для матрицы
	return 1 if n+2*i > m+j else 0

def srez(k, xx, rr):  # функция среза
	h = []
	for j in range(len(xx)):
		if rr[k][j] == 1:
			h.append(xx[j])
	return h

def print_matrix(lst):  # функция для печати матрицы
	for i in lst:
		print(i)

def antisymmetric(rr):
	for i in range(len(rr)):
		for j in range(i):
			if rr[i][j] == 1 and rr[j][i] == 1 and i != j:
				return False
	return True

def nega_transitivity(rr):
	for i in range(len(rr)):
		for j in range(len(rr)):
			for z in range(len(rr)):
				if rr[i][j] == 0 and rr[j][z] == 0 and rr[i][z] == 1:
					return False
	return True

x = [2, 3, 5, 6, 7, 10, 12, 13, 14, 17, 18, 20]  # множество по условию
r = list([0]*len(x) for i in range(len(x)))  # создание матрицы из нулей
for i in range(len(r)):
	for j in range(len(r)):
		r[i][j] = rule(x[i], i+1, x[j], j+1)  # заполнение матрицы на основе правила rule
print("Множество X =", x)
print("Матрица:")
print_matrix(r)
check = [i for i in range(len(x)) if (i+1)%3==0]  # номера, кратные 3
print("Нижние срезы, номера которых кратны 3:")
for i in check:
	print("Hr({0}) = {1}".format(x[i], srez(i, x, r)))
print("Проверка свойств: ")
if antisymmetric(r):
	print("1. Матрица антисимметрична")
else:
	print("1. Матрица не антисимметрична")
if nega_transitivity(r):
	print("2. Матрица негатранзитивна")
else:
	print("2. Матрица не негатранзитивна")
