def leiaStr(msg):
    # Loop infinito, que só se encerra caso o usúario digite UMA letra.
    while True:
        letra = str(input(msg)).strip().lower()
        if len(letra) == 1 and letra.isalpha():
            return letra
        else:
            # Caso o valor digitado não seja apenas UMA caractere, ou o valor não seja uma letra, será exibindo uma mensagem de erro.
            print('ERRO! Por favor digite uma letra.')
            print('-' * 50)


def forca():
    # Importando a função choice da biblioteca random.
    from random import choice
    # Um contador de erros, para saber quantas vezes o usúario já errou.
    cont_erro = 0
    # Palavras que serão utilizadas (pode ser inseridas outras palavras).
    palavras = ['Sonho', 'Horizonte', 'Mistério', 'Liberdade', 'Cristal', 'Esperança', 'Vento', 'Silêncio',
                'Universo', 'Jardim', 'Memória', 'Riacho', 'Fogo', 'Estrela', 'Caminho', 'Segredo', 'Lua', 'Tempo', 'Raiz']
    # Pega uma palavra da lista de palavras.
    pala_esc = choice(palavras).lower()
    # Aqui terá a quantidade de linhas igual a quantidade de letras da palavra escolhida, que depois serão substituidos.
    palavra = '_ ' * len(pala_esc)
    # Aqui faz uma lista que terá as letras/linhas da palavra.
    letras = palavra.split()
    # Loop infinito.
    while True:
        rep = 0
        # Função que exibe a forca e o boneco.
        boneco(cont_erro)
        # Exibição do estado atual da palavra.
        print('PALAVRA: ', ' '.join(letras).capitalize())
        # Se a palavra estiver completa o loop se encerra.
        if ''.join(letras).isalpha():
            return 1
        # Se o usúario errar 6 vezes o loop também se encerra.
        if cont_erro == 6:
            return pala_esc
        print('-' * 50)
        # Aqui está recebendo o valor digitando pelo usúario.
        letra_dig = leiaStr('Digite uma letra: ')
        # Caso a letra digitada não exista na palavra, irá se exibido uma mensagem dizendo que o usúario errou, e o contador de erro sobe mais um.
        if pala_esc.find(letra_dig) == -1:
            print(f'VOCÊ ERROU!!! A LETRA "{letra_dig}" ESTÁ INCORRETA.')
            print('-' * 50)
            cont_erro += 1
        else:
            # Caso a letra exista na palavra, será exibido uma mensagem dizendo que o usúario acertou.
            for i, p in enumerate(pala_esc):
                if p == letra_dig:
                    # Caso o usúario já tenha usado a letra anteriormente, irá ser exibido uma mensagem dizendo que a letra já foi utilizada.
                    if letras[i] == letra_dig and rep == 0:
                        print(
                            f'A LETRA "{letra_dig}" JÁ FOI UTILIZADA!!!')
                        print('-' * 50)
                    elif letras[i] != letra_dig and rep == 0:
                        print(
                            f'VOCÊ ACERTOU!!! A LETRA "{letra_dig}" ESTÁ CORRETA.')
                        print('-' * 50)
                    rep += 1
                    # Aqui ocorrerá a troca da linha pela letra digitada.
                    letras[i] = letra_dig


def boneco(erros):
    # Aqui será feito a forca e o boneco, dependendo da quantidade de erros, será adicionado uma parte do corpo do boneco.
    print('+-------+')
    print('|       |')
    if erros >= 1:
        print(f'|', f'{'O':>7}')
    if erros >= 2:
        if erros == 2:
            print(f'|', f'{'|':>7}')
        elif erros == 3:
            print(f'|', f'{'/':>5}', f'{'|'}')
        elif erros >= 4:
            print(f'|', f'{'/':>5}', f'{'|'}', f'{'\\'}')
    if erros >= 5:
        if erros == 5:
            print(f'|', f'{'/':>6}')
        elif erros == 6:
            print(f'|', f'{'/':>6}', f'{'\\'}')
    print('|')
    print('|')
    print('|')
    print('|')
    print('=========')
