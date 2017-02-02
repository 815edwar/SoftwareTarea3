import unittest
from datetime import *
import datetime
import time
from Tarea3 import *
import sys

class EstructuraCreditoTester(unittest.TestCase):
    
    def setUp(self):
        self.wallet = BilleteraElectronica("B","B",1,4321,0)
    
    # Extremos
    
    def testMaxCredito(self):
        self.wallet.saldo = sys.float_info.max
        fecha = datetime.date.max
        self.debito = Recarga(sys.float_info.max, fecha)
        self.assertEquals(self.wallet.saldo, self.debito.monto, "ESTRUCTURA CREDITO: Inconsistencia en el monto.")
        self.assertGreater(self.debito.fecha, datetime.date(9999,12,30), "ESTRUCTURA CREDITO: Inconsistencia en la fecha.")
        
    def testMinCredito(self):
        self.wallet.saldo = sys.float_info.min
        fecha = datetime.date.min
        self.debito = Recarga(sys.float_info.min, fecha)
        self.assertEquals(self.wallet.saldo, self.debito.monto, "ESTRUCTURA CREDITO: Inconsistencia en el monto.")
        self.assertGreater(datetime.date(1, 1, 2), self.debito.fecha, "ESTRUCTURA CREDITO: Inconsistencia en la fecha.")
        
    # Esquinas
    
    def testCornerROne(self): # Debito(MAX, min)
        self.wallet.saldo = sys.float_info.max
        fecha = datetime.date.min
        self.debito = Recarga(sys.float_info.max, fecha)
        self.assertEquals(self.wallet.saldo, self.debito.monto, "ESTRUCTURA CREDITO: Inconsistencia en el monto.")
        self.assertGreater(datetime.date(1, 1, 2), self.debito.fecha, "ESTRUCTURA CREDITO: Inconsistencia en la fecha.")
    
    def testCornerRTwo(self): # Debito(min, MAX)
        self.wallet.saldo = sys.float_info.min
        fecha = datetime.date.max
        self.debito = Recarga(sys.float_info.min, fecha)
        self.assertEquals(self.wallet.saldo, self.debito.monto, "ESTRUCTURA CREDITO: Inconsistencia en el monto.")
        self.assertGreater(self.debito.fecha, datetime.date(9999,12,30), "ESTRUCTURA CREDITO: Inconsistencia en la fecha.")
    
    #def tearDown(self):
    #    self.wallet.dispose()
    