#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Authors:	Edwar Yepez		Carnet: 12-10855
# 			Edgar Silva		Carnet: 
# 

from datetime import *
import datetime

# Billetera Electronica
# Esta objeto permite llevar un registro de saldo para una
# persona, asi como el hisotorial de transacciones de debito
# y credito correspondientes a dicha persona
class BilleteraElectronica(object):
	# Se define el constructor del objeto, donde se inicializan
	# todos sus atributos
	def __init__(self, Nombre, Apellido, ci, pin = 1234, saldo = 0):
		self.id = id(self)
		self.nombre = Nombre
		self.apellido = Apellido
		self.cedula = ci
		self.pin = pin
		self.ListaRecargas = []
		self.saldo = saldo

	def obtenerSaldo():
		return self.saldo
