#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer to the head of the linked list.
 * @number: The number to insert.
 *
 * Return: NULL if the function fails, or a pointer to the new node.
 */

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node, *temp;

    if (head == NULL)
        return (NULL);
    new_node = malloc(sizeof(listint_t));
    if (!new_node)
        return (NULL);
    new_node->n = number;
    new_node->next = NULL;

    if (*head == NULL)
    {
        *head = new_node;
        return (*head);
    }
    temp = *head;
    while (temp->next && temp->n < number)
        temp = temp->next;
    new_node->next = temp->next;
    temp->next = new_node;

    return (new_node);
}
