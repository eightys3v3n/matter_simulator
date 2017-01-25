from sys import argv,exit


if __name__ == "__main__":
  if len(argv) > 1:
    if str(argv[1]) == "test":
      import test
      exit(test.test_all())

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

      sphere = ScreenObject("sphere",[Position3f(0,0,0),Position3f(1,30,30)])
      window.load_sphere(sphere)

      sphere1 = ScreenObject("sphere",[Position3f(2,2,0),Position3f(1,30,30)])
      window.load_sphere(sphere1)

      sphere2 = ScreenObject("sphere",[Position3f(2,0,2),Position3f(1,30,30)])
      window.load_sphere(sphere2)

      sphere3 = ScreenObject("sphere",[Position3f(2,2,2),Position3f(1,30,30)])
      window.load_sphere(sphere3)

      # load the bounds shape into the window so it is being drawn
      window.load_object(bounds)

      # run the window, starts drawing and all that stuff
      run()

      # quit the window, close any threads and such
      window.quit()

    exit(main())