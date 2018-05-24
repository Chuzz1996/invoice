from extractInformation import *
def main():
    url = "http://34.209.24.195/facturas"
    id = "4e25ce61-e6e2-457a-89f7-116404990967"
    startDay = "2017-01-01"
    finishDay = "2017-12-31"
    informationInvoice = extractInformation(url)
    numberInvoice = informationInvoice.getNumOfInvoice(id,startDay,finishDay)
    print("Calculate :",str(numberInvoice),"invoice from",startDay,"to",finishDay,"in",str(informationInvoice.getNumOfCalls()),"calls")


if __name__=="__main__":
    main()
