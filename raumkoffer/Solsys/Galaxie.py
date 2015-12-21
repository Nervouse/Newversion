__author__ = 'Faiku Fitim, Janusz Gradonski'
__version__ = "1.0"

from PyQt5 import QtWidgets

from Objekte.Fixstern import *
from Objekte.Planet import *


class Galaxie(QtWidgets.QWidget):

    def __init__(self, width, height):
        #Variablen Initialisierung
        QtWidgets.QWidget.__init__(self)
        self.light = Light([0, 0, 0, 80], [0.8, 1.0, 0.8, 1.0])
        self.pos = False
        self.mod = True
        self.lights = True
        self.anim = True
        self.zoom = 0
        self.width = width
        self.height = height
        self.erdenTextur = None
        self.jupiterTextur = None
        self.marsTextur = None
        self.merkurTextur = None
        self.mondTextur = None
        self.neptunTextur = None
        self.plutoTextur = None
        self.saturnTextur = None
        self.sonnenTextur = None
        self.uranusTextur = None
        self.venusTextur = None

    def init(self, Width, Height):
        """
        gl Fesnter einstellungen
        """
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClearDepth(1.0)
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glutKeyboardFunc(self.TestenControll)
        gluPerspective(45.0, float(Width) / float(Height), 0.1, 100000.0)
        glMatrixMode(GL_MODELVIEW)

        #Fesnter initialisierung
        self.light.init()
        self.texturLaden()
        self.loadPlanets()
        self.texturenEin()
        self.pos = True
        self.help()

    def TestenControll(self, *args):
        """
        Tastatur ereignise werden abgefangen und interpretiert
        :param args:
        :return:
        """
        #t- Texturen aktiviren
        if args[0] == b't':
            if self.mod:
                self.texturenAus()
                self.mod = False
            else:
                self.texturenEin()
                self.mod = True

        # l - Licht aktivieren
        if args[0] == b'l':
            if self.lights:
                self.sonne.disableLight()
                self.lights = False
            else:
                self.sonne.enableLight()
                self.lights = True

        #P fur Pause
        if args[0] == b'p':
            if self.anim:
                self.pauseAll()
                self.anim = False
            else:
                self.playAll()
                self.anim = True

        #1 - Erste Perspektive (default)
        if args[0] == b'1':
            if self.pos:
                self.zoom = 0
                self.pos = False

        #2- Zweite Perspektive
        if args[0] == b'2':
                self.zoom = 0
                self.pos = True
        #Zoom
        if args[0] == b'+':
            self.zoom += 5
        if args[0] == b'-':
            self.zoom -= 5

        #h - hilfe
        if args[0] == b'h':
            self.help()

        #f - (faster) schneller
        if args[0] == b'f':
            self.sonne.animateAllChildrenFaster(0.05, 0.0001)

        #s - (slower) langsamer
        if args[0] == b's':
            self.sonne.animateAllChildrenSlower(0.05, 0.0001)


    def loadPlanets(self):
        """
        Die Planeten werden initialisiert
        """

        # Planeten
        # Parameter(Planet): (position, anim, rotation, rotSpeed, rotPoint, movSpeed, radius, textur, divisions, monde)
        self.merkur = Planet([-17, 0, -80], True, [90, 0, 0], 0.05, self.sonne.position, 0.0001, 0.4, self.merkurTextur, 32, None)
        self.venus = Planet([-20.5, 0, -80], True, [90, 0, 0], 0.05, self.sonne.position, 0.000125, 1.21, self.venusTextur, 32, None)
        self.erde = Planet([-29, 0, -80], True, [90, 0, 0], 0.6, self.sonne.position, 0.00006, 1.28, self.erdenTextur, 32, None)
        self.mars = Planet([-36.5, 0, -80], True, [90, 0, 0], 0.05, self.sonne.position, 0.00009, 0.6, self.marsTextur, 32, None)
        self.jupiter = Planet([-59, 0, -80], True, [90, 0, 0], 0.05, self.sonne.position, 0.000035, 14.3, self.jupiterTextur, 32, None)
        self.saturn = Planet([-85, 0, -80], True, [90, 0, 0], 0.05, self.sonne.position, 0.000056, 12.05, self.saturnTextur, 32, None)
        self.uranus = Planet([-98, 0, -80], True, [90, 0, 0], 0.05, self.sonne.position, 0.00004, 5.11, self.uranusTextur, 32, None)
        self.neptun = Planet([-115, 0, -80], True, [90, 0, 0], 0.05, self.sonne.position, 0.000087, 4.95, self.neptunTextur, 32, None)
        self.pluto = Planet([-125, 0, -80], True, [90, 0, 0], 0.05, self.sonne.position, 0.000025, 0.1, self.plutoTextur, 32, None)

        # Fixstern ist die Sonne
        # Parameter(Fixstern): (position, rotSpeed, textur, planeten, anim, licht, radius, divisions)
        self.sonne = Fixstern([0, 0, -80], 0.2, self.sonnenTextur, None, True, self.light, 10, 64)

        # Monde
         # Parameter(Mond): (anim, rotation, rotSpeed, parent, entf_rotPoint, movSpeed, radius, textur, divisions)
        self.mond = Mond(True, [-90, 0, -80], 0, self.erde, 5, -0.00005, 0.4, self.mondTextur, 24)

        self.erde.addMond(self.mond)
        self.sonne.addPlanet(self.erde)
        self.sonne.addPlanet(self.jupiter)
        self.sonne.addPlanet(self.mars)
        self.sonne.addPlanet(self.merkur)
        self.sonne.addPlanet(self.neptun)
        self.sonne.addPlanet(self.pluto)
        self.sonne.addPlanet(self.saturn)
        self.sonne.addPlanet(self.uranus)
        self.sonne.addPlanet(self.venus)

    def texturLaden(self):
        """
        Die Texturen fuer die Planeten werden aus den Ordner
        img herausgeholt und geladen
        """
        self.plutoTextur = Texturen.LoadTexture("../img/pluto.jpg")
        self.saturnTextur = Texturen.LoadTexture("../img/saturn.jpg")
        self.sonnenTextur = Texturen.LoadTexture("../img/sonne.jpg")
        self.erdenTextur = Texturen.LoadTexture("../img/erde.jpg")
        self.jupiterTextur = Texturen.LoadTexture("../img/jupiter.jpg")
        self.marsTextur = Texturen.LoadTexture("../img/mars.jpg")
        self.merkurTextur = Texturen.LoadTexture("../img/merkur.jpg")
        self.mondTextur = Texturen.LoadTexture("../img/mond.jpg")
        self.neptunTextur = Texturen.LoadTexture("../img/neptun.jpg")
        self.uranusTextur = Texturen.LoadTexture("../img/uranus.jpg")
        self.venusTextur = Texturen.LoadTexture("../img/venus.jpg")








    def ReSizeGLScene(self, Width, Height):
        """
        Wenn die grosse vom Fesnter sich verandert wird somit die Galaxie angepasst
        damit die Planeten rund bleiben.
        """
        # Wenn das Fenster zu klein ist, erhoehen auf 1
        if Height == 0:
            Height = 1

        glViewport(0, 0, Width, Height)  # Reset The Current Viewport And Perspective Transformation
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        # Perspektive
        gluPerspective(50.0, float(Width) / float(Height), 0.1, 100000.0)  # Naehe
        glMatrixMode(GL_MODELVIEW)

        self.width = Width
        self.height = Height


    """
    szene zeichenn
    """
    def DrawGLScene(self):
        """
        alle komponenten zeichnen
        :return:
        """
        self.update()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Screen loeschen und depth buffer loeschen

        self.sonne.draw(self.pos, self.zoom)


        glutSwapBuffers()  # zeichnen

    def update(self):
        """
        alle komponenten aktualisierne
        :return:
        """
        self.sonne.update()

    def help(self):
        """
        Method help
        This displays an extern window with the description of the controls
        http://projects.skylogic.ca/blog/how-to-install-pyqt5-and-build-your-first-gui-in-python-3-4/
        """
        self.setGeometry(300, 300, 300, 330)
        self.setWindowTitle('Solarsystem Help')
        self.setToolTip('This is the <i>Help</i> of the <i>controls</i> ')
        self.setMaximumSize(300, 330)
        self.move(650, 0)
        self.edit = QtWidgets.QTextEdit()
        self.edit.setEnabled(False)
        self.edit.append('<h1>Controls</h1>'
                         '<b><i>Mouse controls:</i></b>'
                         '<br>Turn light on/ off: <b>Left mouse click</b>'
                         '<br>Turn texture on/ off: <b>Right mouse click</b>'
                         '<br>'
                         '<br><b><i>Keyboard controls:</i></b>'
                         '<br>Increase speed of Planets: <b>f</b>'
                         '<br>Decrease speed of Planets: <b>s</b>'
                         '<br>Stop animation: <b>p</b>'
                         '<br>Load your own textures: <b>t</b>'
                         '<br>Switch view: <b>1 or 2</b>'
                         '<br>Zoom in: <b>+</b>'
                         '<br>Zoom out: <b>-</b>'
                         '<br>Display this help: <b>h</b>'
                         '<br>Quit program: <b>ESC</b>')
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.edit)
        self.setWindowOpacity(0.9)
        self.show()


    def texturenEin(self):
        """
        Texturen einschalten mittels glEnable
        """
        glEnable(GL_TEXTURE_2D)

    def texturenAus(self):
        """
        Texturen ausschalten mittels glDisable
        """
        glDisable(GL_TEXTURE_2D)

    def pauseAll(self):
        """
        Alle Planeten werden gestoppt
        """
        self.sonne.setAnimation(False)

    def playAll(self):
        """
        Alle Planeten werden wieder rotiert
        """
        self.sonne.setAnimation(True)
