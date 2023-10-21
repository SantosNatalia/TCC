class CountingSort:
    @staticmethod
    def counting_sort(A, B, k): # Inicializa um array C com tamanho k+1 preenchido com zeros
        C = [0] * (k + 1)

        for i in range(k + 1): # Inicializa todos os elementos de C com zero
            C[i] = 0

        for j in range(len(A)): # Conta a ocorrência de cada elemento em A e armazena em C
            C[A[j]] = C[A[j]] + 1

        for i in range(1, k + 1):  # Atualiza os valores em C para indicar as posições finais de cada elemento em B
            C[i] = C[i] + C[i - 1]

        for j in range(len(A), 0, -1): # Preenche o array B com os elementos de A, classificados
            B[C[A[j - 1]] - 1] = A[j - 1]
            C[A[j - 1]] = C[A[j - 1]] - 1




















