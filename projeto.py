from modulos import ganha, mostrar                                         #funções importadas 
    
jogo = [0, 1, 2, 3, 4, 5, 6, 7, 8]                                         #definição da quantidade de espaços
max_rodadas = 4                                                            #definição do máximo de rodadas
vez_jogada = 1                                                             #definição do número de tentativas


for jogo_completo in range(0, max_rodadas + 1):                                #laço para controle de rodadas
    for jogada in range(vez_jogada):                                       #laço para controle de tentativa
        mostrar(jogo)
        print('Vez do jogador 1:')
        posicao = int(input('Qual posição você quer jogar?'))
        correto = posicao >= 0 and posicao < 9
        while correto == True:                                             #laço para filtrar resultados
            if jogo[posicao] != posicao:
                posicao = int(input('Digite uma posição válida:'))
                correto = posicao >= 0 and posicao < 9
                
            else:
                jogo[posicao] = 'X'
                jogador = ganha(jogo, 'X', '1')
                if jogador == '1':
                    break
                
                else:
                    break
                
        while correto == False:                                             #laço para filtrar resultados
            posicao = int(input('Digite uma posição válida: '))
            correto = posicao >= 0 and posicao < 9
            if correto == True:
                if jogo[posicao] == posicao:
                    jogo[posicao] = 'X'
                    jogador = ganha(jogo, 'X', '1')
                    if jogador == '1':
                        break
                    
                    else:
                        break
                else:
                    correto = False
                    
    if jogador == '1':                                                      #condicional filtro de vitória
        mostrar(jogo)
        break
    
    if jogo_completo == max_rodadas:                                        #condicional filtro de empate
        mostrar(jogo)
        print('O jogo chegou ao fim e não houve ganhador!')
        break
    
    for jogada in range(vez_jogada):                                        #laço para controle de tentativa
        mostrar(jogo)
        print('Vez do jogador 2: ')
        posicao = int(input('Qual posição você quer jogar?'))
        correto = posicao >= 0 and posicao < 9
        while correto == True:                                              #laço para filtrar resultados
            if jogo[posicao] != posicao:
                posicao = int(input('Digite uma posição válida:'))
                correto = posicao >= 0 and posicao < 9
                
            else:
                jogo[posicao] = 'O'
                jogador = ganha(jogo, 'O', '2')
                if jogador == '2':
                    break
                
                else:
                    break
                
        while correto == False:                                            #laço para filtrar resultados
            posicao = int(input('Digite uma posição válida: '))
            correto = posicao >= 0 and posicao < 9
            if correto == True:
                if jogo[posicao] == posicao:
                    jogo[posicao] = 'O'
                    jogador = ganha(jogo, 'O', '2')
                    if jogador == '2':
                        break
                    
                    else:
                        break
                else:
                    correto = False
                    
    if jogador == '2':                                                     #condicional filtro de vitória
        mostrar(jogo)
        break
