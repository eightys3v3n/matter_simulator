from sys import argv,exit


if __name__ == "__main__":
  if len(argv) > 1:
    if str(argv[1]) == "test":
      import tests
      exit(tests.tests())

  else:
    from pyglet.app import run
    from pyglet.gl import glPointSize
    import variables
    from window import Window
    from screen_object import ScreenObject
    from space import Position3f

    def main():
      # create a window
      window = Window()

      # create a shape that will draw lines around the simulation boundries
      bounds = ScreenObject("rectangle",[Position3f(0,0,-4),Position3f(10,10,0)])
      sphere = ScreenObject("sphere",[20,20,20])
      window.load_sphere(sphere)

      # load the bounds shape into the window so it is being drawn
      window.load_object(bounds)

      # run the window, starts drawing and all that stuff
      run()

      # quit the window, close any threads and such
      window.quit()

    exit(main())