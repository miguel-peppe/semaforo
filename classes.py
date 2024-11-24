from time import sleep

def verde():
    print('verde')
    sleep(3)
    return amarelo()

def vermelho():
    print('vermelho')
    sleep(3)
    return verde()

def amarelo():
    print('amarelo')
    sleep(1)
    return vermelho()

def init():
    return verde()

init()