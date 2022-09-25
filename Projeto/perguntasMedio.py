import csv

quiz = {}

with open('Perguntas.csv', mode='r') as inp:
    reader = csv.reader(inp)
    for line in reader: 
        quiz = {rows[0]: {rows[1] : rows[2], rows[3] : { rows[4]: rows[5], rows[6]: rows[7], rows[8]: rows[9], rows[10]: rows[11], rows[12]: rows[13], }} for rows in reader}
        print(quiz)

  




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