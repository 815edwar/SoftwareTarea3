import unittest
from datetime import *
import datetime
import time
from Tarea3 import *
import sys

class SaldoTester(unittest.TestCase):
    
    def setUp(self):
        self.wallet = BilleteraElectronica("C","C",1,4321,5000)
        
    # Extremos y esquinas
    
    def testMaxSaldo(self):
        self.wallet.saldo = sys.float_info.max
        self.assertEquals(self.wallet.obtenerSaldo(), sys.float_info.max, "METODO obtenerSaldo: Inconsistencia en el saldo.")
        
    def testMinSaldo(self):
        self.wallet.saldo = sys.float_info.min
        self.assertEquals(self.wallet.obtenerSaldo(), sys.float_info.min, "METODO obtenerSaldo: Inconsistencia en el saldo.")
        
    # Malicia
    
    def testSaldoMal1(self):
        self.assertEquals(self.wallet.obtenerSaldo(), 5000, "METODO obtenerSaldo: Inconsistencia en el saldo.")
        
    def testSaldoMal2(self):
        self.wallet.saldo = 5000 - sys.float_info.min
        self.assertEqual(self.wallet.obtenerSaldo(), 5000, "METODO obtenerSaldo: Inconsistencia en el saldo.")
        
    def testSaldoMal3(self):
        self.wallet.saldo = sys.float_info.max - sys.float_info.min
        self.assertEqual(self.wallet.obtenerSaldo(), sys.float_info.max, "METODO obtenerSaldo: Inconsistencia en el saldo.")
        
    