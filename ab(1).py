# http://10.0.61.81:9000

class NoException(Exception):
    pass

class PosicaoNaoVazia(NoException):
    pass

class ArvoreVaziaException(Exception):
    pass

class No:

    def __init__(self, valor):
        self.valor = valor
        self.filho_esquerda = None
        self.filho_direita = None

    def __str__(self):
        return f'No(valor={self.valor})'

    def add_esquerda(self, valor):
        if self.tem_filho_esquerda():
            raise PosicaoNaoVazia()

        self.filho_esquerda = No(valor)       

    def add_direita(self, valor):
        if self.tem_filho_direita():
            raise PosicaoNaoVazia()
        
        self.filho_direita = No(valor)
            
    def tem_filho_esquerda(self):
        return self.filho_esquerda is not None

    def tem_filho_direita(self):
        return self.filho_direita is not None
    
    def eh_folha(self) -> bool:
        return (not self.tem_filho_direita()) and (not self.tem_filho_esquerda())


class Arvore:

    def __init__(self):
        self.raiz : No = None

    def esta_vazia(self):
        return self.raiz is None

    def obter_raiz(self):
        return self.raiz

    def add(self, valor):
        self.raiz = self._add(self.raiz, valor)
    
    def _add(self, no: No, valor: int):
        if no is None:
            return No(valor)

        if valor > no.valor:
            no.filho_direita = self._add(no.filho_direita, valor)
        else:
            no.filho_esquerda = self._add(no.filho_esquerda, valor)
        
        return no

    def percorrer(self):
        self.percorrer_pos_ordem(self.raiz)
        print()

    def percorrer_pre_ordem(self, no: No):
        if no is None:
            return 

        print(no.valor, end=' ')
        self.percorrer_pre_ordem(no.filho_esquerda)
        self.percorrer_pre_ordem(no.filho_direita)

    def percorrer_em_ordem(self, no : No):
        if no is None:
            return
        
        self.percorrer_em_ordem(no.filho_esquerda)
        print(no.valor, end=' ')
        self.percorrer_em_ordem(no.filho_direita)

    def percorrer_pos_ordem(self, no: No):
        if no is None:
            return

        self.percorrer_pos_ordem(no.filho_esquerda)
        self.percorrer_pos_ordem(no.filho_direita)
        print(no.valor, end=' ')


    def altura(self) -> int:
        return self._altura(self.raiz)

    def _altura(self, no: No) -> int:
        if no.eh_folha():
            return 0

        return max(
            self._altura(no.filho_esquerda),
            self._altura(no.filho_direita)
        ) + 1

    def count(self) -> int:
        return self._count(self.raiz)

    def _count(self, no : No) -> int:
        if no is None:
            return 0

        return 1 +\
             self._count(no.filho_esquerda) +\
             self._count(no.filho_direita)

    def leafs(self):
        return self._leafs(self.raiz)

    def _leafs(self, no: No) -> int:
        if no is None:
            return 0

        if no.eh_folha():
            return 1

        return self._leafs(no.filho_esquerda) +\
             self._leafs(no.filho_direita)

    def busca(self, valor: int) -> bool:
        return self._busca(self.raiz, valor)

    def _busca(self, no: No, valor: int) -> bool:
        if no is None:
            return False
        if no.valor == valor:
            return True
        elif valor < no.valor:
            return self._busca(
                no.filho_esquerda, valor)
        else:
            return self._busca(
                no.filho_direita, valor)

    def no_menor_valor(self, no: No):
        atual = no
        while atual.filho_esquerda is not None:
            atual = atual.filho_esquerda
        return atual
            
    def remover(self, valor: int) -> bool:
        self.raiz = self._remover(self.raiz, valor)

    def _remover(self, no: No, valor: int):
        if no is None:
            return no

        if valor > no.valor:
            no.filho_direita = self._remover(no.filho_direita, valor)
        elif valor < no.valor:
            no.filho_esquerda = self._remover(no.filho_esquerda, valor)
        else:
            if no.filho_esquerda is None:
                return no.filho_direita
            elif no.filho_direita is None:
                return no.filho_esquerda
            else:
                substituto = self.no_menor_valor(no.filho_direita)
                no.valor = substituto.valor
                no.filho_direita = self._remover(
                    no.filho_direita,
                    no.valor
                )
        return no
                


        






    


    


        

    