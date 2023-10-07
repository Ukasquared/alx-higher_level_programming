#include "lists.h"

/**
 * check_cycle - check if there is a cycle in the linked list
 * @list: the head node
 * Return: 1 if the is a cycle 0 if there is no cycle
 */

int check_cycle(listint_t *list)
{
    listint_t *prev, *curr_node;
    if (list == NULL)
        return (0);
    prev = list;
    curr_node = list;
    while (curr_node && curr_node->next)
    {
        curr_node = curr_node->next->next;
        prev = prev->next;
        if (curr_node == prev)
            return (1);
    }
    return (0);
}