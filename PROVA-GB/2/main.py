import random
from equipe import Equipe
from competidor import Competidor
from joken import Joken

ze = Competidor("ze")
maria = Competidor("maria")
joao = Competidor("joao")
yuri = Competidor("yuri")
ricardo = Competidor("ricardo")
mari = Competidor("mari")

time_vermelho = Equipe("Time vermelho")
time_azul = Equipe("Time azul")

time_vermelho.competidores.append(mari)
time_vermelho.competidores.append(ricardo)
time_vermelho.competidores.append(ze)

time_azul.competidores.append(joao)
time_azul.competidores.append(maria)
time_azul.competidores.append(yuri)

game = Joken()

def main():

    def exe_round():
        competidor_time_azul = time_azul.competidores[random.randint(0, 2)]
        competidor_time_vermelho = time_vermelho.competidores[random.randint(0, 2)]

        opcao_competidor_azul = game.opcoes()
        opcao_competidor_vermelho = game.opcoes()

        resultado = game.resultado(opcao_competidor_azul, opcao_competidor_vermelho)

        if resultado == None:
            exe_round()

        if resultado == opcao_competidor_azul:
            competidor_time_azul.num_vitorias_pessoais += 1
            time_azul.num_vitorias += 1
        
        if resultado == opcao_competidor_vermelho:
            competidor_time_vermelho.num_vitorias_pessoais += 1
            time_vermelho.num_vitorias += 1
        

    while time_azul.num_vitorias < 10 or time_vermelho.num_vitorias < 10:
        exe_round()

    if time_azul.num_vitorias == 10:
        print("TIME AZUL FOI VENCEDOR!")

    if time_vermelho.num_vitorias == 10:
        print("TIME VERMELHO FOI VENCEDOR!")

main()