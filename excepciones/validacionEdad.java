import java.util.InputMismatchException;
import java.util.Scanner;


/* Ejercicio 1: 
Validación de Edad Escribe un programa que solicite al usuario ingresar su edad. 
Utiliza el manejo de excepciones para asegurarte de que la edad ingresada sea un número válido (mayor que 0) 
y captura cualquier excepción que pueda ocurrir. 
Muestra un mensaje de error apropiado si se ingresa una edad no válida. */

public class validacionEdad {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Ingresa tu edad: ");

        try {
            int edad = sc.nextInt();
            if (edad > 0) {
                System.out.println("Edad: " + edad);
            } else {
                System.out.println("!!!! Debe ser mayor que 0");
            }
        } catch (InputMismatchException  ex) {
            System.out.println("¡Error! Ingresa un número entero válido");
        }

        sc.close();
    }
}