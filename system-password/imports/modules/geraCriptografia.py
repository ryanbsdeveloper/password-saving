from random import choices

caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@@@!!!###%%%'


def gerador(tam=10):
    seq = ''
    for v in choices(caracteres, k=tam):
        seq += v
    return seq
