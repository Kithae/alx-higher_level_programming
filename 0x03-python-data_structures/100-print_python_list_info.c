#include <Python.h>

/**
 * print_python_list_info -  a function for printing basic python lists info
 * @p: A list, PyObject.
 */
void print_python_list_info(PyObject *p)
{
	int mysize, allo, a;
	PyObject *obj;

	mysize = Py_SIZE(p);
	allo = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", mysize);
	printf("[*] Allocated = %d\n", allo);

	for (a = 0; a < mysize; a++)
	{
		printf("Element %d: ", a);

		obj = PyList_GetItem(p, a);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
