// #include <boost/python.hpp>
#include <Python.h>

/**
 * g++ -I /usr/include/python2.7 -lpython2.7 -lboost_python python2.cpp
 */
int main(int argc, char const *argv[])
{
  Py_Initialize();

  PyRun_SimpleString("print 'hello'");
  PyRun_SimpleString("import sys");
  PyRun_SimpleString("import hello");
  Py_Finalize();
  return 0;
}