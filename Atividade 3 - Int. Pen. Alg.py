from ast import Break, If, Return
from pdb import line_prefix
from pickle import STOP
from re import S
from sre_constants import JUMP
import time
from tkinter import N

print('                                     ')
time.sleep(0.4)
entrevistados = int(input('Qual o total de pessoas entrevistadas?  \n'))

if entrevistados == 0:
    time.sleep(0.5)
    print('\n◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇\n')
    print('Não houveram entrevistados, sistema encerrará! \n')
    print('◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇\n')
    quit() 



time.sleep(0.5)
print('Cadastraremos as respostas agora!\n')
time.sleep(0.5)

resp1 = 0
resp2 = 0
resp3 = 0
resp4 = 0
resp5 = 0
medidor = 0
while medidor < entrevistados:
    medidor = medidor + 1
    print('◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇\n')
    sexo =  str(input ('Homem, Mulher:  '))
    time.sleep(0.5)
    idade = int(input('Idade:  '))
    time.sleep(0.5)
    resposta = str(input('S=sim , N=não, I=indiferente:  '))
    time.sleep(0.5)

    if resposta == 'S':
        resp1 = resp1 + 1
    
    
    if resposta == 'N':
        resp2 = resp2 + 1
        

    if resposta == 'I':
        resp5 = resp5 + 1
        
    

    if sexo == 'Mulher' and resposta == 'S':
        resp3 = resp3 + 1

   

    if sexo =='Homem' and resposta == 'N' :
        resp4 = resp4 + 1



  
print('\n◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇\n')    
print('O total de entrevistados foi: {};'.format (entrevistados))
print('Quantos disseram sim: {};'.format (resp1))
print('Quantos disseram não: {};'.format (resp2))
print('Quantos disseram indiferente: {};'.format (resp5))
print('Quantas mulheres disseram sim: {} e quantos homens disseram não: {}.'.format (resp3, resp4))
