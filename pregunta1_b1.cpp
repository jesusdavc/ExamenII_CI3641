#include <iostream>
using namespace std;

// Función f(n) que define las reglas de la función
int f(int n) {
    if (n % 2 == 0) {
        return n / 2;
    } else {
        return 3 * n + 1;
    }
}

// Función dist(n) que aplica f de manera repetida y cuenta las aplicaciones hasta llegar a 1
int dist(int n) {
    int count = 0;
    while (n != 1) {
        n = f(n);
        count++;
    }
    return count;
}

int main() {
    int n = 42;
    //cout << "Ingrese un numero entero: ";
    //cin >> n;
    cout << "count(" << n << ") = " << dist(n) << endl;
    return 0;
}
