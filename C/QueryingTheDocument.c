#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#define MAX_CHARACTERS 1005
#define MAX_PARAGRAPHS 5

// SOLUTION *************************************************+

char**** get_document(char* text)
{
    char**** final = (char****)malloc(sizeof(char***));
    *final = (char***)malloc(sizeof(char**));
    *(*final) = (char**)malloc(sizeof(char*));

    int p = 0, s = 0, w = 0, i = 0, prov = 0;

    while(text[i] != '\0')
    {
        if(text[i] == ' ')
        {
            *(*(*(final + p) + s) + w) = (char*)malloc((i + 1 - prov) * sizeof(char));
            memset(*(*(*(final + p) + s) + w), '\0', (i + 1 - prov) * sizeof(char));
            strncpy(*(*(*(final + p) + s) + w), &text[prov], i - prov);
            printf("%s\n", *(*(*(final + p) + s) + w));
            w++;
            prov = i + 1;
            *(*(final + p) + s) = (char**)realloc(*(*(final + p) + s), (w + 1) * sizeof(char*));
        }
        else if(text[i] == '.')
        {
            *(*(*(final + p) + s) + w) = (char*)malloc((i + 1 - prov) * sizeof(char));
            memset(*(*(*(final + p) + s) + w), '\0', i + 1 - prov);
            strncpy(*(*(*(final + p) + s) + w), &text[prov], i - prov);
            printf("%s\n", *(*(*(final + p) + s) + w));
            w = 0;
            s++;
            prov = i + 1;
            *(final + p) = (char***)realloc(*(final + p), (s + 1) * sizeof(char**));
            *(*(final + p) + s) = (char**)malloc(sizeof(char*));

        }
        else if(text[i] == '\n')
        {
            *(final + p) = (char***)realloc(*(final + p), s * sizeof(char**));
            s = 0;
            p++;
            prov++;
            final = (char****)realloc(final, (p + 1) * sizeof(char***));
            *(final + p) = (char***)malloc(sizeof(char**));
            *(*(final + p)) = (char**)malloc(sizeof(char*));
        }
        i++;
    }
    *(final + p) = (char***)realloc(*(final + p), s * sizeof(char**));

    return final;
}

// DEFAULT CODE ************************************

char* get_input_text()
{
    int paragraph_count;
    printf("Paragraph count: ");
    scanf("%d", &paragraph_count);

    char p[MAX_PARAGRAPHS][MAX_CHARACTERS], doc[MAX_CHARACTERS];
    memset(doc, 0, sizeof(doc));
    getchar();
    printf("%s\n", doc);
    for (int i = 0; i < paragraph_count; i++)
    {
        printf("String %d: ", i);
        scanf("%[^\n]%*c", p[i]);
        strcat(doc, p[i]);
        if (i != paragraph_count - 1)
            strcat(doc, "\n");
    }

    char* returnDoc = (char*)malloc((strlen (doc)+1) * (sizeof(char)));
    strcpy(returnDoc, doc);
    printf("%s\n", doc);
    return returnDoc;
}

char* kth_word_in_mth_sentence_of_nth_paragraph(char**** document, int k, int m, int n)
{
    return *(*(*(document + n - 1) + m - 1) + k - 1);
}

char** kth_sentence_in_mth_paragraph(char**** document, int k, int m)
{
    return *(*(document + m - 1) + k - 1);
}

char*** kth_paragraph(char**** document, int k)
{
    return *(document + k - 1);
}

void print_word(char* word)
{
    printf("%s", word);
}

void print_sentence(char** sentence)
{
    int word_count;
    printf("Enter number of words: ");
    scanf("%d", &word_count);
    for(int i = 0; i < word_count; i++)
    {
        printf("%s", sentence[i]);
        if(i != word_count - 1) printf(" ");
    }
}

void print_paragraph(char*** paragraph)
{
    int sentence_count;
    printf("Number of sentences: ");
    scanf("%d", &sentence_count);
    for(int i = 0; i < sentence_count; i++)
    {
        print_sentence(*(paragraph + i));
        printf(".");
    }
}


int main()
{
    char* text = get_input_text();
    char**** document = get_document(text);

    int q;
    printf("Queries: ");
    scanf("%d", &q);

    while(q--)
    {
        int type;
        printf("Type of querie: ");
        scanf("%d", &type);

        if(type == 3)
        {
            int k, m, n;
            printf("Enter 'k', 'm' & 'n': ");
            scanf("%d %d %d", &k, &m, &n);
            char *word = kth_word_in_mth_sentence_of_nth_paragraph(document, k, m, n);
            print_word(word);
        }
        else if (type == 2)
        {
            int k, m;
            printf("Enter 'k' & 'm': ");
            scanf("%d %d", &k, &m);
            char** sentence = kth_sentence_in_mth_paragraph(document, k, m);
            print_sentence(sentence);
        }
        else
        {
            int k;
            printf("Enter 'k': ");
            scanf("%d", &k);
            char*** paragraph = kth_paragraph(document, k);
            print_paragraph(paragraph);
        }
        printf("\n");
    }

    return 0;
}
