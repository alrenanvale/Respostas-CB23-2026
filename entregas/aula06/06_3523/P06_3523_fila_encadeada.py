from P06_3523_pilha_encadeada import PilhaEncadeda, Element

class FilaEncadeada:
    """
    A classe FilaEncadeada ira usar duas pilhas encadeadas, de modo que ela possa
    funcionar como um estrutura de dados do tipo FIFO (First In First Out). A idea é que podemos
    adicionar elementos em uma das pilhas, a chamada Head. Se quisermos obter os elementos na ordem
    em que eles foram adicionados, como um FIFO, devemos despejar esses elementos em uma outra
    pilha, de modo que o topo dessa pilha agora seja o primeiro elemento que adicionamos na pilha Head. Chamaremos
    essa segunda pilha de Tail.
    """
    def __init__(self):
        self._head = PilhaEncadeda()
        self._tail = PilhaEncadeda()
        self._size = 0

    def enfileirar(self, data):
        """
        Adicionamos um novo elemento a pilha Head. Possui complexidade O(1)
        
        Args:
            data(Any): é a informação que será adicionada na pilha
        """
        self._head.push(data)
        self._size += 1

    def desenfileirar(self):
        """
        Retira o elemento da frente, o mais "velho" da pilha. Retorna o valor desse elemento. Possui complexidade O(1) amortizada.

        returns:
            Retorna o dado contido no elemento da frente que foi removido. 
        """
        if self._size == 0:
            raise IndexError("Fila vazia")
        if self._tail.esta_vazia(): # Verifica se a tail está vazia
            while self._head.esta_vazia() is False:
                dado = self._head.pop()
                self._tail.push(dado)
        self._size -= 1
        return self._tail.pop()

    def frente(self):
        """
        Retorna o elemento da frente sem o remover. Possui complexidade O(1) amortizada.
        
        returns:
            Retorna o dado contido no elemento da frente.
        """
        if self._size == 0:
            raise IndexError("Fila vazia")
        if self._tail.esta_vazia(): # Verifica se a tail está vazia
            while self._head.esta_vazia() is False:
                dado = self._head.pop()
                self._tail.push(dado)
        return self._tail.topo()

    def esta_vazia(self):
        """
        Avalia se a fila está vazia ou não. Possui complexidade O(1).

        return:
            True or False, se a fila estiver vazia ou não, respectivamente.
        """
        return self._size == 0

    def __len__(self):
        """
        Fornece o tamanho da fila. Possui complexidade O(1)

        returns:
            Retorna o tamanho da fila.
        """
        return self._size
    
    def __repr__(self):
        """
        Representação visual da fila. Possui complexidade O(n)

        returns:
            Retorna uma representação visual da fila
        """
        if self._size == 0:
            return "Fila vazia"

        # Estou pegando o topo de tail, e esse é o primeiro que deve ser colocado para fora,
        # devo percorrer tail até o final e depois percorrer head até o final, na ordem contrária.
        
        temp_tail = PilhaEncadeda()
        str_tail = ""
        while self._tail.esta_vazia() is False:
            dado = self._tail.pop()
            str_tail += f"{dado} --> "
            temp_tail.push(dado)

        while temp_tail.esta_vazia() is False:
            self._tail.push(temp_tail.pop())

        temp_head = PilhaEncadeda()
        str_head = ""
        while self._head.esta_vazia() is False:
            dado = self._head.pop()
            str_head = f"{dado} --> " + str_head
            temp_head.push(dado)

        while temp_head.esta_vazia() is False:
            self._head.push(temp_head.pop())

        return f"Head --> {str_tail} {str_head}Tail"