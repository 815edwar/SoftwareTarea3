import unittest
from datetime import *
import datetime
import time
from Tarea3 import *
import sys

class RecargarTester(unittest.TestCase):
    
    def setUp(self):
        self.wallet = BilleteraElectronica("D","D",1,4321,5000)
        
    # Extremos
    
    def testMaxRecarga(self):
        self.wallet.saldo = 0
        self.wallet.recargar(sys.float_info.max, datetime.date.max)
        self.assertEquals(self.wallet.saldo, sys.float_info.max, "METODO consumir: Inconsistencia en el consumo.")
        self.assertGreater(self.wallet.ListaRecargas[0].fecha, datetime.date(9999,12,30), "METODO consumir: Inconsistencia en la fecha.")
    
    def testMinRecarga(self):
        self.wallet.recargar(sys.float_info.min, datetime.date.min)
        self.assertEquals(self.wallet.saldo, 5000, "METODO consumir: Inconsistencia en el consumo.")
        self.assertGreater(datetime.date(1, 1, 2), self.wallet.ListaRecargas[0].fecha, "METODO consumir: Inconsistencia en la fecha.")

    # Esquinas
    
    def testCornerReOne(self): #consumir(MAX, min)
        self.wallet.saldo = 0
        self.wallet.recargar(sys.float_info.max, datetime.date.min)
        self.assertEquals(self.wallet.saldo, sys.float_info.max, "METODO consumir: Inconsistencia en el consumo.")
        self.assertGreater(datetime.date(1, 1, 2), self.wallet.ListaRecargas[0].fecha, "METODO consumir: Inconsistencia en la fecha.")
        
    def testCornerReTwo(self): #consumir(min, MAX)
        self.wallet.recargar(sys.float_info.min, datetime.date.max)
        self.assertEquals(self.wallet.saldo, 5000, "METODO consumir: Inconsistencia en el consumo.")
        self.assertGreater(self.wallet.ListaRecargas[0].fecha, datetime.date(9999,12,30), "METODO consumir: Inconsistencia en la fecha.")