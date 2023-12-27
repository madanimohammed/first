from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from tkcalendar import DateEntry

class  Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management system")
        self.root.geometry("1540x800+0+0")

        bg_color = "lightblue"
        frame_color = "white"

        self.PatientName=StringVar()
        self.PatientID=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()
        self.disease=StringVar()
        self.Medicine=StringVar()
        self.NameTablet=StringVar()
        self.Dose=StringVar()
        self.NoOftablets=StringVar()
        self.DailyDose=StringVar()
        self.Storage=StringVar()
        self.ExpDate=StringVar()
        self.Sideffect=StringVar()
        self.BloodPressure=StringVar()
        self.Lot=StringVar()
        self.ref=StringVar()
        self.issuedate=StringVar()
        self.Furtherinfo=StringVar()

        lbltitle = Label(self.root, bd=20, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM ", fg="black", bg=bg_color,
                         font=("Courier", 50, "bold"))
        lbltitle.pack(side=TOP, fill=X)

  #   =======================================Data frame =========================================

        Dataframe = Frame(self.root, bd=20, relief=RIDGE, bg=frame_color)
        Dataframe.place(x=0, y=130, width=1530, height=400)

        DataframeLeft=LabelFrame(Dataframe,bd=10,padx=20,relief=RIDGE, font=("Verdana",12,"bold"),text="patient information",)
        DataframeLeft.place(x=0,y=5,width=980,height=350)

        DataframeRight = LabelFrame(Dataframe, bd=10, padx=20, relief=RIDGE, font=("Verdana", 12, "bold"), text="prescription",bg=frame_color)
        DataframeRight.place(x=990, y=5, width=460, height=350)

    #   ============================================Button frame =========================================
        Buttonframe = Frame(self.root, bd=20, relief=RIDGE, bg=bg_color)
        Buttonframe.place(x=0, y=530, width=1530, height=70)
    #  =================================================Deatil frame =======================================

        Detailframe = Frame(self.root, bd=20, relief=RIDGE, bg=frame_color)
        Detailframe.place(x=0, y=600, width=1530, height=190)
    #    =============================================Data frame left =======================================

        lblPatientName = Label(DataframeLeft, font=("Verdana", 12, "bold"), text="Patient Name:-", padx=2, pady=6)
        lblPatientName.grid(row=0, column=0, sticky=W)
        txtref = Entry(DataframeLeft, font=("Verdana", 12),textvariable=self.PatientName, width=30)
        txtref.grid(row=0, column=1)

        lblPatientID = Label(DataframeLeft, font=("Verdana", 12, "bold"), text="Patient ID:-", padx=2, pady=6)
        lblPatientID.grid(row=1, column=0, sticky=W)
        txtref = Entry(DataframeLeft, font=("Verdana", 12),textvariable=self.PatientID, width=30)
        txtref.grid(row=1, column=1)

        lblDateOfBirth = Label(DataframeLeft, font=("Verdana", 12, "bold"), text="Date of Birth:-", padx=2, pady=6)
        lblDateOfBirth.grid(row=2, column=0, sticky=W)
        cal = DateEntry(DataframeLeft, font=("Verdana", 12), textvariable=self.DateOfBirth, width=30)
        cal.grid(row=2, column=1)

        lblPatientAddress = Label(DataframeLeft, font=("Verdana", 12, "bold"), text="Patient Address:-", padx=2, pady=6)
        lblPatientAddress.grid(row=3, column=0, sticky=W)
        txtref = Entry(DataframeLeft, font=("Verdana", 12),textvariable=self.PatientAddress, width=30)
        txtref.grid(row=3, column=1)

        lbldisease = Label(DataframeLeft, font=("Verdana", 12, "bold"), text="Disease:-", padx=2, pady=6)
        lbldisease.grid(row=4, column=0, sticky=W)
        txtref = Entry(DataframeLeft, font=("Verdana", 12),textvariable=self.disease, width=30)
        txtref.grid(row=4, column=1)

        lblMedicine = Label(DataframeLeft, font=("Verdana", 12, "bold"), text="Medicine:-", padx=2, pady=6)
        lblMedicine.grid(row=5, column=0, sticky=W)
        txtref = Entry(DataframeLeft, font=("Verdana", 12),textvariable=self.Medicine, width=30)
        txtref.grid(row=5, column=1)

        lblNameTablet = Label(DataframeLeft, text="Name of the Tablet", font=("Verdana", 12, "bold"), padx=2, pady=6)
        lblNameTablet.grid(row=6, column=0)
        comNametablet=ttk.Combobox(DataframeLeft,font=("Verdana",12),textvariable=self.NameTablet,width=30)
        comNametablet["values"]=("Eletripn","Disprin","Omeprazole","Nice","corona vacacine","Naproxen","Aspirin","Azithromycin")
        comNametablet.grid(row=6,column=1)

        lblDose = Label(DataframeLeft, font=("Verdana", 12, "bold"), text="Dose:-", padx=2,pady=4)
        lblDose.grid(row=7, column=0, sticky=W)
        txtref = Entry(DataframeLeft, font=("Verdana", 12),textvariable=self.Dose, width=30)
        txtref.grid(row=7, column=1)

        lblNoOftablets = Label(DataframeLeft, font=("Verdana", 12, "bold"), text="No of Tblets:-", padx=2, pady=6)
        lblNoOftablets.grid(row=8, column=0, sticky=W)
        txtref = Entry(DataframeLeft, font=("Verdana", 12),textvariable=self.NoOftablets, width=30)
        txtref.grid(row=8, column=1)

        lblDailyDose = Label(DataframeLeft, font=("Verdana", 12, "bold"), text="Daily Dose:-", padx=2, pady=4)
        lblDailyDose.grid(row=0, column=2, sticky=W)
        txtref = Entry(DataframeLeft, font=("Verdana", 12),textvariable=self.DailyDose, width=25)
        txtref.grid(row=0, column=3)

        lblStorage = Label(DataframeLeft, font=("Verdana", 12, "bold"), text="Storage Advice:-", padx=2, pady=6)
        lblStorage.grid(row=1, column=2, sticky=W)
        txtref = Entry(DataframeLeft, font=("Verdana", 12),textvariable=self.Storage, width=25)
        txtref.grid(row=1, column=3)

        lblExpDate = Label(DataframeLeft, font=("Verdana", 12, "bold"), textvariable=self.ExpDate, text="Exp date",  padx=2, pady=6)
        lblExpDate.grid(row=2, column=2, sticky=W)
        txtref = Entry(DataframeLeft, font=("Verdana", 12), width=25)
        txtref.grid(row=2, column=3)

        lblSideffect = Label(DataframeLeft, font=("Verdana", 12, "bold"), text="Side effect:-", padx=2, pady=6)
        lblSideffect.grid(row=3, column=2, sticky=W)
        txtref = Entry(DataframeLeft, font=("Verdana", 12),textvariable=self.Sideffect, width=25)
        txtref.grid(row=3, column=3)

        lblBloodPressure = Label(DataframeLeft, font=("Verdana", 12, "bold"), text="BloodPressure:-", padx=2,pady=6)
        lblBloodPressure.grid(row=4, column=2, sticky=W)
        txtref = Entry(DataframeLeft, font=("Verdana", 12),textvariable=self.BloodPressure, width=25)
        txtref.grid(row=4, column=3)

        lblLot = Label(DataframeLeft, font=("Verdana", 12, "bold"), text="Lot:-", padx=2, pady=6)
        lblLot.grid(row=5, column=2, sticky=W)
        txtref = Entry(DataframeLeft, font=("Verdana", 12),textvariable=self.Lot, width=25)
        txtref.grid(row=5, column=3)

        lblref=Label(DataframeLeft,font=("Verdana",12,"bold"),text="Refence NO:-",padx=2)
        lblref.grid(row=6,column=2,sticky=W)
        txtref=Entry(DataframeLeft,font=("Verdana",12),textvariable=self.ref,width=25)
        txtref.grid(row=6,column=3)

        lblissuedate = Label(DataframeLeft, font=("Verdana", 12, "bold"), text="Issue date:-", padx=2, pady=6)
        lblissuedate.grid(row=7, column=2, sticky=W)
        cal = DateEntry(DataframeLeft, font=("Verdana", 12), textvariable=self.issuedate, width=25)
        cal.grid(row=7, column=3)

        lblFurtherinfo = Label(DataframeLeft, font=("Verdana", 12, "bold"), text="Further info:-", padx=2)
        lblFurtherinfo.grid(row=8, column=2, sticky=W)
        txtref = Entry(DataframeLeft, font=("Verdana", 12),textvariable=self.Furtherinfo, width=25)
        txtref.grid(row=8, column=3)

    #  =========================================Data frame right==================================
        self.textPrescription=Text(DataframeRight,font=("Verdana", 12),width=35,height=16,padx=2,pady=6)
        self.textPrescription.grid(row=0,column=0)

    #  =========================Buttons==================================
        btnprescription = Button(Buttonframe, command=self.iPrescriptionData, text="prescription", bg=bg_color,
                                 fg="black", font=("Verdana", 12, "bold"), width=23, height=1, padx=2, pady=6)
        btnprescription.grid(row=0, column=0)

        btnprescriptionData = Button(Buttonframe, text="prescription Data", bg=bg_color, fg="black", font=("Verdana", 12, "bold"),width=23, height=1, padx=2, pady=6,command=self.iPrescriptionData)
        btnprescriptionData.grid(row=0, column=1)

        btnupdaate = Button(Buttonframe, command=self.update, text="Update", bg=bg_color, fg="black", font=("Verdana", 12, "bold"), width=23, height=1, padx=2, pady=6)
        btnupdaate.grid(row=0, column=2)

        btnDelete = Button(Buttonframe, command=self.idelete, text="Delete", bg=bg_color, fg="black",font=("Verdana", 12, "bold"), width=23, height=1, padx=2, pady=6)
        btnDelete.grid(row=0, column=3)

        btnclear = Button(Buttonframe, command=self.clear, text="Clear", bg=bg_color, fg="black",font=("Verdana", 12, "bold"), width=23, height=1, padx=2, pady=6)
        btnclear.grid(row=0, column=4)

        btnexit = Button(Buttonframe, command=self.iExit, text="Exit", bg=bg_color, fg="black",font=("Verdana", 12, "bold"), width=14, height=1, padx=2, pady=6)
        btnexit.grid(row=0, column=5)


    #  ==========================scroll bar==================================
        scroll_x = ttk.Scrollbar(Detailframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailframe, orient=VERTICAL)

        self.hospital_table = ttk.Treeview(
            Detailframe,
            columns=(
            "PatientName", "PatientID", "DateofBirth", "Patientaddress", "disease", "medicine", "nameoftablet", "dose",
            "Nooftablets", "dailydose", "stroge", "exDate", "sideefect", "bloodpressure", "lot", "refence", "issuedate",
            "furtherinformation"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.hospital_table.pack(fill=BOTH, expand=1)

        scroll_x.configure(command=self.hospital_table.xview)
        scroll_y.configure(command=self.hospital_table.yview)

        self.hospital_table.heading("PatientName", text="PatientName")
        self.hospital_table.heading("PatientID", text="Patient ID")
        self.hospital_table.heading("DateofBirth", text="Date of Birth")
        self.hospital_table.heading("Patientaddress", text="Patient Address")
        self.hospital_table.heading("disease", text="Disease")
        self.hospital_table.heading("medicine", text="Medicine")
        self.hospital_table.heading("nameoftablet", text="Name of tablet")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("Nooftablets", text="No of Tablets")
        self.hospital_table.heading("dailydose", text="Daily dose")
        self.hospital_table.heading("stroge", text="Storage")
        self.hospital_table.heading("exDate", text="Ex Date")
        self.hospital_table.heading("sideefect", text="Side effect")
        self.hospital_table.heading("bloodpressure", text="Blood Pressure")
        self.hospital_table.heading("lot", text="Lot")
        self.hospital_table.heading("refence", text="Refrance")
        self.hospital_table.heading("issuedate", text="Issue Date")
        self.hospital_table.heading("furtherinformation", text="Further information")

        self.hospital_table["show"] = "headings"

        self.hospital_table.column("PatientName", width=100)
        self.hospital_table.column("PatientID", width=100)
        self.hospital_table.column("DateofBirth", width=100)
        self.hospital_table.column("Patientaddress", width=100)
        self.hospital_table.column("disease", width=100)
        self.hospital_table.column("medicine", width=100)
        self.hospital_table.column("nameoftablet", width=100)
        self.hospital_table.column("dose", width=100)
        self.hospital_table.column("Nooftablets", width=100)
        self.hospital_table.column("dailydose", width=100)
        self.hospital_table.column("stroge", width=100)
        self.hospital_table.column("exDate", width=100)
        self.hospital_table.column("sideefect", width=100)
        self.hospital_table.column("bloodpressure", width=100)
        self.hospital_table.column("lot", width=100)
        self.hospital_table.column("refence", width=100)
        self.hospital_table.column("issuedate", width=100)
        self.hospital_table.column("furtherinformation", width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>", self.get_cursar)
        self.fatch_data()

     #  =============================functionalety declartion=============================================

    def iPrescriptionData(self):
        if self.NameTablet.get() == "" or self.ref.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Madani@33149",
                                           database="mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                self.PatientName.get(),
                self.PatientID.get(),
                self.DateOfBirth.get(),
                self.PatientAddress.get(),
                self.disease.get(),
                self.Medicine.get(),
                self.NameTablet.get(),
                self.Dose.get(),
                self.NoOftablets.get(),
                self.DailyDose.get(),
                self.Storage.get(),
                self.ExpDate.get(),
                self.Sideffect.get(),
                self.BloodPressure.get(),
                self.Lot.get(),
                self.ref.get(),
                self.issuedate.get(),
                self.Furtherinfo.get()
            ))

            conn.commit()
            self.fatch_data()
            conn.close()
            messagebox.showinfo("success", "Record has been inserted")

            self.iPrescription()

    def update(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Madani@33149", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute(
            "update hospital set PatientName=%s, PatientID=%s, DateOfBirth=%s, PatientAddress=%s, disease=%s, Medicine=%s, NameTablet=%s, Dose=%s, NoOftablets=%s, DailyDose=%s, Storage=%s, ExpDate=%s, Sideffect=%s, BloodPressure=%s, Lot=%s, issuedate=%s, Furtherinfo=%s where ref=%s",
            (
                self.PatientName.get(),
                self.PatientID.get(),
                self.DateOfBirth.get(),
                self.PatientAddress.get(),
                self.disease.get(),
                self.Medicine.get(),
                self.NameTablet.get(),
                self.Dose.get(),
                self.NoOftablets.get(),
                self.DailyDose.get(),
                self.Storage.get(),
                self.ExpDate.get(),
                self.Sideffect.get(),
                self.BloodPressure.get(),
                self.Lot.get(),
                self.issuedate.get(),
                self.Furtherinfo.get(),
                self.ref.get()
            ))
        conn.commit()
        conn.close()
        self.fatch_data()
        messagebox.showinfo("Success", "Record has been updated")

    def fatch_data(self):
         conn = mysql.connector.connect(host="localhost", username="root", password="Madani@33149", database="mydata")
         my_cursor = conn.cursor()
         my_cursor.execute("select * from hospital")
         rows=my_cursor.fetchall()
         if len(rows)!=0:
             self.hospital_table.delete(*self.hospital_table.get_children())
             for i in rows:
                 self.hospital_table.insert("",END,values=i)
             conn.commit()
             conn.close()

    def get_cursar(self,event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        if row:
            self.PatientName.set(row[0])
            self.PatientID.set(row[1])
            self.DateOfBirth.set(row[2])
            self.PatientAddress.set(row[3])
            self.disease.set(row[4])
            self.Medicine.set(row[5])
            self.NameTablet.set(row[6])
            self.Dose.set(row[7])
            self.NoOftablets.set(row[8])
            self.DailyDose.set(row[9])
            self.Storage.set(row[10])
            self.ExpDate.set(row[11])
            self.Sideffect.set(row[12])
            self.BloodPressure.set(row[13])
            self.Lot.set(row[14])
            self.ref.set(row[15])
            self.issuedate.set(row[16])
            self.Furtherinfo.set(row[17])

    def iPrescription(self):
        self.textPrescription.delete(1.0, END)
        self.textPrescription.insert(END, "Patient Name:\t\t\t" + self.PatientName.get() + "\n")
        self.textPrescription.insert(END, "Patient ID:\t\t\t" + self.PatientID.get() + "\n")
        self.textPrescription.insert(END, "Date Of Birth:\t\t\t" + self.DateOfBirth.get() + "\n")
        self.textPrescription.insert(END, "Patient Address:\t\t\t" + self.PatientAddress.get() + "\n")
        self.textPrescription.insert(END, "Disease:\t\t\t" + self.disease.get() + "\n")
        self.textPrescription.insert(END, "Medicine:\t\t\t" + self.Medicine.get() + "\n")
        self.textPrescription.insert(END, "Name of Tablet:\t\t\t" + self.NameTablet.get() + "\n")
        self.textPrescription.insert(END, "Dose:\t\t\t" + self.Dose.get() + "\n")
        self.textPrescription.insert(END, "No of Tablets:\t\t\t" + self.NoOftablets.get() + "\n")
        self.textPrescription.insert(END, "Daily Dose:\t\t\t" + self.DailyDose.get() + "\n")
        self.textPrescription.insert(END, "Storage Advice:\t\t\t" + self.Storage.get() + "\n")
        self.textPrescription.insert(END, "Exp Date:\t\t\t" + self.ExpDate.get() + "\n")
        self.textPrescription.insert(END, "Side Effect:\t\t\t" + self.Sideffect.get() + "\n")
        self.textPrescription.insert(END, "Blood Pressure:\t\t\t" + self.BloodPressure.get() + "\n")
        self.textPrescription.insert(END, "Lot:\t\t\t" + self.Lot.get() + "\n")
        self.textPrescription.insert(END, "Reference No:\t\t\t" + self.ref.get() + "\n")
        self.textPrescription.insert(END, "Issue Date:\t\t\t" + self.issuedate.get() + "\n")
        self.textPrescription.insert(END, "Further Information:\t\t\t" + self.Furtherinfo.get() + "\n")

    def idelete(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Madani@33149", database="mydata")
        my_cursor = conn.cursor()
        query = "DELETE FROM hospital WHERE ref=%s"
        value = (self.ref.get(),)
        my_cursor.execute(query, value)

        conn.commit()
        conn.close()
        self.fatch_data()
        messagebox.showinfo("Delete", "Patient has been deleted successfully")

    def clear(self):
        self.PatientName.set("")
        self.PatientID.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("")
        self.disease.set("")
        self.Medicine.set("")
        self.NameTablet.set("")
        self.Dose.set("")
        self.NoOftablets.set("")
        self.DailyDose.set("")
        self.Storage.set("")
        self.ExpDate.set("")
        self.Sideffect.set("")
        self.BloodPressure.set("")
        self.Lot.set("")
        self.ref.set("")
        self.issuedate.set("")
        self.Furtherinfo.set("")
        self.textPrescription.delete("1.0", END)

    def iExit(self):
        iExit=messagebox.askyesno("Hospital managemnt system","Confirm you want to exit")
        if iExit>0:
            root.destroy()
            return

root = Tk()
ob = Hospital(root)
root.mainloop()