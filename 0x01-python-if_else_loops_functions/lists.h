#ifndef LISTS_H
#define LISTS_H
#include <stdlib.h>
/**
 * struct listint_s - a linked list, singly
 * @n: an int
 * @next: a pointer
*/
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

void free_listint(listint_t *head);
size_t print_listint(const listint_t *h);
listint_t *insert_node(listint_t **head, int number);
listint_t *add_nodeint_end(listint_t **head, const int n);

#endif

