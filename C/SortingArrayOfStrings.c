#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Solution.

int lexicographical_sort(const char* a, const char* b)
{
    return strcmp(a, b);
}

int lexicographical_sort_revers(const char* a, const char* b)
{
    return strcmp(a, b) >= 0 ? 0 : 1;
}

int sort_by_number_of_distinct_characters(const char* a, const char* b)
{
    int i = 0, j = 0;
    int a_sum = 0, b_sum = 0;
    int a_chars[26] = { 0 };
    int b_chars[26] = { 0 };

    while(a[i] != '\0' || b[j] != '\0')
    {
        if(a[i] != '\0')
        {
            if(a_chars[122 - a[i]] == 0)
            {
                a_chars[122 - a[i]]++;
                a_sum++;
            }
            i++;
        }

        if(b[j] != '\0')
        {
            if(b_chars[122 - b[j]] == 0)
            {
                b_chars[122 - b[j]]++;
                b_sum++;
            }
            j++;
        }
    }
    if(a_sum > b_sum)
    {
        return 1;
    }
    else if(a_sum < b_sum)
    {
        return 0;
    }
    else
    {
        return lexicographical_sort(a, b);
    }
}

int sort_by_length(const char* a, const char* b)
{
    int a_length = strlen(a);
    int b_length = strlen(b);

    if(a_length > b_length)
    {
        return 1;
    }
    else if(a_length < b_length)
    {
        return 0;
    }
    else
    {
        return lexicographical_sort(a, b);
    }
}

void string_sort(char** arr, const int len, int(*cmp_func)(const char* a, const char* b))
{
    char* temp;
    for(int i = 0; i < len; i++)
    {
        for(int j = 0; j < (len - i - 1); j++)
        {
            if(cmp_func(*(arr + j), *(arr + j + 1)) > 0)
            {
                temp = *(arr + j);
                *(arr + j) = *(arr + j + 1);
                *(arr + j + 1) = temp;
            }
        }
    }
}


// DEFAULT CODE **********************************************

int main()
{
    int n;
    printf("Number of strings: ");
    scanf("%d", &n);

    char** arr;
	arr = (char**)malloc(n * sizeof(char*));

    for(int i = 0; i < n; i++)
    {
        *(arr + i) = malloc(1024 * sizeof(char));
        printf("String %d: ", i);
        scanf("%s", *(arr + i));
        *(arr + i) = realloc(*(arr + i), strlen(*(arr + i)) + 1);
    }

    string_sort(arr, n, lexicographical_sort);
    for(int i = 0; i < n; i++)
    {
        printf("%s\n", arr[i]);
    }
    printf("\n");

    string_sort(arr, n, lexicographical_sort_revers);
    for(int i = 0; i < n; i++)
    {
        printf("%s\n", arr[i]);
    }
    printf("\n");

    string_sort(arr, n, sort_by_number_of_distinct_characters);
    for(int i = 0; i < n; i++)
    {
        printf("%s\n", arr[i]);
    }
    printf("\n");

    string_sort(arr, n, sort_by_length);
    for(int i = 0; i < n; i++)
    {
        printf("%s\n", arr[i]);
    }
    printf("\n");

    return 0;
}

