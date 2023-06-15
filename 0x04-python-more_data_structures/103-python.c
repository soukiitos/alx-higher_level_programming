#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
/**
 * print_python_bytes - Print some basic info about PyBytesObject
 * @p: A PyObject
 *
 * Return: 0
 */
void print_python_bytes(PyObject *p)
{
	char *str = NULL;
	Py_ssize_t s, i;

	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	if (PyBytes_AsStringAndSize(p, &str, &s) != -1)
	{
		printf("  size: %zd\n", s);
		printf("  trying string: %s\n", str);
		printf("  first %zd bytes:", s < 10 ? s + 1 : 10);
		for (i = 0; i < s + 1 && i < 10; i++)
		{
			printf(" %2hhx", str[i]);
		}
		printf("\n");
	}
}
/**
 * print_python_list - Print some basic info about PyListObject
 * @p: A PyObject
 *
 * Return: 0
 */
void print_python_list(PyObject *p)
{
	int i;
	Py_ssize_t s;
	PyObject *j;

	if (PyList_CheckExact(p))
	{
		s = PyList_Size(p);
		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %zd\n", s);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		for (i = 0; i < s; i++)
		{
			j = PyList_GET_J(p, i);
			printf("Element %d: %s\n", i, j->ob_type->tp_name);
			if (PyBytes_Check(j))
			{
				print_python_bytes(j);
			}
		}
	}
}
