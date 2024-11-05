#Universidad Simón Bolívar
#CI-3641 Lenguajes de Programación I - Examen II
#Jesús David Cuéllar Carné 15-10345

#Pregunta 4

from collections import deque

#Subrutina recursiva
def recursive_alpha_beta(n, alpha = 5, beta = 7):
    if 0 <= n < alpha * beta:
        return n
    else:#Se implementa tal cual como una traducción de la fórmula. 
        return (recursive_alpha_beta(n-7) + recursive_alpha_beta(n-14) + recursive_alpha_beta(n-21) + recursive_alpha_beta(n-28) + recursive_alpha_beta(n-35)) 
    

#Subrutina con recursión de cola
def recursive_tail_alpha_beta(n, alpha=5, beta = 7, acc=0):
        if 0 <= n < alpha * beta:
            return n + acc
        else:#se usa un acumulador y este se usa para una llamada
            acc += acc
            return (recursive_alpha_beta(n-7*acc))

#Subrutina iterativa
def iterative_alpha_beta(n, alpha=5, beta=7):
    # Caso base de la función
    base_limit = alpha * beta
    # Cola para simular las llamadas recursivas
    queue = deque([n])
    # Resultado acumulado
    result = 0
    while queue:
        current = queue.popleft()  # Obtenemos el primer elemento de la cola
        if 0 <= current < base_limit:
            # Si estamos en el caso base, sumamos el valor al resultado
            result += current
        else:
            # Si no estamos en el caso base, agregamos los cinco siguientes términos
            queue.extend([current - 7, current - 14, current - 21, current - 28, current - 35])
    
    return result

def main():
    print(recursive_alpha_beta(40))
    print(recursive_tail_alpha_beta(40))
    print(iterative_alpha_beta(40))


if __name__ == "__main__":
    main()




