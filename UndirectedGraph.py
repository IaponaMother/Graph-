import random

m = []  # заполняем матрицу нулями
for i in range(15):
    m.append([])
    for j in range(15):
        m[i].append(0)

for i in range(15):     # заполняем значения
    for j in range(15):
        r = random.randint(0, 1)
        a = random.randint(0, 14)
        b = random.randint(0, 14)
        if r == 1:
            m[a][b] = random.randint(1, 10)
        else:
            m[a][b] = 151  # "бесконечность", так как максимальный путь может составлять только 150
        m[b][a] = m[a][b]

for i in m:  # заменяем оставшиеся нули "бесконечностью"
    for j in i:
        if j == 0:
            r = random.randint(0, 1)
            if r == 1:
                i[i.index(j)] = random.randint(1, 10)
            else:
                i[i.index(j)] = 151

for i in m:     # вывод получившейся матрицы смежности
    str1 = " "
    for il in i:
        str1 += str(il) + " "
    print(str1)

# start = int(input("начальная вершина: ")) - 1
# end = int(input("конечная вершина: "))
# active = [True] * end  # все вершины, кроме первой не просмотрены
# active[0] = False
# P = [0] * end
# P[0] = -1
# list = m[0]
# result = []
# iterator = end - 1
#
# for i in range(end - 1):  # поиск кратчайшего пути из начальной вершины в конечную
#     shortestPath = 151  # путь неизвестен, поэтому он равен 151
#     for il in range(end):
#         if active[il] and list[il] < shortestPath:
#             shortestPath = list[il]
#             viewedVertices = il
#     active[viewedVertices] = False
#     for j in range(end):
#         if list[viewedVertices] + m[viewedVertices][j] < list[j]:
#             list[j] = list[viewedVertices] + m[viewedVertices][j]
#             P[j] = viewedVertices
#
# while iterator >= start:
#     print(iterator, end=" ")
#     iterator = P[iterator]