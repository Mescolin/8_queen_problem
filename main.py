#Genótipo : |1|3|5|2|6|4|7|8|
#Penalidade de uma rainha: o número de rainhas que ela pode verificar
#Penalidade de uma configuração: a soma das penalidades de todas as rainhas
#Observação: a penalidade deve ser minimizada
#Aptidão de uma configuração: a penalidade inversa deve ser maximizada
#Resolução do Algoritmo Genético para o problema das 8 rainhas
import random
import numpy as np

# Parâmetros do Algoritmo Genético
POPULATION_SIZE = 100
MUTATION_RATE = 0.1
GENERATIONS = 1000
BOARD_SIZE = 8
TARGET_FITNESS = 1.0
TOURNAMENT_SIZE = 5
ELITISM_COUNT = 2
RANDOM_SEED = 42
random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)

# Função para calcular a penalidade de uma configuração
def calculate_penalty(configuration):
    penalty = 0
    for i in range(len(configuration)):
        for j in range(i + 1, len(configuration)):
            if configuration[i] == configuration[j] or abs(configuration[i] - configuration[j]) == abs(i - j):
                penalty += 1
    return penalty

# Função para calcular a aptidão de uma configuração
def calculate_fitness(configuration):
    penalty = calculate_penalty(configuration)
    return 1 / (1 + penalty)

# Função para criar uma configuração aleatória
def create_configuration():
    configuration = list(range(1, BOARD_SIZE + 1))
    random.shuffle(configuration)
    return configuration

# Função para criar a população inicial
def create_initial_population():
    return [create_configuration() for _ in range(POPULATION_SIZE)]
