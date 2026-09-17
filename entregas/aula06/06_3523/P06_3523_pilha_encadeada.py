class Element:
    """
    A class Element equivale ai Node da pista encadeada, na
    pilha encadeada ela representa cada um dos dados, cada um
    ocupando uma camada da pilha.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class PilhaEncadeda:
    """
    Com a mesma ideia da lista encadeada, a pilha encadeada é uma estrutura de dados
    que armazena os dados por referência e não em uma unidade fixa de memória.
    """
    def __init__(self):
        self._topo = None # Funciona como se fosse a head da lista encadeada
        self._size = 0

    def push(self, data):
        """
        Adiciona um novo elemento no topo da pilha.

        args:
            data(Any): O dado que será adicionado a pilha.
        """
        new_element = Element(data)
        new_element.next = self._topo
        self._topo = new_element
        self._size += 1

    def pop(self):
        """
        Remove e retorna o elemento do topo da pilha.

        returns:
            O dado que estava no topo da pilha.
        """
        if self._topo is None:
            raise IndexError("Pilha vazia")
        data = self._topo.data # Salvando o valor para emitir no pop
        self._topo = self._topo.next
        self._size -= 1
        return data

    def topo(self):
        """
        Retorna o elemento do topo da pilha sem o remover.
        
        returns:
            O dado que está no topo da pilha.
        """
        if self._topo is None:
            raise IndexError("Pilha vazia")
        return self._topo.data

    def esta_vazia(self):
        """
        Verifica se a pilha está vazia.
        
        returns:
            True ou Fale, para pilha vazia ou não, respectivamente.
        """
        return self._topo is None # Se a lista estiver vazia, retorna True, se contiver elementos, retorna False.

    def __len__(self):
        """
        Retorna o número de elementos da pilha.

        returns:
            O número de elementos.
        """
        return self._size

    def __repr__(self):
        """
        Retorna uma representação visual da pilha
        
        returns:
            Representação visual
        """
        if self._topo is None:
            return "Pilha vazia"

        pilha_visu = "Topo --> "
        actual = self._topo

        while actual:
            pilha_visu += f"{actual.data} --> "
            actual = actual.next
        return pilha_visu + "None"