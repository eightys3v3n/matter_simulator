# Variables File
# a file to store constants and stuff so it is easy to change.
# something like the gravity constant, or the size of the simulation space
# and all that go in here


# window stuff
screen_size = [800,600]


# constants
pi = 3.14159265358979323846


# shape stuff
default_colour = [175.0,175.0,175.0] # RGB


# controls
move_speed = [1,1,1]
mouse_sensitivity = [0.5,0.5]


# the default radius and such of spheres
default_sphere_args = [30,30]

# perform a physics update every this many fractions of a second
physics_update_time = 1.0/60.0

# max number of actions that the simulation or the window can queue up before it is told
# to wait before inserting any more
max_queue_size = 10


# number of decimals that all calculations are rounded to
precision = 6


# gravity constant
gravity = 6.67e-11