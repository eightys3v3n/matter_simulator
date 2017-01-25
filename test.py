import os
from sys import exit
from types import ModuleType
import test_files


# Test File
# this file has the classes that make testing nice and easy ;)
# this stuff is used in the tests.py file.


class Test():
  def __init__(self,function,requires):
    self.function = function
    self.requires = requires
    self.completed = False


  def __getattr__(self,key):
    if key == "name":
      return self.function.__name__+" test"
    elif key == "function_name":
      return self.function.__name__



  def __call__(self):
    if self.completed:
      return False

    ret = self.function()
    if ret == False:
      self.completed = True
    return ret


class Tests():
  def __init__(self):
    self.completed = []
    self.tests = []


  def already_testing(self,function):
    for test in self.tests:
      if test.function == function:
        return True
    return False


  def new(self,function,func_requires=[]):
    if not self.already_testing(function):
      self.tests.append(Test(function,func_requires))


  def run_test(self,test):
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
    for test in self.tests:
      self.run_test(test)


tests = Tests()


def compile_tests(module):
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
  compile_tests(test_files)
  tests()