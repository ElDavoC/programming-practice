#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* link;
} Node;

Node* top = NULL;

void Push(int x) {
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

int main() {

    return 0;
}
