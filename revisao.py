baseDeDados = [
    ['Fa fe fi fo Funk',	'Anira', 'Funk', 2019, '3:05'],
    [ 'Sofrência de programar', 'Ada & Turing',	'Sertanejo', 1998, '2:58' ],
    [ 'Rock’n Rolo', 'The Buns','Rock',	1984, '4:01' ],
    [ 'Grifinoria Girls', 'Katy Potter', 'Pop',	2017, '2:25' ]
]

# a)  Visualizar base de dados: se escolhida esta opção, o programa deve mostrar ao usuário a tabela 
# com todas as músicas 
# b)  Montar  uma  playlist:  quando  o  usuário  escolher  esta  opção,  o  programa  deve  permitir,  
# enquanto ele quiser, adicionar músicas da base de dados. Para isso, o usuário deve fornecer 
# um ID válido da música do banco de dados e este ID deve ser armazenado na lista. Atenção! Só 
# poderão ser adicionadas músicas que não estejam na playlist. 
# c)  Visualizar a playlist: se escolhida esta opção, o programa deve mostrar apenas as informações 
# a respeito das músicas da playlist. 
# d)  Embaralhar playlist: se escolhida esta opção, o programa deve embaralhar a ordem das músicas 
# da playlist e exibir o resultado. 
# e)  Mostrar a duração total da playlist, em minutos 
# f) Consultar música: o usuário entra com o título da música e o programa retorna o ID da música 
# no banco de dados, se houver 
# g)  Consultar por banda/artista: usuário entra com o nome da banda/artista e o programa retorna 
# a lista da(s) ID(s) das música(s) encontradas, se houver. 

tabela = [['ID', 'Nome da música', 'Artista/Banda', 'Gênero', 'Ano', 'Duração']]
playlist = []

def visualiza_base_dados():
    for index, x in enumerate(baseDeDados,):
        x.insert(0, index)
        tabela.append(x)
    print('\n')
    for y in tabela:
        print(y)
    print('\n')

def monta_playlist():
    escolha = int(input('digite o ID de uma música: '))
    if escolha in playlist:
        print('digite novamente')


def EscolherOpcao():
    print('a -Opção a')
    print('b -Opção b')
    print('c -Opção c')
    print('h -Sair\n')
    escolha_usuario = str(input('Escolha uma opção: '))
    return escolha_usuario

def menu():
    terminarExecucao = False
    while not terminarExecucao:
        escolha = EscolherOpcao()
        if (escolha == 'a'):
            visualiza_base_dados()
        elif (escolha == 'b'):
            monta_playlist()
        elif (escolha == 'c'):
            terminarExecucao = True
            return "fim"
        elif (escolha == 'h'):
            terminarExecucao = True
            return "fim"
        else:
            print('Escolha invalida!Tente de novo.')



opcao_escolhida = menu()
