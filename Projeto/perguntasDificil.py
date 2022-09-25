class Arquivo() :
    __path__: str
    def __init__(self,path) :
        self._path = path
    def mostrarConteudo(self) :
        with open(self._path, 'r', encoding='utf-8') as arq :
            for item in arq :
                print(item)
            

arquivo = Arquivo('Perguntas.txt')
arquivo.mostrarConteudo()
