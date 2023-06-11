#include "lists.h"

/**
 * is_palindrome - a function for hecking palindrome in singly linked lists
 * @head: a pointer
 * Return: 1 else,  0
 */

int is_palindrome(listint_t **head)
{
	int a = 0, b, k;
	listint_t  *node = *head, *curr, *lst;

	if (!head)
		return (1);
	while (node)
	{
		node = node->next;
		a++;
	}
	curr = *head, lst = *head;
	for (b = 0; b < a / 2 ; b++)
	{
		for (k = b; k < a - 1; k++)
			lst = lst->next;
		if (lst->n != curr->n)
			return (0);
		curr = curr->next;
		lst = *head;
	}
	return (1);
}
