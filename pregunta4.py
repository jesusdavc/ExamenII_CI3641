#Universidad Simón Bolívar
#CI-3641 Lenguajes de Programación I - Examen II
#Jesús David Cuéllar Carné 15-10345

#Pregunta 4

#Subrutina recursiva

def recursive_alpha_beta(n, alpha = 5, beta = 7):
    if 0 <= n < alpha * beta:
        return n
    else:
        return (recursive_alpha_beta(n-7) + recursive_alpha_beta(n-14) + recursive_alpha_beta(n-21) + recursive_alpha_beta(n-28) + recursive_alpha_beta(n-35)) 
    

#Subrutina con recursión de cola

def recursive_tail_alpha_beta(n, alpha=5, beta = 7, acc=0):
        if 0 <= n < alpha * beta:
            return n + acc
        else:
            acc += acc
            return (recursive_alpha_beta(n-7*acc))

def main():
    print(recursive_alpha_beta(40))
    print(recursive_tail_alpha_beta(40))

if __name__ == "__main__":
    main()




