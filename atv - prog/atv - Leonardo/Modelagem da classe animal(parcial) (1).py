class Animal:

   def __init__(self, nome, idade, especie, peso, altura):
       self.nome = nome
       self.idade = idade
       self.especie = especie
       self.peso = peso
       self.altura = altura
       self.dormindo = False
       self.comendo = False
       self.caminhando = False

  def dormir(self):
      if self.falando:
          print(f'{self.nome} não pode falar, pois está dormindo.')
      if self.comendo:
          print(f'{self.nome} não pode comer, pois está dormindo.')
      if self.caminhando:
       print(f'{self.nome} não pode caminhar, pois está dormindo.')
       if self.correndo:
       print(f'{self.nome} não pode correr, pois está dormindo.')
      print(f'{self.nome} está dormindo.')
      self.dormindo = True