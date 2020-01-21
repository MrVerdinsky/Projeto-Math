# Import pygame into our program
import pygame
import pygame.freetype
import time

from scene import *
from object3d import *
from mesh import *
from material import *
from color import *

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


    verts = []
    # vertice da direita
    verts.append(vector3(0.5, -0.5, -0.5))
    # primeiro muda x da altura
    # meio muda altura
    # último muda z da altura
    verts.append(vector3(0, 0.5, 0))
    # primeiro muda x do vértice da esquerda
    # meio muda altura do vértice da esquerda
    # último muda z do vértice da esquerda
    verts.append(vector3(-0.5, -0.5, -0.5/2))
    
    verts.append(vector3(0, -0.5, 0.5))

    obj1 = Object3d("Pyramid")
    obj1.position += vector3(0, 0, 0)
    obj1.mesh = Mesh.create_triPyramid(verts)
    obj1.material = Material(color(1,0,1,1), "TestMaterial1")
    scene.add_object(obj1)
    
    verts_child = []
    verts_child.append(vector3(-0.5/2, -0.5/2, -0.5/2))
    verts_child.append(vector3(0, -0.5/2, 0))
    verts_child.append(vector3(0.5/2, -0.5/2, -0.5/2))
    verts_child.append(vector3(0, 0.5, -0.5/2))
    
    # Create a second object, and add it as a child of the first object
    # When the first object rotates, this one will also mimic the transform
    obj2 = Object3d("ChildObject")
    obj2.position += vector3(0, -0.75, 0)
    obj2.mesh = Mesh.create_triPyramid(verts_child)
    obj2.material = Material(color(0,1,0,1), "TestMaterial2")
    obj1.add_child(obj2)

    # Specify the rotation of the object. It will rotate 15 degrees around the axis given, 
    # every second
    angle = 0
    axis = vector3(1,0.7,0.2)
    axis = vector3(0,1,0)
    axis.normalize()

    # Timer
    delta_time = 0
    prev_time = time.time()
    move_horizontal = 0
    move_vertical = 0
    move_depth = 0
    move_value = 0.002
    object_still = 0
    # Game loop, runs forever
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

            # Rotates object around its Y axis to the right
            if pygame.key.get_pressed()[pygame.K_RIGHT] == True:
                angle = 50
                axis = vector3(0,1,0)

                # Keep the object from rotating if there's an attempt to turn it to oppisite direction
                # Or rotates the object to the opposite direction
                if pygame.key.get_pressed()[pygame.K_LEFT] == True:
                    angle = 0
                # Rotates object arrouns its Y and Z axis to the right and up simultaneously
                elif pygame.key.get_pressed()[pygame.K_UP] == True:
                    angle = 50
                    axis = vector3(0,1,1)
                # Rotates object arrouns its Y and Z axis to the right and down simultaneously
                elif pygame.key.get_pressed()[pygame.K_DOWN] == True:
                    axis = vector3(1,1,0)
            

            # Rotates object arround its Y axis to the left
            elif pygame.key.get_pressed()[pygame.K_LEFT] == True:
                angle = -50
                axis = vector3(0,1,0)
                
                # Keep the object from rotating if there's an attempt to turn it to oppisite direction
                # Or rotates the object to the opposite direction
                # não sei maltinha, decidam o que acham melhor
                if pygame.key.get_pressed()[pygame.K_RIGHT] == True:
                    angle = 50
                    axis = vector3(0,1,0)

                # Rotates object arrouns its Y and Z axis to the right and up simultaneously 
                elif pygame.key.get_pressed()[pygame.K_UP] == True:
                    axis = vector3(0,1,1)

                # Rotates object arrouns its Y and Z axis to the right and down simultaneously
                elif pygame.key.get_pressed()[pygame.K_DOWN] == True:
                    angle = -50
                    axis = vector3(0,1,1)
       
            # Rotates object up arround its X axis 
            elif pygame.key.get_pressed()[pygame.K_UP] == True:
                angle = -50
                axis = vector3(1,0,0)

            # Rotates object down arround its X axis
            elif pygame.key.get_pressed()[pygame.K_DOWN] == True:
                angle = 50
                axis = vector3(1,0,0)

            # Rotates object up arround its Z axis
            elif pygame.key.get_pressed()[pygame.K_PAGEDOWN] == True:
                angle = 50
                axis = vector3(0, 0, 1)
                if pygame.key.get_pressed()[pygame.K_PAGEUP] == True:
                    angle = -50

            # Rotates object down arround its Z axis
            elif pygame.key.get_pressed()[pygame.K_PAGEUP] == True:
                angle = -50
                axis = vector3(0, 0, 1)
            else:
                angle = 0
            # Moves object to the right
            if pygame.key.get_pressed()[pygame.K_d] == True:
                move_horizontal = move_value
               # Stops the object if there's an attempt to move it to the opposite direction
                if pygame.key.get_pressed()[pygame.K_a] == True:
                    move_horizontal = object_still 
                elif pygame.key.get_pressed()[pygame.K_w] == True:
                    move_vertical = move_value
                
                elif pygame.key.get_pressed()[pygame.K_s] == True:
                    move_vertical = -move_value
                elif pygame.key.get_pressed()[pygame.K_e] == True:
                    move_depth = move_value
                    if pygame.key.get_pressed()[pygame.K_q] == True:
                        move_depth = 0
                elif pygame.key.get_pressed()[pygame.K_q] == True:
                    move_depth = -move_value
                    if pygame.key.get_pressed()[pygame.K_e] == True:
                        move_depth = 0
                else:
                    move_vertical = 0
                    move_depth = 0
            
                
            # Moves object to the left
            elif pygame.key.get_pressed()[pygame.K_a] == True:
                move_horizontal = -move_value
                if pygame.key.get_pressed()[pygame.K_d] == True:
                    move_horizontal = object_still

                elif pygame.key.get_pressed()[pygame.K_w] == True:
                    move_vertical = move_value
                
                elif pygame.key.get_pressed()[pygame.K_s] == True:
                    move_vertical = -move_value
                elif pygame.key.get_pressed()[pygame.K_e] == True:
                    move_depth = move_value
                    if pygame.key.get_pressed()[pygame.K_q] == True:
                        move_depth = 0
                        
                elif pygame.key.get_pressed()[pygame.K_q] == True:
                    move_depth = -move_value
                    if pygame.key.get_pressed()[pygame.K_e] == True:
                        move_depth = 0
                else:
                    move_vertical = 0
                    move_depth = 0


            # Moves object up 
            elif pygame.key.get_pressed()[pygame.K_w] == True:
                move_vertical = move_value

                if pygame.key.get_pressed()[pygame.K_s] == True:
                    move_vertical = object_still

                elif pygame.key.get_pressed()[pygame.K_d] == True:
                    move_horizontal = move_value
               
                elif pygame.key.get_pressed()[pygame.K_a] == True:
                    move_horizontal = -move_value

                elif pygame.key.get_pressed()[pygame.K_e] == True:
                    move_depth = move_value
                    if pygame.key.get_pressed()[pygame.K_q] == True:
                        move_depth = 0
                elif pygame.key.get_pressed()[pygame.K_q] == True:
                    move_depth = -move_value
                    if pygame.key.get_pressed()[pygame.K_e] == True:
                        move_depth = 0
                else:
                    move_horizontal = 0
                    move_depth = 0
            # Moves object down
            elif pygame.key.get_pressed()[pygame.K_s] == True:
                move_vertical = -move_value
                if pygame.key.get_pressed()[pygame.K_w] == True:
                    move_vertical = object_still

                elif pygame.key.get_pressed()[pygame.K_d] == True:
                    move_horizontal = move_value
                
                elif pygame.key.get_pressed()[pygame.K_a] == True:
                    move_horizontal = -move_value

                elif pygame.key.get_pressed()[pygame.K_e] == True:
                    move_depth = move_value
                    if pygame.key.get_pressed()[pygame.K_q] == True:
                        move_depth = 0
                elif pygame.key.get_pressed()[pygame.K_q] == True:
                    move_depth = -move_value
                    if pygame.key.get_pressed()[pygame.K_e] == True:
                        move_depth = 0

                
                else:
                    move_horizontal = 0
                    move_depth = 0

            # Moves object forward
            elif pygame.key.get_pressed()[pygame.K_e] == True:
                move_depth = move_value
                if pygame.key.get_pressed()[pygame.K_q]:
                    move_depth = 0
                
                
                
            # Moves object back
            elif pygame.key.get_pressed()[pygame.K_q] == True:
                move_depth = -move_value
                if pygame.key.get_pressed()[pygame.K_e]:
                    move_depth = 0
            
            # if none of those keys are pressed, the object stays still
            else:
                move_horizontal = object_still
                move_vertical = object_still
                move_depth = object_still


        # sets the camera position accordly to the keyboard input
        scene.camera.position -= vector3(move_horizontal,move_vertical,move_depth)

        # Clears the screen with a very dark blue (0, 0, 20)
        screen.fill((0,0,0))

        # Rotates the object, considering the time passed (not linked to frame rate)
        q = from_rotation_vector((axis * math.radians(angle) * delta_time).to_np3())
        obj1.rotation = q * obj1.rotation

        scene.render(screen)

        # Swaps the back and front buffer, effectively displaying what we rendered
        pygame.display.flip()

        # Updates the timer, so we we know how long has it been since the last frame
        delta_time = time.time() - prev_time
        prev_time = time.time()


# Run the main function
main()
