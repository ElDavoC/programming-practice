#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#define MAX_CHARACTERS 1005
#define MAX_PARAGRAPHS 5

struct word {
    char* data;
};

struct sentence {
    struct word* data;
    int word_count;//denotes number of words in a sentence
};

struct paragraph {
    struct sentence* data  ;
    int sentence_count;//denotes number of sentences in a paragraph
};

struct document {
    struct paragraph* data;
    int paragraph_count;//denotes number of paragraphs in a document
};

// SOLUTION       ***********************************

struct document get_document(char* text) {
    struct document doc;
    int i, j, k, m, prov;
    m = prov = i = j = k = 0;
    doc.data = malloc(sizeof(struct paragraph));
    doc.paragraph_count = 0;
    doc.data[i].data = malloc(sizeof(struct sentence));
    doc.data[i].sentence_count = 0;
    doc.data[i].data[j].data = malloc(sizeof(struct word));
    doc.data[i].data[j].word_count = 0;

    while(text[m] != '\0'){
        if(text[m] == ' ') {
            doc.data[i].data[j].word_count = k > 0 ? ++doc.data[i].data[j].word_count : 1;
            doc.data[i].data[j].data = realloc(doc.data[i].data[j].data, sizeof(struct word) * doc.data[i].data[j].word_count);
            doc.data[i].data[j].data[k].data = malloc((m + 1 - prov) * sizeof(char));
            memset(doc.data[i].data[j].data[k].data, '\0', (m + 1 - prov) * sizeof(char));
            strncpy(doc.data[i].data[j].data[k].data, &text[prov], m - prov);
            k++;
            prov = m + 1;
        }
        else if(text[m] == '.') {
            doc.data[i].data[j].word_count = k > 0 ? ++doc.data[i].data[j].word_count : 1;
            doc.data[i].data[j].data = realloc(doc.data[i].data[j].data, sizeof(struct word) * doc.data[i].data[j].word_count);
            doc.data[i].data[j].data[k].data = malloc((m + 1 - prov) * sizeof(char));
            memset(doc.data[i].data[j].data[k].data, '\0', (m + 1 - prov) * sizeof(char));
            strncpy(doc.data[i].data[j].data[k].data, &text[prov], m - prov);
            doc.data[i].sentence_count = j > 0 ? ++doc.data[i].sentence_count : 1;
            doc.data[i].data = realloc(doc.data[i].data, sizeof(struct sentence) * (doc.data[i].sentence_count + 1));

            k = 0;
            j++;
            prov = m + 1;

            doc.data[i].data[j].data = malloc(sizeof(struct word));
        }
        else if(text[m] == '\n') {
            free(doc.data[i].data[j].data);
            doc.data[i].data = realloc(doc.data[i].data, sizeof(struct sentence) * (doc.data[i].sentence_count));


            doc.paragraph_count = i > 0 ? ++doc.paragraph_count : 2;
            doc.data = realloc(doc.data, sizeof(struct paragraph) * doc.paragraph_count);

            j = 0;
            i++;
            prov++;

            doc.data[i].data = malloc(sizeof(struct sentence));
            doc.data[i].data[j].data = malloc(sizeof(struct word));
        }
        m++;
    }
    free(doc.data[i].data[j].data);
    doc.data[i].data = realloc(doc.data[i].data, sizeof(struct sentence) * (doc.data[i].sentence_count));

    doc.paragraph_count = doc.paragraph_count == 0 && doc.data[i].data[i].word_count > 0 ? 1 : doc.paragraph_count;

    //printf("SIUUU\n");
    return doc;
}

struct word kth_word_in_mth_sentence_of_nth_paragraph(struct document Doc, int k, int m, int n) {
    return Doc.data[n - 1].data[m - 1].data[k - 1];
}

struct sentence kth_sentence_in_mth_paragraph(struct document Doc, int k, int m) {
    return Doc.data[m - 1].data[k - 1];
}

struct paragraph kth_paragraph(struct document Doc, int k) {
    return Doc.data[k - 1];
}


// DEFAULT CODE ************************************+

void print_word(struct word w) {
    printf("%s", w.data);
}

void print_sentence(struct sentence sen) {
    for(int i = 0; i < sen.word_count; i++) {
        print_word(sen.data[i]);
        if (i != sen.word_count - 1) {
            printf(" ");
        }
    }
}

void print_paragraph(struct paragraph para) {
    for(int i = 0; i < para.sentence_count; i++){
        print_sentence(para.data[i]);
        printf(".");
    }
}

void print_document(struct document doc) {
    for(int i = 0; i < doc.paragraph_count; i++) {
        print_paragraph(doc.data[i]);
        if (i != doc.paragraph_count - 1)
            printf("\n");
    }
}

char* get_input_text() {
    int paragraph_count;
    printf("Number of paragraphs: ");
    scanf("%d", &paragraph_count);

    char p[MAX_PARAGRAPHS][MAX_CHARACTERS], doc[MAX_CHARACTERS];
    memset(doc, 0, sizeof(doc));
    getchar();
    for (int i = 0; i < paragraph_count; i++) {
        printf("%d paragraph: ", i);
        scanf("%[^\n]%*c", p[i]);
        strcat(doc, p[i]);
        if (i != paragraph_count - 1)
            strcat(doc, "\n");
    }

    char* returnDoc = (char*)malloc((strlen (doc)+1) * (sizeof(char)));
    strcpy(returnDoc, doc);
    return returnDoc;
}

int main()
{
    char* text = get_input_text();
    struct document Doc = get_document(text);

    int q;
    printf("Queries: ");
    scanf("%d", &q);

    while (q--) {
        int type;
        printf("Type of query: ");
        scanf("%d", &type);

        if (type == 3){
            int k, m, n;
            printf("kth word, mth sentence, nth paragraph: ");
            scanf("%d %d %d", &k, &m, &n);
            struct word w = kth_word_in_mth_sentence_of_nth_paragraph(Doc, k, m, n);
            print_word(w);
        }

        else if (type == 2) {
            int k, m;
            printf("kth sentence, mth paragraph: ");
            scanf("%d %d", &k, &m);
            struct sentence sen= kth_sentence_in_mth_paragraph(Doc, k, m);
            print_sentence(sen);
        }

        else{
            int k;
            printf("kth paragraph: ");
            scanf("%d", &k);
            struct paragraph para = kth_paragraph(Doc, k);
            print_paragraph(para);
        }
        printf("\n");
    }
}
