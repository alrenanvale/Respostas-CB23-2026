
# 1 - Identifique relações de herança entre as classes.
## Identificando a organização geral
A partir do diagrama podemos definifir que há três superclasses absolutas: Pessoa, Restaurante e
Iguaria. Além dessas, como uma superclasse relativa, temos Funcionário, que é subclasse de Pessoa.
Tratando das classes restantes temos que Chefe de Cozinha, Gerente e Garçom são subclasses de
Funcionário; Pizzaria é uma subclasse de Restaurante e Pizza e Bolo são subclasses de Iguaria.
A partir dessa análise, podemos montar o esquema hieráquico:

- Pessoa
    - Funcionário
        - Chefe de cozinha
        - Gerente
        - Garçom
- Restaurante
    - Pizzaria
- Iguaria
    - Pizza
    - Bolo  

## Analisando as superclasses e subclasses
### Sobre as relações da classe restaurante e suas subclasses
A superclasse restaurante possui três atributos que são o seu nome, endereço e telefone, que são todos do tipo string. Essa classe possui apenas uma subclasse que é Pizzaria. Eu acabei por implementar, como atributo da classe Restaurante, uma classe nova ao diagrama. Essa é a chamada ItensCardapio, que organiza o cardápio de uma instância do restaurante. Um código que exemplifica o funcionamento dessa classe está abaixo, onde será falado sobre cada classe:
- Pizzaria: a subclasse Pizzaria define um tipo específico de restaurante, que são as pizzarias, e que possuem a caractrística de terem ou não rodizio, atributo que pode receber um valor booleano (True ou False).
- ItensCardapio: essa subclasse implementada cria instâncias de cardápios, onde o cardápio do restaurante é armazenado em um dicionário, de modo que a **Key** do dicionário é o nome de uma instância da classe Iguaria (usando o atributo **nome** definido na Classe Iguaria) e oque ela armazena é a instância que foi referida na Key, mas completa . Essa classe possui um método que adiciona itens (comida) ao cardápio também. A seguir há um exemplo do código para ela.
```python
class ItensCardapio:
	def __init__(self):
		self.comidas = {}
		
	def adicionar_comida(self, iguaria):
		self.comidas[iguaria.nome] = iguaria
```
### Sobre as relações da classe Iguaria e suas subclasses
A superclasse Iguaria é a classe mãe que define atributos universais de todas as comidas vendidas no resturante, como o seu nome, uma string, e seu preço, um float. As suas subclasses são duas, Bolo e Pizza, que são dois tipos mais específico de Iguaria que possuem características próprias e exclusivas: em relação ao bolo, apenas uma pizza pode ter a borda recheada, por exemplo.
Ja as suas subclasses estão abaixo:
- Bolo: essa Iguaria possui um atributo chamado formato, uma string que dita o formato do bolo.
- Pizza: já essa outra Iguaria possui um atributo que define se sua borda é recheada ou não, de modo que seu valor deve ser um bool (True ou False).

### **Sobre as relações da classe Pessoa e suas subclasses**
A superclasse Pessoa é a classe da qual todas as outras classes relacionadas com indivíduos do diagrama herdam atributos universais, como nome, uma string, e idade, um inteiro. Funcionário é a subclasse direta da classe Pessoa e introduz dois novos atributos: salario, um float, e carga_horaria, um inteiro. Estes atributos são comuns a todos os funcionários do nosso contexto de restaurantes, mas não são algo essencial a descrição de uma pessoa.
A relação da classe Funcionário (subclasse de Pessoa mas superclasse das classes Garçom, Gerente, e Chefe de Cozinha, tudo depende do referencial) com suas subclasses se dá pelo uso destas dos atrtibutos salario e carga_horaria definidos anteriormente.
Finalmente, a estrutura de cada uma das subclasses que definem um funcionário propriamente dito é dada a seguir:
- Garçom: essa classe possue o método **anotar_pedido** que recebe uma lista de instâncias de Iguaria.
- Gerente: a classe gerente conta com o método demitir, que recebe uma instância da classe funcionário. 
- Chefe de Cozinha: por fim, o chefe de cozinha recebe em seu método, preparar, uma instância da classe Iguaria.

## 2 - Como você modelaria a relação entre a classe Restaurante e a classe Iguaria?
As classes Restaurante e Iguaria, no meu diagrama, foram conectadas por uma classe de suporte, a ItensCardapio. Essa classe é atributo da classe Restaurante e armazena as instâncias da classe Iguaria que pertencem aquele restaurante. Ela cria um dicionário, que usa o nome da iguaria como identificador, e guarda a classe inteira como valor para esse identificador.

## 3 - Indique os tipos que você atribuiria para os argumentos: argumento1, argumento2, argumento3.
- Argumento 1: o garçom deve anotar um pedido, que pode ser apenas uma comida ou uma lista delas. Deste modo optei por atribuir no lugar de argumento1 uma lista de instâncias de Iguaria.
- Argumento 2: para o argumento 2, defini que o deve ser recebido uma instância de Iguaria
- Argumento 3: por fim, o método 'demitir' deve receber instâncias da classe Funcionário.

# 4 - Diagrama
O novo diagrama representando as modificações que fiz está na imagem a abaixo. ![[05_3523_diagrama.png]]

Renderizar o arquivo de código mandado no drawio provavelmente irá destruir a formatação, mas na ferramenta do Visual Paradigm para transformar código para diagrama, a formatação é conservada. 
