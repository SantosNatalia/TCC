class SelectionSort:
    @staticmethod
    def selection_sort(vet):
        n = len(vet)  # Obtém o tamanho da lista
        for i in range(n - 1): #percorre a lista até o penúltimo elemento
            im = i
            for j in range(i + 1, n): #encontra o índice do menor elemento no restante da lista
                if vet[j] < vet[im]:# Se o elemento atual é menor do que o elemento no índice 'im', atualize 'im'
                    im = j
            if im > i: # Se 'im' foi atualizado, troque os elementos nas posições 'i' e 'im'
                aux = vet[i]
                vet[i] = vet[im]
                vet[im] = aux


