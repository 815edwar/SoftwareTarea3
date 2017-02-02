import unittest
from datetime import *
import datetime
import time
from Tarea3 import *
import sys

class EstructuraDebitoTester(unittest.TestCase):
    
    def setUp(self):
        self.wallet = BilleteraElectronica("A","A",1,1234,0)
    
    # Extremos
    
    def testMaxDebito(self):
        self.wallet.saldo = sys.float_info.max
        fecha = datetime.time.max.strftime("%c")
        id_local = sys.maxint
        self.debito = Debito(sys.float_info.max, sys.maxint, fecha)
        self.assertEquals(self.wallet.saldo, self.debito.monto)
        self.assertEquals(id_local, self.debito.idLocal)
        
    def testMinDebito(self):
        self.wallet.saldo = sys.float_info.min
        fecha = datetime.time.min.strftime("%c")
        id_local = 1
        self.debito = Debito(sys.float_info.min, 1, fecha)
        self.assertEquals(self.wallet.saldo, self.debito.monto)
        self.assertEquals(id_local, self.debito.idLocal)
        
    # Esquinas
    
    def testCornerOne(self): # Debito(MAX, min, min)
        self.wallet.saldo = sys.float_info.max
        fecha = datetime.time.min.strftime("%c")
        id_local = 1
        self.debito = Debito(sys.float_info.max, 1, fecha)
        self.assertEquals(self.wallet.saldo, self.debito.monto)
        self.assertEquals(id_local, self.debito.idLocal)
    
    def testCornerTwo(self): # Debito(MAX, MAX, min)
        self.wallet.saldo = sys.float_info.max
        fecha = datetime.time.min.strftime("%c")
        id_local = sys.maxint
        self.debito = Debito(sys.float_info.max, sys.maxint, fecha)
        self.assertEquals(self.wallet.saldo, self.debito.monto)
        self.assertEquals(id_local, self.debito.idLocal)
        
    def testCornerThree(self): # Debito(min, min, MAX)
        self.wallet.saldo = sys.float_info.min
        fecha = datetime.time.max.strftime("%c")
        id_local = 1
        self.debito = Debito(sys.float_info.min, 1, fecha)
        self.assertEquals(self.wallet.saldo, self.debito.monto)
        self.assertEquals(id_local, self.debito.idLocal)
        
    def testCornerFour(self): # Debito(min, MAX, MAX)
        self.wallet.saldo = sys.float_info.min
        fecha = datetime.time.max.strftime("%c")
        id_local = sys.maxint
        self.debito = Debito(sys.float_info.min, sys.maxint, fecha)
        self.assertEquals(self.wallet.saldo, self.debito.monto)
        self.assertEquals(id_local, self.debito.idLocal)
        
    def testCornerFive(self): # Debito(MAX, min, MAX)
        self.wallet.saldo = sys.float_info.max
        fecha = datetime.time.max.strftime("%c")
        id_local = 1
        self.debito = Debito(sys.float_info.max, 1, fecha)
        self.assertEquals(self.wallet.saldo, self.debito.monto)
        self.assertEquals(id_local, self.debito.idLocal)
        
    def testCornerSix(self): # Debito(min, MAX, min)
        self.wallet.saldo = sys.float_info.min
        fecha = datetime.time.min.strftime("%c")
        id_local = sys.maxint
        self.debito = Debito(sys.float_info.min, sys.maxint, fecha)
        self.assertEquals(self.wallet.saldo, self.debito.monto)
        self.assertEquals(id_local, self.debito.idLocal)

    #def tearDown(self):
    #    self.wallet.dispose()
    