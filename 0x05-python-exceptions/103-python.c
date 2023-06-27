#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Print lists
 * @p: A python object
 *
 * Return: 0
 */
void print_python_list(PyObject *p)
{
	PyListObject *i = (PyListObject *)p;
	PyVarObject *j = (PyVarObject *)p;
	Py_ssize_t size, n, m = 0;
	const char *ch;

	size = j->ob_size;
	n = i->allocated;
	fflush(stdout);
	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "i") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", n);
	while (m < size)
	{
		m++;
		ch = i->ob_item[m]->ob_type->tp_name;
		printf("Element %ld: %s\n", m, ch);
		if (strcmp(ch, "float") == 0)
		{
			print_python_float(i->ob_item[m]);
		}
		else if (strcmp(ch, "bytes") == 0)
		{
			print_python_bytes(i->ob_item[m]);
		}
	}
}
/**
 * print_python_bytes - Print python bytes's info
 * @p: A python object
 *
 * Return: 0
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *b = (PyBytesObject *)p;
	Py_ssize_t size, s;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", b->ob_sval);
	if (((PyVarObject *)p)->ob_size < 10)
	{
		size = ((PyVarObject *)p)->ob_size + 1;
	}
	else
                size = 10;
        printf("  first %ld bytes: ", size);
	for (s = 0; s < size; s++)
	{
		printf("%02hhx", b->ob_sval[s]);
		if (s != (size - 1))
			printf(" ");
		else
			printf("\n");
	}
}
/**
 * print_python_float - Print python float's info
 * @p: A python object
 *
 * Return: 0
 */
void print_python_float(PyObject *p)
{
	char *c = NULL;
	PyFloatObject *obj = (PyFloatObject *)p;

	fflush(stdout);
	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	c = PyOS_double_to_string(obj->ob_fval, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", c);
	PyMem_free(c);
}
