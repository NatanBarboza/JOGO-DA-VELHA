                                                                                    #organização das funções para melhor controle e manutenção futura;


def ganha(lista, escolha, jogador):                                                  #função filtro, utilizando condicionais para definição de vitória;
    if lista[0:3] == [escolha, escolha, escolha]:
        print(f'O jogador_{jogador} ganhou.')
        return jogador
    elif lista[3:6] == [escolha, escolha, escolha]:
        print(f'O jogador_{jogador} ganhou.')
        return jogador
    elif lista[6:9] == [escolha, escolha, escolha]:
        print(f'O jogador_{jogador} ganhou.')
        return jogador
    elif lista[0:7:3] == [escolha, escolha, escolha]:
        print(f'O jogador_{jogador} ganhou.')
        return jogador
    elif lista[1:8:3] == [escolha, escolha, escolha]:
        print(f'O jogador_{jogador} ganhou.')
        return jogador
    elif lista[2:9:3] == [escolha, escolha, escolha]:
        print(f'O jogador_{jogador} ganhou.')
        return jogador
    elif lista[2:7:2] == [escolha, escolha, escolha]:
        print(f'O jogador_{jogador} ganhou.')
        return jogador
    elif lista[0:9:4] == [escolha, escolha, escolha]:
        print(f'O jogador_{jogador} ganhou.')
        return jogador
    else:
        pass
    
    
    
def mostrar(lista):                                                                  #função para mostrar na tela os valores presentes em uma lista;
    print(f'{lista[0]}', f'{lista[1]}', f'{lista[2]}', sep=(' | '))
    print('-' * 10)
    print(f'{lista[3]}', f'{lista[4]}', f'{lista[5]}', sep=(' | '))
    print('-' * 10)
    print(f'{lista[6]}', f'{lista[7]}', f'{lista[8]}', sep=(' | '))
    