def print_hi(name):
    print(f'Hi, {name}')
if __name__ == '__main__':
    print_hi('PyCharm')
    # для 1 лабы
    from math import *
    with open("input_lab1.txt", "r") as f_in, open("output_lab1.txt", "w") as f_out:

        alpha = float(f_in.readline().strip())

        chislitel_z1 = 1 - 2 * (sin(alpha) ** 2)
        znamenatel_z1 = 1 + sin(2 * alpha)
        z1 = chislitel_z1 / znamenatel_z1

        chislitel_z2 = 1 - tan(alpha)
        znamenatel_z2 = 1 + tan(alpha)
        z2 = chislitel_z2 / znamenatel_z2

        f_out.write(f"Результат z1 = {z1:.4f}\n")
        f_out.write(f"Результат z2 = {z2:.4f}\n")

    print("готово данные записаны в:output_lab1.txt")
    #для 4 лабы
    from random import *

    with open("input_lab4.txt", "r") as f_in, open("output_lab4.txt", "w") as f_out:

        n = int(f_in.readline().strip())
        a = float(f_in.readline().strip())
        b = float(f_in.readline().strip())

        mas = []
        for i in range(n):
            chislo = uniform(-10, 10)
            mas.append(round(chislo, 2))

        f_out.write(f"исходный массив: {mas}\n")

        min_abs = abs(mas[0])
        min_index = 0

        for i in range(1, n):
            if abs(mas[i]) < min_abs:
                min_abs = abs(mas[i])
                min_index = i

        f_out.write(f"номер минимального по модулю элемента {min_index + 1}\n")

        summa = 0
        nasli_otricatelniy = False

        for i in range(n):
            if nasli_otricatelniy == True:
                summa = summa + abs(mas[i])

            if mas[i] < 0:
                nasli_otricatelniy = True

        f_out.write(f"сумма модулей после первого отрицательного: {round(summa, 2)}\n")

        j = 0
        for i in range(n):
            if mas[i] < a or mas[i] > b:
                mas[j] = mas[i]
                j = j + 1

        for i in range(j, n):
            mas[i] = 0

        f_out.write(f"массив после сжатия: {mas}\n")

    print("готово данные записаны в:output_lab4.txt")

    def print_matrix_to_file(matrix, f, title="матрица"):
        f.write(f"\n{title}:\n")
        for row in matrix:
            for elem in row:
                f.write(f"{elem:8.2f}")
            f.write("\n")

    def to_triangular(matrix):
        n = len(matrix)
        m = len(matrix[0])
        tri_matrix = [row[:] for row in matrix]

        for i in range(min(n, m)):
            if tri_matrix[i][i] == 0:
                for k in range(i + 1, n):
                    if tri_matrix[k][i] != 0:
                        tri_matrix[i], tri_matrix[k] = tri_matrix[k], tri_matrix[i]
                        break

            if tri_matrix[i][i] != 0:
                for j in range(i + 1, n):
                    factor = tri_matrix[j][i] / tri_matrix[i][i]
                    for k in range(i, m):
                        tri_matrix[j][k] -= factor * tri_matrix[i][k]

        for i in range(n):
            for j in range(m):
                tri_matrix[i][j] = round(tri_matrix[i][j], 2)

        return tri_matrix

    def count_rows_less_than(matrix, value):
        count = 0
        for row in matrix:
            avg = sum(row) / len(row)
            if avg < value:
                count += 1
        return count
    #для 5 лабы
    with open("input_lab5.txt", "r") as f_in, open("output_lab5.txt", "w") as f_out:

        n = int(f_in.readline().strip())
        m = int(f_in.readline().strip())
        val = float(f_in.readline().strip())

        mat = []
        for _ in range(n):
            row = list(map(float, f_in.readline().split()))
            mat.append(row)

        print_matrix_to_file(mat, f_out, "исходная матрица")

        tri_mat = to_triangular(mat)
        print_matrix_to_file(tri_mat, f_out, "треугольная матрица")

        result = count_rows_less_than(tri_mat, val)
        f_out.write(f"\nколичество строк где среднее < {val}: {result}\n")

    print("готово данные записаны в:output_lab5.txt")