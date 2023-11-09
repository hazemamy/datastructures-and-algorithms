#include <iostream>

struct Node
{
    int data;
    Node *prev;
    Node *next;
    Node(int value) : data(value), prev(nullptr), next(nullptr) {}
};

class DoublyLinkedList
{
private:
    Node *head;
    Node *tail;

public:
    DoublyLinkedList() : head(nullptr), tail(nullptr) {}

    void push_back(int value)
    {
        Node *newNode = new Node(value);
        if (head == nullptr)
        {
            head = newNode;
            tail = newNode;
        }
        else
        {
            newNode->prev = tail;
            tail->next = newNode;
            tail = newNode;
        }
    }

    void push_front(int value)
    {
        Node *newNode = new Node(value);
        if (head == nullptr)
        {
            head = newNode;
            tail = newNode;
        }
        else
        {
            newNode->next = head;
            head->prev = newNode;
            head = newNode;
        }
    }

    void delete_node(int value)
    {
        Node *current = head;
        while (current != nullptr)
        {
            if (current->data == value)
            {
                if (current->prev != nullptr)
                {
                    current->prev->next = current->next;
                }
                else
                {
                    head = current->next;
                }
                if (current->next != nullptr)
                {
                    current->next->prev = current->prev;
                }
                else
                {
                    tail = current->prev;
                }
                delete current;
                break;
            }
            current = current->next;
        }
    }

    void display()
    {
        Node *current = head;
        while (current != nullptr)
        {
            std::cout << current->data << " & ";
            current = current->next;
        }
        std::cout << "nullptr" << std::endl;
    }
};

int main()
{
    DoublyLinkedList dll;
    dll.push_back(123);
    dll.push_back(785);
    dll.push_back(5465465465);
    dll.push_back(123);

    dll.push_front(0000);

    dll.delete_node(5465465465);

    dll.display();
    

    return 0;
}
