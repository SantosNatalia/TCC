class HeapSort:
    @staticmethod
    def build_max_heap(A):
        tamanho_do_heap = len(A) # Obtém o tamanho do array
        for i in range(tamanho_do_heap // 2, 0, -1):   # Começa a partir da metade do array e move para a esquerda.
            HeapSort.max_heapify(A, i) # Garante que o array seja convertido em uma heap max.

    @staticmethod
    def max_heapify(A, i):
        tamanho_do_heap = len(A) # Obtém o tamanho do array
        l = 2 * i # Calcula o índice do filho esquerdo
        r = 2 * i + 1 # Calcula o índice do filho direito

        if l <= tamanho_do_heap and A[l - 1] > A[i - 1]:# Compara o valor do filho esquerdo com o valor do pai
            maior = l
        else:
            maior = i

        if r <= tamanho_do_heap and A[r - 1] > A[maior - 1]: # Compara o valor do filho direito com o maior valor (pai ou filho esquerdo)
            maior = r

        if maior != i: # Se o maior valor não for o pai, troque o pai com o maior filho e continue a heapify
            A[i - 1], A[maior - 1] = A[maior - 1], A[i - 1]
            HeapSort.max_heapify(A, maior)

    @staticmethod
    def heap_sort(A):
        tamanho_do_heap = len(A) # Obtém o tamanho do array
        HeapSort.build_max_heap(A) # Converte o array em uma heap max
        for i in range(len(A), 1, -1):
            A[0], A[i - 1] = A[i - 1], A[0] # Troca o maior elemento com o último elemento não classificado
            tamanho_do_heap = tamanho_do_heap - 1 # Reduz o tamanho do heap
            HeapSort.max_heapify(A, 1) # Reorganiza a heap max sem o elemento classificado


