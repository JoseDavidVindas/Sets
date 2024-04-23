numeros = {1, 2, 3, 4, 5}
numeros.add(6)
numeros.add(5)
otros_numeros = {4, 5, 6, 7, 8}
union_numeros = numeros.union(otros_numeros)
interseccion_numeros = numeros.intersection(otros_numeros)
print("Conjunto original:", numeros)
print("Conjunto otro:", otros_numeros)
print("Unión de conjuntos:", union_numeros)
print("Intersección de conjuntos:", interseccion_numeros)
