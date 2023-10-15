import java.util.InputMismatchException;
import java.util.Scanner;

/* Ejercicio 3: Acceso a Elemento de Arreglo 
Escribe un programa que solicite al usuario ingresar un índice y acceda a un elemento en un arreglo predefinido. 
Utiliza el manejo de excepciones para capturar excepciones que puedan ocurrir si el índice está fuera del rango del arreglo 
y muestra un mensaje de error apropiado. */

public class accesoArreglo {
    public static void main(String[] args) {
        int[] a = {2,8,9,10,25,1};

        Scanner sc = new Scanner(System.in);

        try {
            System.out.print("Ingresa un indice: ");
            int i = sc.nextInt();

            if (i >= 0 && i < a.length) {
                System.out.println("Elemento #" + i + ": " + a[i]);
            } else {
                System.out.println("Ese indice no existe");
            }
        } catch (InputMismatchException e) {
            System.out.println("¡Error! Ingresa un número entero válido.");
        }

        sc.close();
    }
}