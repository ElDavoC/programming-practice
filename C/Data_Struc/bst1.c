#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int max(int a, int b) {
    return a > b ? a : b;
}

typedef struct BstNode{
    int data;
    struct BstNode* left;
    struct BstNode* right;
} BstNode;

BstNode* GetNewNode(int data) {
    BstNode* newNode = (BstNode*)malloc(sizeof(BstNode));
    newNode->data = data;
    newNode->left = newNode->right = NULL;
    return newNode;
}

BstNode* Insert(BstNode* root, int data) {
    if(root == NULL) {
        root = GetNewNode(data);
    }
    else if(data <= root->data) {
        root->left = Insert(root->left, data);
    }
    else {
        root->right = Insert(root->right, data);
    }
    return root;
}

bool Search(BstNode* root, int data) {
    if(root == NULL) return false;
    else if(root->data == data) return true;
    else if(data < root->data) return Search(root->left, data);
    else return Search(root->right, data);
}

BstNode* FindMin(BstNode* root) {
    if(root == NULL) {
        printf("Error: Tree is empty\n");
        return NULL;
    }

    if(root->left == NULL)
        return root;

    return FindMin(root->left);
}

int FindMax(BstNode* root) {
    if(root == NULL) {
        printf("Error: Tree is empty\n");
        return -1;
    }

    if(root->right == NULL)
        return root->data;

    return FindMax(root->right);
}

int FindHeight(BstNode* root) {
    if(root == NULL)
        return -1;

    return max(FindHeight(root->left), FindHeight(root->right)) + 1;
}

void LevelOrder(BstNode* root) {
    if(root == NULL) return;
    // Create queue
    // Q.push(root); Push root to the queue
    /*
    while(!Q.empty()){
        BstNode* current = Q.front();
        printf("%d ", current->data);
        if(current->left != NULL) Q.push(current->left);
        if(current->right != NULL) Q.push(current->right);
        Q.pop();
    }
    */
}

void PreorderTraversal(BstNode* root) {
    if(root == NULL) return;

    printf("%d ", root->data);
    PreorderTraversal(root->left);
    PreorderTraversal(root->right);
}

void InorderTraversal(BstNode* root) {
    if(root == NULL) return;

    InorderTraversal(root->left);
    printf("%d ", root->data);
    PreorderTraversal(root->right);
}

void PostorderTraversal(BstNode* root) {
    if(root == NULL) return;

    PostorderTraversal(root->left);
    PostorderTraversal(root->right);
    printf("%d ", root->data);
}

bool IsSubtreeLesser(BstNode* root, int value) {
    if(root == NULL) return true;
    if(root->data <= value
        && IsSubtreeLesser(root->left, value)
        && IsSubtreeLesser(root->right, value))
        return true;
    else
        return false;
}

bool IsSubtreeGreater(BstNode* root, int value) {
    if(root == NULL) return true;
    if(root->data <= value
        && IsSubtreeGreater(root->left, value)
        && IsSubtreeGreater(root->right, value))
        return true;
    else
        return false;
}

bool IsBstUtil(BstNode* root, int minValue, int maxValue) {
    if(root == NULL) return true;

    /*
    if(IsSubtreeLesser(root->left, root->data)
        && IsSubtreeGreater(root->right, root->data)
        && IsBinarySearchTree(root->left)
        && IsBinarySearchTree(root->right))
        return true;
    */
    if(root->data > minValue
       && root->data < maxValue
       && IsBstUtil(root->left, minValue, root->data)
       && IsBstUtil(root->right, root->data, maxValue))
        return true;
    else
        return false;
}

bool IsBinarySearchTree(BstNode* root) {
    return IsBstUtil(root, INT_MIN, INT_MAX);
}

BstNode* Delete(BstNode* root, int data) {
    if(root == NULL) return root;
    else if(data < root->data) root->left = Delete(root->left, data);
    else if(data > root->data) root->right = Delete(root->right, data);
    else {
        // Case 1: No child
        if(root->left == NULL && root->right == NULL) {
            free(root);
            root = NULL;
        }
        // Case 2: One child
        else if(root->left == NULL) {
            BstNode* temp = root;
            root = root->right;
            free(temp);
        }
        else if(root->right == NULL) {
            BstNode* temp = root;
            root = root->left;
            free(temp);
        }
        // Case 3: 2 children
        else {
            BstNode* temp = FindMin(root->right);
            root->data = temp->data;
            root->right = Delete(root->right, temp->data);
        }

    }
    return root;
}

BstNode* Getsuccessor(BstNode* root, int data) {
    // Search the Node
    BstNode* current = Find(root, data);
    if(current == NULL) return NULL;

    // Case 1: Node has right subtree
    if(current->right != NULL) {
        return FindMin(current->right);
    }

    // Case 2: No right subtree
    else {
        BstNode* successor = NULL;
        BstNode* ancestor = root;
        while(ancestor != current) {
            if(current->data < ancestor->data) {
                successor = ancestor;
                ancestor = ancestor->left;
            }
            else
                ancestor = ancestor->right;
        }
        return successor;
    }
}

void Print(BstNode* root, int level) {
    if(root != NULL)
        Print(root->right, level + 1);

    if(level > 0)
        for(int i = 0; i < level; i++)
            printf("\t");

    printf("%d\n", root == NULL ? 0 : root->data);

    if(root != NULL)
        Print(root->left, level + 1);
}

int main() {
    BstNode* root = NULL;
    root = Insert(root, 15);
    root = Insert(root, 10);
    //Insert(root,10);
    root = Insert(root, 20);
    //Insert(root,20);
    root = Insert(root, 25);
    //Insert(root,25);
    root = Insert(root, 8);
    root = Insert(root, 12);
    Print(root, 0);
    printf("\n");

    int number;
    printf("Enter number be searched: ");
    scanf("%d", &number);
    if(Search(root, number) == true) printf("Found!\n");
    else printf("NOT Found\n");

    printf("Min: %d\n", FindMin(root)->data);
    printf("Max: %d\n", FindMax(root));

    printf("Height : %d\n", FindHeight(root));

    printf("Preorder Traversal: ");
    PreorderTraversal(root);
    printf("\n\n");

    printf("Inorder Traversal: ");
    InorderTraversal(root);
    printf("\n\n");

    printf("Postorder Traversal: ");
    PostorderTraversal(root);
    printf("\n\n");

    printf("Is BST?: %s", IsBinarySearchTree(root) ? "true": "false");

    return 0;
}
