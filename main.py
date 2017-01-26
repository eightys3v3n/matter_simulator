from sys import argv,exit


if __name__ == "__main__":
  if len(argv) > 1:
    if str(argv[1]) == "test":
      import test
      exit(test.test_all())

  else:
    import threading
    from pyglet.app import run
    import variables
    from window import Window
    from simulation import Simulation

    def main():
      # create a window

      # an array of ScreenObject types that should be drawn.
      # this is passed by reference to the window amd simulation
      # classes; so when simulation adds a new screen object
      # window starts drawing it.
      screen_objects = []

      # the drawer and event handler (keyboard/mouse)
      window = Window(screen_objects)
      
      # the physics simulator, particle mover
      simulation = Simulation(screen_objects)

      # run main program loop, starts drawing and all that stuff
      run()

      # quit the window, close any threads and such
      window.quit()

    exit(main())