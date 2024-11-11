// hello.c
#include <stdio.h>

int main() {
    printf("Hello, World!\n");

    char name[50];
    printf("Введите ваше имя: ");
    scanf("%49s", name);
    printf("Привет, %s!\n", name)
    return 0;
}