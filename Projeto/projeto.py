#Abrir arquivo txt
import random

quiz = {

    'Questão 01' : {
        'Pergunta' : ' Quanto é 2+2?',
        'Respostas' : {
            ' a' : '1',
            ' b' : '2',
            ' c' : '3',
            ' d' : '4'},
            'respostaCerta' : 'd',
        },

    'Questão 02' : {
        'Pergunta' : ' Quanto é 2+2?',
        'Respostas' : {
            ' a' : '1',
            ' b' : '2',
            ' c' : '3',
            ' d' : '4'},
            'respostaCerta' : 'd',
        },
    'Questão 03' : {
        'Pergunta' : ' Quanto é 2+2?',
        'Respostas' : {
            ' a' : '1',
            ' b' : '2',
            ' c' : '3',
            ' d' : '4'},
            'respostaCerta' : 'd',
        },
    'Questão 04' : {
        'Pergunta' : ' Quanto é 2+2?',
        'Respostas' : {
            ' a' : '1',
            ' b' : '2',
            ' c' : '3',
            ' d' : '4'},
            'respostaCerta' : 'd',
        },
    'Questão 05' : {
        'Pergunta' : ' Quanto é 2+2?',
        'Respostas' : {
            ' a' : '1',
            ' b' : '2',
            ' c' : '3',
            ' d' : '4'},
            'respostaCerta' : 'd',
        },
    }

print("----------------------------------------------")
print("            Q U I Z Z - Soft Skills           ")
print("----------------------------------------------")
print('''Você está no nível FÁCIL! 
        Acerte 70% para seguir para o próximo nível. :)\n''')

resposta_certas = 0

#random.choice(quiz.items) 
for pk, pv in quiz.items() :
    print(f'{pk}: {pv["Pergunta"]}')

    for rk, rv in pv["Respostas"].items() : 
        print (f'{rk}) {rv}')
    print()

    resposta_user = input('Digite a reposta correta: ')

    if resposta_user == pv['respostaCerta'] : 
        print('⭐ Sua reposta está correta, parabéns! ⭐')
        resposta_certas +=1

    else : 
        print('Você errou! :( Continue tentando...')
    
    print()

qtd_perguntas = len(quiz)
percentual = resposta_certas / qtd_perguntas * 100

print(f" Você acertou {resposta_certas} questões.")
print(f" O seu score foi {percentual}%.")