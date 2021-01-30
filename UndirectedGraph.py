import random
from abc import ABC
result1 = []
result2 = []
class Graph(ABC):

    def create_matrix(self):
        pass

    def Path(self, result):
        semieulerian_path, eulerian_path = [], []
        for i in result:  # вывод полустепеней исхода
            j = []
            for il in i:
                if il != 0 and il != 151:
                    j.append(il)
            semieulerian_path.append(len(j))
        print("полустепени исхода: ")
        print(semieulerian_path)

        y = list(zip(*result))
        for i in y:  # вывод полустепеней захода
            j = []
            for il in i:
                if il != 0 and il != 151:
                    j.append(il)
            eulerian_path.append(len(j))
        print("полустепени захода: ")
        print(eulerian_path)

class DirectedGraph(Graph):
    matrix1, matrix2, matrix3 = [], [], []
    m1, m2 = [], []


    def __init__(self):
        self.create_matrix()


    def create_matrix(self):
        for i in range(15):  # параметры для всех вершин
            for j in range(2):
                a = random.random()
                num = round(a, 1)
                self.m2.append(num)
            self.m1.append(self.m2)
        res = self.m1[0]
        for i in range(15):
            v = res[i + i:i + i + 2]
            i += 2
            self.matrix1.append(v)

        for i in range(15):  # записываем параметры для нужных вершин
            for j in range(15):
                res = random.randint(0, 1)
                if res == 1:
                    self.matrix2 = self.matrix1[j]
                else:
                    self.matrix2 = 0
                self.matrix3.append(self.matrix2)

        for i in range(15):  # разбитие на массивы и запись массивов в матрицу смежности
            v = self.matrix3[i + i: i + i + 15]
            i += 15
            result1.append(v)

        for i in range(15):  # вывод матрицы смежности
            print(result1[i])


class UndirectedGraph(Graph):

    def __init__(self):
        self.create_matrix()

    def create_matrix(self):
        for i in range(15):  # заполняем матрицу нулями
            result2.append([])
            for j in range(15):
                result2[i].append(0)

        for i in range(15):  # заполняем значения
            for j in range(15):
                r = random.randint(0, 1)
                a = random.randint(0, 14)
                b = random.randint(0, 14)
                if r == 1:
                    result2[a][b] = random.randint(1, 10)
                else:
                    result2[a][b] = 151  # "бесконечность", так как максимальный путь может составлять только 150
                result2[b][a] = result2[a][b]

        for i in result2:  # заменяем оставшиеся нули "бесконечностью"
            for j in i:
                if j == 0:
                    r = random.randint(0, 1)
                    if r == 1:
                        i[i.index(j)] = random.randint(1, 10)
                    else:
                        i[i.index(j)] = 151

        for i in result2:  # вывод получившейся матрицы смежности
            str1 = " "
            for il in i:
                str1 += str(il) + " "
            print(str1)


newDirectedGraph = DirectedGraph()
newDirectedGraph.Path(result1)
newUndirectedGraph = UndirectedGraph()
newUndirectedGraph.Path(result2)
