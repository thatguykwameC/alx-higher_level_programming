#include "lists.h"

/**
 * insert_node - Inserts a number into a singly-linked list
 * @head: pointer to the head of the linked list
 * @number: number to insert
 *
 * Return: NULL on failure, else a pointer to the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (!*head || number <= (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	else
	{
		temp = *head;
		while (temp->next && number > temp->next->n)
			temp = temp->next;

		new->next = temp->next;
		temp->next = new;
		return (new);
	}
	return (NULL);
}
