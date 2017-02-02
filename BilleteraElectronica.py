#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Authors:	Edwar Yepez		Carnet: 12-10855
# 			Edgar Silva		Carnet: 11-10968
# 

from datetime import *
import datetime
import time


class Recarga(object):
	def __init__(self, monto, fecha):
		self.id = id(self)
		self.monto = monto
		self.fecha = fecha

# Billetera Electronica
# Esta objeto permite llevar un registro de saldo para una
# persona, asi como el hisotorial de transacciones de debito
# y credito correspondientes a dicha persona
class BilleteraElectronica(object):
	
	# Se define el constructor del objeto, donde se inicializan
	# todos sus atributos
	def __init__(self, Nombre, Apellido, ci, pin):
		self.id = id(self)
		self.nombre = Nombre
		self.apellido = Apellido
		self.cedula = ci
		self.pin = pin
		self.ListaRecargas = []

	def recargar(self, monto, fecha = time.strftime("%c")):
		self.ListaRecargas.append( Recarga(monto, fecha) )
		print("Su recarga se ha completado exitosamente")