# Variables File
# a file to store constants and stuff so it is easy to change.
# something like the gravity constant, or the size of the simulation space
# and all that go in here


# window stuff
screen_size = [800,600]


# constants
pi = 3.14159265358979323846


# shape stuff
default_colour = [0.0,0.0,255.0] # RGB
cool_colour = [255.0,0.0,0.0]


# controls
move_speed = [4,4,4]
mouse_sensitivity = [0.5,0.5]


# the default radius and such of spheres
default_sphere_args = [30,30]

# perform a physics update every this many fractions of a second
physics_update_time = 0.00001

# max number of actions that the simulation or the window can queue up before it is told
# to wait before inserting any more
max_queue_size = 10


# number of decimals that all calculations are rounded to
precision = 10


# gravity constant
gravity = 6.67e-11


# simulation world size
simulation_bounds = [10000,10000,10000]