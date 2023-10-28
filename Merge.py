class MergeSort:
    @staticmethod
    def merge_sort(A, p, r):
        if p < r: # Verifica se a lista tem mais de um elemento
            q = (p + r) // 2 # Calcula o ponto médio da lista
            MergeSort.merge_sort(A, p, q) # Ordena a metade esquerda
            MergeSort.merge_sort(A, q + 1, r) # Ordena a metade direita
            MergeSort.merge(A, p, q, r) # Combina as duas metades ordenadas

    @staticmethod
    def merge(A, p, q, r):
        n1 = q - p + 1 # Tamanho da primeira metade
        n2 = r - q # Tamanho da segunda metade

        L = [0] * (n1 + 1)  # Cria uma lista temporária para a metade esquerda
        R = [0] * (n2 + 1)  # Cria uma lista temporária para a metade direita

        for i in range(n1):
            L[i] = A[p + i]  # Copia os elementos da metade esquerda para L

        for j in range(n2):
            R[j] = A[q + j + 1] # Copia os elementos da metade direita para R

        L[n1] = float('inf') # Adiciona um valor infinito ao final de L
        R[n2] = float('inf') # Adiciona um valor infinito ao final de R

        i = 0
        j = 0

        for k in range(p, r + 1): # Percorre a lista original
            if L[i] <= R[j]: # Compara os elementos de L e R
                A[k] = L[i] # Se o elemento de L for menor, coloca em A
                i += 1
            else:
                A[k] = R[j] # Se o elemento de R for menor, coloca em A
                j += 1



