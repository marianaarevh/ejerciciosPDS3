import java.util.InputMismatchException;
import java.util.Scanner;

/* Ejercicio 2: División Segura 
Escribe un programa que solicite al usuario ingresar dos números y realice una división segura. 
Utiliza el manejo de excepciones para capturar excepciones que puedan ocurrir durante la división 
(por ejemplo, división por cero) 
y muestra un mensaje de error apropiado en caso de excepción. */

public class divisionSegura {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        try {
            System.out.print("Ingresa un numero (numerador): ");
            int numerador = sc.nextInt();

            System.out.print("Ingresa otro numero (denominador): ");
            int denominador = sc.nextInt();

            if (denominador != 0) {
                double resultado = (double) numerador/denominador;
                System.out.printf("%d / %d = %.2f\n", numerador, denominador, resultado);
            } else {
                System.out.println("La division no es segura :(( el denominador no puede ser 0. Intenta de nuevo.");
            }
        } catch (InputMismatchException e) {
            System.out.println("¡Error! Ingresa un número entero válido.");
        }
        sc.close();
    }
}