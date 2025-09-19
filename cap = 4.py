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
   print("ninguém para sair! Espere")

   print("\n--------------------------------------")

entrar()
entrar()
entrar()
sair()
entrar()