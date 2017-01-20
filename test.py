from sys import exit


class Test():
  def __init__(self,function,requires=[]):
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


  def new(self,function,func_requires=[]):
    requires = []

    for req in func_requires:
      for test in self.tests:
        if test.function == test:
          requires.append(test)
    self.tests.append(Test(function,requires))


  def run_test(self,test):
    for req in test.requires:
      if not isinstance(req,Test):
        raise Exception(test.name+" requires a non-test ",req)
      self.run_test(req)

    ret = test()
    if ret == False:
      print("\033[92m"+test.name+" passed\033[0m")
      test.completed = True
    elif ret == None:
      print("\033[90m"+test.name+" has no test\033[0m")
    else:
      print("\033[91m"+test.name+" failed\033[0m")
      exit(2)


  def __call__(self):
    for test in self.tests:
      self.run_test(test)