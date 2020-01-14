import pygame
import pygame.freetype
import time

from object3d import *
from backface_culling import *
from material import *
from color import *
from scene import *

# Define a main function, just to keep things nice and tidy
def main():
    # Initialize pygame, with the default parameters
    pygame.init()

    # Define the size/resolution of our window
    res_x = 640
    res_y = 480

    # Create a window and a display surface
    screen = pygame.display.set_mode((res_x, res_y))

    # Create a scene
    scene = Scene("TestScene")
    scene.camera = Camera(False, res_x, res_y)

    # Moves the camera back 2 units
    scene.camera.position -= vector3(0,0,2)

    # Create a cube and place it in a scene, at position (0,0,0)
    # This cube has 1 unit of side, and is red
    obj1 = Object3d("TestObject")
    obj1.scale = vector3(1, 1, 1)
    obj1.position = vector3(0, -1, 0)
    obj1.mesh = Mesh.create_cube((1, 1, 1))
    obj1.material = Material(color(1,0,0,1), "TestMaterial1")
    scene.add_object(obj1)

    # Create a second object, and add it as a child of the first object
    # When the first object rotates, this one will also mimic the transform
    obj2 = Object3d("ChildObject")
    obj2.position += vector3(0, 0.75, 0)
    obj2.mesh = Mesh.create_cube((0.5, 0.5, 0.5))
    obj2.material = Material(color(0,1,0,1), "TestMaterial2")
    obj1.add_child(obj2)

    # Specify the rotation of the object. It will rotate 15 degrees around the axis given, 
    # every second
    #angle = 0
    axis = vector3(1,0.7,0.2)
    axis = vector3(0,1,0)
    axis.normalize()

    # Timer
    #delta_time = 0
    #prev_time = time.time()
    #move_horizontal = 0
    #move_vertical = 0
    #move_depth = 0
    #move_value = 0.002
    #object_still = 0

    while (True):
        # Process OS events
        for event in pygame.event.get():
            # Checks if the user closed the window
            if (event.type == pygame.QUIT):
                # Exits the application immediately
                return
            elif (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_ESCAPE):
                    return

        # Clears the screen with a very dark blue (0, 0, 20)
        screen.fill((0,0,0))

        scene.render(screen)

        # Swaps the back and front buffer, effectively displaying what we rendered
        pygame.display.flip()

# Run the main function
main()