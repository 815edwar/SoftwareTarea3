#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Authors:	Edwar Yepez		Carnet: 12-10855
# 			Edgar Silva		Carnet: 
# 

from datetime import *
import datetime
import time

class Debito(object):
	def __init__(self, monto, idLocal, fecha):
		self.id = id(self)
		self.monto = monto
		self.fecha = fecha
		self.idLocal = idLocal

# Billetera Electronica
# Esta objeto permite llevar un registro de saldo para una
# persona, asi como el hisotorial de transacciones de debito
# y credito correspondientes a dicha persona
class BilleteraElectronica(object):
	# Se define el constructor del objeto, donde se inicializan
	# todos sus atributos
	def __init__(self, Nombre, Apellido, ci, pin, saldo = 0):
		self.id = id(self)
		self.nombre = Nombre
		self.apellido = Apellido
		self.cedula = ci
		self.pin = pin
		self.ListaRecargas = []
		self.ListaDebitos = []
		self.saldo = saldo

	def consumir(self, monto, idLocal, pin, fecha = time.strftime("%c")):
		try:
			assert(self.pin == pin)
			if monto <= self.saldo:
				self.saldo -= monto
				self.ListaDebitos.append( Debito(monto, idLocal, fecha) )
				print("Se ha realizado el consumo exitosamente.")
			else:
				print("Su saldo es insuficiente para realizar el consumo. Recargue saldo y vuelva a intentar.")
		except:
			print("Ha ingresado un pin invalido.")
	
	# Metodo que devuelve el saldo actual de la billetera
	def obtenerSaldo():
		return self.saldo
