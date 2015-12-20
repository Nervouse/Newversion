__author__ = 'Faiku Fitim, Janusz Gradonski'

from OpenGL.GL import *


class Light:
    def __init__(self, position, color):
        """
        Konstruktor für das licht
        """
        self.enabled = True
        self.color = color
        self.position = position

    def init(self):
        """
        initialisiert das licht
        """
        # Lichter
        zeros = (0.15, 0.15, 0.15, 0.3)
        ones = (1.0, 1.0, 1.0, 0.3)
        half = (0.5, 0.5, 0.5, 0.5)

        glLightfv(GL_LIGHT0, GL_AMBIENT, (0.25, 0.25, 0.25, 1.0))   # Ambient Light
        glLightfv(GL_LIGHT0, GL_DIFFUSE, (1.0, 1.0, 1.0, 1.0))   # Diffuse Light
        glLightfv(GL_LIGHT0, GL_POSITION, (0.0, 0.0, 2.0, 1.0))  # Position The Light
        glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, zeros)
        glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, half)
        glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 100)
        glEnable(GL_LIGHT0)
        glEnable(GL_LIGHTING)
        glColorMaterial(GL_FRONT_AND_BACK, GL_DIFFUSE)
        """
        Wenn diese Zeilen nicht deaktiviert werden, kann man die Drehung nicht sehen auf den Planeten,
        weil die Texturen nicht mitgedreht werden bzw immer eine neue erzeugt wird
        glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
        glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
        glEnable(GL_TEXTURE_GEN_S)
        glEnable(GL_TEXTURE_GEN_T)
        """
        glEnable(GL_COLOR_MATERIAL)
        glEnable(GL_NORMALIZE)
        glShadeModel(GL_SMOOTH)

    def draw(self):
        """
        zeichnet das licht je nach dem ob schatten erwuensch sind
        :return:
        """
        if self.enabled:
            glShadeModel(GL_SMOOTH)
            glEnable(GL_CULL_FACE)
            glEnable(GL_DEPTH_TEST)
            glEnable(GL_LIGHTING)
            glDepthFunc(GL_LESS)
            lightZeroPosition = self.position
            lightZeroColor = self.color

            glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
            glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
            glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.01)
            glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.01)
            glEnable(GL_LIGHTING)
            glEnable(GL_LIGHT0)
        else:
            glDisable(GL_LIGHTING)
            glDisable(GL_LIGHT0)

    def disable(self):
        """
        deaktiviert das licht
        :return:
        """
        self.enabled = False

    def enable(self):
        """
        aktiviert das licht
        :return:
        """
        self.enabled = True