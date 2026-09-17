import unittest
from P06_3523_pilha_encadeada import PilhaEncadeda
from P06_3523_fila_encadeada import FilaEncadeada

class TestPilhaEncadeada(unittest.TestCase):
    
    def test_ordem_lifo(self):
        """
        Testa se a ordem LIFO.
        """
        pilha = PilhaEncadeda()
        pilha.push(10)
        pilha.push(20)
        pilha.push(30)
        self.assertEqual(pilha.pop(), 30) 
        self.assertEqual(pilha.pop(), 20)
        self.assertEqual(pilha.pop(), 10)

    def test_erro_pilha_vazia(self):
        """
        Testa se levanta IndexError ao dar pop e topo em pilha vazia.
        """
        pilha = PilhaEncadeda()
        with self.assertRaises(IndexError):
            pilha.pop()
        with self.assertRaises(IndexError):
            pilha.topo()

    def test_coerencia_len(self):
        """
        Testa o len após inserções e remoções.
        """
        pilha = PilhaEncadeda()
        self.assertEqual(len(pilha), 0)
        pilha.push("A")
        pilha.push("B")
        self.assertEqual(len(pilha), 2)
        pilha.pop()
        self.assertEqual(len(pilha), 1)
        pilha.pop()
        self.assertEqual(len(pilha), 0)

    def test_alternancia_operacoes(self):
        """
        Testa o comportamento alternando push e pop.
        """
        pilha = PilhaEncadeda()
        pilha.push(1)
        self.assertEqual(pilha.pop(), 1)
        pilha.push(2)
        pilha.push(3)
        self.assertEqual(pilha.pop(), 3)
        pilha.push(4)
        self.assertEqual(pilha.pop(), 4)
        self.assertEqual(pilha.pop(), 2)
        self.assertTrue(pilha.esta_vazia())

    def test_tipos_diferentes(self):
        """
        Testa o armazenamento de itens de tipos diferentes
        """
        pilha = PilhaEncadeda()
        pilha.push(100)
        pilha.push(100)
        pilha.push("Texto")
        pilha.push(3.14)         
        pilha.push(None)

        self.assertIsNone(pilha.pop())
        self.assertEqual(pilha.pop(), 3.14)
        self.assertEqual(pilha.pop(), "Texto")
        self.assertEqual(pilha.pop(), 100)
        self.assertEqual(pilha.pop(), 100)


class TestFilaEncadeada(unittest.TestCase):

    def test_ordem_fifo(self):
        """
        Testa a ordem FIFO.
        """
        fila = FilaEncadeada()
        fila.enfileirar("A")
        fila.enfileirar("B")
        fila.enfileirar("C")
 
        self.assertEqual(fila.desenfileirar(), "A")
        self.assertEqual(len(fila), 2)
        self.assertEqual(fila.desenfileirar(), "B")
        self.assertEqual(fila.desenfileirar(), "C")

    def test_intercalacao_operacoes(self):
        """
        Testa intercalação de enfileirar e desenfileirar.
        """
        fila = FilaEncadeada()
        fila.enfileirar(1)
        self.assertEqual(fila.desenfileirar(), 1) 
        fila.enfileirar(2)
        fila.enfileirar(3)
        self.assertEqual(fila.desenfileirar(), 2)
        fila.enfileirar(4)
        self.assertEqual(fila.desenfileirar(), 3)
        self.assertEqual(fila.desenfileirar(), 4)

    def test_esvaziar_e_reusar(self):
        """
        Testa esvaziar a fila e voltar a usar a mesma instância.
        """
        fila = FilaEncadeada()
        fila.enfileirar(10)
        fila.enfileirar(20)
        fila.desenfileirar()
        fila.desenfileirar()
        
        self.assertTrue(fila.esta_vazia())
        
        fila.enfileirar(30)
        self.assertEqual(len(fila), 1)
        self.assertEqual(fila.frente(), 30)
        self.assertEqual(fila.desenfileirar(), 30)

    def test_erro_fila_vazia(self):
        """
        Testa se levanta IndexError ao chamar desenfileirar e frente em fila vazia.
        """
        fila = FilaEncadeada()
        with self.assertRaises(IndexError):
            fila.desenfileirar()
        with self.assertRaises(IndexError):
            fila.frente()

    def test_len(self):
        """
        Testa o len
        """
        fila = FilaEncadeada()
        self.assertEqual(len(fila), 0)
        fila.enfileirar(1)
        fila.enfileirar(2)
        self.assertEqual(len(fila), 2)
        fila.desenfileirar()
        self.assertEqual(len(fila), 1)
        fila.desenfileirar()
        self.assertEqual(len(fila), 0)

if __name__ == '__main__':
    unittest.main()