def valida_simples(senha):
    if len(senha) < 4:
       return 'Fraca'

    elif len(senha) < 7:
        if senha.isalpha():
            return 'Fraca'
        elif senha.isidentifier():
            return 'Média'

    else:
        if senha.isalpha():
            return 'Média'
        elif senha.isidentifier():
            return 'Forte'


