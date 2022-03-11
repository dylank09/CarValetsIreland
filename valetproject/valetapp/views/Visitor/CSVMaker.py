from valetapp.views.Visitor.exportToCSV import exportToCSV_Adapter
import csv


class CSVMaker:
    def __init__(self) -> None:
        pass

    def get_emails(self):
        return exportToCSV_Adapter().get_customer_emails()

    def get_money(self):
        return exportToCSV_Adapter().get_total_money()

    def get_money_in_store(self):
        return exportToCSV_Adapter().get_money_by_each_store()

    def get_all_stores(self):
        return exportToCSV_Adapter().get_stores()

    def get_all_valets(self):
        return exportToCSV_Adapter().get_valets()

    def get_all_staff(self):
        return exportToCSV_Adapter().get_staff()

    def get_all_membershipTypes(self):
        return exportToCSV_Adapter().get_membership_types()

    def create_CSV(self):
        header = ['emails', 'money', 'money_in_store',
                  'all_stores', 'all_valets', 'all_staff', 'all_membershipTypes']
        data = [CSVMaker().get_emails(), CSVMaker().get_money(), CSVMaker().get_money_in_store(), CSVMaker(
        ).get_all_stores(), CSVMaker().get_all_valets(), CSVMaker().get_all_staff(), CSVMaker().get_all_membershipTypes()]

        with open('storedata.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)

            writer.writerow(header)

            # write the data
            writer.writerow(data)
