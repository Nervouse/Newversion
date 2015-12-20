__author__ = 'Faiku Fitim, Janusz Gradonski'

from raum.Gestirn import Gestirn
from raum.Mond import Mond
from math import *

class Planet(Gestirn):
    def __init__(self, position, anim, rotation, rotSpeed, rotPoint, movSpeed, radius, textur, divisions, monde):
        """
        konstruktor der einen planeten anlegt
        :param position: position
        :param anim: animation
        :param rotation: raotaion
        :param rotSpeed: roataionsgeschwindiglit
        :param rotPoint: rotationsounkt
        :param movSpeed: bewwgungsgeschwindigkeit
        :param radius: radius groesse
        :param textur: tetxur des planeten
        :param divisions: unterteiungen
        :param monde: mond eines planete; kann nachtraeglich auch hinzuefugt werden
        :return:
        """
        self.position = position  # Position im XYZ-Raum
        self.anim = anim  # Animationen an/aus
        self.rotation = rotation  # Rotation um die eigene Achse
        self.rotSpeed = rotSpeed  # Rotationsgeschwindigkeit
        self.rotPoint = rotPoint  # Punkt, um den sich der Planet bewegen soll
        self.entf_rotPoint = abs(rotPoint[0] - position[0])  # Entfernung von ebendiesem Punkt
        self.movSpeed = movSpeed  # Orbitalgeschwindigkeit
        self.radius = radius  # Radius des Himmelskoerpers
        self.textur = textur  # Textur
        self.divisions = divisions  # Unterteilungen. Mehr = feinere, schoenere Kugel
        self.orbitalPos = 0  # Wie weit hat sich der Planet auf seiner Kreisbahn bereits bewegt?
        self.inialSpeeds = [rotSpeed, movSpeed]

        if isinstance(monde, list):
            self.monde = monde
        else:
            self.monde = []

    def getMondAt(self, index):
        """
        gibt dem mond am index zurueck
        :param index: vom mond
        :return: mon am angegeben index
        """
        if 0 <= index < len(self.monde):
            return self.monde[index]
        else:
            return None

    def update(self):
        """
        aktualisiert die animation des planeten
        :return:
        """
        if self.anim:
            Gestirn.update(self)

            self.orbitalPos += self.movSpeed * 0.2

            # Eigenes Update Verhalten hier erzeugen (Auf einer Kreisbahn bewegen)
            rads = self.orbitalPos*(180/3.14)

            self.position[0] = self.rotPoint[0] + cos(rads) * self.entf_rotPoint
            self.position[2] = self.rotPoint[2] + sin(rads) * self.entf_rotPoint

        for x in range(0, len(self.monde)):
            self.monde[x].update()

    def draw(self, top, zoom):
        """
        zeichnet den planeten
        :param top:
        :param zoom:
        :return:
        """
        Gestirn.draw(self, top, zoom)

        for x in range(0, len(self.monde)):
            self.monde[x].draw(top, zoom)

    def getMonde(self):
        """
        gibt alle monde zurueck
        :return: alle minde
        """
        return self.monde

    def addMond(self, m):
        """
        fuegt einen mond hinzu
        :param m: mond
        :return:
        """
        if isinstance(m, Mond):
            self.monde.append(m)

    def createMond(self, rotation, rotSpeed, entf_rotPoint, movSpeed, radius, textur, divisions):
        """
        bildet einen mond und fuegt ign hinzu
        :param rotation: roation
        :param rotSpeed: rotationsgeschw
        :param entf_rotPoint: roatations entfernung zum planeten
        :param movSpeed: bewegungsgeschw
        :param radius: radius
        :param textur: textur vom mond
        :param divisions: unterteilungen
        :return:
        """
        self.addMond(Mond(self.anim, rotation, rotSpeed, self, entf_rotPoint, movSpeed, radius, textur, divisions))

    def animateAllChildrenFaster(self, factor, factorMov):
        """
        animiert planeten schneller
        :param factor: geschwindigkeitsfaktor
        :param factorMov: bewegungsgeschwindigkeitfaktor
        :return:
        """
        self.rotSpeed += factor
        self.movSpeed += factorMov

        for i in range(0, len(self.monde)):
            self.monde[i].animateFaster(factor, factorMov)


    def animateAllChildrenSlower(self, factor, factorMov):
        """
        animiert planeten langsamer
        :param factor: geschwindigkeitsfaktor
        :param factorMov: bewegungsgeschwindigkeitfaktor
        :return:
        """
        if self.rotSpeed - factor > self.inialSpeeds[0]:
            self.rotSpeed -= factor
        else:
            self.rotSpeed = self.inialSpeeds[0]

        if self.movSpeed - factorMov > self.inialSpeeds[1]:
            self.movSpeed -= factorMov
        else:
            self.movSpeed = self.inialSpeeds[1]

        for i in range(0, len(self.monde)):
            self.monde[i].animateSlower(factor, factorMov)

    def setAnimation(self, anim):
        """
        animation hinzufuegen
        :param anim: animation die hinzugefuegt wird
        :return:
        """
        Gestirn.setAnimation(self, anim)

        for i in range(0, len(self.monde)):
            self.monde[i].setAnimation(anim)