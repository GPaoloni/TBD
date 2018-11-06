#! usr/bin/python

def f_plus(R, F):
    '''
    Toma un conjunto de dependencias funcionales F y una relacion R
    y devuelve el cierre de conjuntos de DF sobre R. 
    R y F se pasan en formato de lista.
    Cada dependencia es una tupla (par) donde "el 2nd elemento depende del 1st".
    Representamos las DF en un diccionario, con los valores dependientes
    en forma de lista.
    '''
    dependencies = {f[0]:{f[1]} for f in F}
    r_power = powerset(R)
    # Aplicamos todas las reflexividades a P(R)
    for alpha in r_power:
        for beta in powerset(alpha):
            try:
                dependencies[alpha[0]].add(beta[0])
            except KeyError:
                dependencies[alpha[0]] = set(beta[0])
    '''
    continue = True
    while(continue):
        continue = False
        # Aplicamos las reglas de aumentatividad
        for alpha in r_power:
            for beta, dep in dependencies:
    '''            
    return dependencies
    

def powerset(seq):
    """
    Returns all the subsets of this set. This is a generator.
    """
    #if len(seq) == 0:
        #yield []
    if len(seq) == 1:
        yield seq
        #yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]]+item
            yield item



def main():
    pass

if __name__ == "__main__":
    main()
