import math
from typing import List

from OpenGL.GL import glReadPixels
from OpenGL.raw.GL.VERSION.GL_1_0 import glEnable, GL_DEPTH_TEST, GL_TEXTURE_2D, glBlendFunc, GL_SRC_ALPHA, \
    GL_ONE_MINUS_SRC_ALPHA, glCullFace, GL_BACK, GL_COLOR_BUFFER_BIT, glClear, GL_DEPTH_BUFFER_BIT, GL_CULL_FACE, \
    glDisable, glClearColor, GL_DEPTH_COMPONENT, GL_FRONT
from OpenGL.raw.GL._types import GL_FLOAT
from glm import mat4, vec3

from pykotor.gl.scene import Camera

from pykotor.gl.shader import Shader, TERRAIN_VSHADER, TERRAIN_FSHADER

from pykotor.gl.models.terrain import Terrain
from pykotor.resource.formats.mdl import MDL


class EditorScene:
    def __init__(self):
        glEnable(GL_TEXTURE_2D)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)
        glCullFace(GL_BACK)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        self.terrain_shader = Shader(TERRAIN_VSHADER, TERRAIN_FSHADER)
        self.camera = Camera()
        self.cursor: vec3 = vec3()

        self.camera.x = 0
        self.camera.y = 0
        self.camera.z = 4
        self.camera.pitch = math.pi / 4

        # Data -----------------
        self.terrain: Terrain = Terrain()
        self.objects: List = []

    def render(self):
        glClearColor(1.0, 0.9, 0.9, 1.0)
        glEnable(GL_TEXTURE_2D)
        glEnable(GL_DEPTH_TEST)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        self.terrain_shader.use()
        self.terrain_shader.set_matrix4("view", self.camera.view())
        self.terrain_shader.set_matrix4("projection", self.camera.projection())
        self.terrain_shader.set_vector3("cursor", self.cursor)

        self.terrain.draw(self.terrain_shader, mat4())

    def dCompile(self):
        ...
