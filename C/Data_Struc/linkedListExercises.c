#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} node;

void Insert(node** head, int data) {
    node* temp = (node*)malloc(sizeof(node));
    temp->data = data;
    temp->next = NULL;
    if(*head == NULL) {
        *head = temp;
        return;
    }

    node* prov = *head;
    while(prov->next != NULL) prov = prov->next;

    prov->next = temp;
}

void Reverse(node** head) {
    if(*head == NULL || (*head)->next == NULL) return;

    node *prev, *temp, *next;

    temp = *head;
    prev = NULL;

    while(temp != NULL){
        next = temp->next;
        temp->next = prev;
        prev = temp;
        temp = next;
    }

    *head = prev;
}

void PrintElements(node* head) {
    while(head != NULL) {
            printf("%d -> ", head->data);
            head = head->next;
    }
    printf("\n");
}

int main() {
    node* head = NULL;
    PrintElements(head);

    Insert(&head, 2);
    PrintElements(head);

    Insert(&head, 3);
    Insert(&head, 4);
    Insert(&head, 5);

    PrintElements(head);

    Reverse(&head);
    PrintElements(head);

    return 0;
}
