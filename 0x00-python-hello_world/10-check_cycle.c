#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: A linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *i = list;
	listint_t *j = list;

	if (!list)
		return (0);
	while (i && j && j->next)
	{
		i = i->next;
		j = j->next->next;
		if (i == j)
		{
			return (1);
		}
	}
	return (0);
}
