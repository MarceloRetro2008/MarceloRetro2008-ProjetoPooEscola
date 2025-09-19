from turtle import goto


class animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print("som do animal")

class cachorro(animal):
    def falar(self):
        print("au au au")

class Gato(animal):
      def falar(self):
       return print("miau miau")
  

dog = cachorro("rex")
cat = Gato("serena")

dog.falar()
cat.falar()


  git config --global user.email "bommergouveia@gmail.com"
  git config --global user.name "MarceloRetro2008"