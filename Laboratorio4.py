class Pila:
    def __init__(self):
        self.items = []

    def push(self, elemento):
        self.items.append(elemento)

    def pop(self):
        if not self.esta_vacia():
            return self.items.pop()

    def peek(self):
        if not self.esta_vacia():
            return self.items[-1]

    def esta_vacia(self):
        return len(self.items) == 0


class Cola:
    def __init__(self):
        self.items = []

    def enqueue(self, elemento):
        self.items.append(elemento)

    def dequeue(self):
        if not self.esta_vacia():
            return self.items.pop(0)

    def front(self):
        if not self.esta_vacia():
            return self.items[0]

    def esta_vacia(self):
        return len(self.items) == 0


def invertir_lista(lista):
    pila = Pila()
    for elemento in lista:
        pila.push(elemento)
    lista_invertida = []
    while not pila.esta_vacia():
        lista_invertida.append(pila.pop())
    return lista_invertida


def simulacion_atencion(fila):
    while not fila.esta_vacia():
        print("Atendiendo a:", fila.dequeue())


def parentesis_balanceados(cadena):
    pila = Pila()
    for caracter in cadena:
        if caracter == '(':
            pila.push(caracter)
        elif caracter == ')':
            if pila.esta_vacia():
                return False
            pila.pop()
    return pila.esta_vacia()


class ColaConPilas:
    def __init__(self):
        self.pila_entrada = Pila()
        self.pila_salida = Pila()

    def enqueue(self, elemento):
        self.pila_entrada.push(elemento)

    def dequeue(self):
        if self.pila_salida.esta_vacia():
            while not self.pila_entrada.esta_vacia():
                self.pila_salida.push(self.pila_entrada.pop())
        return self.pila_salida.pop()


def revertir_mitad_cola(cola):
    pila_auxiliar = Pila()
    tamano_cola = len(cola.items)
    mitad = tamano_cola // 2
    for _ in range(mitad):
        pila_auxiliar.push(cola.dequeue())
    while not pila_auxiliar.esta_vacia():
        cola.enqueue(pila_auxiliar.pop())
    for _ in range(mitad):
        cola.enqueue(cola.dequeue())


# Ejemplo de uso
if __name__ == "__main__":
    # 1. Ejemplo de uso de la pila para invertir una lista
    lista_original = [1, 2, 3, 4, 5]
    print("Lista original:", lista_original)
    print("Lista invertida:", invertir_lista(lista_original))

    # 2. Ejemplo de uso de la cola para simular atención
    fila = Cola()
    fila.enqueue("Persona 1")
    fila.enqueue("Persona 2")
    fila.enqueue("Persona 3")
    print("Fila original:", fila.items)
    simulacion_atencion(fila)

    # 3. Ejemplo de uso de la función para verificar paréntesis balanceados
    cadena = "()()((()))"
    print("Los paréntesis están balanceados:", parentesis_balanceados(cadena))

    # 4. Ejemplo de uso de la cola con pilas para simular una cola
    cola = ColaConPilas()
    cola.enqueue(1)
    cola.enqueue(2)
    cola.enqueue(3)
    print(cola.dequeue())  # Output: 1
    print(cola.dequeue())  # Output: 2

    # 5. Ejemplo de uso de la función para revertir la mitad de una cola
    cola_ejemplo = Cola()
    cola_ejemplo.enqueue(1)
    cola_ejemplo.enqueue(2)
    cola_ejemplo.enqueue(3)
    cola_ejemplo.enqueue(4)
    cola_ejemplo.enqueue(5)
    print("Cola original:", cola_ejemplo.items)
    revertir_mitad_cola(cola_ejemplo)
    print("Cola con la mitad revertida:", cola_ejemplo.items)
