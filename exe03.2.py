class Aluno:
    def __init__(self,matr,nome,notas=[]):
        self._matr=matr
        self._nome=nome
        self._notas=notas
    def get__nome(self):
        return self._nome
    def get__matr(self):
        return str(self._matr)
    def set__nome(self,novo_nome):
        self._nome=novo_nome
    def adiciona_nota(self,nota):
        self._notas.append(nota)
    def _media(self):
        return (sum(self._notas)/len(self._notas))
aluno1=Aluno(20191370014,'Lucas',[8,8])
aluno1.adiciona_nota(5)
print('Matrícula:',aluno1.get__matr(),'\n','Nome:',aluno1._nome,'\n','Notas:',aluno1._notas)
print('Média:',aluno1._media())