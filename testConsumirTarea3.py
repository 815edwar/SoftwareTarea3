import unittest
from datetime import *
import datetime
import time
from Tarea3 import *
import sys

class ConsumirTester(unittest.TestCase):
    
    def setUp(self):
        self.wallet = BilleteraElectronica("D","D",1,4321,5000)
        
    # Extremos
    
    def testMaxConsumo(self):
        self.wallet.saldo = sys.float_info.max
        self.wallet.pin = sys.maxint
        id_local = sys.maxint
        self.wallet.consumir(sys.float_info.max, sys.maxint, sys.maxint, datetime.date.max)
        self.assertEquals(self.wallet.saldo, 0, "METODO consumir: Inconsistencia en el consumo.")
        self.assertEquals(id_local, self.wallet.ListaDebitos[0].idLocal, "METODO consumir: Inconsistencia en el id del local.")
        self.assertGreater(self.wallet.ListaDebitos[0].fecha, datetime.date(9999,12,30), "METODO consumir: Inconsistencia en la fecha.")
    
    def testMinConsumo(self):
        self.wallet.saldo = sys.float_info.min
        self.wallet.pin = 1
        id_local = 1
        self.wallet.consumir(sys.float_info.min, 1, 1, datetime.date.min)
        self.assertEquals(self.wallet.saldo, 0, "METODO consumir: Inconsistencia en el consumo.")
        self.assertEquals(id_local, self.wallet.ListaDebitos[0].idLocal, "METODO consumir: Inconsistencia en el id del local.")
        self.assertGreater(datetime.date(1, 1, 2), self.wallet.ListaDebitos[0].fecha, "METODO consumir: Inconsistencia en la fecha.")
        
    # Esquinas
    
    def testCornerCOne(self): #consumir(MAX, min, min, min)
        self.wallet.saldo = sys.float_info.max
        self.wallet.pin = 1
        id_local = 1
        self.wallet.consumir(sys.float_info.max, 1, 1, datetime.date.min)
        self.assertEquals(self.wallet.saldo, 0, "METODO consumir: Inconsistencia en el consumo.")
        self.assertEquals(id_local, self.wallet.ListaDebitos[0].idLocal, "METODO consumir: Inconsistencia en el id del local.")
        self.assertGreater(datetime.date(1, 1, 2), self.wallet.ListaDebitos[0].fecha, "METODO consumir: Inconsistencia en la fecha.")
        
    def testCornerCTwo(self): #consumir(min, MAX, min, min)
        self.wallet.saldo = sys.float_info.min
        self.wallet.pin = 1
        id_local = sys.maxint
        self.wallet.consumir(sys.float_info.min, sys.maxint, 1, datetime.date.min)
        self.assertEquals(self.wallet.saldo, 0, "METODO consumir: Inconsistencia en el consumo.")
        self.assertEquals(id_local, self.wallet.ListaDebitos[0].idLocal, "METODO consumir: Inconsistencia en el id del local.")
        self.assertGreater(datetime.date(1, 1, 2), self.wallet.ListaDebitos[0].fecha, "METODO consumir: Inconsistencia en la fecha.")
        
    def testCornerCThree(self): #consumir(min, min, MAX, min)
        self.wallet.saldo = sys.float_info.min
        self.wallet.pin = sys.maxint
        id_local = 1
        self.wallet.consumir(sys.float_info.min, 1, sys.maxint, datetime.date.min)
        self.assertEquals(self.wallet.saldo, 0, "METODO consumir: Inconsistencia en el consumo.")
        self.assertEquals(id_local, self.wallet.ListaDebitos[0].idLocal, "METODO consumir: Inconsistencia en el id del local.")
        self.assertGreater(datetime.date(1, 1, 2), self.wallet.ListaDebitos[0].fecha, "METODO consumir: Inconsistencia en la fecha.")
        
    def testCornerCFour(self): #consumir(min, min, min, MAX)
        self.wallet.saldo = sys.float_info.min
        self.wallet.pin = 1
        id_local = 1
        self.wallet.consumir(sys.float_info.min, 1, 1, datetime.date.max)
        self.assertEquals(self.wallet.saldo, 0, "METODO consumir: Inconsistencia en el consumo.")
        self.assertEquals(id_local, self.wallet.ListaDebitos[0].idLocal, "METODO consumir: Inconsistencia en el id del local.")
        self.assertGreater(self.wallet.ListaDebitos[0].fecha, datetime.date(9999,12,30), "METODO consumir: Inconsistencia en la fecha.")
        
    def testCornerCFive(self): #consumir(MAX, MAX, min, min)
        self.wallet.saldo = sys.float_info.max
        self.wallet.pin = 1
        id_local = sys.maxint
        self.wallet.consumir(sys.float_info.max, sys.maxint, 1, datetime.date.min)
        self.assertEquals(self.wallet.saldo, 0, "METODO consumir: Inconsistencia en el consumo.")
        self.assertEquals(id_local, self.wallet.ListaDebitos[0].idLocal, "METODO consumir: Inconsistencia en el id del local.")
        self.assertGreater(datetime.date(1, 1, 2), self.wallet.ListaDebitos[0].fecha, "METODO consumir: Inconsistencia en la fecha.")
        
    def testCornerCSix(self): #consumir(min, MAX, MAX, min)
        self.wallet.saldo = sys.float_info.min
        self.wallet.pin = sys.maxint
        id_local = sys.maxint
        self.wallet.consumir(sys.float_info.min, sys.maxint, sys.maxint, datetime.date.min)
        self.assertEquals(self.wallet.saldo, 0, "METODO consumir: Inconsistencia en el consumo.")
        self.assertEquals(id_local, self.wallet.ListaDebitos[0].idLocal, "METODO consumir: Inconsistencia en el id del local.")
        self.assertGreater(datetime.date(1, 1, 2), self.wallet.ListaDebitos[0].fecha, "METODO consumir: Inconsistencia en la fecha.")
        
    def testCornerCSeven(self): #consumir(min, min, MAX, MAX)
        self.wallet.saldo = sys.float_info.min
        self.wallet.pin = sys.maxint
        id_local = 1
        self.wallet.consumir(sys.float_info.min, 1, sys.maxint, datetime.date.max)
        self.assertEquals(self.wallet.saldo, 0, "METODO consumir: Inconsistencia en el consumo.")
        self.assertEquals(id_local, self.wallet.ListaDebitos[0].idLocal, "METODO consumir: Inconsistencia en el id del local.")
        self.assertGreater(self.wallet.ListaDebitos[0].fecha, datetime.date(9999,12,30), "METODO consumir: Inconsistencia en la fecha.")
        
    def testCornerCEight(self): #consumir(MAX, min, MAX, min)
        self.wallet.saldo = sys.float_info.max
        self.wallet.pin = sys.maxint
        id_local = 1
        self.wallet.consumir(sys.float_info.max, 1, sys.maxint, datetime.date.min)
        self.assertEquals(self.wallet.saldo, 0, "METODO consumir: Inconsistencia en el consumo.")
        self.assertEquals(id_local, self.wallet.ListaDebitos[0].idLocal, "METODO consumir: Inconsistencia en el id del local.")
        self.assertGreater(datetime.date(1, 1, 2), self.wallet.ListaDebitos[0].fecha, "METODO consumir: Inconsistencia en la fecha.")
        
    def testCornerCNine(self): #consumir(MAX, min, min, MAX)
        self.wallet.saldo = sys.float_info.max
        self.wallet.pin = 1
        id_local = 1
        self.wallet.consumir(sys.float_info.max, 1, 1, datetime.date.max)
        self.assertEquals(self.wallet.saldo, 0, "METODO consumir: Inconsistencia en el consumo.")
        self.assertEquals(id_local, self.wallet.ListaDebitos[0].idLocal, "METODO consumir: Inconsistencia en el id del local.")
        self.assertGreater(self.wallet.ListaDebitos[0].fecha, datetime.date(9999,12,30), "METODO consumir: Inconsistencia en la fecha.")
        
    def testCornerCTen(self): #consumir(min, MAX, min, MAX)
        self.wallet.saldo = sys.float_info.min
        self.wallet.pin = 1
        id_local = sys.maxint
        self.wallet.consumir(sys.float_info.min, sys.maxint, 1, datetime.date.max)
        self.assertEquals(self.wallet.saldo, 0, "METODO consumir: Inconsistencia en el consumo.")
        self.assertEquals(id_local, self.wallet.ListaDebitos[0].idLocal, "METODO consumir: Inconsistencia en el id del local.")
        self.assertGreater(self.wallet.ListaDebitos[0].fecha, datetime.date(9999,12,30), "METODO consumir: Inconsistencia en la fecha.")
        
    def testCornerCEleven(self): #consumir(MAX, MAX, MAX, min)
        self.wallet.saldo = sys.float_info.max
        self.wallet.pin = sys.maxint
        id_local = sys.maxint
        self.wallet.consumir(sys.float_info.max, sys.maxint, sys.maxint, datetime.date.min)
        self.assertEquals(self.wallet.saldo, 0, "METODO consumir: Inconsistencia en el consumo.")
        self.assertEquals(id_local, self.wallet.ListaDebitos[0].idLocal, "METODO consumir: Inconsistencia en el id del local.")
        self.assertGreater(datetime.date(1, 1, 2), self.wallet.ListaDebitos[0].fecha, "METODO consumir: Inconsistencia en la fecha.")
        
    def testCornerCTwelve(self): #consumir(MAX, min, MAX, MAX)
        self.wallet.saldo = sys.float_info.max
        self.wallet.pin = sys.maxint
        id_local = 1
        self.wallet.consumir(sys.float_info.max, 1, sys.maxint, datetime.date.max)
        self.assertEquals(self.wallet.saldo, 0, "METODO consumir: Inconsistencia en el consumo.")
        self.assertEquals(id_local, self.wallet.ListaDebitos[0].idLocal, "METODO consumir: Inconsistencia en el id del local.")
        self.assertGreater(self.wallet.ListaDebitos[0].fecha, datetime.date(9999,12,30), "METODO consumir: Inconsistencia en la fecha.")
        
    def testCornerCThirteen(self): #consumir(MAX, MAX, min, MAX)
        self.wallet.saldo = sys.float_info.max
        self.wallet.pin = 1
        id_local = sys.maxint
        self.wallet.consumir(sys.float_info.max, sys.maxint, 1, datetime.date.max)
        self.assertEquals(self.wallet.saldo, 0, "METODO consumir: Inconsistencia en el consumo.")
        self.assertEquals(id_local, self.wallet.ListaDebitos[0].idLocal, "METODO consumir: Inconsistencia en el id del local.")
        self.assertGreater(self.wallet.ListaDebitos[0].fecha, datetime.date(9999,12,30), "METODO consumir: Inconsistencia en la fecha.")
        
    def testCornerCFourteen(self): #consumir(min, MAX, MAX, MAX)
        self.wallet.saldo = sys.float_info.min
        self.wallet.pin = sys.maxint
        id_local = sys.maxint
        self.wallet.consumir(sys.float_info.min, sys.maxint, sys.maxint, datetime.date.max)
        self.assertEquals(self.wallet.saldo, 0, "METODO consumir: Inconsistencia en el consumo.")
        self.assertEquals(id_local, self.wallet.ListaDebitos[0].idLocal, "METODO consumir: Inconsistencia en el id del local.")
        self.assertGreater(self.wallet.ListaDebitos[0].fecha, datetime.date(9999,12,30), "METODO consumir: Inconsistencia en la fecha.")
