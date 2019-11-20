class Aluno:
    def __init__(self,matr,nome,n1,n2,n3):
        self.mat=matr
        self.nom=nome
        self.n1=n1
        self.n2=n2
        self.n3=n3
    def get_nome(self):
        return str(self.nome)
    def get_matr(self):
        return self.matr
    def media(self):
        self.med=((self.n1+self.n2+self.n3)/3)
        return med
    def set_nome(self,novo_nome):
        self.nome = novo_nome
matr1=int(input('DIGITE SUA MATRÍCULA:'))
nome1=input('DIGITE SEU NOME:')
nota1=int(input('DIGITE A PRIMEIRA NOTA:'))
nota2=int(input('DIGITE A SEGUNDA NOTA:'))
nota3=int(input('DIGITE A TERCEIRA NOTA:'))
boletim=Aluno(matr1,nome1,nota1,nota2,nota3)
print('------------------------------------------------')
print('MATRÍCULA:',boletim.mat,'\n','NOME:',boletim.nom,'\n','NOTA1:',boletim.n1,'\n','NOTA2:',boletim.n2,'\n','NOTA3:',boletim.n3)