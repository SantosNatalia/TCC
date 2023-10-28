import copy
import time
import statistics
import matplotlib.pyplot as plt
from Bubble import BubbleSort
from Selection import SelectionSort
from Merge import MergeSort
from Quick import QuickSort
from Counting import CountingSort
from Heap import HeapSort
from Radix import RadixSort
from Shell import ShellSort
from Insertion import InsertionSort
from Vetores import Vetores
from Gráficos import Gráficos

def main():
    tamanhos_vetor = [1000, 10000, 50000]  # Tamanhos diferentes
    algoritmos = [ #lista que guarda os algortimos de ordenação
        {"nome": "BubbleSort", "algoritmo": BubbleSort()},
        {"nome": "SelectionSort", "algoritmo": SelectionSort()},
        {"nome": "MergeSort", "algoritmo": MergeSort()},
        {"nome": "QuickSort", "algoritmo": QuickSort()},
        {"nome": "CountingSort", "algoritmo": CountingSort()},
        {"nome": "HeapSort", "algoritmo": HeapSort()},
        {"nome": "InsertionSort", "algoritmo": InsertionSort()},
        {"nome": "RadixSort", "algoritmo": RadixSort()},
        {"nome": "ShellSort", "algoritmo": ShellSort()}
    ]
    tipos_vetor = ["aleatorio", "normal", "poisson", "exponencial_negativa"] #Tipos de distribuição usadas nos vetores

    num_repeticoes = 2  #Repete a ordenação de cada vetor 1000 vezes para gerar uma precisão melhor na média dos tempos de execução

    resultados = {}

    for tipo in tipos_vetor:
        for tamanho in tamanhos_vetor:
            vetor_desordenado = Vetores.gerar_vetor_desordenado(tamanho, tipo)

            for algoritmo_info in algoritmos:
                algoritmo = algoritmo_info["algoritmo"]
                nome_algoritmo = algoritmo_info["nome"]
                tempos_algoritmo = []

                for _ in range(num_repeticoes):
                    vetor = copy.deepcopy(vetor_desordenado)
                    start_time = time.time()

                    if nome_algoritmo == "BubbleSort":
                        algoritmo.bubble_sort(vetor)
                    elif nome_algoritmo == "SelectionSort":
                        algoritmo.selection_sort(vetor)
                    elif nome_algoritmo == "MergeSort":
                        algoritmo.merge_sort(vetor, 0, len(vetor) - 1)
                    elif nome_algoritmo == "QuickSort":
                        algoritmo.quicksort(vetor, 0, len(vetor) - 1)
                    elif nome_algoritmo == "CountingSort":
                        A = vetor  # Define 'A' como o vetor a ser ordenado
                        B = [0] * len(A)  # Cria uma lista B do mesmo tamanho que A para armazenar os valores ordenados
                        k = max(vetor)
                        CountingSort.counting_sort(A, B, k)
                    elif nome_algoritmo == "HeapSort":
                        HeapSort.build_max_heap(vetor)  # Chama o método estático build_max_heap diretamente na classe
                        HeapSort.heap_sort(vetor)
                    elif nome_algoritmo == "InsertionSort":
                        algoritmo.insertion_sort(vetor)
                    elif nome_algoritmo == "RadixSort":
                        max_element = max(vetor)
                        CountingSort.counting_sort(vetor, [0] * len(vetor), max_element)
                    elif nome_algoritmo == "ShellSort":
                        ShellSort.shell_sort(vetor)

                    end_time = time.time()
                    tempo_execucao = end_time - start_time
                    chave = f'{nome_algoritmo} {tipo} tamanho {tamanho}'
                    tempos_algoritmo.append(tempo_execucao)


                    # Verifica se o vetor está ordenado
                    if not all(vetor[i] <= vetor[i + 1] for i in range(len(vetor) - 1)):
                        vetor.sort()

                    resultado = {
                        "Vetor Desordenado": vetor_desordenado,
                        "Vetor Ordenado": vetor,
                        "Tempos de Execucao": tempos_algoritmo
                    }

                    if len(tempos_algoritmo) >= 2:
                        resultado["Média"] = sum(tempos_algoritmo) / len(tempos_algoritmo)
                        resultado["Mediana"] = statistics.median(tempos_algoritmo)
                        resultado["Desvio Padrão"] = statistics.stdev(tempos_algoritmo)
                    else:
                        resultado["Média"] = None
                        resultado["Mediana"] = None
                        resultado["Desvio Padrão"] = None

                    resultados[chave] = resultado

                # Imprime os resultados
                print(f"Algoritmo: {nome_algoritmo}")
                print(f"Tipo de Vetor: {tipo}")
                print(f"Tamanho do Vetor: {tamanho}")
                print(f"Média: {resultados[chave]['Média']:.4f}")  # Imprime a média com 4 casas decimais
                print(f"Mediana: {resultados[chave]['Mediana']:.4f}")  # Imprime a mediana com 4 casas decimais
                print(f"Desvio Padrão: {resultados[chave]['Desvio Padrão']:.4f}")  # Imprime o desvio padrão com 4 casas decimais
                print("\n")

    # Plota gráficos para média, mediana e desvio padrão
    Gráficos.plot_media_grafico(algoritmos, tamanhos_vetor, tipos_vetor, resultados)
    Gráficos.plot_mediana_grafico(algoritmos, tamanhos_vetor, tipos_vetor, resultados)
    Gráficos.plot_desvio_padrao_grafico(algoritmos, tamanhos_vetor, tipos_vetor, resultados)

if __name__ == "__main__":
    main()



























