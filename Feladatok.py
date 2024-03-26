#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Image


class Feladatok():

    def __init__(self):
        # tégla
        self.ev3 = EV3Brick()
        # motorok
        self.jm = Motor(Port.B)
        self.bm = Motor(Port.C)
        self.km = Motor(Port.A)
        # szenzorok
        self.cs = ColorSensor(Port.S3)
        self.ts = TouchSensor(Port.S1)
        self.gs = GyroSensor(Port.S2)
        self.us = UltrasonicSensor(Port.S4)
        #self.ir = InfraredSensor(Port.S4)

        # dupla motorkezelő
        self.robot = DriveBase(self.jm, self.bm, 55, 115)

        #időzítő, stopperóra
        self.ido=StopWatch()

    def csipog(self):
        self.ev3.speaker.beep()

    def scanner(self):
        #2.	A robotképernyőn szeretném ha megjelenne a függőleges vonalak a mintának megfelelően. (scanner)
        #szürke 69
        #fekete 10
        #asztalról le 0
        #félig azstalrol 46
        self.robot.drive(100,0)
        self.ido.reset()
        hol = 0
        while self.ido.time()<3500:
            if self.cs.reflection()<(69+10)/2:
                self.ev3.screen.draw_line(hol,0,hol, 127)
            hol +=1
            wait(3500/178)
        self.robot.stop(Stop.BRAKE)
        wait(10000)
    
    def elsoa(self):
        #nem látt feketét addig megy
        while self.cs.reflection()>(69+10)/2-20:
            self.robot.drive(100,0)
        self.robot.stop(Stop.BRAKE)
        #addig megy ami feketét lát
        while self.cs.reflection()<(69+10)/2-10:
            self.robot.drive(100,0)
        self.robot.stop(Stop.BRAKE)

    def elsoa2(self):
        vege= False
        fekete= False   
        self.robot.drive(100,0)
        while not vege:
            if self.cs.reflection()<(69+10)/2-20:
                fekete=True 
            if fekete and self.cs.reflection()>(69+10)/2-10:
                vege =True
        self.robot.stop(Stop.BRAKE)

    def hanyvonal(self, db, seb, hatar):
        for vonalakSzama in range (db):
            vege= False
            fekete= False   
            self.robot.drive(seb,0)
            while not vege:
                if self.cs.reflection()< hatar:
                    fekete=True 
                if fekete and self.cs.reflection()>hatar+10:
                    vege =True
            self.robot.stop(Stop.BRAKE)

    def elsob(self):
        hatar = (69+10)/2-20
        self.hanyvonal(5,100,hatar)

    def elsoc (self):
        hatar = (69+10)/2-20
        self.hanyvonal(5,-100,hatar)
        self.robot.stop(Stop.BRAKE)

    def elsod(self):
        hosszok = []
        self.robot.drive(100,0)
        for vonalakSzama in range(5):
            vege= False
            fekete= False   
            self.robot.drive(100,0)
            while not vege:
                if self.cs.reflection()<(69+10)/2-20 and not fekete:
                    fekete=True 
                    self.ido.reset()
                if fekete and self.cs.reflection()>(69+10)/2-10:
                    vege =True
                    hosz = self.ido.time()
                    hosszok.append(hosz)
            self.robot.stop(Stop.BRAKE)
            print(hosz)
        print(hosszok)

    def elsoe(self):
        vege= False
        fekete= False   
        self.robot.drive(100,0)
        hanyadik=0
        while not vege:
            if self.cs.reflection()<(69+10)/2-20:
                fekete=True 
                for i in range (0,hanyadik,1):
                    self.ev3.speaker.beep()
            if fekete and self.cs.reflection()>(69+10)/2-10:
                vege =True
                for i in range (0,hanyadik,1):
                    self.ev3.speaker.beep()
        self.robot.stop(Stop.BRAKE)