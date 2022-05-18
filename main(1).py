from ab import No, Arvore

no = No(valor=5)
assert no.filho_esquerda is None
assert no.filho_direita is None
assert no.tem_filho_esquerda() == False
assert no.tem_filho_direita() == False

no.add_esquerda(9)
assert no.filho_esquerda is not None
assert no.tem_filho_esquerda()

no.filho_esquerda.add_esquerda(11)
# print(no.filho_esquerda.valor)
# print(no.filho_esquerda.filho_esquerda.valor)

no.filho_esquerda.add_direita(12)
# print(no.filho_esquerda.filho_direita.valor)

# no.filho_esquerda.add_direita(15)

arvore = Arvore()
assert arvore.raiz is None
arvore.add(5)
assert arvore.raiz is not None
assert arvore.raiz.filho_esquerda is None

arvore.add(7)

assert arvore.raiz.filho_esquerda is None
assert arvore.raiz.filho_direita is not None
assert arvore.raiz.filho_direita.valor == 7

arvore.add(9)
arvore.add(3)
arvore.add(6)

assert arvore.raiz.filho_direita.filho_direita.valor == 9
assert arvore.raiz.filho_esquerda.valor == 3
assert arvore.raiz.filho_direita.filho_esquerda.valor == 6

arvore = Arvore()
arvore.add('A')

arvore.raiz.add_esquerda('B')
arvore.raiz.filho_esquerda.add_esquerda('D')
arvore.raiz.filho_esquerda.add_direita('E')

arvore.raiz.add_direita('C')
arvore.raiz.filho_direita.add_esquerda('F')
arvore.raiz.filho_direita.add_direita('G')

assert arvore.altura() == 2
assert arvore.count() == 7
assert arvore.leafs() == 4
assert arvore.busca('A') is True
assert arvore.busca('Z') is False
assert arvore.busca('G') is True


arvore = Arvore()
arvore.add(1)
assert arvore.altura() == 0
assert arvore.count() == 1
assert arvore.leafs() == 1


arvore = Arvore()
arvore.add(5)
arvore.add(3)
arvore.add(2)
arvore.add(4)

arvore.add(7)
arvore.add(6)
arvore.add(8)

assert arvore.count() == 7
assert arvore.no_menor_valor(arvore.raiz).valor == 2
assert arvore.no_menor_valor(arvore.raiz.filho_direita).valor == 6
arvore.remover(8)
assert arvore.count() == 6
arvore.remover(6)
assert arvore.count() == 5
arvore.remover(3)
assert arvore.count() == 4
arvore.remover(4)
assert arvore.count() == 3
arvore.remover(5)
assert arvore.count() == 2
assert arvore.raiz.valor == 7
arvore.remover(7)
arvore.remover(2)
assert arvore.count() == 0