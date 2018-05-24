import unittest
from extractInformation import *

class extractInformationTest(unittest.TestCase):

    def setUp(self):
        self.url = "http://34.209.24.195/facturas"
        self.id = "4e25ce61-e6e2-457a-89f7-116404990967"
        self.startDay = "2017-01-01"
        self.finishDay = "2017-12-31"

    def test_responseOk(self):
        """
        Check if a URL has request to give
        """
        check = extractInformation(self.url)
        params = check.buildParams(self.id,self.startDay,self.finishDay)
        if None!=check.getResponse(params):
            self.assertTrue(True)
        else:
            self.asserTrue(False)

    def test_isNumeric(self):
        """
        Check if a chain is a number
        """
        check = extractInformation(self.url)
        if check.isNumeric("4564") and not check.isNumeric("deef"):
            self.assertTrue(True)
        else:
            self.assertTrue(False)

def main():
    unittest.main()
main()
