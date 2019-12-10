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

	if (tort->next && tort->next->next && list)
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
