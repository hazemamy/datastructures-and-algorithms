#include <iostream>

class Node
{
public:
    int data;
    Node *next;

    Node(int value) : data(value), next(nullptr) {}
};

class SinglyLinkedList
{
public:
    SinglyLinkedList() : head(nullptr) {}

    void append(int value)
    {
        Node *newNode = new Node(value);
        if (head == nullptr)
        {
            head = newNode;
        }
        else
        {
            Node *current = head;
            while (current->next != nullptr)
            {
                current = current->next;
            }
            current->next = newNode;
        }
    }

    void display()
    {
        Node *current = head;
        while (current != nullptr)
        {
            std::cout << current->data << " -> ";
            current = current->next;
        }
        std::cout << "nullptr" << std::endl;
    }

    void deleteNode(int value)
    {
        if (head == nullptr)
        {
            return;
        }
        if (head->data == value)
        {
            Node *temp = head;
            head = head->next;
            delete temp;
            return;
        }
        Node *current = head;
        while (current->next != nullptr)
        {
            if (current->next->data == value)
            {
                Node *temp = current->next;
                current->next = current->next->next;
                delete temp;
                return;
            }
            current = current->next;
        }
    }

private:
    Node *head;
};

int main()
{
    SinglyLinkedList sll;
    sll.append(1);
    sll.append(2);
    sll.append(3);
    sll.display();
    sll.deleteNode(2);
    sll.display();
    return 0;
}
