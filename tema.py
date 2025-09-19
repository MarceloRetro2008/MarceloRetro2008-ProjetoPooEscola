 
def escola():
    esc=input
nome = input("qual é o seu nome: ")
turma = input("qual é a sua turma: ")
CPF = input("qual é o seu CPf: ")
idade = int(input("digite a sua idade: "))
nota = int(input("digite a sua nota da prova: "))

def menu():
   
 print("\n----------FICHA DO ALUNO----------")

print ("seu nome é", nome)
print ("sua turma é de", turma)
print ("seu CPF é:", CPF)
print ("sua idade é:", idade)
print ("sua nota é:", nota)

if idade < 18:
  print("voce é maior de idade")
else:
  print("voce é menor de idade") 

if nota <=7:
  print("voce não passou de ano")
else:
  print("voce passou de ano")

print("\n----------------------------------")
def media():
  nsd = input
n1 = int(input("digite a sua primeira nota da prova: "))
n2 = int(input("digite a sua segunda nota da prova: "))
n3 = int(input("digite a sua terceira nota da prova: "))
n4 = int(input("digite a sua quarta nota da prova: "))
mt =(n1 + n2 +n3+ n4)/4
print("sua media é de exatamente de", mt)

media()

escola()
print("\n----------AVALIAÇÃO ESCOLAR----------")
def avaliaçao():
    no1 = int(input("o que vc acha da comida escolar ? "))
    no2 = int(input("o que vc acha da coordenacão da escola ? "))
    no3 = int(input("o que vc acha da sala da escola ? "))
    no4 = int(input("o que vc acha organização da escola ? "))
    no5 = int(input("o que vc acha da educação escolar ? "))
    mp =(no1 + no2 +no3 + no4 + no5)/5
    print("sua media sobre a nossa escola", mp)
print("\n--------------------------------------")
avaliaçao()
print("\n----------BIBLIOTECA----------")
def biblioteca():

 
   ksk = input
livros = int(input("quantos livros o senhor pegou emprestado ? "))
dias = int(input("quantos dias o senhor devolve os livros ?"))
if livros == 0:
   print("vc ainda não utilizou a biblioteca.")
else:
    print("vc já leu bastante livros nessa semana.")

if dias <= 7:
   print("vc devolve os livros dentro do prazo")
else:
   print("tente devolver os livros no prazo")
   print("\n--------------------------------------")    
   print("\n----------CANTINA----------")
def cantina():
  lam = input
lanche = input("qual é o seu alimento favorito ?")
print("seu alimento favorito é", lanche)


cantina()
print("\n--------------------------------------")

print("----------BANHEIRO----------")
cap = 4
pessoas = 0

def entrar():
   global pessoas 
if pessoas < cap:
      pessoas += 1
      print(f"Entrou total: ", pessoas)
else:
   print("lotado! Espere")

def sair():
   global pessoas 
if pessoas < 0:
      pessoas -= 1
      print(f"saiu total: ", pessoas)
else:
   print("ninguém para sair! Espere até alguém sair do banheiro para entrar")

   print("\n--------------------------------------")

entrar()
entrar()
entrar()
sair()
entrar()
entrar()
entrar()