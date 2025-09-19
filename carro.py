def carro():
    carr0 = input
modelo = input("qual o modelo: ")
cor = input("qual a cor: ")
ano = input(int("qual ano: "))

print("o modelo é: ", modelo)
print("a cor é: ", cor)
print("minha idade é: ",ano)

if ano < 2000:
  print("antigo")
else:
  print("novo") 
  carro()