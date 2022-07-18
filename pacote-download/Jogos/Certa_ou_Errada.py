from time import sleep
def linha():
    print('-=' * 30)

def cabeçalho(msg):
    print(msg)

perguntas = {

    'Pergunta1': {
            'pergunta': 'Quanto é 2+2? ',
            'resposta': {'a': '1', 'b': '4', 'c': '5',},
            'resposta_certa': 'b',
    },
    'Pergunta2': {
            'pergunta': 'Quanto é 3*2? ',
            'resposta': {'a': '4', 'b': '10', 'c': '6',},
            'resposta_certa': 'c',
    },
}
resposta_certa = 0
for pk, pv in perguntas.items():
    linha()
    print(f'{pk}: {pv["pergunta"]}')
    cabeçalho('Qual é sua resposta?')
    for rk, rv in pv['resposta'].items():
        print(f'[{rk}]: {rv}')
    resposta_usuário = str(input('Qual é sua resposta: '))



    if resposta_usuário == pv['resposta_certa']:
        cabeçalho('PARABENS!!!!! Você ACERTOU!!! ')
        resposta_certa += 1
        sleep(1)
        print()
    else:
        cabeçalho('INFELIZMENTE! Você ERROU')


qta_pergunta = len(perguntas)
porcentagem_acerto = resposta_certa / qta_pergunta * 100

cabeçalho(f'Você acertou {resposta_certa} respostas.')
cabeçalho(f'Sua % de acerto foi de: {porcentagem_acerto}%')

