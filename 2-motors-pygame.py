#!/usr/bin/env python

# CamJam EduKit 3 - Robotics

import RPi.GPIO as GPIO # Import the GPIO Library
import time # Import the Time library
import pygame, sys
import pygame.event as GAME_EVENTS
import os

# ------------- Constantes -----------------

# GPIO pins pour les moteurs
pinMotorAAvance = 9 # moteur de droite
pinMotorARecule = 10  # moteur de droite
pinMotorBAvance = 7  # moteur de gauche
pinMotorBRecule = 8  # moteur de gauche

# ------------- Fonctions -----------------

def robot_init():
	# Set the GPIO modes
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)

	# Set the GPIO Pin mode
	GPIO.setup(pinMotorAAvance, GPIO.OUT)
	GPIO.setup(pinMotorARecule, GPIO.OUT)
	GPIO.setup(pinMotorBAvance, GPIO.OUT)
	GPIO.setup(pinMotorBRecule, GPIO.OUT)

	# Configure pygame (la session SSH doit etre ouverte avec -X pour le display)
	#os.environ['SDL_VIDEODRIVER'] = 'dummy'
	pygame.init()
	pygame.display.set_mode((300,200))


def robot_exit():
	# Terminate pygame
	pygame.quit()

	# Reset the GPIO pins (turns off motors too)
	GPIO.cleanup()

	# System exit
	sys.exit()


def robot_stop():
	GPIO.output(pinMotorAAvance, 0)
	GPIO.output(pinMotorARecule, 0)
	GPIO.output(pinMotorBAvance, 0)
	GPIO.output(pinMotorBRecule, 0)

def robot_avance():
	GPIO.output(pinMotorAAvance, 1)
	GPIO.output(pinMotorARecule, 0)
	GPIO.output(pinMotorBAvance, 1)
	GPIO.output(pinMotorBRecule, 0)

def robot_recule():
	GPIO.output(pinMotorAAvance, 0)
	GPIO.output(pinMotorARecule, 1)
	GPIO.output(pinMotorBAvance, 0)
	GPIO.output(pinMotorBRecule, 1)

def robot_tourne_gauche():
	GPIO.output(pinMotorAAvance, 0)
	GPIO.output(pinMotorARecule, 0)
	GPIO.output(pinMotorBAvance, 1)
	GPIO.output(pinMotorBRecule, 0)

def robot_tourne_droite():
	GPIO.output(pinMotorAAvance, 1)
	GPIO.output(pinMotorARecule, 0)
	GPIO.output(pinMotorBAvance, 0)
	GPIO.output(pinMotorBRecule, 0)

def robot_pivote_gauche():
	GPIO.output(pinMotorAAvance, 0)
	GPIO.output(pinMotorARecule, 1)
	GPIO.output(pinMotorBAvance, 1)
	GPIO.output(pinMotorBRecule, 0)

def robot_pivote_droite():
	GPIO.output(pinMotorAAvance, 1)
	GPIO.output(pinMotorARecule, 0)
	GPIO.output(pinMotorBAvance, 0)
	GPIO.output(pinMotorBRecule, 1)

# ------------- Programme Principal -----------------

robot_init()
robot_stop()

running = True
while running:
	for event in GAME_EVENTS.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_v:
				print 'pivote a gauche'
				robot_pivote_gauche()
			if event.key == pygame.K_b:
				print 'pivote a droite'
				robot_pivote_droite()
			if event.key == pygame.K_LEFT:
				print 'tourne a gauche'
				robot_tourne_gauche()
			if event.key == pygame.K_RIGHT:
				print 'tourne a droite'
				robot_tourne_droite()
			if event.key == pygame.K_UP:
				print 'avance'
				robot_avance()
			if event.key == pygame.K_DOWN:
				print 'recule'
				robot_recule()
			if event.key == pygame.K_SPACE:
				print 'stop'
				robot_stop()
			if event.key == pygame.K_ESCAPE:
				print 'quit'
				running = False

robot_exit()

