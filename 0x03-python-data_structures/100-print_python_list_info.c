#include <Python.h>

/**
 * print_python_list_info - basic info Python lists
 * @p: Pointer
 */
void print_python_list_info(PyObject *p)
{
    Py_ssize_t aq, x;
    PyObject *aw;

    aq = PyList_Size(p);

    printf("[*] Size of the Python List = %zd\n", aq);
    printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

    for (x = 0; x < aq; x++)
    {
        aw = PyList_GetItem(p, x);
        printf("Element %zd: %s\n", x, Py_TYPE(aw)->tp_name);
    }
}

