# d. Dadas dos listas, lista1 y lista2, escribir un método 
# listas_diferencia(lista1, lista2)
# que tome ambas como parámetros e imprima dos listas, cada una con:
# i. Los elementos en común, en orden inverso.
# ii. Los elementos no comunes, en orden alfabético.
# El programa debería arrojar el siguiente resultado:
# listas(['b', 'a', 'c'], ['e', 'b', 'd', 'c'])
# ['c', 'b']
# ['a', 'e', 'd']

l1 = ['b', 'a', 'c']
l2 = ['e', 'b', 'd', 'c']
# Ver estas funciones - set y set().symmetric_difference() 
# Busco Los elementos en comun de 2 listas
linv = set(l1) & set(l2)
# Los clasifico en orden inverso
linv = sorted(linv, reverse = True )

print(linv)

#Busco Los elementos no comunes de ambas listas
diff_1 = set(l1).difference(set(l2))
diff_2 = set(l2).difference(set(l1))

# Uno ambas diferencias
diferencias = list(diff_1.union(diff_2))
# las ordeno alfabéticamente
diferencias.sort()
print(diferencias)
