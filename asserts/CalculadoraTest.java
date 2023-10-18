// Realiza los asserts de la clase calculadora en sus métodos.

package asserts;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertThrows;
import org.junit.Test;

public class CalculadoraTest {

    @Test
    public void testAdd() {
        Calculadora calculadora = new Calculadora();
        assertEquals(10, calculadora.add(5,5));
        assertEquals(2, calculadora.add(-5,7));
    }

    @Test
    public void testSubstract() {
        Calculadora calculadora = new Calculadora();
        assertEquals(7, calculadora.substract(10, 3));
        assertEquals(-3, calculadora.substract(0, 3));
    }


    @Test
    public void testMultiply() {
        Calculadora calculadora = new Calculadora();
        assertEquals(15, calculadora.multiply(3, 5));
        assertEquals(0, calculadora.multiply(0, 10));
    }

    @Test
    public void testDivide() {
        Calculadora calculadora = new Calculadora();
        assertEquals(50, calculadora.divide(100, 2), 0.001);
        assertEquals(0.02, calculadora.divide(2, 100), 0.001);

        assertThrows(ArithmeticException.class, () -> calculadora.divide(2, 0));
    }
}
