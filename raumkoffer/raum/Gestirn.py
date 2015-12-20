__author__ = 'Faiku Fitim, Janusz Gradonski'

from raum.Texturen import *


class Gestirn:
    def __init__(self, position, anim, rotation, rotSpeed, rotPoint, entf_rotPoint, movSpeed, radius, textur, divisions):
        """
        kosnturktor des "interfaces" getsrin
        :param position: posotion
        :param anim: animation
        :param rotation: roatation
        :param rotSpeed: rotationsgeschw
        :param rotPoint: rotationspunkt
        :param entf_rotPoint: entferntung zum rotationspkt
        :param movSpeed: bewegungsgeschw
        :param radius: radius
        :param textur: textur d gestrins
        :param divisions: unterteulungen
        :return:
        """
        self.position = position  # Position im XYZ-Raum
        self.anim = anim  # Animationen an/aus
        self.rotation = rotation  # Rotation um die eigene Achse
        self.rotSpeed = rotSpeed  # Rotationsgeschwindigkeit
        self.rotPoint = rotPoint  # Punkt, um den sich der Planet bewegen soll
        self.entf_rotPoint = entf_rotPoint  # Entfernung von ebendiesem Punkt
        self.movSpeed = movSpeed  # Orbitalgeschwindigkeit
        self.radius = radius  # Radius des Himmelskoerpers
        self.textur = textur  # Textur
        self.divisions = divisions  # Unterteilungen. Mehr = feinere, schoenere Kugel
        self.top = False


    def update(self):
        """
        Beim update einfach immer den Himmelskoerper um seine eigene achste rotieren
        :return:
        """
        if self.anim:
            # Nur dann, wenn die animation nicht pausiert wurde
            self.rotate([0, 0, self.rotSpeed])

    def draw(self, top, zoom):
        """
        zeichent das gestrin
        :param top:
        :param zoom:
        :return:
        """
        # Identity-Matrix neu laden
        glLoadIdentity()

        # Je nachdem, welchen Sichtmodus der User gewaehlt hat, wird die Kamera
        # an einer anderen Stelle gezeichnet bzw. zeigt auf einen anderen Punkt
        if top:
            # Ansicht von oben
            gluLookAt(0, 100-zoom, 0, 0, 0, -80, 0, 1, 0)
        else:
            # Seitenansicht
            gluLookAt(0, 0, 10-zoom, 0, 0, -80, 0, 1, 0)

        # Den Himmelskoerper auf seine Position bewegen, bevor er rotiert
        # wird. Aendert man die Reihenfolge der Transformationen, aendert
        # sich auch das Ergebnis. Zuerst drehen, dann bewegen ->
        # Bewegung evtl falsch, daher zuerst bewegen, dann drehen
        glTranslatef(self.position[0], self.position[1], self.position[2])

        # Objekt um die eigene Achse drehen
        glRotatef(self.rotation[0], 1.0, 0.0, 0.0)  # Rotatation um X-Achse
        glRotatef(self.rotation[1], 0.0, 1.0, 0.0)  # Rotatation um Y-Achse
        glRotatef(self.rotation[2], 0.0, 0.0, 1.0)  # Rotatation um Z-Achse

        # Die Textur zuweisen
        glBindTexture(GL_TEXTURE_2D, self.textur)
        quadratic = gluNewQuadric()
        gluQuadricNormals(quadratic, GLU_SMOOTH)
        gluQuadricTexture(quadratic, GL_TRUE)

        # Zeichnet eine Kugel auf den Bildschirm
        gluSphere(quadratic, self.radius, self.divisions, self.divisions)

    def rotate(self, rotation):
        """
        dreht den himmelskoerper
        :param rotation: array mit den werten
        :return:
        """
        # Nur wenn das Array drei werte hat, weitermachen
        if isinstance(rotation, list) and len(rotation) == 3:
            if rotation[0] >= 0:
                self.rotation[0] += rotation[0]
            if rotation[1] >= 0:
                self.rotation[1] += rotation[1]
            if rotation[2] >= 0:
                self.rotation[2] += rotation[2]
        else:
            raise TypeError


    def translate(self, pos):
        """
        bewegt das gestirn weiter
        :param pos: position um die es weiter bewegt wird
        :return:
        """
        if isinstance(pos, list) and len(pos) == 3:
            # Nur wenn das Array drei werte hat, weitermachen
            if pos[0] >= 0:
                self.position[0] += pos[0]
            if pos[1] >= 0:
                self.position[1] += pos[1]
            if pos[2] >= 0:
                self.position[2] += pos[2]
        else:
            raise TypeError("Array with len 3 needed")

    def setAnimation(self, anim):
        """
        setzt die animation
        :param anim: true oder false ob es sich bewegen soll
        :return:
        """
        if isinstance(anim, bool):
            self.anim = anim

    def setAbstand(self, abstand):
        """
        abstand der gestrine setzen
        :param abstand: abstand auf den es gesetzt wird
        :return:
        """
        # Nur wenn der Abstand numerisch ist, weitermachen
        if isinstance(abstand, int) or isinstance(abstand, float):
            if abstand >= 0:
                self.entf_rotPoint = abstand
        else:
            raise TypeError

    def isInArea(self, width, height, depth):
        """
        ob ein planet im sichtfeld ist
        :param width:
        :param height:
        :param depth:
        :return:
        """
        if self.position[0] + self.radius > width / -2 and self.position[0] + self.radius < width / 2:
            if self.position[1] + self.radius > height / -2 and self.position[1] + self.radius < height / 2:
                if self.position[2] + self.radius > -depth and self.position[2] + self.radius < depth:
                    return True
        else:
            return False