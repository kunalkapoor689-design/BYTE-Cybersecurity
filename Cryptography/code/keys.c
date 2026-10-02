#include <stdio.h>
int main()
{
    char p_text[] = "BYTE";
    char c_text[] = "BAIN";
    printf("The beaufort key is ");
    for (int i = 0; i < 4; i++)
    {
        int p = p_text[i] - 'A';
        int c = c_text[i] - 'A';
        int beaufort_key = (p + c) % 26;
        printf("%c", beaufort_key + 'A');
    }
    printf("\nThe vignere key is ");
    for (int i = 0; i < 4; i++)
    {
        int p = p_text[i] - 'A';
        int c = c_text[i] - 'A';
        int vignere_key = (c - p + 26) % 26;
        printf("%c", vignere_key + 'A');
    }
}

 

