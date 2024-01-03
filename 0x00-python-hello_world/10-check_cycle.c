#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle or not
 * @list: pointer to the linked list's head
 * Return: 0 if there is no cycle, else 1
 */

int check_cycle(list_int_t *list)
{
	listint_t *node_1, *node_2;

	if (!(list == NULL || list->next == NULL))
	{
		node_1 = list;
		node_2 = list->next;

		while (node_2 != NULL && node_2->next != NULL)
		{
			if (node_1 == node_2)
				return (1);

			node_1 = node_1->next;
			node_2 = node_2->next->next;
		}
		return (0);
	}
	else
		return (0);
}
