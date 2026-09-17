import random
import AP_03_ordenacao as ap3
import sys
import time

# Limita o número de recursões
sys.setrecursionlimit(10**6)

# Retorna uma lista aletória com os números de 1 a N
def avg_case(N):
    """
    Cria o caso medio para o Quick Sort, o que acaba como servir
    como caso medio para os outros métodos tambem.

    Cria uma lista de números de 1 a N e embaralha os elementos aleatoriamente,
    usando a biblioteca random. A função retorna a lista embaralhada, o caso medio.

    Args:
        N (int): O tamanho da lista a ser criada.

    Returns:
        my_list (list): A lista embaralhada de números de 1 a N.
    """

    # Criação de uma lista com númeoros de 1 a N usando list comprehession
    original = [x for x in range(N)]
    my_list = []

    # Usa o fato de quando uma lista fica vazia se compportar como valor de False quando possui 0 elementos
    while len(original):
        random_index = random.randint(0,len(original) - 1) # Pega um indice aleatório da lista que criamos
        my_list.append(original[random_index]) # Adiciona o elemento aletório que acabei de pegar na lista vazia
        original[random_index], original[-1] = original[-1], original[random_index] # Inverte o último termo com o termo que acabei de adicionar em my_list, para que ele seja excluido
        original.pop()
    return my_list # Retorna a lista com números aletórios

def gera_worst_case_quick(N):
    """
    A função gera uma lista de números de 0 a N-1 em ordem decrescente
    por list comprehension.

    Args:
        N (int): O tamanho da lista a ser criada.

    Returns:
        list: A lista de números de 0 a N-1 em ordem decrescente.
    """
    return [x for x in range(N)][::-1]

def perfomance(metodo, N, k, worst_case = None):
    """
    Função que mede o tempo de execução de cada método de ordenação.

    A função analisa de qualquer um dos três métodos a serem testados, mas
    possui opção de gerar o pior caso para o Quick Sort.

    Args:
        metodo (function): O método de ordenação a ser testado.
        N (int): O tamanho das listas a serem ordenadas.
        k (int): O número de listas a serem testadas.
        worst_case (function, optional): Função que gera o pior caso
            para o Quick Sort. Se não for passado, o caso médio é que será testado.

    Returns:
        sum(times)/k (float): média dos tempos para um método
    """
    # Lista criada para armazenar os tempos
    times = []
    # N é o tamanho da lista que será testada
    # K é o número de vezes que o método de sorteamento será testado
    for _ in range(k):
        # Avalia se foi passado o parâmetro para gerar o pior caso ou não, e com base nisso gera a lista média ou do pior caso
        if worst_case:
            my_list = worst_case(N)
        else:
            my_list = avg_case(N)
        start_t = time.perf_counter()
        # Aplica a função escolhida para a avaliação
        metodo(my_list)
        end_t = time.perf_counter()
        # Adiciona o tempo para fazer a média
        times.append(end_t - start_t) 
    return sum(times)/k

def executar_benchmark(métodos, listas_tam, k):
    """
    A função executar_benchmark engloba duas funções: a função armazena_dados
    e a função tabela_aut. As duas funções trabalham juntas para gerar os dados
    de tempo e a tabela.

    Independente s

    Args:
        metodos(list): lista de tuplas contendo os métodos a serem testados
            seu nome nas colunas da tabela e se possuem worst_case ou não.
        listas_tam(list): lista que contem inteiros que definem o tamanho das
            que serão testadas.
        k(int): número de vezes que uma lista de tamanho N será testada. Aumenta a
            precisão do valor do tempo médio quando k aumenta.

    Return:
        A tabela formatada mostrando os valores de tempo médio para cada tamanho de lista e método.
    """

    def armazenar_dados(métodos, listas_tam, k):
        """
        A função deve armazenar os dados de todos os tipos de métodos
        de ordenação tidos como parâmetros dentro das tuplas em metodos.

        A organização da lista metodos faz com que sempre o primeiro item da tupla
        seja o método a ser testado.

        Args:
            Recebe os mesmos parâmetros da função executar_benchmark
        """

        for metodo, coluna, caso in métodos:
            dados[coluna] = [] #criação da coluna na tabela de benchmark
            for j in listas_tam:
                tempo = perfomance(metodo, j, k, caso)
                dados[coluna].append(tempo)

    def tabela_aut ():
        """
        A função deve receber os diferentes tipos de ordenação e os
        diferentes tamanhos de listas e gerar uma tabela de benchmark.
        """

        print()
        for i in range(len(met)):
            if i == 0:
                print(f"|{'Tamanho': ^10}|", end="")
            print(f"{met[i][1]: ^30}|", end="")

        print()
        print("|" +10*"-" + "|" + f"{len(met) * '------------------------------|'}", end="")

        for j in range(len(listas_tam)):
            for i in range(len(met)):
                if i == 0:
                    print(f"\n|{'N = ' + str(listas_tam[j]): ^10}|", end="")

                print(f"{dados[met[i][1]][j]: ^30}|", end="")
        print()

    armazenar_dados(met, listas_tam, k)
    tabela_aut()

# --------------- Dados para gera a tabela pedida com o worst case de Quick Sort ------------------

# tam_listas: tamanhos de lista. Por exemplo, em tam_listas temos listas de tamanho 750 e 5000 por exemplo.
# dados: dicionário com os dados de tempo relacionados com cada um dos métodos. O dicionŕio armazena todos os dados.
# met: lista com os métodos e outras atribuições.

tam_listas = [750, 1000, 2500, 5000, 10000]
dados = {}
met = [
    (ap3.quick_sort, "Quick Sort (Caso Médio)", None),
    (ap3.quick_sort, "Quick Sort (Pior Caso)", gera_worst_case_quick),
    (ap3.divide_and_conquer_sort, "Divide and Conquer", None),
    (ap3.selection_sort, "Selection Sort", None)
]

# Chamando a função
executar_benchmark(met, tam_listas, 100)

