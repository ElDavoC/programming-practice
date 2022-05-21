#include <stdio.h>
#include <stdlib.h>

typedef struct Node{
    int data;
    struct Node* next;
} node;

node* head;

void Reverse() {
    node *current, *prev, *next;
    current = head;
    prev = NULL;
    while(current != NULL) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    head = prev;
}

node* Insert(node* head, int data) {
    node* temp = (node*)malloc(sizeof(node));
    temp->data = data;
    temp->next = NULL;
    if(head == NULL) head = temp;
    else {
        node* temp1 = head;
        while(temp1->next != NULL) temp1 = temp1->next;
        temp1->next = temp;
    }
    return head;
}

void Print(node* p) {
    if(p == NULL) return;
    Print(p->next); // Reverse
    printf("%d ", p->data);
    //Print(p->next); // normal
}

int main() {
    node* A = NULL;
    A = Insert(A, 2);
    A = Insert(A, 4);
    A = Insert(A, 6);
    A = Insert(A, 5);
    Print(A);

    return 0;
}
