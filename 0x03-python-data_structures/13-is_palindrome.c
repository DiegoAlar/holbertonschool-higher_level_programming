#include "lists.h"
/**
  * is_palindrome - determines if palindrome
  * @head: pointer of the head
  * Return: 1 if palindrome, 0 if it is not
  */
int is_palindrome(listint_t **head)
{
	listint_t *t1 = *head;
	listint_t *t2 = *head;
	int cont = 1;
	int flag = 0;
	int c = 1;
	int total = 0;

	if ((head == NULL) || (*head == NULL))
		return (1);
	while (t1->next)
	{
		cont++;
		t1 = t1->next;
	}
	if (cont == 1)
		return (1);
	if (cont % 2 != 0)
		flag = 1;
	while (t2)
	{
		if ((flag == 1) && (c == ((cont / 2) + 1)))
		{
			c++;
			t2 = t2->next;
			continue;
		}
		if (c <= (cont / 2))
			total += t2->n;
		else
			total -= t2->n;
		c++;
		t2 = t2->next;
	}
	if (total == 0)
		return (1);
	else
		return (0);
}
