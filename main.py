lista_ady = {}
heuristica = {}
with open('grafo.txt', 'r') as f:
    lineas = f.readlines()


nodo_inicial = lineas[0].strip().split(': ')[1][1:-1]
nodo_objetivo = lineas[1].strip().split(': ')[1][1:-1]

for linea in lineas[2:10]:
    datos = linea.strip().split(' ')
    #print(datos)
    nodo = datos[0][1:-1]  # Elimina los símbolos < > de los nodos
    #print(nodo)
    lista_ady[nodo] = []    # Asegúrar que la lista de adyacencia para el nodo de origen existe
    if len(datos) >= 2:
        valor = datos[1][1:-1]  # Elimina los símbolos < > de la heuristica
        heuristica[nodo] = valor
    else:
        valor = None  # asigna un valor por defecto si no hay suficientes elementos


#for nodo, adyacencias in lista_ady.items():
#    print(f"{nodo}:")
    
for linea in lineas[10:len(lineas)-1]:
    datos = linea.strip().split(', ')
    #print(datos)
    origen = datos[0][1:-1]  # Elimina los símbolos < > de los nodos de origen
    #print(f"origen:{origen}")
    destino = datos[1][1:-1]  # Elimina los símbolos < > de los nodos de destino
    #print(f"destino:{destino}{type(destino)}")
    costo = int(datos[2][1:-1])  # Elimina los símbolos < > del costo de la arista
    #print(f"costo:{costo}")
    lista_ady[origen].append((destino,costo))     
    #print(lista_ady["G"])

#for node in lista_ady:
#    print(f"{node}: {lista_ady[node]}")


def dfs_recursiva(lista_ady, nodo_inicial, visited = None):
    costo = 0
    if visited is None:
        visited = set()

    visited.add(nodo_inicial)

    print(f"{nodo_inicial}->", end=" ")
    
        
    for neighbor in lista_ady[nodo_inicial]:
        if neighbor not in visited:
            costo = costo + int(heuristica[nodo_inicial])   
            dfs_recursiva(lista_ady, neighbor[0])
        if neighbor := nodo_objetivo:
                break 
       




dfs_recursiva(lista_ady, nodo_inicial)

