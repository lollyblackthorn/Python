# -*- coding: utf-8 -*-
"""Exercicio_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ivZshpSN2k8sL-6UQl4qnT3VVj1qEUKm
"""

#1. Faça um programa que peça um valor monetário e diminua-o em 15%. Seu programa deve imprimir a mensagem “O novo valor é [valor]”.

valor = input("Informe o valor: ")
valor = float(valor)

valor = valor-(15/100)
print("O novo valor é: ",valor)
#--------------------------------------------------------------------------------------------------------------------------------------------------
#2. Faça um programa que leia a validade das informações:
#a. Idade: entre 0 e 150;
#b. Salário: maior que 0;
#c. Sexo: M, F ou Outro;
#O programa deve imprimir uma mensagem de erro para cada informação inválida.

Idade = int(input("Informe sua idade: "))
if Idade >= 0 and Idade <= 150:
  print("Informação idade válida!")
else:
  print("Informação idade inválida!")

Salario = input ("Informe seu salário R$: ")
Salario = float(Salario)
if Salario > 0:
  print("Informação salário válida!")
else:
  print("Informação salário inválida!")


Sexo = input("Informe seu sexo, M, F ou Outro: ")

if Sexo == "M":
  print("Informação sexo válida!") 
elif Sexo == "F":
  print("Informação sexo válida!")
elif Sexo == "Outro":
  print("Informação sexo válida!")
else:
  print("Informação sexo inválida!")
#----------------------------------------------------------------------------------------------------------------------------------
'''3. Vamos fazer um programa para verificar quem é o assassino de um crime.
Para descobrir o assassino, a polícia faz um pequeno questionário com 5
perguntas onde a resposta só pode ser sim ou não:
a. Mora perto da vítima?
b. Já trabalhou com a vítima?
c. Telefonou para a vítima?
d. Esteve no local do crime?
e. Devia para a vítima?
Cada resposta sim dá um ponto para o suspeito. A polícia considera que os
suspeitos com 5 pontos são os assassinos, com 4 a 3 pontos são cúmplices e
2 pontos são apenas suspeitos, necessitando outras investigações. Valores
iguais ou abaixo de 1 são liberados'''

interrogado = input("Informe o nome do interrogado: ")
perguntas = 0

a = input("Mora perto da vítima? ")
if a == "Sim":
  perguntas = perguntas + 1

b = input("Já trabalhou com a vítima? ")
if b == "Sim":
  perguntas = perguntas + 1

c = input("Telefonou para a vítima? ")
if c == "Sim":
  perguntas = perguntas + 1

d = input("Esteve no local do crime? ")
if d == "Sim":
  perguntas = perguntas + 1

e = input("Devia para a vítima? ")
if e == "Sim":
  perguntas = perguntas + 1
  
if perguntas >= 5:
  print(interrogado,"você está preso, é o assasino!!!")
elif perguntas == 3 or perguntas == 4:
  print(interrogado,"Está detido, é cúmplice do ocorrido!!")
elif perguntas == 2:
  print(interrogado,"É suspeito, faça mais algumas investigações!!")
else: #Valores iguais ou abaixo de 1 são liberados
  print(interrogado,"Liberado!!!")


#-----------------------------------------------------------------------------------------------------------------------------------
#4. Faça um programa que imprima a tabuada do 9 (de 9*1 a 9*10) usando loops.

tabuada = 9

while tabuada <= 9*10:
  print(tabuada)
  tabuada = tabuada + 9
 
  

