from random import randint
def linha():
    print('=' * 30)

def cabeçalho(msg):
    print(msg)

def palavra():
    n = randint(0, 4)
    palavras = ['perfume', 'celular', 'livro', 'colar', 'geladeira']

    if n == 0:
        return palavras[0]
    if n == 1:
        return palavras[1]
    if n == 2:
        return palavras[2]
    if n == 3:
        return palavras[3]
    else:
        return palavras[4]

def dicas():
    secreto = palavra()
    if secreto == 'perfume':
        return 'É cheiroso.', secreto
    if secreto == 'celular':
        return 'Serve para falar', secreto
    if secreto == 'livro':
        return 'Nele tem palavras', secreto
    if secreto == 'colar':
        return 'Coloca no pescoço', secreto
    else:
        return 'Serve para gelar.', secreto


linha()
cabeçalho('Vamos Jogar Força')
linha()
cabeçalho('Você tem 5 chance!')
linha()
palavra_e_dica = dicas()
secreto = palavra_e_dica[1]
digitadas = []
chances = 5
linha()
cabeçalho(f'Vamos de dar uma dica: {palavra_e_dica[0]} ')
linha()
while True:
    if chances <= 0:
        print('Você perdeu!!!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Ahhh isso não vale, digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'\033[32mPARABENS!\033[m A letra "\033[32m{letra.upper()}\033[m" \033[32MEXISTE\033[M na palavra secreta.')
    else:
        print(f'\033[31mQUE PENA!\033[m A letra "\033[31m{letra.upper()}\033[m" \033[32MNÃO EXISTE\033[M na palavra secreta.')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Que legal, VOCÊ GANHOU!!! A palavra era {secreto_temporario}.')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1
        print(f'Você ainda tem {chances} chances.')
        print()
