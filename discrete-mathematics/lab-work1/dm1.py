from numpy import array
# блок функций программы:
def comb(data, k):
    s = len(data)
    a = list(i for i in range(1, s**s+2))
    result = []
    for i in range(1, k+1):
    	a[i] = i
    p = k
    while p >= 1:
        if k != s:
            for m in range(1, k+1):
                result.append(data[a[m]-1])
            if a[k] == s:
                p = p - 1
            else:
                p = k
            if p >= 1:
                for i in list(range(p, k+1))[::-1]:
                    a[i] = a[p] + i - p + 1
        else:
            p = 0
    lst = array(result)
    if k != s:
        lst.shape = (int(len(result)/k), k)
        lst = list(i for i in lst.tolist())
    else:
        lst = [data]
    return lst

def mnozh(lst):
	count = 1
	for i in lst:
		count *= i
	return count
	
# головная программа:
m = int(input("введите m: "))
enter_n = input("введите числа n: ")
list_n = list(int(i) for i in enter_n.split(","))
memory = list(set([i for i in list_n for j in list_n if j % i == 0 and j > i]))
n = list(i for i in list_n if i not in memory)
no = m
for i in range(1, len(n)+1):
	summa = 0
	for pp in comb(n, i):
		summa = int(m/mnozh(pp))
		if i%2 != 0:
			no = no - summa
		else:
			no = no + summa
print("кол-во m, которые не делятся на n:", no)
