import numpy as nmp
import matplotlib.pyplot as plt

class Saati:
    matrix_1 = nmp.array([
        [1, 1/3, 3, 1/5],
        [3, 1, 5, 1/3],
        [1/3, 1/5, 1, 1/7],
        [5, 3, 7, 1]
    ])
    matrix_2 = nmp.array([
        [1, 2, 1/5, 1/5],
        [1/2, 1, 1/7, 1/7],
        [5, 7, 1, 1],
        [5, 7, 1, 1]
    ])
    matrix_3 = nmp.array([
        [1, 5, 3, 7],
        [1/5, 1, 1/3, 1/3],
        [1/3, 3, 1, 5],
        [1/7, 1/3, 1/5, 1]
    ])
    matrix_4 = nmp.array([
        [1, 1/3, 5, 5],
        [3, 1, 7, 7],
        [1/5, 1/7, 1, 1],
        [1/5, 1/7, 1, 1]
    ])
    matrix_wight = nmp.array([
        [1, 3, 5, 7],
        [1/3, 1, 3, 5],
        [1/5, 1/3, 1, 3],
        [1/7, 1/5, 1/3, 1]
    ])

    def __init__(self):
        v_1 = self.normalization(self.matrix_1)
        v_2 = self.normalization(self.matrix_2)
        v_3 = self.normalization(self.matrix_3)
        v_4 = self.normalization(self.matrix_4)
        self.r_v = nmp.array(self.normalization(self.matrix_wight))
        self.r_v.shape = (4, 1)
        self.r_mat = nmp.array([v_1, v_2, v_3, v_4]).transpose()

    def normalization(self, matrix):
        m_list = list()
        al_sum = nmp.sum(matrix)
        for row in matrix:
            sum_str = nmp.sum(row) / al_sum
            m_list.append(sum_str)
        return m_list

    def solution(self):
        return nmp.dot(self.r_mat, self.r_v)


class Weight:
    my_matrix = nmp.array([
        [3, 3, 5, 6],
        [4, 2, 3, 5],
        [2, 7, 4, 1],
        [5, 7, 2, 1]
    ], dtype=nmp.float)

    cr = nmp.array([
        [5/2],
        [5/2],
        [1],
        [0]
    ], dtype=nmp.float)

    def __init__(self):
        self.m_sum = []
        for j in range(self.my_matrix.shape[1]):
            s = 0
            for i in range(self.my_matrix.shape[0]):
                s += self.my_matrix[i][j]
            self.m_sum.append(s)
        self.my_matrix.round()
        for i in range(len(self.my_matrix)):
            for j in range(len(self.my_matrix[0])):
                self.my_matrix[i][j] = round((self.my_matrix[i][j] / self.m_sum[j]), 2)

        summ = nmp.sum(self.cr)
        for i in range(self.cr.size):
            self.cr[i][0] /= summ

        self.solution = nmp.dot(self.my_matrix, self.cr)

    def get_solution(self):
        return self.solution


class Main:
    my_matrix = nmp.array([
        [3, 3, 5, 6],
        [4, 2, 3, 5],
        [2, 7, 4, 1],
        [5, 7, 2, 1]
    ], dtype=nmp.float)
    main = 0

    def __init__(self):
        self.m_min = []
        self.m_max = []
        for j in range(self.my_matrix.shape[1]):
            m_max = 0
            m_min = 100
            for i in range(self.my_matrix.shape[0]):
                if j == self.main:
                    continue
                if self.my_matrix[i][j] > m_max:
                    m_max = self.my_matrix[i][j]
                if self.my_matrix[i][j] < m_min:
                    m_min = self.my_matrix[i][j]
            self.m_min.append(m_min)
            self.m_max.append(m_max)
        self.my_matrix.round()
        for i in range(len(self.my_matrix)):
            for j in range(len(self.my_matrix[0])):
                if j == self.main:
                    continue
                self.my_matrix[i][j] = round((self.my_matrix[i][j] - self.m_min[j]) / (self.m_max[j] - self.m_min[j]), 2)

    def get_solution(self):
        restriction = [0.2, 0.5, 0.5]
        solution = []
        num = 0
        for row in self.my_matrix:
            good = True
            j = 0
            for element in row:
                if j == 0:
                    j += 1
                    continue
                if element < restriction[j - 1]:
                    good = False
            if good:
                solution.append(num)
            num += 1
            j += 1
        return solution


class Pareto2:
    my_matrix = nmp.array([
        [3, 3, 5, 6],
        [4, 2, 3, 5],
        [2, 7, 4, 1],
        [5, 7, 2, 1]
    ])

    def __init__(self):
        k1, k2 = 0, 2
        self.n_m = list()
        for row in self.my_matrix:
            n_list = list(row[k1:k2 + 1:k2 - k1])
            self.n_m.append(n_list)
        self.x_max = 0
        self.y_max = 0
        for row in self.n_m:
            if row[0] > self.x_max:
                self.x_max = row[0]
            if row[1] > self.y_max:
                self.y_max = row[1]
        self.dis = []
        for row in self.n_m:
            self.dis.append(self.x_max - row[0] + self.y_max - row[1])
        self.min_dis = min(self.dis)
        pass

    def print(self):
        fig = plt.figure()
        new_n_m = list(list(row) for row in self.n_m)
        new_n_m.sort()
        x = list(row[0] for row in new_n_m)
        y = list(row[1] for row in new_n_m)
        # Добавление на рисунок прямоугольной (по умолчанию) области рисования
        scatter1 = plt.scatter(self.x_max, self.y_max)
        count = 0
        for row in self.n_m:
            plt.scatter(row[0], row[1])
            plt.text(row[0], row[1], chr(count + ord('A')))
            count += 1

        plt.plot(x, y)
        plt.text(self.x_max, self.y_max, 'Точка утопии')
        grid1 = plt.grid(True)  # линии вспомогательной сетки
        plt.show()

    def get_solution(self):
        count = 0
        s = list()
        for el in self.dis:
            if el == self.min_dis:
                s.append(count)
            count += 1
        return s

def saati():
    s = Saati().solution()
    ch = 'A'
    for row in s:
        for el in row:
            print(ch, "=", el)
            ch = chr(ord(ch) + 1)

def weight():
    s = Weight().get_solution()
    ch = 'A'
    for row in s:
        for el in row:
            print(ch, "=", el)
            ch = chr(ord(ch) + 1)

def main():
    s = Main().get_solution()
    for el in s:
        print(chr(el + ord('A')))

def pareto():
    obj = Pareto2()
    s = obj.get_solution()
    for el in s:
        print(chr(el + ord('A')))
    obj.print()

saati()
print("\n")
weight()
print("\n")
main()
print('\n')
pareto()
