class BubbleSort:
    @staticmethod
    def bubble_sort(A):
        n = len(A) #Determina o tamanho da lista
        for i in range(n):   # Loop externo para percorrer toda a lista
            for j in range(0, n-i-1):    # Loop interno para comparar e trocar elementos adjacentes
                if A[j] > A[j+1]: # Verifica se o elemento atual é maior que o próximo
                    A[j], A[j+1] = A[j+1], A[j] # Troca os elementos
