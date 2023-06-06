#include "lists.h"
listint_t *make_node(int n);
/**
 * insert_node - a function for inserting nodes
 * @head: a pointer to modify in edge
 * cases
 * @number: new node data
 *
 * Return: a pointer
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node_curr = NULL, *node_new = NULL;

	if (!head)
		return (NULL);
	else if (!(*head))
	{
		node_new = make_node(number);
		*head = node_new;
		return (node_new);
	}
	node_curr = *head;
	while (node_curr)
	{

		if (node_curr->n >= number)
		{
			node_new = make_node(number);
			node_new->next = node_curr;
			*head = node_new;
			return (node_new);
		}
		else if (node_curr->n <= number)
		{
			if (!node_curr->next || node_curr->next->n >= number)
			{
				node_new = make_node(number);
				node_new->next = node_curr->next;
				node_curr->next = node_new;
				return (node_curr->next);
			}
		}
		node_curr = node_curr->next;
	}
	return (NULL);
}

/**
 * make_node - a function for creating new nodes
 * @n: data
 *
 * Return: a pointer
 */
listint_t *make_node(int n)
{
	listint_t *r = NULL;

	r = malloc(sizeof(listint_t));
	if (!r)
		return (NULL);
	r->next = NULL;
	r->n = n;
	return (r);
}
