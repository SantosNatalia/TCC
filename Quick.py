class QuickSort:
    @staticmethod
    def quicksort(A, p, r):
        while p < r:
            q = QuickSort.partition(A, p, r)  # Chama a função partition para encontrar o pivô
            if q - p < r - q: # Verifica se a parte esquerda é menor que a parte direita
                QuickSort.quicksort(A, p, q - 1) # Recursivamente ordena a parte esquerda
                p = q + 1 # Atualiza o início para a parte direita
            else:
                QuickSort.quicksort(A, q + 1, r) # Recursivamente ordena a parte direita
                r = q - 1 # Atualiza o fim para a parte esquerda

    @staticmethod
    def partition(A, p, r):
        x = A[r] # Seleciona o elemento na posição r como pivô
        i = p - 1
        for j in range(p, r): # Percorre o array da posição p até r-1
            if A[j] <= x: # Se o elemento atual for menor ou igual ao pivô
                i = i + 1
                A[i], A[j] = A[j], A[i]
        A[i + 1], A[r] = A[r], A[i + 1]
        return i + 1 # Retorna a posição do pivô após a partição







