#include "lists.h"

/**
 * check_cycle – a function that confirms cycles in the list
 * @list: the linked list
 * Return: 1 else, 0
 */

int check_cycle(listint_t *list)
{
	listint_t *ptr_a, *ptr_b;

	if (!list || !list->next)
		return (0);
	ptr_a = list->next;
	ptr_b = list->next->next;
	while (ptr_a && ptr_b && ptr_b->next)
	{
		if (ptr_a == ptr_b)
		{
			return (1);
		}
		ptr_a = ptr_a->next;
		ptr_b = ptr_b->next->next;
	}
	return (0);
}
