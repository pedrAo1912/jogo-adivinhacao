import random
from datetime import datetime
import pygame
pygame.init()
pygame.mixer.init()


print(f"\n\033[1;32m{'='* 20}' Jogo de adivinhação do pedrAo!! '{'='* 20}\033[0m")
agora = datetime.now()
agora2 = agora.strftime("%H:%M:%S do dia %d do mês %m de %Y")





while True:
    dificuldade = str(input(
        f'\033[1;32mPara começar... qual dificuldade irá escolher? \n [1]- Fácil \n [2]- Normal \n [3]- Difícil \n [4]- Pesadelo \n\033[0m')).strip()
    if dificuldade not in ('1', '2', '3', '4'):
        print(f'\033[1;31mERRO! Escolha uma dificuldade válida.\033[0m')
    else:
        break

if dificuldade == '1':
    dif = 'FÁCIL'
    min_num, max_num = 1, 50
    tentativas_maximas = 7

elif dificuldade == '2':
    dif = 'NORMAL'
    min_num, max_num = 1, 100
    tentativas_maximas = 15

elif dificuldade == '3':
    dif = 'DIFÍCIL'
    min_num, max_num = 1, 150
    tentativas_maximas = 15

else:
    dif = 'PESADELO'
    min_num, max_num = 1, 200
    tentativas_maximas = 20

sorteio = random.randint (min_num, max_num)
for tentativas in range(1, tentativas_maximas + 1):
        try:
            escolha = int(  input(f'\n\033[1;34m{'-' * 5}DIFICULDADE {dif} {'-' * 5} \n Tentativa {tentativas}/{tentativas_maximas} Vamos começar... escolha entre {min_num} e {max_num} para darmos ínicio ao nosso pequeno jogo: \033[0m'))

        except ValueError:
            print(f'\033[1;31mERRO! Digite um >NÚMERO> entre 1 e {max_num}.\033[0m')
            continue

        if escolha > max_num:
             print(f'\033[1;31mERRO! Digite um número até no MÁXIMO >{max_num}<\033[0m')
             continue
        if escolha < 1:
            print('\033[1;31mERRO! Digite um número até no MÍNIMO >1<\033[0m')
            continue


        if escolha == sorteio:


            print(f'\033[1;32mFinalmente... no momento {agora2}, com {tentativas} tentivas, você acertou!!!\033[0m')
            pygame.mixer_music.load('victory_sJDDywi.mp3')
            pygame.mixer_music.play()
            while pygame.mixer.music.get_busy():
             continue
            pygame.quit()
            break
        elif escolha < sorteio:
         print(f'\033[1;33mERRADO! Aqui vai uma dica de amigo... tente um número MAIOR!!\033[0m')
        else:
         print('\033[1;33mERRADO!Aqui vai uma dica de amigo... tente um número MENOR!!\033[0m')

else:
        print(f'\033[1;31mVocê PERDEU! Você usou todas as {tentativas_maximas} tentativas. O número era {sorteio}.\033[0m')
        pygame.mixer_music.load('spongebob-fail.mp3')
        pygame.mixer_music.play()
        while pygame.mixer.music.get_busy():
            continue
        pygame.quit()
    #--------------------------------------------------------------------------------------------------------------------
