import time

class InsertionSort:
    @staticmethod
    def insertion_sort(A):
        for j in range(1, len(A)):  # Percorre a lista A a partir do segundo elemento
            chave = A[j]  # Armazena o valor do elemento atual em 'chave'
            i = j - 1    # Inicializa 'i' com o índice anterior ao elemento atual
            while i >= 0 and A[i] > chave:   # Move os elementos maiores que 'chave' uma posição à direita
                A[i + 1] = A[i]
                i = i - 1
            A[i + 1] = chave  # Insere 'chave' na posição correta




