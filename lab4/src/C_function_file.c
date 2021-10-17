#include <stdio.h>

int ADD(int num_1, int num_2){
    printf("[C] ADD function running ...\n");
    printf("[C] num_1 = %d\n", num_1);
    printf("[C] num_2 = %d\n", num_2);

    int sum = num_1 + num_2;

    printf("\n[C] sum = %d\n", sum);

    return sum;
}
