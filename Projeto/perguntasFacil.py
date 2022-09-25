def calculandoScore() : 
    qtd_perguntas = 5
    percentual = resposta_certas / qtd_perguntas * 100

    print(f" Você acertou {resposta_certas} questões.")
    print(f" O seu score foi {percentual}%.")


#comtador para score
resposta_certas = 0

class Arquivo() :
    #Lendo as perguntas no arquivo
    __path__: str
    def __init__(self,path) :
        self._path = path
    
    def mostrarConteudo(self) :
        with open(self._path, 'r', encoding='utf-8') as arq :
            for item in arq :
                #problema: quando eu passo os indices das linhas, ela só imprime as linhas que tem indice, pensar em como 
                #pensar em como controlar a contagem das linhas para que não precise passar os indices e limitar quais questões
                #são impressas. Pensar na possibilidade de aribuir o valor de cada linha a unha chave : valor de dict para poder automatizar a impressão das questões 
                
                linhas = arq.readlines()

                
                Questao = linhas[0]  
                linhaPergunta = linhas[1]
                a = linhas[2]
                respostaA= linhas[3]
                b = linhas[4]
                respostaB= linhas[5]
                c = linhas[6]
                respostaC= linhas[7]
                d = linhas[8]
                respostaD= linhas[9]
                respostaCerta = linhas[10]
                
                #Imprimindo a pergunta e corrigindod
                respostaJogador = input(f''' 
                {Questao}{linhaPergunta}
                {a}){respostaA}
                {b}){respostaB}
                {c}){respostaC}
                {d}){respostaD}

                Qual a resposta correta?
                ''')

                if respostaJogador == respostaCerta :
                    print('⭐ Sua reposta está correta, parabéns! ⭐')
                    resposta_certas +=1
                else : print('Você errou! :( Continue tentando...')

arquivo = Arquivo('Perguntas.txt')
arquivo.mostrarConteudo()



    

#Transformando os dados do txt em variáveis



    



