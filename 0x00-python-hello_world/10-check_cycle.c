#include "lists.h"

/**
 * check_cycle - check if there is a cycle in the linked list
 * list: the head node
 * Return: 1 if the is a cycle 0 if there is no cycle
 */

int check_cycle(listint_t *list)
{
    listint_t *p, *curr_node;
    if (list == NULL)
        return (0);
    p = list;
    while (list != NULL)
    {
        curr_node = list->next;
        if (curr_node == p)
            return (1);
        list = list->next;
    }
    return (0);
}