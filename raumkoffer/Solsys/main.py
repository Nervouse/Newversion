__author__ = 'Faiku Fitim, Janusz Gradonski'
__version__ = "1.0"

from Solsys.Galaxie import *

def main(sc):
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)   # Select type of Display mode
        glutInitWindowSize(900, 600)                               # get a 640 x 480 window
        glutInitWindowPosition(500, 300)                              # the window starts at the upper left corner of the screen
        glutCreateWindow(b'Fitim Gradonski Solarsystem')   # Titel
        glutDisplayFunc(sc.DrawGLScene)                           # Register the drawing function with glut
        glutIdleFunc(sc.DrawGLScene)
        glutReshapeFunc(sc.ReSizeGLScene)
        sc.init(640, 480)
        glutMainLoop()



if __name__ == '__main__':
    app = QtWidgets.QApplication(glutInit(sys.argv))
    app.processEvents()

    s = Galaxie(900, 600)
    main(s)