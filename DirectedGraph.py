import random

matrix1, matrix2, matrix3 = [], [], []
m1, m2 = [], []
semieulerian_parh, eulerian_path, result = [], [], []

for i in range(15):  # параметры для всех вершин
    for j in range(2):
        a = random.random()
        num = round(a, 1)
        m2.append(num)
    m1.append(m2)
res = m1[0]
for i in range(15):
    v = res[i + i:i + i + 2]
    i += 2
    matrix1.append(v)


for i in range(15):  # записываем параметры для нужных вершин
    for j in range(15):
        res = random.randint(0, 1)
        if res == 1:
            matrix2 = matrix1[j]
        else:
            matrix2 = 0
        matrix3.append(matrix2)

for i in range(15):  # разбитие на массивы и запись массивов в матрицу смежности
    v = matrix3[i + i: i + i + 15]
    i += 15
    result.append(v)


for i in range(15):  # вывод матрицы смежности
    print(result[i])


for i in result:  # вывод полустепеней исхода
    j = []
    for il in i:
        if il != 0:
            j.append(il)
    semieulerian_parh.append(len(j))
print("полустепени исхода: ")
print(semieulerian_parh)

y = list(zip(*result))
for i in y:  # вывод полустепеней захода
    j = []
    for il in i:
        if il != 0:
            j.append(il)
    eulerian_path.append(len(j))
print("полустепени захода: ")
print(eulerian_path)