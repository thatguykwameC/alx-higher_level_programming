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
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
}
