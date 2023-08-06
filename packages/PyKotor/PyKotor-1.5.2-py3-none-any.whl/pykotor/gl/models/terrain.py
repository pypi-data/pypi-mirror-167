import ctypes
import random

import numpy as np
from OpenGL.GL import glGenVertexArrays, glBufferData, glDrawElements
from OpenGL.GL.shaders import GL_FALSE
from OpenGL.raw.GL.ARB.vertex_shader import GL_FLOAT
from OpenGL.GL import glVertexAttribPointer, glGenVertexArrays, glGenBuffers
from OpenGL.raw.GL.VERSION.GL_1_0 import GL_TRIANGLES, GL_UNSIGNED_SHORT
from OpenGL.raw.GL.VERSION.GL_1_3 import glActiveTexture, GL_TEXTURE0, GL_TEXTURE1
from OpenGL.raw.GL.VERSION.GL_1_5 import glBindBuffer, GL_ARRAY_BUFFER, GL_ELEMENT_ARRAY_BUFFER, GL_STATIC_DRAW
from OpenGL.raw.GL.VERSION.GL_2_0 import glEnableVertexAttribArray, glVertexAttribPointer
from OpenGL.raw.GL.VERSION.GL_3_0 import glBindVertexArray
from glm import mat4
from pykotor.common.geometry import Vector3, Vector2, Vector4, SurfaceMaterial
from pykotor.resource.formats.bwm import BWM, BWMFace

from pykotor.resource.formats.mdl.mdl_data import MDLFace, MDLController, MDLControllerType, MDLControllerRow

from pykotor.resource.formats.mdl import MDLNode, MDLMesh

from pykotor.gl.shader import Shader, Texture
from pykotor.resource.formats.mdl import MDL
from pykotor.resource.formats.tpc import read_tpc


class TerrainVertex:
    def __init__(self, x, y, z, u, v):
        self.x = x
        self.y = y
        self.z = z
        self.u = u
        self.v = v


class TerrainFace:
    def __init__(self, i1, i2, i3):
        self.i1: TerrainVertex = i1
        self.i2: TerrainVertex = i2
        self.i3: TerrainVertex = i3


class Terrain:
    def __init__(self, width=100, height=100):
        self.vertices = []
        self.faces = []
        for i in range(height+1):
            for j in range(width+1):
                self.vertices.append(TerrainVertex(j, i, random.uniform(0.0, 0.5), j, i))
        for y in range(height):
            for x in range(width):
                i1 = self.vertices[y*(width+1) + x]
                i2 = self.vertices[y*(width+1) + (x+1)]
                i3 = self.vertices[(y+1)*(width+1) + x]
                i4 = self.vertices[(y+1)*(width+1) + (x+1)]
                self.faces.append(TerrainFace(i1, i2, i3))
                self.faces.append(TerrainFace(i2, i4, i3))

        vertex_data = self.raw_vertices()
        element_data = self.raw_elements()

        self._vao = glGenVertexArrays(1)
        self._vbo = glGenBuffers(1)
        self._ebo = glGenBuffers(1)
        glBindVertexArray(self._vao)

        glBindBuffer(GL_ARRAY_BUFFER, self._vbo)
        glBufferData(GL_ARRAY_BUFFER, len(vertex_data)*4, vertex_data, GL_STATIC_DRAW)

        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self._ebo)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, len(element_data)*2, element_data, GL_STATIC_DRAW)
        self._face_count = len(element_data)

        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 20, ctypes.c_void_p(0))

        glEnableVertexAttribArray(3)
        glVertexAttribPointer(3, 2, GL_FLOAT, GL_FALSE, 20, ctypes.c_void_p(12))

        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glBindVertexArray(0)

        self.texture = Texture.from_tpc(read_tpc("lda_grass01.tpc"))

    def raw_vertices(self):
        vertex_data = []
        for face in self.faces:
            vertex_data.extend([face.i1.x, face.i1.y, face.i1.z, face.i1.u, face.i1.v])
            vertex_data.extend([face.i2.x, face.i2.y, face.i2.z, face.i2.u, face.i2.v])
            vertex_data.extend([face.i3.x, face.i3.y, face.i3.z, face.i3.u, face.i3.v])
        return np.array(vertex_data, dtype='float32')

    def raw_elements(self):
        element_data = []
        for i in range(len(self.faces)):
            start = i*3
            element_data.extend([start+0, start+1, start+2])
        return np.array(element_data, dtype='uint16')

    def draw(self, shader: Shader, transform: mat4):
        shader.set_matrix4("model", transform)

        glActiveTexture(GL_TEXTURE0)
        self.texture.use()

        glBindVertexArray(self._vao)
        glDrawElements(GL_TRIANGLES, self._face_count, GL_UNSIGNED_SHORT, None)

    def compile_mdl(self) -> MDL:
        mdl = MDL()
        mdl.root.name = "tery"
        mdl.name = "tery"

        node = MDLNode()
        node.node_id = 1
        node.name = "terrain"

        pos_c = MDLController()
        pos_c.controller_type = MDLControllerType.POSITION
        pos_c.rows = [MDLControllerRow(0.0, [0.0, 0.0, 0.0])]
        node.controllers.append(pos_c)

        rot_c = MDLController()
        rot_c.controller_type = MDLControllerType.ORIENTATION
        rot_c.rows = [MDLControllerRow(0.0, [0.0, 0.0, 0.0, 1.0])]
        node.controllers.append(rot_c)

        node.mesh = MDLMesh()
        node.mesh.texture_1 = "lda_grass01"
        node.mesh.vertex_uv1 = []
        node.mesh.vertex_normals = []
        for ter_vert in self.vertices:
            node.mesh.vertex_positions.append(Vector3(ter_vert.x, ter_vert.y, ter_vert.z))
            node.mesh.vertex_uv1.append(Vector2(ter_vert.u, ter_vert.v))

            node.mesh.vertex_normals.append(Vector3(0, 0, 1))
        for ter_face in self.faces:
            face = MDLFace()
            face.v1, face.v2, face.v3 = self.vertices.index(ter_face.i1), self.vertices.index(ter_face.i2), self.vertices.index(ter_face.i3)
            node.mesh.faces.append(face)
        '''for face in self.faces:
            node.mesh.vertex_positions.append(Vector3(face.i1.x, face.i1.y, face.i1.z))
            node.mesh.vertex_positions.append(Vector3(face.i2.x, face.i2.y, face.i2.z))
            node.mesh.vertex_positions.append(Vector3(face.i3.x, face.i3.y, face.i3.z))
            node.mesh.vertex_uv1.append(Vector2(face.i1.u, face.i1.v))
            node.mesh.vertex_uv1.append(Vector2(face.i2.u, face.i2.v))
            node.mesh.vertex_uv1.append(Vector2(face.i3.u, face.i3.v))
        for i in range(len(self.faces)):
            start = i * 3
            face = MDLFace()
            face.v1, face.v2, face.v3 = start + 0, start + 1, start + 2
            node.mesh.faces.append(face)'''
        mdl.root.children.append(node)

        return mdl

    def compile_bwm(self) -> BWM:
        wok = BWM()

        for ter_face in self.faces:
            v1 = Vector3(ter_face.i1.x, ter_face.i1.y, ter_face.i1.z)
            v2 = Vector3(ter_face.i2.x, ter_face.i2.y, ter_face.i2.z)
            v3 = Vector3(ter_face.i3.x, ter_face.i3.y, ter_face.i3.z)
            face = BWMFace(v1, v2, v3)
            face.material = SurfaceMaterial.GRASS
            wok.faces.append(face)

        return wok
