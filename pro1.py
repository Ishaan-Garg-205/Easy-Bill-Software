from tkinter import*
import math, random, os
from tkinter import messagebox

class Bill_app:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1260x630+0+0")
        self.root.title("Easy Bill Software") 
        bg_color = '#074463'
        title =Label(self.root,text = "Easy Bill Software",bd=12,
                                 relief= GROOVE,bg=bg_color,fg="White",
                                 font=("algerian",30,"bold"),pady = 2).pack(fill=X)
        
        #.................Variables to be used.........................

        #.............Tricycles..............
        self.Winie=IntVar()
        self.Jupiter=IntVar()
        self.Dora=IntVar()
        self.Crazy=IntVar()
        self.Goldy=IntVar()
        self.Sunny=IntVar()

        #..............Chairs.................
        self.Elano=IntVar()
        self.Italia=IntVar()
        self.Rock=IntVar()
        self.Lumina=IntVar()
        self.Marble=IntVar()
        self.Fevina=IntVar()

        #...............Shoe Rack...............
        self.PC_3_Shelf=IntVar()
        self.PC_4_Shelf=IntVar()
        self.PC_5_Shelf=IntVar()
        self.PC_6_Shelf=IntVar()
        self.JC_4_Shelf=IntVar()
        self.JC_5_Shelf=IntVar()


        #................Total Product price & Tax Variables........
        self.tricycle_price=StringVar()
        self.chair_price=StringVar()
        self.shoe_rack_price=StringVar()

        self.tricycle_tax=StringVar()
        self.chair_tax=StringVar()
        self.shoe_rack_tax=StringVar()

        #.................Customer Variables.................
        self.c_name=StringVar()
        self.c_phone=StringVar()
        
        self.bill_no=StringVar()
        x=random.randint(1,10)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()



#         #=================== customer details=============================
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("curlz mt",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl = Label(F1,text="Customer Name",bg = bg_color, fg= "white",font=("kristen itc",14,"bold")).grid(row=0,column=0,padx=10,pady=5)
        cname_txt = Entry(F1,width =13,textvariable=self.c_name,font= "arial 15",bd=7, relief =SUNKEN).grid(row=0,column =1, padx=20,pady=5)

        cphn_lbl = Label(F1,text="Phone No.",bg = bg_color, fg= "white",font=("kristen itc",14,"bold")).grid(row=0,column=2,padx=10,pady=5)
        cphn_txt = Entry(F1,width =13,textvariable=self.c_phone,font= "arial 15",bd=7, relief =SUNKEN).grid(row=0,column =3, padx=20,pady=5)

        cbill_lbl = Label(F1,text="Invoice No.",bg = bg_color, fg= "white",font=("kristen itc",14,"bold")).grid(row=0,column=4,padx=10,pady=5)
        cbill_txt = Entry(F1,width =13,textvariable=self.search_bill,font= "arial 15",bd=7, relief =SUNKEN).grid(row=0,column =5, padx=20,pady=5)

        bill_btn = Button(F1,text="Search",command = self.find_bill,width =10, bd =7, font="arial 12 bold").grid(row=0,column=6, padx=7,pady = 5)
        

        # ========================== Product Details=============================
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Tricycles",font=("curlz mt",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=170,width=280,height=380)

        Winie_lbl = Label(F2,text="Winie",font=("times new roman",16,"bold"),fg="light green",bg=bg_color).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        Winie_txt = Entry(F2,width=10,textvariable=self.Winie,font=("times new roman",16,"bold"),bd=5,relief = SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Jupiter_lbl = Label(F2,text="Jupiter",font=("times new roman",16,"bold"),fg="light green",bg=bg_color).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Jupiter_txt = Entry(F2,width=10,textvariable=self.Jupiter,font=("times new roman",16,"bold"),bd=5,relief = SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        Dora_lbl = Label(F2,text="Dora",font=("times new roman",16,"bold"),fg="light green",bg=bg_color).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Dora_txt = Entry(F2,width=10,textvariable=self.Dora,font=("times new roman",16,"bold"),bd=5,relief = SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        Crazy_lbl = Label(F2,text="Crazy",font=("times new roman",16,"bold"),fg="light green",bg=bg_color).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Crazy_txt = Entry(F2,width=10,textvariable=self.Crazy,font=("times new roman",16,"bold"),bd=5,relief = SUNKEN).grid(row=3,column=1,padx=10,pady=10)
        
        Goldy_lbl = Label(F2,text="Goldy",font=("times new roman",16,"bold"),fg="light green",bg=bg_color).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Goldy_txt = Entry(F2,width=10,textvariable=self.Goldy,font=("times new roman",16,"bold"),bd=5,relief = SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        Sunny_lbl = Label(F2,text="Sunny",font=("times new roman",16,"bold"),fg="light green",bg=bg_color).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Sunny_txt = Entry(F2,width=10,textvariable=self.Sunny,font=("times new roman",16,"bold"),bd=5,relief = SUNKEN).grid(row=5,column=1,padx=10,pady=10)


        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Chairs",font=("curlz mt",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=300,y=170,width=270,height=380)

        Elano_lbl = Label(F3,text="Elano",font=("times new roman",16,"bold"),fg="light green",bg=bg_color).grid(row=0,column=0,padx=10,
        pady=10,sticky="w")
        Elano_txt = Entry(F3,width=10,textvariable=self.Elano,font=("times new roman",16,"bold"),bd=5,relief = SUNKEN).grid(row=0,
        column=1,padx=10,pady=10)

        Italia_lbl = Label(F3,text="Italia",font=("times new roman",16,"bold"),fg="light green",bg=bg_color).grid(row=1,column=0,padx=10,
        pady=10,sticky="w")
        Italia_txt = Entry(F3,width=10,textvariable=self.Italia,font=("times new roman",16,"bold"),bd=5,relief = SUNKEN).grid(row=1,
        column=1,padx=10,pady=10)

        Rock_lbl = Label(F3,text="Rock",font=("times new roman",16,"bold"),fg="light green",bg=bg_color).grid(row=2,column=0,
        padx=10,pady=10,sticky="w")
        Rock_txt = Entry(F3,width=10,textvariable=self.Rock,font=("times new roman",16,"bold"),bd=5,relief = SUNKEN).grid(row=2,
        column=1,padx=10,pady=10)

        Lumina_lbl = Label(F3,text="Lumina",font=("times new roman",16,"bold"),fg="light green",bg=bg_color).grid(row=3,column=0,
        padx=10,pady=10,sticky="w")
        Lumina_txt = Entry(F3,width=10,textvariable=self.Lumina,font=("times new roman",16,"bold"),bd=5,relief = SUNKEN).grid(row=3,
        column=1,padx=10,pady=10)
        
        Marble_lbl = Label(F3,text="Marble",font=("times new roman",16,"bold"),fg="light green",bg=bg_color).grid(row=4,
        column=0,padx=10,pady=10,sticky="w")
        Marble_txt = Entry(F3,width=10,textvariable=self.Marble,font=("times new roman",16,"bold"),bd=5,relief = SUNKEN).grid(row=4,
        column=1,padx=10,pady=10)

        Fevina_lbl = Label(F3,text="Fevina",font=("times new roman",16,"bold"),fg="light green",bg=bg_color).grid(row=5,column=0,
        padx=10,pady=10,sticky="w")
        Fevina_txt = Entry(F3,width=10,textvariable=self.Fevina,font=("times new roman",16,"bold"),bd=5,
        relief = SUNKEN).grid(row=5,column=1,padx=10,pady=10)


        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Shoe Rack",font=("curlz mt",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=590,y=170,width=300,height=380)

        PC3_lbl = Label(F4,text="PC-3 shelf",font=("times new roman",16,"bold"),fg="light green",bg=bg_color).grid(row=0,
        column=0,padx=10,pady=10,sticky="w")
        PC3_txt = Entry(F4,width=10,textvariable=self.PC_3_Shelf,font=("times new roman",16,"bold"),bd=5,
        relief = SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        PC4_lbl = Label(F4,text="PC-4 Shelf",font=("times new roman",16,"bold"),fg="light green",bg=bg_color).grid(row=1,
        column=0,padx=10,pady=10,sticky="w")
        PC4_txt = Entry(F4,width=10,textvariable=self.PC_4_Shelf,font=("times new roman",16,"bold"),bd=5,
        relief = SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        PC5_lbl = Label(F4,text="PC-5 Shelf",font=("times new roman",16,"bold"),fg="light green",bg=bg_color).grid(row=2,
        column=0,padx=10,pady=10,sticky="w")
        PC5_txt = Entry(F4,width=10,textvariable=self.PC_5_Shelf,font=("times new roman",16,"bold"),
        bd=5,relief = SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        PC6_lbl = Label(F4,text="PC-6 Shelf",font=("times new roman",16,"bold"),fg="light green",bg=bg_color).grid(row=3,
        column=0,padx=10,pady=10,sticky="w")
        PC6_txt = Entry(F4,width=10,textvariable=self.PC_6_Shelf,font=("times new roman",16,"bold"),bd=5,
        relief = SUNKEN).grid(row=3,column=1,padx=10,pady=10)
        
        JC4_lbl = Label(F4,text="JC-4 Shelf",font=("times new roman",16,"bold"),fg="light green",bg=bg_color).grid(row=4,
        column=0,padx=10,pady=10,sticky="w")
        JC4_txt = Entry(F4,width=10,textvariable=self.JC_4_Shelf,font=("times new roman",16,"bold"),bd=5,
        relief = SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        JC5_lbl = Label(F4,text="JC-5 Shelf",font=("times new roman",16,"bold"),fg="light green",bg=bg_color).grid(row=5,
        column=0,padx=10,pady=10,sticky="w")
        JC5_txt = Entry(F4,width=10,textvariable=self.JC_5_Shelf,font=("times new roman",16,"bold"),bd=5,
        relief = SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        # ===================== Billing Frame ===============================
        F5 = Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=910,y=170,width=350,height=380)
        bill_title= Label(F5,text="Bill Area",font="algerian 15 bold",bd=7,relief=GROOVE).pack(fill=X)

        # =================== scroll bar ============================
        scrol_y = Scrollbar(F5,orient=VERTICAL)
        self.txtarea = Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #===================== Button frame ============================

        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("curlz mt",15,"bold"),fg="gold",bg=bg_color)
        F6.place (x=0,y=560,relwidth=1, height=140)
        m1_lbl=Label(F6,text="Total Tricycle Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,
        pady=1,sticky="w")
        m1_txt=Entry(F6,width=10,font="arial 10 bold",bd=7,textvariable=self.tricycle_price,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl=Label(F6,text="Total Chair Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,
        pady=1,sticky="w")
        m2_txt=Entry(F6,width=10,font="arial 10 bold",textvariable=self.chair_price,bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3_lbl=Label(F6,text="Total Shoe Rack Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2, column=0,
        padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=10,font="arial 10 bold",textvariable=self.shoe_rack_price,bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        c1_lbl=Label(F6,text="Tricycle Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0, column=2,padx=20,
        pady=1,sticky="w")
        c1_txt=Entry(F6,width=10,font="arial 10 bold",bd=7,textvariable=self.tricycle_tax,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        c2_lbl=Label(F6,text="Chair Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1, column=2,padx=20,pady=1,
        sticky="w")
        c2_txt=Entry(F6,width=10,font="arial 10 bold",bd=7,textvariable=self.chair_tax,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        c3_lbl=Label(F6,text="Shoe Rack Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2, column=2,padx=20,
        pady=1,sticky="w")
        c3_txt=Entry(F6,width=10,font="arial 10 bold",bd=7,textvariable=self.shoe_rack_tax,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=640,width=570,height=95)

        total_btn=Button(btn_F,text="Total",command=self.total, bg="cadetblue",fg="white",bd=2,pady=15,width=9,font="arial 14 bold").grid(row=0,
        column=0,padx=5,pady=5)
        GnBill_btn=Button(btn_F,text="Generate Bill",command=self.bill_area, bg="cadetblue",fg="white",bd=2,pady=15,width=11,font="arial 14 bold").grid(row=0,column=1,padx=5,pady=5)
        Clear_btn=Button(btn_F,text="Clear",bg="cadetblue",command = self.clear_data, fg="white",bd=2,pady=15,width=10,
         font="arial 14 bold").grid(row=0,column=2,padx=5,pady=5)
        Exit_btn=Button(btn_F,text="Exit",bg="cadetblue",command = self.exit_app,fg="white",bd=2,pady=15,width=9,
          font="arial 14 bold").grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()

#===================== Classes ===============================
    def total(self):   
        self.twn = self.Winie.get()*1140
        self.jpt = self.Jupiter.get()*920
        self.dor = self.Dora.get()*860
        self.crz = self.Crazy.get()*880
        self.gld = self.Goldy.get()*740
        self.sny = self.Sunny.get()*1280

        self.total_tricycle_price=float(
                                            self.twn + self.jpt +self.dor +self.crz +self.gld +self.sny     
                                            )
        self.tricycle_price.set("Rs. "+str(self.total_tricycle_price))
        self.trcltax = round((self.total_tricycle_price*0.12),2)
        self.tricycle_tax.set("Rs. "+str(self.trcltax)) 


        self.eln = self.Elano.get()*380
        self.itl = self.Italia.get()*380
        self.rck = self.Rock.get()*260
        self.lmn = self.Lumina.get()*540
        self.mrb = self.Marble.get()*245
        self.fvn = self.Fevina.get()*350
                                                           
        self.total_chair_price=float(
                                        self.eln+ self.itl+ self.rck + self.lmn+ self.mrb+ self.fvn  
                                         ) 

        self.chair_price.set("Rs. "+str(self.total_chair_price))   
        self.chrtax = round((self.total_chair_price*0.18),2)   
        self.chair_tax.set("Rs. "+str(self.chrtax))                        


        self.pc3 = self.PC_3_Shelf.get()*560
        self.pc4 = self.PC_4_Shelf.get()*660
        self.pc5 = self.PC_5_Shelf.get()*750
        self.pc6 = self.PC_6_Shelf.get()*860
        self.jc4 = self.JC_4_Shelf.get()*580
        self.jc5 = self.JC_5_Shelf.get()*680
        self.total_shoe_rack_price=float(
                                        self.pc3+self.pc4+self.pc5+self.pc6+self.jc4+self.jc5    
                                                )

        self.shoe_rack_price.set("Rs. "+str(self.total_shoe_rack_price))
        self.srtax= round((self.total_shoe_rack_price*0.09),2)
        self.shoe_rack_tax.set("Rs. "+str(self.srtax))  


        self.Total_bill= float(self.total_tricycle_price + self.total_chair_price + self.total_shoe_rack_price)
        self.Total_tax = float(self.trcltax + self.chrtax + self.srtax)
        self.Total_amt = float(self.Total_bill + self.Total_tax)


# ==================== Bill Area ===============================
    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t   Garg Enterprises")
        self.txtarea.insert(END,f"\n Bill Number : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name : {self.c_name.get()} ")
        self.txtarea.insert(END,f"\n Phone Number : {self.c_phone.get()}")
        self.txtarea.insert(END,f"\n=====================================") 
        self.txtarea.insert(END,f"\n Products\t\tQnty.\t\tPrice")                
        self.txtarea.insert(END,f"\n=====================================")   


# ======= IF Customer Details or Product Details are empty ====================
    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error","Custumer Details cannot be empty")
        elif self.tricycle_price.get()== "Rs. 0.0" and self.chair_price.get()== "Rs. 0.0" and self.shoe_rack_price.get() == "Rs. 0.0":
            messagebox.showerror("Error","Please Select Any product")
        else:
            self.welcome_bill()

        #=================== Tricycles  ===================
            if self.Winie.get()!=0:
                    self.txtarea.insert(END,f"\n Winie \t\t{self.Winie.get()}\t\t{self.twn}")
            if self.Jupiter.get()!=0:
                    self.txtarea.insert(END,f"\n Jupiter\t\t{self.Jupiter.get()}\t\t{self.jpt}")
            if self.Dora.get()!=0:
                    self.txtarea.insert(END,f"\n Dora\t\t{self.Dora.get()}\t\t{self.dor}")
            if self.Crazy.get()!=0:
                    self.txtarea.insert(END,f"\n Crazy\t\t{self.Crazy.get()}\t\t{self.crz}")  
            if self.Goldy.get()!=0:
                    self.txtarea.insert(END,f"\n Goldy\t\t{self.Goldy.get()}\t\t{self.gld}") 
            if self.Sunny.get()!=0:
                    self.txtarea.insert(END,f"\n Sunnyl\t\t{self.Sunny.get()}\t\t{self.sny}") 
                
        #=================  Chairs  =======================
            if self.Elano.get()!=0:                                                                                                                                                                                                
                    self.txtarea.insert(END,f"\n Elano\t\t{self.Elano.get()}\t\t{self.eln}")
            if self.Italia.get()!=0: 
                    self.txtarea.insert(END,f"\n Italia\t\t{self.Italia.get()}\t\t{self.itl}")
            if self.Rock.get()!=0: 
                    self.txtarea.insert(END,f"\n Rock\t\t{self.Rock.get()}\t\t{self.rck}")
            if self.Lumina.get()!=0:
                    self.txtarea.insert(END,f"\n Lumina\t\t{self.Lumina.get()}\t\t{self.lmn}")  
            if self.Marble.get()!=0:
                    self.txtarea.insert(END,f"\n Marble\t\t{self.Marble.get()}\t\t{self.mrb}") 
            if self.Fevina.get()!=0:
                    self.txtarea.insert(END,f"\n Fevina\t\t{self.Fevina.get()}\t\t{self.fvn}")   

        #=================Shoe Rack =========================
            if self.PC_3_Shelf.get()!=0:                                                                                                                                                                                                
                    self.txtarea.insert(END,f"\n PC_3_Shelf\t\t{self.PC_3_Shelf.get()}\t\t{self.pc3}")
            if self.PC_4_Shelf.get()!=0: 
                    self.txtarea.insert(END,f"\n PC_4_Shelf\t\t{self.PC_4_Shelf.get()}\t\t{self.pc4}")
            if self.PC_5_Shelf.get()!=0: 
                    self.txtarea.insert(END,f"\n PC_5_Shelf\t\t{self.PC_5_Shelf.get()}\t\t{self.pc5}")
            if self.PC_6_Shelf.get()!=0:
                    self.txtarea.insert(END,f"\n PC_6_Shelf\t\t{self.PC_6_Shelf.get()}\t\t{self.pc6}")  
            if self.JC_4_Shelf.get()!=0:
                    self.txtarea.insert(END,f"\n JC_4_Shelf\t\t{self.JC_4_Shelf.get()}\t\t{self.jc4}") 
            if self.JC_5_Shelf.get()!=0:
                    self.txtarea.insert(END,f"\n JC_5_Shelf\t\t{self.JC_5_Shelf.get()}\t\t{self.jc5}") 
                                
        # =============== inserting taxes and bill amount in bill area =========================                                                           
            self.txtarea.insert(END,f"\n------------------------------------") 
            if self.tricycle_tax.get()!="Rs. 0.0":
                    self.txtarea.insert(END,f"\n Tricycle Tax\t\t\t{self.tricycle_tax.get()}") 
            if self.chair_tax.get()!="Rs. 0.0":
                    self.txtarea.insert(END,f"\n Chair Tax\t\t\t{self.chair_tax.get()}") 
            if self.shoe_rack_tax.get()!="Rs. 0.0":
                    self.txtarea.insert(END,f"\n Shoe Rack Tax\t\t\t{self.shoe_rack_tax.get()}")
            self.txtarea.insert(END,f"\n------------------------------------- ")  

            self.txtarea.insert(END,f"\n Bill Value:\t\t\tRs. {self.Total_bill}") 
            self.txtarea.insert(END,f"\n Total Tax Value:\t\t\tRs. {self.Total_tax}")   
            self.txtarea.insert(END,f"\n Total Amount:\t\t\tRs. {self.Total_amt}")           
            self.txtarea.insert(END,f"\n------------------------------------- ")  
            self.save_bill()


#==================== To save the bill for future use ====================
    def save_bill(self):
        op = messagebox.askyesno("Save Bill","Do you want to save the bill?")
        if op>0:
            self.bill_data = self.txtarea.get('1.0',END)         
            f1 = open("bills/" + str(self.bill_no.get())+ ".txt","w")
            f1.write(self.bill_data)      
            f1.close()    
            messagebox.showinfo("Saved",f"Bill No. {self.bill_no.get()} saved successfully")
        else:
            return       

# ==================== to search already existing bill =================================
    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present = "yes"

        if present == "no":
                messagebox.showerror("Error","Invalid Bill No.")

# ====================== To clear the data on the screen ======================
    def clear_data(self):
        op = messagebox.askyesno("Clear","Do you really want to clear the data?")
        if op>0:
                
                self.Winie.set(0)
                self.Jupiter.set(0)
                self.Dora.set(0)
                self.Crazy.set(0)
                self.Goldy.set(0)
                self.Sunny.set(0)

                #..............Chairs.................
                self.Elano.set(0)
                self.Italia.set(0)
                self.Rock.set(0)
                self.Lumina.set(0)
                self.Marble.set(0)
                self.Fevina.set(0)

                #...............Shoe Rack...............
                self.PC_3_Shelf.set(0)
                self.PC_4_Shelf.set(0)
                self.PC_5_Shelf.set(0)
                self.PC_6_Shelf.set(0)
                self.JC_4_Shelf.set(0)
                self.JC_5_Shelf.set(0)


                #................Total Product price & Tax Variables........
                self.tricycle_price.set("")
                self.chair_price.set("")
                self.shoe_rack_price.set("")

                self.tricycle_tax.set("")
                self.chair_tax.set("")
                self.shoe_rack_tax.set("")

                #.................Customer Variables.................
                self.c_name.set("")
                self.c_phone.set("")
                
                self.bill_no.set("")
                x=random.randint(1,10)
                self.bill_no.set(str(x))
                self.search_bill.set("")

                self.welcome_bill()

# =========================== to perform exit button function =====================
    def exit_app(self):
        op = messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.root.destroy()
        
                
root =Tk()
obj = Bill_app(root)
root.mainloop()