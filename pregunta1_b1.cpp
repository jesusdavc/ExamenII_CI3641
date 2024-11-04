//Universidad Simón Bolívar
//CI-3641 Lenguajes de Programación I - Examen II
//Jesús David Cuéllar Carné 15-10345

//Pregunta 1.b i

#include <iostream>
using namespace std;

//Función f(n) que se define a partir de las reglas dadas
//en el enunciado. 
int f(int n) {
    if (n % 2 == 0) {
        return n / 2;
    } else {
        return 3 * n + 1;
    }
}

// Función dist(n) que aplica f de manera repetida 
// y cuenta las aplicaciones hasta llegar a 1
int dist(int n) {
    int count = 0;
    while (n != 1) {
        n = f(n);
        count++;
    }
    return count;
}
//Se ejecuta el programa principal. 
int main() {
    int n = 42; //Se usa el ejemplo dado en el enunciado
    //cout << "Ingrese un numero entero: ";
    //cin >> n;
    cout << "count(" << n << ") = " << dist(n) << endl;
    return 0;
}
