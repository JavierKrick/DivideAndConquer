import java.util.Scanner;

public class VacasEnojadas {

    public static void algoritmoDeFloyd(int[] arr, int n, int i) {
        int maxi = i;  // Inicializar el mayor como la raíz
        int NodoIzq = 2 * i + 1;  // hijo izquierdo
        int NodoDer = 2 * i + 2;  // hijo derecho

        // ¿hijo izquierdo es más grande que la raíz?
        if (NodoIzq < n && arr[NodoIzq] > arr[maxi]) {
            maxi = NodoIzq;
        }

        // ¿erificar si el hijo derecho es más grande el más grande?
        if (NodoDer < n && arr[NodoDer] > arr[maxi]) {
            maxi = NodoDer;
        }

        // Si el mayor no es la raíz
        if (maxi != i) {
            int aux = arr[i];
            arr[i] = arr[maxi];
            arr[maxi] = aux;  // intercambiar

            // Recursivamente aplicar algoritmoDeFloyd en el subárbol afectado
            algoritmoDeFloyd(arr, n, maxi);
        }
    }

    public static void ordenarConMaxHeapInPlace(int[] arr) {
        int n = arr.length;

        // Construir un max-heap
        for (int i = n / 2 - 1; i >= 0; i--) {
            algoritmoDeFloyd(arr, n, i);
        }

        // Extraer elementos uno por uno (desde la mitad hsta el incio)
        for (int i = n - 1; i > 0; i--) {
            int aux = arr[0];
            arr[0] = arr[i];
            arr[i] = aux;  // intercambiar el mayor elemento con el último
            algoritmoDeFloyd(arr, i, 0);  // heapificar el resto de la lista
        }
    }

    public static boolean entranLasVacas(int vacas, int N, int[] posiciones, int d) {
        // La idea es ver si dado una distancia d entran las vacas
        if (vacas == 0) {
            return true;
        } else {
            int vacasRestantes = vacas - 1;
            int ultimaPosicion = posiciones[0];
            int i = 1;

            while (vacasRestantes > 0 && i < N) {
                int distancia = posiciones[i] - ultimaPosicion;
                if (distancia >= d) {
                    vacasRestantes--;
                    ultimaPosicion = posiciones[i];
                }
                i++;
            }

            return vacasRestantes == 0;
        }
    }

    public static int busquedaBinariaDeDistancias(int vacas, int N, int[] posiciones) {
        // La idea es buscar el último True de una serie de T T T T F F F F F F F F F F F F 
        // obvio que no calculo todos los true sino los que
        // Lo voy a usar con las distancias
        int izq = 1;
        int der = posiciones[N - 1] - posiciones[0];
        int res = 1;  // para guardar la última posición del True

        while (izq <= der) {
            int medio = (izq + der) / 2;

            boolean hay = entranLasVacas(vacas, N, posiciones, medio);

            if (hay) {
                res = medio;  // Guardo la posición
                izq = medio + 1;
            } else {
                der = medio - 1;  // Descartar la mitad derecha
            }
        }

        return res;
    }

    public static int vacasEnojadas(int N, int vacas, int[] posiciones) {
        ordenarConMaxHeapInPlace(posiciones);  // ordenar ascendentemente
        return busquedaBinariaDeDistancias(vacas, N, posiciones);
    }

    public static void main(String[] args) {

        // uso de Scanner 
        Scanner scanner = new Scanner(System.in);
        
        int t = scanner.nextInt();

        for (int i = 0; i < t; i++) {
            
            int N = scanner.nextInt();
            int vacas = scanner.nextInt();

            
            int[] posiciones = new int[N];
            for (int j = 0; j < N; j++) {
                posiciones[j] = scanner.nextInt();
            }
            
            int resultado = vacasEnojadas(N, vacas, posiciones);
            System.out.println(resultado);
        }
        
        scanner.close();
    }
}
