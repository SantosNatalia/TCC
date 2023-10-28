class ShellSort:
    @staticmethod
    def less(x, y):
        return x < y

    @staticmethod
    def exch(a, i, j):
        a[i], a[j] = a[j], a[i]

    @staticmethod
    def shell_sort(a):
        N = len(a)
        h = 1
        while h < N // 3: # O loop a seguir calcula o valor inicial de h usando a sequência 3x + 1
            h = 3 * h + 1

        while h >= 1: # O loop executa a ordenação com um determinado valor de h
            for i in range(h, N):
                j = i
                while j >= h and ShellSort.less(a[j], a[j - h]): #verifica e troca os elementos a[j] e a[j-h]
                    ShellSort.exch(a, j, j - h)
                    j -= h
            h = h // 3  # Reduz o valor de h para a próxima iteração

