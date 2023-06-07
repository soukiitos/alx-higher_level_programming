#include "lists.h"
/**
 * insert_node - insert a number into into a sorted singly linked list
 * @head: A pointer
 * @number: An integer
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *i = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}
	new->n = number;
	if (i == NULL || i->n >= number)
	{
		new->next = i;
		*head = new;
		return (new);
	}
	while (i && i->next && i->next->n < number)
	{
		i = i->next;
	}
	new->next = i->next;
	i->next = new;
	return (new);
}
