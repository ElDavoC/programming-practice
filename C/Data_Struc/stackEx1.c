#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Node {
    char data;
    struct Node* link;
} Node;

Node* top;

void Push(char x) {
    Node* temp = (Node*)malloc(sizeof(Node));
    temp->data = x;
    temp->link = top;
    top = temp;
}

void Pop() {
    if(top == NULL) return;
    Node* temp = top;
    top = top->link;
    free(temp);
}

char Top() {
    if(top == NULL) return '\0';
    return top->data;
}

void Reverse(char *C, int n) {
    for(int i = 0; i < n; i++)
        Push(C[i]);

    for(int i = 0; i < n; i++) {
        C[i] = Top();
        Pop();
    }
}
int main() {
    top = NULL;
    char C[51];
    printf("Enter a string: ");
    scanf("%s", C);
    Reverse(C, strlen(C));
    printf("Output = %s", C);
}
