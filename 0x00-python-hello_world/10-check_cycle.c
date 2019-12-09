#include "lists.h"
/**
  * check_cycle - checks if a list has a loop
  * @list: the list
  * Return: 0 if there is no cycle and 1 otherwise
  *
  */
int check_cycle(listint_t *list)
{
	listint_t *tort = list;
	listint_t *lieb = list;

	if (!list)
		return (0);
	if (tort->next && tort->next->next)
	{
		do {
			tort = tort->next;
			lieb = lieb->next->next;

			if (tort == lieb)
				return (1);
		} while (tort->next && lieb->next->next);
	}
	return (0);
}
