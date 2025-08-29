print("Algoritmo del Cifrado Vigen�re en Python con implementaci�n de metodolog�a Kasiski")

from collections import Counter

# Alfabeto con � incluido
alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', '�', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Funciones para encriptaci�n de descencriptaci�n
def encriptacionVigenere(M, K):
    return (M + K) % len(alfabeto)

def desencriptacionVigenere(C, K):
    return (C - K) % len(alfabeto)

# Cifrado Vigen�re
def cifrar_vigenere(mensaje, clave):
    mensaje = mensaje.upper()  
    clave = clave.upper()
    textoCifrado = ""
    j = 0
    for i in range(len(mensaje)):
        if mensaje[i] in alfabeto:
            posM = alfabeto.index(mensaje[i])
            posK = alfabeto.index(clave[j % len(clave)])
            nuevaPos = encriptacionVigenere(posM, posK)
            textoCifrado += alfabeto[nuevaPos]
            j += 1
        else:
            textoCifrado += mensaje[i]
    return textoCifrado

# Descifrado Vigen�re
def descifrar_vigenere(cifrado, clave):
    cifrado = cifrado.upper()
    clave = clave.upper()
    textoDescifrado = ""
    j = 0
    for i in range(len(cifrado)):
        if cifrado[i] in alfabeto:
            posC = alfabeto.index(cifrado[i])
            posK = alfabeto.index(clave[j % len(clave)])
            nuevaPos = desencriptacionVigenere(posC, posK)
            textoDescifrado += alfabeto[nuevaPos]
            j += 1
        else:
            textoDescifrado += cifrado[i]
    return textoDescifrado

# Implementaci�n del Ataque Kasiski 
def encontrar_repeticiones(cifrado, min_len=3):
    posiciones = {}
    for i in range(len(cifrado) - min_len + 1):
        sub = cifrado[i:i+min_len]
        if sub in posiciones:
            posiciones[sub].append(i)
        else:
            posiciones[sub] = [i]
    repeticiones = {k:v for k,v in posiciones.items() if len(v) > 1}
    return repeticiones

def factores_distancias(repeticiones):
    factores = []
    for indices in repeticiones.values():
        for i in range(len(indices)-1):
            distancia = indices[i+1] - indices[i]
            for f in range(2, distancia+1):
                if distancia % f == 0:
                    factores.append(f)
    return factores

def kasiski(cifrado):
    repes = encontrar_repeticiones(cifrado)
    factores = factores_distancias(repes)
    if not factores:
        print("No se encontraron repeticiones para aplicar Kasiski.")
        return []
    conteo = Counter(factores)
    # Retorna las 3 longitudes de clave m�s probables
    candidatos = [f for f, _ in conteo.most_common(3)]
    print("Las longitudes de clave m�s probables seg�n Kasiski son:", candidatos)
    return candidatos

# Men� principal con Kasiski
def main():
    opcion = input("�Desea cifrar o descifrar un texto? (cifrar = 1,descifrar = 2): ").strip().lower()

    if opcion == "1":
        clave = input("Ingrese la clave: ").upper()
        texto = input("Ingrese el texto que desea cifrar: ").upper()
        textoCifrado = cifrar_vigenere(texto, clave)
        print("Texto cifrado:", textoCifrado)

    elif opcion == "2":
        metodo = input("�Desea ingresar la clave o usar Kasiski? (clave = 1 / Kasinski = 2): ").strip().lower()
        texto = input("Ingrese el texto a descifrar: ").upper()

        if metodo == "1":
            clave = input("Ingrese la clave: ").upper()
            textoDescifrado = descifrar_vigenere(texto, clave)
            print("Texto descifrado:", textoDescifrado)

        elif metodo == "2":
            candidatos = kasiski(texto)
            print("Usando Kasiski, intente con cada longitud candidata para deducir la clave.")
            print("Nota: Este programa solo sugiere longitudes de clave, el an�lisis de frecuencia para encontrar la clave completa debe hacerse aparte.")

        else:
            print("Opci�n no v�lida.")
    else:
        print("Opci�n no v�lida.")


while True:
    main()