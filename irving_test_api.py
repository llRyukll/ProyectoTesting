import unittest
from unittest.mock import Mock 
from Summoner import *
from SqlCRUD import *
from AbstractClassDeveloper import Invocador, AbstractLOL, AbstractSummoner
class TestLolapp(unittest.TestCase):
    def setUp(self): 
        self.player = AppInvocador() 
        self.crud = SqlCRUD() 
        self.invmock = Mock(Id= 402492, Name= 'jarasdeboy', Level= 120, Wins= 173, Losses= 192, Tier= 'PLATINUM', Comportamiento= None)
        self.inv1 = Invocador(self.invmock.Id, self.invmock.Name, self.invmock.Level, self.invmock.Wins, self.invmock.Losses, self.invmock.Tier, self.invmock.Comportamiento)
        self.com1 = Comportamiento('jarasdeboy', 'comportamiento')
#verifica que la funcion DatosSummoner regrese los valores correctos de un invocador
    def test_Summoner(self):
        print("======================SummonerTest======================")
        invocador1 = self.player.DatosSummoner('jarasdeboy')

        self.assertEqual(invocador1.Id, self.inv1.Id)
        self.assertEqual(invocador1.Name, self.inv1.Name)
        self.assertEqual(invocador1.Level, self.inv1.Level)
        self.assertEqual(invocador1.Wins, self.inv1.Wins)
        self.assertEqual(invocador1.Losses, self.inv1.Losses)
        self.assertEqual(invocador1.Tier, self.inv1.Tier)
        self.assertEqual(invocador1.Comportamiento, self.inv1.Comportamiento)

    def test_CrearInvocador(self):
        print("======================CrearInvocadorTest======================")
        self.assertIsInstance(self.crud.CrearInvocador(self.inv1), Invocador)

    def test_BorrarInvocador(self):
        print("======================BorrarInvocadorTest======================")
        self.assertTrue(self.crud.BorrarInvocador('jarasdeboy'))

    def test_ModificarInvocador(self):
    	print("======================ModificarInvocadorTest======================")
    	self.assertTrue(self.crud.ModificarInvocador(self.com1))

    def test_Conexion(self):
        print("======================ConexionTest======================")
        self.assertTrue(self.crud.Close())

if __name__ == '__main__':
	unittest.main()
