#Universidad Simón Bolívar
#CI-3641 Lenguajes de Programación I - Examen II
#Jesús David Cuéllar Carné 15-10345

#Pregunta 4

from collections import deque
import time

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
    # Dentro del programa principal declaramos tres arreglos donde
    # guardaremos los resultados de varias llamadas con varios valores
    # a estas llamadas se les calcula el tiempo de visualización usando 
    # la libreria time. Ahora bien luego con esos resultados se saca el tiempo de ejecución promedio para
    # cada implementación y de allí se pueden sacar algunas concluciones.
    recursive_alpha_beta_results =[]
    recursive_tail_alpha_beta_results =[]
    iterative_alpha_beta_results = []
    temporal = 0
    media_r = 0
    media_rt = 0
    media_i = 0
    for i in range(36,40):

        t1 = time.time() 
        recursive_alpha_beta(i)
        f1 = time.time()
        e1 = f1 - t1
        recursive_alpha_beta_results.append(e1)

        t2 = time.time() 
        recursive_tail_alpha_beta(i)
        f2 = time.time()
        e2 = f2 - t2
        recursive_tail_alpha_beta_results.append(e2)
        
        t3 = time.time() 
        iterative_alpha_beta(i)
        f3 = time.time()
        e3 = f3 - t3
        iterative_alpha_beta_results.append(e3)

    for i in recursive_alpha_beta_results:
        temporal += i
    media_r = temporal/len(recursive_alpha_beta_results)
    temporal = 0

    for i in recursive_tail_alpha_beta_results:
        temporal += i
    media_rt = temporal/len(recursive_tail_alpha_beta_results)
    temporal = 0

    for i in iterative_alpha_beta_results:
        temporal += i
    media_i = temporal/len(iterative_alpha_beta_results)
    temporal = 0

    print(f'La media de ejecuión de la recursión fue:         {media_r}')
    print(f'La media de ejecuión de la recursión de cola fue: {media_rt}')
    print(f'La media de ejecuión de la versión iterativa    : {media_i}')
if __name__ == "__main__":
    main()




