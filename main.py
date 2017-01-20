from sys import argv,exit


if __name__ == "__main__":
  if len(argv) > 1:
    if str(argv[1]) == "test":
      import tests
      exit(tests.tests())

  else:
    from pyglet.app import run
    import variables
    from window import Window
    from screen_object import ScreenObject
    from space import Position3f

    def main():
      # create a window
      window = Window()

      obj = ScreenObject("point",Position3f(0,0,-4))
      window.load_object(obj)

      # run the window, starts drawing and all that stuff
      run()

      # quit the window, close any threads and such
      window.quit()

    exit(main())