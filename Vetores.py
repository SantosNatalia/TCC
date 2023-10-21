import random
import numpy as np


class Vetores:
    # Dicionário para armazenar vetores desordenados
    vetores_desordenados = {}

    @staticmethod
    def gerar_vetor_desordenado(tamanho, tipo):
        chave = (tamanho, tipo) # Cria uma chave para identificar o vetor com base no tamanho e tipo

        if chave in Vetores.vetores_desordenados: # Verifica se o vetor já foi gerado e armazenado
            return Vetores.vetores_desordenados[chave] #Se sim, retorna o vetor previamente gerado

        if tipo == "aleatorio": # Gera um vetor de números aleatórios com distribuição normal, limitando entre 0 e 1.000.000
            vetor_desordenado = [random.randint(0, 1000000) for _ in range(tamanho)]
        elif tipo == "normal": # Gera um vetor de números aleatórios com distribuição normal, limitando entre 0 e 1.000.000
            vetor_desordenado = np.random.normal(0, 1, tamanho)
            vetor_desordenado = [max(0, min(int(x), 1000000)) for x in vetor_desordenado]
        elif tipo == "poisson": # Gera um vetor de números aleatórios com distribuição normal, limitando entre 0 e 1.000.000
            vetor_desordenado = np.random.poisson(1, tamanho)
            vetor_desordenado = [max(0, min(int(x), 1000000)) for x in vetor_desordenado]
        elif tipo == "exponencial_negativa": # Gera um vetor de números aleatórios com distribuição normal, limitando entre 0 e 1.000.000
            vetor_desordenado = np.random.exponential(1, tamanho)
            vetor_desordenado = [max(0, min(int(x), 1000000)) for x in vetor_desordenado]

        Vetores.vetores_desordenados[chave] = vetor_desordenado # Armazena o vetor gerado no dicionário para reutilização
        return vetor_desordenado # Retorna o vetor gerado





