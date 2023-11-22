# Dividir
def divicion(problema):
    mitad=len(problema)//2
    return problema[:mitad], problema[mitad:]

def caso_base(problema):
    return len(problema)<=1

def resolver_caso_base(problema):
    if len(problema) == 0:
        return 0
    else:
        return problema[0]

def combine(problema):
    return s1+s2


