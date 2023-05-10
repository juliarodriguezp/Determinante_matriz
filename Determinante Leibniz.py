#Declarando as matrizes
matriz_1 = [
        [1, 2, 3, 4], [5, 6, 7, 8],
        [9, 10, 11, 12], [13, 14, 15, 15]
      ]

matriz_2 = [
        [1, 0, 0, 0], [0, 1, 0, 0],
        [0, 0, 1, 0], [0, 0, 0, 1]
     ]

#Lei leibniz
def determinante_leibniz(matriz):

    calculo = 0
    determinante = 0

    for i in range(0, 4):
        for j in range(0, 6):
            if i == 0:
                if j == 0:
                    calculo = matriz[0][0] * matriz[1][1] * matriz[2][2] * matriz[3][3]

                elif j == 1:
                    calculo = (matriz[0][0] * matriz[1][1] * matriz[2][3] * matriz[3][2]) * -1

                elif j == 2:
                    calculo = (matriz[0][0] * matriz[1][2] * matriz[2][1] * matriz[3][3]) * -1

                elif j == 3:
                    calculo = matriz[0][0] * matriz[1][2] * matriz[2][3] * matriz[3][1]

                elif j == 4:
                    calculo = matriz[0][0] * matriz[1][3] * matriz[2][1] * matriz[3][2]

                elif j == 5:
                    calculo = (matriz[0][0] * matriz[1][3] * matriz[2][2] * matriz[3][1]) * -1

            if i == 1:
                if j == 0:
                    calculo = (matriz[0][1] * matriz[1][0] * matriz[2][2] * matriz[3][3]) * -1

                elif j == 1:
                    calculo = matriz[0][1] * matriz[1][0] * matriz[2][3] * matriz[3][2]

                elif j == 2:
                    calculo = matriz[0][1] * matriz[1][2] * matriz[2][0] * matriz[3][3]

                elif j == 3:
                    calculo = (matriz[0][1] * matriz[1][2] * matriz[2][3] * matriz[3][0]) * -1

                elif j == 4:
                    calculo = (matriz[0][1] * matriz[1][3] * matriz[2][0] * matriz[3][2]) * -1

                elif j == 5:
                    calculo = matriz[0][1] * matriz[1][3] * matriz[2][2] * matriz[3][0]

            if i == 2:
                if j == 0:
                    calculo = matriz[0][2] * matriz[1][0] * matriz[2][1] * matriz[3][3]

                elif j == 1:
                    calculo = (matriz[0][2] * matriz[1][0] * matriz[2][3] * matriz[3][1]) * -1

                elif j == 2:
                    calculo = (matriz[0][2] * matriz[1][1] * matriz[2][0] * matriz[3][3]) * -1

                elif j == 3:
                    calculo = matriz[0][2] * matriz[1][1] * matriz[2][3] * matriz[3][0]

                elif j == 4:
                    calculo = matriz[0][2] * matriz[1][3] * matriz[2][0] * matriz[3][1]

                elif j == 5:
                    calculo = (matriz[0][2] * matriz[1][3] * matriz[2][1] * matriz[3][0]) * -1

            if i == 3:
                if j == 0:
                    calculo = (matriz[0][3] * matriz[1][0] * matriz[2][1] * matriz[3][2]) * -1

                elif j == 1:
                    calculo = matriz[0][3] * matriz[1][0] * matriz[2][2] * matriz[3][1]

                elif j == 2:
                    calculo = matriz[0][3] * matriz[1][1] * matriz[2][0] * matriz[3][2]

                elif j == 3:
                    calculo = (matriz[0][3] * matriz[1][1] * matriz[2][2] * matriz[3][0]) * -1

                elif j == 4:
                    calculo = (matriz[0][3] * matriz[1][2] * matriz[2][0] * matriz[3][1]) * -1

                elif j == 5:
                    calculo = matriz[0][3] * matriz[1][2] * matriz[2][1] * matriz[3][0]

            determinante += calculo
            calculo = 0

    return determinante

#chamando função
determinante_1 = determinante_leibniz(matriz_1)
determinante_2 = determinante_leibniz(matriz_2)

#mostrando os resultados
print("O resultado do determinante da primeira matriz é:", determinante_1)
print("O resultado do determinante da segunda matriz é: ", determinante_2)
