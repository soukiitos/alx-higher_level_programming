#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

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
