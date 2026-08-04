def contador(i, f, p=1):
    """
    -> Conta do início 'i' ao fim 'f'
    :param i: Início da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: sem retorno
    """

    if p == 0:
        p = 1

    c = i
    while c < f:
        print(f"{c} ", end="")
        c += p
    print("FIM")


help(contador)
