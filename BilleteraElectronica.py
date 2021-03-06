#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Authors:	Edwar Yepez		Carnet: 12-10855
# 			Edgar Silva		Carnet: 11-10968
# 

from datetime import *
import datetime
import time

# Recarga
# Este objeto representa la estructura que guarda los datos de
# una recarga
class Recarga(object):
	# Se define el constructor de Recarga, donde se inicializan
	# todos sus atributos
	def __init__(self, monto, fecha):
		self.id = id(self)
		self.monto = monto
		self.fecha = fecha

# Debito
# Este objeto representa la estructura que guarda los datos de
# un consumo
class Debito(object):
	# Se define el constructor de Debito, donde se inicializan
	# todos sus atributos
	def __init__(self, monto, idLocal, fecha):
		self.id = id(self)
		self.monto = monto
		self.fecha = fecha
		self.idLocal = idLocal

# Billetera Electronica
# Esta objeto permite llevar un registro de saldo para una
# persona, asi como el historial de transacciones de debito
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

	# Metodo que devuelve el saldo actual de la billetera
	def obtenerSaldo():
		return self.saldo

	# Metodo que permite procesar un consumo en la billetera 
	# electronica, se guarda en el historial de registros y
	# se actualiza el saldo
	def consumir(self, monto, idLocal, pin, fecha = time.strftime("%c")):
		try:
			assert(self.pin == pin)
			if monto <= self.saldo:
				self.ListaDebitos.append( Debito(monto, idLocal, fecha) )
				self.saldo -= monto
				print("Se ha realizado el consumo exitosamente.")
			else:
				print("Su saldo es insuficiente para realizar el consumo. Recargue saldo y vuelva a intentar.")
		except:
			print("Ha ingresado un pin invalido.")
	

	# Metodo que permite procesar una recarga en la billetera 
	# electronica, se guarda en el historial de registros y
	# se actualiza el saldo
	def recargar(self, monto, fecha = time.strftime("%c")):
		self.ListaRecargas.append( Recarga(monto, fecha) )
		self.saldo += monto
		print("Su recarga se ha completado exitosamente")