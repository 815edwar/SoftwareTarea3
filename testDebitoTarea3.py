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
        fecha = datetime.date.max
        id_local = sys.maxint
        self.debito = Debito(sys.float_info.max, sys.maxint, fecha)
        self.assertEquals(self.wallet.saldo, self.debito.monto, "ESTRUCTURA DEBITO: Inconsistencia en el monto.")
        self.assertEquals(id_local, self.debito.idLocal, "ESTRUCTURA DEBITO: Inconsistencia en el id del local.")
        self.assertGreater(self.debito.fecha, datetime.date(9999,12,30), "ESTRUCTURA DEBITO: Inconsistencia en la fecha.")
        
    def testMinDebito(self):
        self.wallet.saldo = sys.float_info.min
        fecha = datetime.date.min
        id_local = 1
        self.debito = Debito(sys.float_info.min, 1, fecha)
        self.assertEquals(self.wallet.saldo, self.debito.monto, "ESTRUCTURA DEBITO: Inconsistencia en el monto.")
        self.assertEquals(id_local, self.debito.idLocal, "ESTRUCTURA DEBITO: Inconsistencia en el id del local.")
        self.assertGreater(datetime.date(1, 1, 2), self.debito.fecha, "ESTRUCTURA DEBITO: Inconsistencia en la fecha.")
        
    # Esquinas
    
    def testCornerOne(self): # Debito(MAX, min, min)
        self.wallet.saldo = sys.float_info.max
        fecha = datetime.date.min
        id_local = 1
        self.debito = Debito(sys.float_info.max, 1, fecha)
        self.assertEquals(self.wallet.saldo, self.debito.monto, "ESTRUCTURA DEBITO: Inconsistencia en el monto.")
        self.assertEquals(id_local, self.debito.idLocal, "ESTRUCTURA DEBITO: Inconsistencia en el id del local.")
        self.assertGreater(datetime.date(1, 1, 2), self.debito.fecha, "ESTRUCTURA DEBITO: Inconsistencia en la fecha.")
    
    def testCornerTwo(self): # Debito(MAX, MAX, min)
        self.wallet.saldo = sys.float_info.max
        fecha = datetime.date.min
        id_local = sys.maxint
        self.debito = Debito(sys.float_info.max, sys.maxint, fecha)
        self.assertEquals(self.wallet.saldo, self.debito.monto, "ESTRUCTURA DEBITO: Inconsistencia en el monto.")
        self.assertEquals(id_local, self.debito.idLocal, "ESTRUCTURA DEBITO: Inconsistencia en el id del local.")
        self.assertGreater(datetime.date(1, 1, 2), self.debito.fecha, "ESTRUCTURA DEBITO: Inconsistencia en la fecha.")
        
    def testCornerThree(self): # Debito(min, min, MAX)
        self.wallet.saldo = sys.float_info.min
        fecha = datetime.date.max
        id_local = 1
        self.debito = Debito(sys.float_info.min, 1, fecha)
        self.assertEquals(self.wallet.saldo, self.debito.monto, "ESTRUCTURA DEBITO: Inconsistencia en el monto.")
        self.assertEquals(id_local, self.debito.idLocal, "ESTRUCTURA DEBITO: Inconsistencia en el id del local.")
        self.assertGreater(self.debito.fecha, datetime.date(9999,12,30), "ESTRUCTURA DEBITO: Inconsistencia en la fecha.")
        
    def testCornerFour(self): # Debito(min, MAX, MAX)
        self.wallet.saldo = sys.float_info.min
        fecha = datetime.date.max
        id_local = sys.maxint
        self.debito = Debito(sys.float_info.min, sys.maxint, fecha)
        self.assertEquals(self.wallet.saldo, self.debito.monto, "ESTRUCTURA DEBITO: Inconsistencia en el monto.")
        self.assertEquals(id_local, self.debito.idLocal, "ESTRUCTURA DEBITO: Inconsistencia en el id del local.")
        self.assertGreater(self.debito.fecha, datetime.date(9999,12,30), "ESTRUCTURA DEBITO: Inconsistencia en la fecha.")
        
    def testCornerFive(self): # Debito(MAX, min, MAX)
        self.wallet.saldo = sys.float_info.max
        fecha = datetime.date.max
        id_local = 1
        self.debito = Debito(sys.float_info.max, 1, fecha)
        self.assertEquals(self.wallet.saldo, self.debito.monto, "ESTRUCTURA DEBITO: Inconsistencia en el monto.")
        self.assertEquals(id_local, self.debito.idLocal, "ESTRUCTURA DEBITO: Inconsistencia en el id del local.")
        self.assertGreater(self.debito.fecha, datetime.date(9999,12,30), "ESTRUCTURA DEBITO: Inconsistencia en la fecha.")
        
    def testCornerSix(self): # Debito(min, MAX, min)
        self.wallet.saldo = sys.float_info.min
        fecha = datetime.date.min
        id_local = sys.maxint
        self.debito = Debito(sys.float_info.min, sys.maxint, fecha)
        self.assertEquals(self.wallet.saldo, self.debito.monto, "ESTRUCTURA DEBITO: Inconsistencia en el monto.")
        self.assertEquals(id_local, self.debito.idLocal, "ESTRUCTURA DEBITO: Inconsistencia en el id del local.")
        self.assertGreater(datetime.date(1, 1, 2), self.debito.fecha, "ESTRUCTURA DEBITO: Inconsistencia en la fecha.")

    #def tearDown(self):
    #    self.wallet.dispose()
    