from Counting import CountingSort
class RadixSort:
    @staticmethod
    def radix_sort(A):
        max_element = max(A) # Encontra o elemento máximo na lista A.
        exp = 1  # Inicializa o expoente para o primeiro dígito.
        exp = 1

        while max_element // exp > 0: # Enquanto o maior elemento dividido por exp for maior que 0, continue o loop.
            CountingSort.counting_sort(A, exp) # Chama o CountingSort para ordenar a lista A com base no dígito atual (exp).
            exp *= 10 # Aumenta o expoente para selecionar o próximo dígito.







