import heapq

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

for node in lista_ady:
    print(f"{node}: {lista_ady[node]}")


def busqueda_profundidad_recursiva(lista_ady, nodo_inicial, visited = None):
    costo = 0
    if visited is None:
        visited = set()
    visited.add(nodo_inicial)
    print(f"{nodo_inicial}->", end=" ")
    if nodo_inicial == nodo_objetivo:
        return True
    
        
    for neighbor in lista_ady[nodo_inicial]:
        if neighbor not in visited:
            costo = costo + int(heuristica[nodo_inicial])  
            busqueda_profundidad_recursiva(lista_ady, neighbor[0])
        if busqueda_profundidad_recursiva(lista_ady, neighbor[0], visited):
            return True
    return False

#def busqueda_costo_uniforme(lista_ady, nodo_inicial, nodo_objetivo):
#    cola_p = [(0,nodo_inicial)]
#    costo = {nodo_inicial: 0}
#    padre ={nodo_inicial: None}
#    while cola_p: 
#        (costo, nodo_actual) = heapq.heappop(cola_p)
#        if nodo_inicial == nodo_objetivo:
#            camino = []
#            while nodo_inicial is not None:
#                camino.append(nodo_inicial)
#                nodo_inicial = padre[nodo_inicial]                
#            print(nodo_inicial)

def busqueda_costo_uniforme(graph, start, goal):
    visited = set()
    queue = [(0, start, [])]
    
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        
        if node not in visited:
            visited.add(node)
            path = path + [node]
            
            if node == goal:
                return path
            
            for (neighbor, weight) in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + weight, neighbor, path))
                 
    return None


def busqueda_greedy(graph, start, goal):
    visited = set()
    queue = [(heuristica[start], start, [])] # Use heuristic value as priority
    
    while queue:
        (_, node, path) = heapq.heappop(queue)
        
        if node not in visited:
            visited.add(node)
            path = path + [node]
            
            if node == goal:
                return path
            
            for (neighbor, weight) in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(queue, (heuristica[neighbor], neighbor, path))                
    return None





print("Busqueda Profundidad (dps)")
print("Busqueda Greedy (grd)")
print("Busqueda costo uniforme (ucs)")
print("A estrella (a))")
tipo = input("Ingrese el tipo de busqueda que desea realizar: ")

if tipo == "dps":
    busqueda_profundidad_recursiva(lista_ady, nodo_inicial)
if tipo == "grd":
    path = busqueda_greedy(lista_ady ,nodo_inicial, nodo_objetivo)
    for nodo in path:
        print(f"{nodo}-> ", end = " ")
if tipo == "ucs":
    path = busqueda_costo_uniforme(lista_ady  ,nodo_inicial, nodo_objetivo)
    for nodo in path:
        print(f"{nodo}-> ", end = " ")
if tipo == "a":
    path = busqueda_profundidad_recursiva(lista_ady, nodo_inicial)

#busqueda_costo_uniforme(lista_ady  ,nodo_inicial, nodo_objetivo)
#busqueda_profundidad_recursiva(lista_ady, nodo_inicial)
