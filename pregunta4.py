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
    
print(recursive_alpha_beta(36))