#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s – a linked list, singly structure
 * @n: an integer
 * @next: a pointer to the next node
 *
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

int check_cycle(listint_t *list);
size_t print_listint(const listint_t *h);
void free_listint(listint_t *head);
listint_t *add_nodeint(listint_t **head, const int n);
#endif 
