from space import Position2i,Position3f,Position2f


# Variables File
# a file to store constants and stuff so it is easy to change.
# something like the gravity constant, or the size of the simulation space
# and all that go in here


# window stuff
screen_size = Position2i(800,600)


# constants
pi = 3.14159265358979323846


# shape stuff
default_colour = [175.0,175.0,175.0] # RGB


# controls
move_speed = Position3f(0.1,0.1,0.1)
mouse_sensitivity = Position2f(0.5,0.5)