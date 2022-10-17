from bill_info import Bill
from flatmates_info import FlatMates

your_name = input("Your name : ")
your_stay_duration = int(input("Stay duration : "))
flatmate_name = input("Flatmate name  : ")
flatmate_stay_duration = int(input("Flatmate stay duration : "))
total_rent_amount = int(input("Total Amount of Payment  :"))   
stay_period = input("Stay Month Period  : ")



class PDFReport:
    """making a pdf file for flatemates rent report
    """
    def __init__(self, filename):
        self.filename = filename
        

    def generate(self, flatmate1, flatemate2, bill, flatmate1_paid, flatmate2_paid) :
        self.flatmate1 = flatmate1
        self.flatemate2 = flatemate2
        self.bill = bill
        self.flatmate1_paid = flatmate1_paid
        self.flatmate2_paid = flatmate2_paid
        from fpdf import FPDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_xy(0,0)
        pdf.set_font('arial', 'B',13.0)
        pdf.multi_cell(h=5.0, align='L', w=0, \
            txt=f"BIll Sharing Report for Tenants \n  your name : {your_name} \n  Your stay duration: {your_stay_duration}  \n flatmate_name :{flatmate_name} \n  flatmate stay duration : {flatmate_stay_duration} \n  flatmate_name :{flatmate_name} \n  flatmate stay duration : {flatmate_stay_duration} \n total_rent_amount : {total_rent_amount}  \n stay period : {stay_period} \n stay period : {stay_period} \n Rent paid by you :  {flatmate1_paid} \n Rent paid by flatmate2 : {flatmate2_paid}." , border=0)
         
        
        file_name = self.filename
        pdf.output(file_name, 'F')      
                     