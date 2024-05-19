#include <stdio.h>
#include <string.h>

void show_bb_roshona_bilash(char arr[][100], int length)
{
    printf("\n=== BiyeBari ROSHONA BILASH ===\n\n");
    int i;
    for (i = 0; i < length; i++)
    {
        printf("%d. %s\n", i + 1, arr[i]);
    }
    printf("\n\n");
}

void show_bb_thala(char arr[][200], int length)
{
    printf("\n\n==== BiyeBari THALA ====\n\n");
    int i;
    for (i = 0; i < length; i++)
    {
        printf("%d. %s\n", i + 1, arr[i]);
    }
    printf("\n\n");
}

void bb_cover()
{
    printf("\n\n=====Welcome To Biye Bari=====\n\n");
    printf("\n1. MENU\n");
    printf("\n2. OFFERS\n");
    printf("\n3. EVENTS\n");
    printf("\n4. CONTACTS\n");
    printf("\n5. RESERVATION\n");
    printf("\n6. HOME DELIVERY\n\n");
}

int main()
{

    char bb_roshona_bilash[][100] = {
        "Kachchi (Bashmoti)             280/-",
        "Beef Tehari                    220/-",
        "Morog Polao                    245/-",
        "Plain Polao                    120/-",
        "Mutton Leg Roast               380/-",
        "Achari Beef                    260/-",
        "Chicken Roast                  155/-",
        "Chingri Malaikari              355/-",
        "Rupchada Fry                   420/-",
        "Jali Kabab                     65/-",
    };
    char bb_thala[][200] = {
        "BiyeBari Special Kachchi (Bashmoti),           250/-(1 Person)\n   kabab Chicken Roast, Salad, Firni/Jorda        1180/-(2 Person)\n   Soft Drinks / Borhani                          2240/-(4 Person)",

    };
start_1:
    bb_cover();

    int choice_1, choice_2;

    printf("\n\nChoose Your Option: ");
    scanf("%d", &choice_1);
    switch (choice_1)
    {
    case 1:
    start_2:
        printf("\n1. All Menu At A Glance");
        printf("\n2. Roshona Bilash");
        printf("\n3. Biye Bari Thala"); // Roshona Bilash
        printf("\n4. Mistanno");
        printf("\n5. Pan Bahar\n\n");

        int a;
        printf("\nChoose Your Menu: ");
        scanf("%d", &a);
        switch (a)
        {
        case 1:
            show_bb_roshona_bilash(bb_roshona_bilash, 10);
            show_bb_thala(bb_thala, 1);
            goto jump;
            // break;
        case 2:
            // printf("\n=== BiyeBari ROSHONA BILASH ===\n\n");
            show_bb_roshona_bilash(bb_roshona_bilash, 10);
            // goto jump;

            printf("\n0. Go Back");
            printf("\n1. See More Items\n\n");
            // goto start_2;

            printf("\n\nChoose Your Option: ");
            scanf("%d", &choice_2);

            switch (choice_2)
            {
            case 0:
                goto start_1;
            case 1:
                goto start_2;
            }
        case 3:
            //            printf("\n\n==== BiyeBari THALA ====\n");
            show_bb_thala(bb_thala, 1);
            goto jump;
        }
    }
jump:
    printf("\n0. Go Back");
    printf("\n1. See More Items\n\n");
    // goto start_2;

    printf("\n\nChoose Your Option: ");
    scanf("%d", &choice_2);

    switch (choice_2)
    {
    case 0:
        goto start_1;
    case 1:
        goto start_2;
    }

    return 0;
}
