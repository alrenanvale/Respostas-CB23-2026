# Amortização na Fila

No pior caso poderiamos ter que precisariamos de revirar toda a pilha Head para a piilha Tail, ou seja, a pilha Tail, que por definição já guarda a ordem dos termos pela altura (o elemento mais alto é o primeiro que foi adicionado nessa estrutura de dados e será o primeiro que serpa retirado da pilha Tail, respeitando a FIFO) está vazia. Se ela está vazia, temos de percorrer todos os **N** elementos da pilha Head para que assim chegemos no seu termo mais profundo, que foi o primeiro adicionado. A complexidade para isso é N.

Mas uma vez feito esse processo, veja que para as próximas vezes não é necessário refaze-lo, pois os elementos já foram reorganizados na ordem correta na pilha Tail, de modo que apenas usando tail.pop() já obtemos o primeiro elemento que foi adicionado nessa arquitetura de dados. Ou seja, a complexidade para isso é O(1).

Entendemos então que usando-se pop() uma vez, o custo não se perde apenas para essa utilização em específico, mas se reaproveita para as proximas vezes em que este método for utilizado, já que Tail está organizada de modo favorável a isso.

Da mesma forma ocorre para .frente(), afinal a única diferença entre este método e o .pop() é que o último remove o item da fila.