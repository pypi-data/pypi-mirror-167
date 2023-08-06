import math

import glfw
import glm
from OpenGL.GL import glReadPixels
from OpenGL.raw.GL.VERSION.GL_1_0 import GL_DEPTH_COMPONENT
from OpenGL.raw.GL.VERSION.GL_1_2 import GL_UNSIGNED_INT_8_8_8_8
from OpenGL.raw.GL._types import GL_FLOAT
from OpenGL.raw.GLU import gluUnProject
from glm import mat4, vec3, vec4

from pykotor.resource.formats.bwm import write_bwm
from pykotor.resource.type import ResourceType

from pykotor.gl.editor import EditorScene
from pykotor.gl.shader import Shader, KOTOR_VSHADER, KOTOR_FSHADER, TERRAIN_FSHADER, TERRAIN_VSHADER

from pykotor.common.module import Module
from pykotor.extract.installation import Installation
from pykotor.gl.models.terrain import Terrain

from pykotor.gl.scene import Scene, Camera
from pykotor.resource.formats.mdl import write_mdl, read_mdl


def view_module():
    if not glfw.init():
        return

    installation = Installation("C:/Program Files (x86)/Steam/steamapps/common/swkotor")
    module = Module("danm13", installation)

    window = glfw.create_window(640, 480, "Hello World", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    scene = None
    init = False
    while not glfw.window_should_close(window):
        if not init:
            scene = Scene(module, installation)
            init = True
        scene.render()

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()


def view_module2():
    if not glfw.init():
        return

    installation = Installation("C:/Program Files (x86)/Steam/steamapps/common/swkotor")
    module = Module("danm13", installation)

    window = glfw.create_window(640, 480, "Hello World", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    scene = None
    init = False
    while not glfw.window_should_close(window):
        if not init:
            scene = Scene(module, installation)
            scene.objects["wololo"] = Terrain()
            init = True
        scene.render()

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()


def view_terrain():
    init = False
    scene = None
    mouse = vec3()

    if not glfw.init():
        return

    def key_callback(window, key, scancode, action, mods):
        if key == 87:  # W
            scene.camera.y += 1
        elif key == 65:  # A
            scene.camera.x -= 1
        elif key == 83:  # S
            scene.camera.y -= 1
        elif key == 68:  # D
            scene.camera.x += 1
        elif key == 81:  # Q
            scene.camera.z += 1
        elif key == 69:  # E
            scene.camera.z -= 1

    def cursor_pos_callback(window, xpos, ypos):
        mouse.x = xpos
        mouse.y = 1080 - ypos

    window = glfw.create_window(1920, 1080, "Hello World", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    while not glfw.window_should_close(window):
        if not init:
            terrain = Terrain(15, 15)
            path = "C:/Program Files (x86)/Steam/steamapps/common/swkotor/Override/"
            #write_mdl(terrain.compile_mdl(), path+"tery.mdl", ResourceType.MDL, path+"tery.mdx")
            #write_bwm(terrain.compile_bwm(), path+"tery.wok")

            init = True
            scene = EditorScene()
            scene.camera.z = 4
            scene.camera.pitch = math.pi/5*3
            scene.camera.yaw = -math.pi/2

        scene.render()

        zpos = glReadPixels(mouse.x, mouse.y, 1, 1, GL_DEPTH_COMPONENT, GL_FLOAT)[0][0]
        scene.cursor = glm.unProject(vec3(mouse.x, mouse.y, zpos), scene.camera.view(), scene.camera.projection(), vec4(0, 0, 1920, 1080))

        glfw.swap_buffers(window)
        glfw.poll_events()

        glfw.set_key_callback(window, key_callback)
        glfw.set_cursor_pos_callback(window, cursor_pos_callback)

    glfw.terminate()


if __name__ == "__main__":
    view_terrain()

