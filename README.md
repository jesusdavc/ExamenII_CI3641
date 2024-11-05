# Examen II CI-3641:

Aquí estaran las instrucciones o comentarios sobre el código para el Examen II

## Pregunta 1b: 

Se implemento en C++, dentro del código se documenta el funcionamiento. Se uso el compilador G++. 

## Pregunta 2: 

Se tiene una primera versión. Tiene detalle en la impresión de la acción MOSTRAR hay parentización de más. 
Faltan pruebas unitarias. 

## Pregunta 4:

Las tres versiones: Recursiva, Recursiva de Cola e Iterativa se encuentran implementadas. Estan en el archivo **pregunta4.py**

### Analisis
Al probar las implementaciones varias veces se puede notar que la versión iterativa consume mucho más tiempo de ejecución. Sin emebargo la diferencia entre la recursión y la recursión de cola si bien entre ellas no es mucha si se ve la tendencia a que la recursión de cola es mucho más rápida. 

Para ejecuciones desde 1 al 35
```
+-------------------+----------------------------+
|  Implementación   | Tiempo promedio (segundos) |
+-------------------+----------------------------+
|     Recursión     |   4.427773611886161e-07    |
| Recursión de Cola |   2.2479466029575892e-07   |
|     Iterativa     |   3.0245099748883927e-06   |
+-------------------+----------------------------+

```
Para ejecuciones desde 36 al 40
```
+-------------------+----------------------------+
|  Implementación   | Tiempo promedio (segundos) |
+-------------------+----------------------------+
|     Recursión     |   1.0132789611816406e-06   |
| Recursión de Cola |   1.1920928955078125e-06   |
|     Iterativa     |   1.8477439880371094e-06   |
+-------------------+----------------------------+

```

Para ejecuciones desde 36 al 100
```
+-------------------+----------------------------+
|  Implementación   | Tiempo promedio (segundos) |
+-------------------+----------------------------+
|     Recursión     |   5.033239722251892e-05    |
| Recursión de Cola |   4.4327229261398315e-05   |
|     Iterativa     |   3.496930003166199e-05    |
+-------------------+----------------------------+

```
Pero cuando tenemos números más grandes es más rapida la iterativa. Y se intenta con numeros más grandes la recursiva arroja errores o se demora en ejecutar. 

Entonces se podría concluir que para cantidades pequeñas es mejor la recursión, en especial la recursión de cola. Sin embargo si se aumenta la cantidad es mejor usar la iterativa hasta cierto punto.
