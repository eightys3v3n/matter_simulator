import os
from sys import exit
from types import ModuleType
import test_files


"""
Contains a framework for automatically compiling and running tests
"""


class Test():
  """
  Stores a refernece to the actual test function, and a list of tests that must be run before this one is
  """
  def __init__(self,function,requires):
    self.function = function
    self.requires = requires
    self.completed = False


  def __getattr__(self,key):
    """
    .name:            return the name of the test function with a ' test' added on
    .function_name:   returns the name of the test function
    """
    if key == "name":
      return self.function.__name__+" test"
    elif key == "function_name":
      return self.function.__name__


  def __call__(self):
    """
    Runs the function referenced if it has not already been completed
    """
    if self.completed:
      return False

    ret = self.function()
    if ret == False:
      self.completed = True
    return ret


class Tests():
  """
  A collection of Test objects with no duplicates.
  This class handles running all of the tests in the correct order
  """
  def __init__(self):
    self.completed = []
    self.tests = []


  def already_testing(self,function):
    """
    param function: a reference to a function
    returns:
      True: if the test function is already in this collection of tests; i.e. it doesn't need to be added again
      False: if the test function is not in this collection of tests
    """
    for test in self.tests:
      if test.function == function:
        return True
    return False


  def new(self,function,func_requires=[]):
    """
    Adds a new test and it's prerequisites to the collection

    param function: a reference to the test function
    param func_requires: an array of references to the functions that must be run before this one
    """
    if not self.already_testing(function):
      self.tests.append(Test(function,func_requires))


  def run_test(self,test):
    """
    Runs the Test object after all of it's prerequisites

    param test: A Test object
    """
    if not test.completed:
      for req in test.requires:
        req_test = None
        for funcs in self.tests:
          if req == funcs.function:
            req_test = funcs

        if req_test == None:
          raise Exception(test.name+" requires a non-test ",req)

        if not req_test.completed:
          self.run_test(req_test)

    ret = test()
    if ret == False:
      if os.name == "posix":
        print("\033[92m"+test.name+" passed\033[0m")
      elif os.name == "nt":
        print(test.name+" passed")
      test.completed = True
    elif ret == None:
      if os.name == "posix":
        print("\033[90m"+test.name+" has no test\033[0m")
      elif os.name == "nt":
        print(test.name+" has no test")
    else:
      if os.name == "posix":
        print("\033[91m"+test.name+" failed\033[0m")
      elif os.name == "nt":
        print(test.name+" failed")
      exit(2)


  def __call__(self):
    """
    Runs all the tests in the collection
    """
    for test in self.tests:
      self.run_test(test)


tests = Tests()


def compile_tests(module):
  """
  Adds all the functions that meet a criteria to the global Tests object
  criteria:
    function ends in '_Test'
    an array called 'functions name'+'_req' that is [] or contains references to other test functions
  """
  for function_str in dir(module):
    function = getattr(module,function_str)

    if isinstance(function,ModuleType):
      compile_tests(function)
    elif callable(function) and len(function_str) > 5 and function_str[-5:] == "_Test":
      requirements = getattr(module,function_str+"_req")
      tests.new(function,requirements)
      #print("found test",function_str)
      #print("  requires",requirements)


def test_all():
  """
  Compiles and runs all the tests included in the specified module
  Currently retrieving all tests from 'test_files.py'
  """
  compile_tests(test_files)
  tests()