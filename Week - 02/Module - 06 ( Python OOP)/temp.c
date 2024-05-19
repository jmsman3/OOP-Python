#include <stdio.h>
int main()
{
    char a[10], b[10];
    for (int i = 0; i < 10; i++)
    {
        scanf("%c", &a[i]);
    }
    for (int i = 0; i < 10; i++)
    {
        scanf("%c", &b[i]);
    }
    char res[10], temp[10];
    for( int i = 0; i<10; i++)
    {
       char res = a[i];
    }
    for( int i = 0; i<10; i++)
    {
       char res = b[i];
    }
    for( int i = 0; i<10; i++)
    {
        if(res[i] == res[i+1])
        {
            char temp = res[i];
        }
    }
    printf("%c", temp);
    return 0;
}