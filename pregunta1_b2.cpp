//Universidad Simón Bolívar
//CI-3641 Lenguajes de Programación I - Examen II
//Jesús David Cuéllar Carné 15-10345

//Pregunta 1.b ii - Algoritmo MergeSort

//A continuación se implementa el algoritmo Merge Sort. Se usa la 
//función mergeSort y merge para primero separar el arreglo 
//a la mitad  e ir separando en subarreglos 
//que se pueden ir ordenando. 
//dentro de la función merge se utilizan arreglos temporales para 
//ir almacenando los subarreglas mientras se ordenan.
// Además se llama de manera recursiva a mergesort para cada subarreglo
//y así queda más sencillo aplicar merge a cada uno hasta obtener el arreglo original. 
//Aunque se usan varios ciclos en merge, y pareciera que podría ser lento al implementar ciclos en C++
//se tiene la ventaja del diseño del lenguaje sea más rapido que usando otro lenguaje. 

#include <iostream>
#include <vector>

using namespace std;

// Función que mezcla dos subarreglos en uno solo ordenado
void merge(vector<int>& arr, int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;

    // Crear arreglos temporales
    vector<int> L(n1), R(n2);

    // Copiar datos a los arreglos temporales
    for (int i = 0; i < n1; ++i)
        L[i] = arr[left + i];
    for (int j = 0; j < n2; ++j)
        R[j] = arr[mid + 1 + j];

    // Combinar los subarreglos
    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            ++i;
        } else {
            arr[k] = R[j];
            ++j;
        }
        ++k;
    }

    // Copiar los elementos restantes de L, si quedan
    while (i < n1) {
        arr[k] = L[i];
        ++i;
        ++k;
    }

    // Copiar los elementos restantes de R, si quedan
    while (j < n2) {
        arr[k] = R[j];
        ++j;
        ++k;
    }
}

// Función de ordenación Merge Sort
void mergeSort(vector<int>& arr, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;

        // Ordenar la primera y segunda mitad
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);

        // Mezclar las dos mitades ordenadas
        merge(arr, left, mid, right);
    }
}

int main() {
    vector<int> arr = {12, 11, 13, 5, 16, 7};

    cout << "Array original: ";
    for (int val : arr)
        cout << val << " ";
    cout << endl;

    mergeSort(arr, 0, arr.size() - 1);

    cout << "Array ordenado: ";
    for (int val : arr)
        cout << val << " ";
    cout << endl;

    return 0;
}
