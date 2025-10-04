# Importando as minhas funções
import game
# Loop infinto
while True:
    res = ''
    # Menu
    print('-' * 50)
    print('JOGO DA FORCA'.center(50))
    print('-' * 50)
    # Recebendo a variável que irá dizer ser o jogador ganhou ou perdeu.
    dec = game.forca()
    # Depedendo do valor da variável "dec", irá ser exibido uma mensagem de vitória ou derrota.
    if dec == 1:
        print('-' * 50)
        print('PARABÊNS VOCÊ VENCEU!!!'.center(50))
        print('-' * 50)
    else:
        print('-' * 50)
        print(
            f'VOCÊ PERDEU!!! A PALAVRA CORRETA ERA "{dec.upper()}"'.center(50))
        print('-' * 50)
    # Pergunta ser o usúario quer continuar, se sim, o programa continua, se não, ele termina.
    while res not in ('S', 'N'):
        res = str(input('Quer continuar [S/N]? ').strip().upper())
        # Se ele digite uma opção que não seja S ou N, uma mensagem de erro será exibida.
        if res not in ('S', 'N'):
            print('ERRO!!! Opção inválida.')
            print('-' * 50)
    if res in 'N':
        break
# Mensagem final.
print('-' * 50)
print('OBRIGADO POR USAR O MEU JOGO DA FORCA.'.center(50))
print('-' * 50)
