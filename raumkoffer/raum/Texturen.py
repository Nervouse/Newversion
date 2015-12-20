__author__ = 'Faiku Fitim, Janusz Gradonski'

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL.Image import *


class Texturen():

    @staticmethod
    def LoadTexture(pic):
        """
        ladet eine textur
        :param pic: pfad des Bilds der als textur geladen werden soll
        :return:
        """

        image = open(pic)

        # Textur
        ix = image.size[0]
        iy = image.size[1]
        image = image.tostring("raw", "RGBX", 0, -1)

        # Textur erstellen
        textures = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, textures)  # 2d texture (x and y size)

        # Planet P1
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_NEAREST)
        gluBuild2DMipmaps(GL_TEXTURE_2D, 3, ix, iy, GL_RGBA, GL_UNSIGNED_BYTE, image)

        return textures