#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} node;

node* head;

// Inserting a node at beginning
void insertBeginning(int x) {
    node* temp = (node*)malloc(sizeof(node));
    temp->data = x;     //(*temp).data = x;
    temp->next = head;
    head = temp;
}

// Inserting a node at nth position
void insertNthPosition(int data, int n) {
    if(n == 1) {
        insertBeginning(data);
        return;
    }

    node* temp1 = (node*)malloc(sizeof(node));
    temp1->data = data;
    temp1->next = NULL;

    node* temp2 = head;
    for(int i = 0; i < n - 2; i++) {
        temp2 = temp2->next;
    }

    temp1->next = temp2->next;
    temp2->next = temp1;
}

// Insert a node at the end
void InsertEnd(int data) {
    node* temp = (node*)malloc(sizeof(node));
    temp->data = data;
    temp->next = NULL;
    if(head == NULL) {
        head = temp;
        return;
    }
    node* temp1 = head;
    while(temp1->next != NULL)
        temp1 = temp1->next;

    temp1->next = temp;
}

// Delete a node at nth position
void DeleteNthNode(int n) {
    node* temp1 = head;
    if(n == 1) {
        head = temp1->next;
        free(temp1);
        return;
    }

    for(int i = 0; i < n - 2; i++)
        temp1 = temp1->next;

    node* temp2 = temp1->next;
    temp1->next = temp2->next;
    free(temp2);
}

// Reverse the Linked List (iterable solution)
void ReverseIt() {
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

// Reverse Linked List (recursion solution)
void ReverseRec(node* p) {
    if(p->next == NULL)
    {
        head = p;
        return;
    }
    ReverseRec(p->next);
    node* q = p->next;
    q->next = p;
    p->next = NULL;
}

// Print elements (iterable)
void Print() {
    node* temp = head;
    printf("List is: ");
    while(temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}

int main() {
    head = NULL;

    // INSERT AT BEGINNING***********
    //printf("How many numbers?: ");
    //int n, x;
    //scanf("%d", &n);

    //for(int i = 0; i<n; i++) {
    //    printf("Enter the number: ");
    //    scanf("%d", &x);
    //    insertBeginning(x);
    //    Print();
    //}
    //***************

    //INSERT AT NTH POSITION***********
    //insertNthPosition(2,1);
    //insertNthPosition(3,2);
    //insertNthPosition(4,1);
    //insertNthPosition(5,2);
    //Print();
    //***************

    //DELETE AT NTH POSITION************
    InsertEnd(2);
    InsertEnd(4);
    InsertEnd(6);
    InsertEnd(8);
    //int n;
    //printf("Enter a position: ");
    //scanf("%d", &n);
    //DeleteNthNode(n);
    Print();
    //**************

    //REVERSE (ITERABLE)*************
    ReverseIt();
    Print();
    //******************
    return 0;
}
