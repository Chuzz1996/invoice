import requests
from datetime import datetime,timedelta

class extractInformation:

    def __init__(self,url):
        """
        Create an object to extract invoice
        information
        Args:
            url: URL to extract the information
        """
        self.calls = 0
        self.url = url

    def getResponse(self,params):
        """
        Get a response from the Web Service
        Args:
            params: parameterss for consuming a web service.
        Return:
            A Response from the request
        """
        return requests.get(self.url,params = params).json()

    def diveDates(self,start,finish):
        """
        Calculate a middle day between two dates
        Args:
            start: The star day
            finish: The finish day
        Return:
            The middle date between two dates
        """
        start = datetime.strptime(start,"%Y-%m-%d")
        finish = datetime.strptime(finish,"%Y-%m-%d")
        return start+(finish-start)/2

    def removeHours(self,date):
        """
        Remove the Hours from a date
        Args:
            date: The day to check
        Return:
            A string from the date without hour
        """
        return str(date).split()[0]

    def getNumOfInvoice(self,id,start,finish):
        """
        Extract the number of invoices form a person
        between two dates.
        If dont know a number of invoice between
        this days, divide and calculate with two
        diferentes dates more shorter.
        Args:
            id: The id from a person to check
            start: The start day
            finish: The finish day
        Return:
            The number of Invoices from a person
        """
        self.calls += 1
        invoice = self.getResponse(self.buildParams(id,start,finish))
        if not self.isNumeric(invoice):
            middle = self.diveDates(start,finish)
            plusMiddle = middle + timedelta(days = 1)
            middle = self.removeHours(middle)
            plusMiddle = self.removeHours(plusMiddle)
            invoice = self.getNumOfInvoice(id,start,middle)+\
                   self.getNumOfInvoice(id,plusMiddle,finish)
        return invoice

    def countAndGetCallInvoice(self,id,start,finish):
        """
        Start and count of num of invoice call
        Args:
            id: The id from a person to check
            start: The start day
            finish: The finish day
        Return:
            The number of Invoices from a person
        """
        self.calls = 0
        return self.getNumOfInvoice(id,start,finish)
    
    def getNumOfCalls(self):
        """
        Return:
            The number of calls to Num Invoice
        """
        return self.calls
    
    def buildParams(self,id,start,finish):
        """
        Build the params for a conection
        Args:
            id: The id from a person to check
            start: The start day
            finish: The finish day
        Return:
            A tuple with the params
        """
        return (
            ("id",id),
            ("start",start),
            ("finish",finish)
        )

    def isNumeric(self,chain):
        """
        Check if some chain is or not a number
        Args:
            chain: The chain to check
        Return:
            Is or not a number
        """
        res = True
        try:
            int(chain)
        except:
            res = False
        return res
        
