#include "lists.h"
/**
  * insert_node - inserts node in sorted list
  * @head: the list
  * @number: number to determine the insertion location
  * Return: an updated list
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head;
	listint_t *newN;
	listint_t *temp2 = NULL;

	newN = malloc(sizeof(listint_t));
	if (!newN)
		return (NULL);
	if (!temp)
		return (add_nodeint_end(head, number));
	while (temp->next)
	{
		if (number < temp->next->n)
			break;
		temp = temp->next;
	}
	if (temp->next)
		temp2 = temp->next;
	temp->next = NULL;
	newN = add_nodeint_end(head, number);
	temp = newN;
	while (temp->next)
		temp = temp->next;
	temp->next = temp2;
	return (newN);
}
