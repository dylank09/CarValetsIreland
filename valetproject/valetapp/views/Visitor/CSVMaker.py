from valetapp.views.Visitor.exportToCSV import exportToCSV_Adapter

class CSVMaker():

    def get_emails(self):
        print(exportToCSV_Adapter.get_customer_emails())
