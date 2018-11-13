#! usr/bin/python

from pprint import pprint as pp
from copy import deepcopy as dc

def arrows(F):
    for alpha, betalist in F.items():
            for beta in betalist:
                yield alpha, beta

def f_plus(R, F):
    '''
    Toma un conjunto de dependencias funcionales F y una relacion R
    y devuelve el cierre de conjuntos de DF sobre R. 
    R y F se pasan en formato de lista.
    Cada dependencia es una tupla (par) donde "el 2nd elemento depende del 1st".
    Representamos las DF en un diccionario, con los valores dependientes
    en forma de lista.
    '''
    
    r_power = [ frozenset(x) for x in powerset(R) if x != [] ]
    resultado = { x: list(powerset(x)) for x in r_power }
    for key, value in resultado.items():
        value.remove([])
        resultado[key] = { frozenset(x) for x in value }
    
    pp(resultado)
    
    
    hayCambios = True
    while hayCambios:
        resultado2 = dc(resultado)
        for alpha, beta in arrows(resultado):
            for gamma in r_power:
                resultado2[gamma | alpha].add(gamma | beta)
        if resultado == resultado2:
            hayCambios = False
        else:
            resultado = resultado2
       
        #~ resultado2 = dc(resultado)
        #~ for a, b in arrows(resultado):
            #~ for c, d in arrows(resultado):
                #~ if c == b:
                    #~ resultado2[a].add(d)
        #~ if resultado == resultado2:
            #~ hayCambios = False
        #~ else:
            #~ resultado = resultado2
        
    pp(len([x for x in arrows(resultado)]))
    
    return resultado
    
    

def powerset(seq):
    """
    Returns all the subsets of this set. This is a generator.
    """
    if not isinstance(seq, list):
        seq = list(seq)
    if len(seq) == 0:
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]]+item
            yield item



def main():
    R = "ABCD"
    s1 = [("A","B"),("B","AD"),("BC","A")]
    s2 = [("AB","C"),("BD","EF")]
    
    f_plus("ABCDEF", s2)
    
    pass

if __name__ == "__main__":
    main()
