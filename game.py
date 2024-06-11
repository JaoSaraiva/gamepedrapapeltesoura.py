import random

#JOGO TRADICIONAL DE PEDRA, PAPEL OU TESOURA:

#O jogador escolhe pedra, papel ou tesoura, a máquina também escolhe:
def escolhas():
 
     escolha_do_jogador = input('Escolha pedra, papel ou tesoura:')
     
     opcoes_do_jogo = ['pedra', 'papel', 'tesoura']
     escolha_da_maquina = random.choice(opcoes_do_jogo)

     dic_escolhas = {'jogador':escolha_do_jogador, 'maquina':escolha_da_maquina}

     return dic_escolhas 

def verificacoes(jogador, maquina):
     
     print('Você escolheu:' + jogador +', a máquina escolheu:' + maquina)
     
     if jogador == maquina:
          return 'Empate!'
     elif jogador == 'pedra':
         if maquina == 'tesoura':
              return 'Você ganhou!'
         else:
              return 'Você perdeu!'
     elif jogador == 'papel': 
         if maquina == 'pedra':
              return 'Você ganhou!'
         else:
              return 'Você perdeu!'
     elif jogador == 'tesoura':
         if maquina == 'papel':
              return 'Você ganhou!'
         else:
              return 'Você perdeu!'

escolhas_feitas = escolhas()
resultado = verificacoes(escolhas_feitas['jogador'], escolhas_feitas['maquina'])
print(resultado)

