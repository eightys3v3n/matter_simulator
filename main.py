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

      screen_objects = []

      window = Window(screen_objects)
      simulation = Simulation(screen_objects)

      # run the window, starts drawing and all that stuff
      run()

      # quit the window, close any threads and such
      window.quit()

    exit(main())