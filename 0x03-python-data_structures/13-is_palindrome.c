#include "lists.h"
#include <stdlib.h>
/**
 * is_palindrome - Check if a singly linked list is a palindrome
 * @head: The head of list
 *
 * Return: 0
 */
int is_palindrome(listint_t **head)
{
	int i, j, a[2048];
	listint_t *resp = *head;

	if (*head)
	{
		for (i = 0; resp; i++)
		{
			a[i] = resp->n;
			resp = resp->next;
		}
		for (j = 0; j < i / 2; j++)
		{
			if (a[j] == a[i - j - 1])
				;
			else
				return (0);
		}
	}
	return (1);
}
