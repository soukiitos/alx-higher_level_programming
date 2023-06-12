#include <Python.h>
#include <stdio.h>
/**
 * print_python_list_info - Print some basic info about Python lists
 * @p: A pointer
 *
 * Return: 0
 */
void print_python_list_info(PyObject *p)
{
	int i = 0;
	Py_ssize_t j = 0;

	if (PyList_CheckExact(p))
	{
		j = PyList_Size(p);
		printf("[*] Size of the Python List = %zd\n", j);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		for (; i < j; i++)
		{
			printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
		}
	}
}
