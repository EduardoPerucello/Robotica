def area(comp, larg):
    if type(comp) not in [int,float]:
        raise ValueError('Tipo errado')

    return comp*larg

# print(area('10',10))