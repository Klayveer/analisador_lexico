#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int opcao, i;
    int numeros[5];
    srand(time(NULL));

    while (1) {
        printf("\n1 - Gerar numeros aleatorios\n");
        printf("2 - Somar numeros\n");
        printf("3 - Encontrar maior numero\n");
        printf("4 - Sair\n");
        printf("Opcao: ");
        scanf("%d", &opcao);

        if (opcao == 1) {
            for (i = 0; i < 5; i++) {
                numeros[i] = rand() % 100;
            }
            printf("Numeros gerados: ");
            for (i = 0; i < 5; i++) printf("%d ", numeros[i]);
            printf("\n");
        }

        else if (opcao == 2) {
            int soma = 0;
            for (i = 0; i < 5; i++) soma += numeros[i];
            printf("Soma: %d\n", soma);
        }

        else if (opcao == 3) {
            int maior = numeros[0];
            for (i = 1; i < 5; i++) {
                if (numeros[i] > maior) maior = numeros[i];
            }
            printf("Maior numero: %d\n", maior);
        }

        else if (opcao == 4) {
            break;
        }

        else {
            printf("Opcao invalida!\n");
        }
    }

    return 0;
}
