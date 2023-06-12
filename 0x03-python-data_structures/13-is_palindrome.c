#include "lists.h"
#include <stdlib.h>
/**
 * reverse_palindrome - Check the reverse of palindrome
 * @a: A pointer to pointer
 * @b: A pointer
 *
 * Return: 0
 */
int reverse_palindrome(listint_t **a, listint_t *b)
{
	int i;

	if (b != NULL)
	{
		i = reverse_palindrome(a, b->next);
		if (!i)
		{
			i = (b->n == (*a)->n);
			*a = (*a)->next;
			return (i);
		}
		return (0);
	}
	return (1);
}
/**
 * is_palindrome - Check if a singly linked list is a palindrome
 * @head: The head of list
 *
 * Return: 0
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL)
	{
		return (0);
	}
	return (reverse_palindrome(head, *head));
}
