import statistics
import matplotlib.pyplot as plt

class Gráficos:
    @staticmethod
    def plot_mediana_grafico(algoritmos, tamanhos_vetor, tipos_vetor, resultados):
        for tipo in tipos_vetor:
            plt.figure(figsize=(12, 6))
            legend_labels = []

            for algoritmo_info in algoritmos:
                nome_algoritmo = algoritmo_info["nome"]
                medianas = []

                for tamanho in tamanhos_vetor:
                    chave = f'{nome_algoritmo} {tipo} tamanho {tamanho}'

                    if chave in resultados:   # Verifica se há dados de tempo de execução disponíveis
                        tempos_algoritmo = resultados[chave]["Tempos de Execucao"]

                        if tempos_algoritmo:
                            medianas.append(statistics.median(tempos_algoritmo))  # Calcula a mediana dos tempos de execução

                if medianas: #Plota os dados no gráfico
                    plt.plot(tamanhos_vetor, medianas, marker='o')
                    legend_labels.append(nome_algoritmo)

            #Configurações do gráfico
            plt.xlabel("Tamanho do Vetor")
            plt.ylabel("Tempo de Execução Mediana (segundos)")
            plt.title(f"Mediana dos Tempos de Execução dos Algoritmos de Ordenação para Vetores usando {tipo}")
            plt.legend(legend_labels, loc="upper left")
            plt.grid(True)
            plt.show()

    @staticmethod
    def plot_desvio_padrao_grafico(algoritmos, tamanhos_vetor, tipos_vetor, resultados):
        for tipo in tipos_vetor:
            plt.figure(figsize=(12, 6))
            legend_labels = []

            for algoritmo_info in algoritmos:
                nome_algoritmo = algoritmo_info["nome"]
                desvios_padrao = []

                for tamanho in tamanhos_vetor:
                    chave = f'{nome_algoritmo} {tipo} tamanho {tamanho}'

                    if chave in resultados:
                        tempos_algoritmo = resultados[chave]["Tempos de Execucao"]

                        if tempos_algoritmo and len(tempos_algoritmo) > 1:   # Calcula o desvio padrão dos tempos de execução
                            desvios_padrao.append(statistics.stdev(tempos_algoritmo))
                        else:
                            desvios_padrao.append(0.0)

                if desvios_padrao: #Plota os dados no gráfico
                    plt.plot(tamanhos_vetor, desvios_padrao, marker='o')
                    legend_labels.append(nome_algoritmo)

            #Configurações do gráfico
            plt.xlabel("Tamanho do Vetor")
            plt.ylabel("Desvio Padrão dos Tempos de Execução (segundos)")
            plt.title(f"Desvio Padrão dos Tempos de Execução dos Algoritmos de Ordenação para Vetores usando {tipo}")
            plt.legend(legend_labels, loc="upper left")
            plt.grid(True)
            plt.show()

    @staticmethod
    def plot_media_grafico(algoritmos, tamanhos_vetor, tipos_vetor, resultados):
        plt.figure(figsize=(12, 6))

        for tipo in tipos_vetor:
            for algoritmo_info in algoritmos:
                nome_algoritmo = algoritmo_info["nome"]
                tempos_medios = []

                for tamanho in tamanhos_vetor:
                    chave = f'{nome_algoritmo} {tipo} tamanho {tamanho}'

                    if chave in resultados:
                        tempos_algoritmo = resultados[chave]["Tempos de Execucao"]

                        if tempos_algoritmo:
                            # Calcula a média dos tempos de execução
                            tempos_medios.append(statistics.mean(tempos_algoritmo))

                if tempos_medios: #Plota os dados no gráfico
                    label = nome_algoritmo
                    plt.plot(tamanhos_vetor, tempos_medios, marker='o', label=label)

            #Configurações do gráfico
            plt.title(f'Gráfico de Média de Tempo de Execução ({tipo})')  # Adicione o tipo de vetor ao título
            plt.xlabel('Tamanho do Vetor')
            plt.ylabel('Tempo Médio (s)')
            plt.legend()
            plt.grid()
            plt.show()

