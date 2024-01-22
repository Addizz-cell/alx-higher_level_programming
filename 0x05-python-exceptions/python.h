/* Python.h */

#ifndef Py_PYTHON_H
#define Py_PYTHON_H

/* Include the standard C headers */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* Define basic Python types */
typedef int PyObject;
typedef int PyListObject;
typedef int PyBytesObject;
typedef int PyFloatObject;

/* Define basic Python API functions */
PyObject* PyList_New(int size);
void PyList_SetItem(PyObject* list, int index, PyObject* item);
PyObject* PyList_GetItem(PyObject* list, int index);
int PyList_Size(PyObject* list);

PyObject* PyBytes_FromStringAndSize(const char* str, int size);
int PyBytes_Size(PyObject* bytes);
const char* PyBytes_AsString(PyObject* bytes);

PyObject* PyFloat_FromDouble(double value);
double PyFloat_AsDouble(PyObject* floatObj);

#endif /* Py_PYTHON_H */
