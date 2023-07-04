#include <Python.h>
#include <object.h>
#include <unicodeobject.h>


void print_python_string(PyObject *p)
{
const char *type = NULL;
Py_ssize_t nlength = 0;
wchar_t *nstring = NULL;

printf("[.] string object info\n");
if (!PyUnicode_Check(p))
{
	printf("  [ERROR] Invalid String Object\n");
	return;
}

if (PyUnicode_IS_COMPACT_ASCII(p))
	type = "compact ascii";
else
	type = "compact unicode object";

nstring = PyUnicode_AsWideCharString(p, &nlength);

printf("  type: %s\n", type);
printf("  length: %ld\n", nlength);
printf("  value: %ls\n", nstring);
}
