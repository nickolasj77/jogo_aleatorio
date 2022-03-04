from random import randint
from time import sleep
a = randint(0,240)
print('-=-'*20)
print('Radar à sua frente.')
print('-=-'*20)
sleep(2)
print('Processando sua velocidade...')
print('-=-'*20)
sleep(1)
if a <= 120:
    print(f'Você não foi multado, siga sua viagem....')
else:
    print(f'Você foi multado por excesso de velocidade({a} Km/h).')
    sleep(1)
    print('Você deverá pagar a seguinte multa:')
    sleep(2)
    if 120<a<=135: print('Sua multa é de 250 reais.')
    if 135<a<=150: print('Sua multa é de 350 reais.')
    if 150<a<=240: print('Sua multa é de 500 reais.')
    sleep(1)
    x = str(input('Você quer pagar? 1 - SIM/ 2 - NÃO ')).strip()
    if x == ('1'):
        print('-=-'*20)
        print('Entre a direita no próximo posto policial...')
        print('-=-'*20)
        sleep(0.5)
        print('Parando no posto policial...')
        sleep(1.5)
        y = str(input('Digite 1 para pagar e 2 para não pagar. ')).strip()
        if y == ('1'):
            sleep(0.5)
            print('Pagamento aprovado, siga sua viagem...e mais cuidado da próxima vez.')
        if y == ('2'):
            print('Você não pagou e o policial te furou...')
    if x == ('2'):
        print('Você optou por não pagar a multa, agora a polícia está te perseguindo...')
        sleep(0.5)
        z = str(input('Você tem duas opções: 1 - Pular com o carro do barranco a sua frente e tentar despistar a polícia ou 2 - Se render. ')).strip()
        if z == ('1'):
            sleep(0.5)
            print('Realizando tal proeza...')
            sleep(1)
            print('Parabéns, você tentou descer o barranco e seu carro explodiu e você morreu. Você pensou que era quem? O RAMBO?')
        if z == ('2'):
            sleep(0.5)
            print('Se rendendo...')
            sleep(1)
            print('Você se rendeu, mas a polícia achou que vc tinha uma arma e te furou.')
    sleep(1)
    print('-=-'*20)
    print('Moral da história: Pague a multa.')
    print('-=-'*20)
input()