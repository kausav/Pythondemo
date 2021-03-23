from tkinter import *
import math,random,os
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("XYZ Software")
        bg_color="#00ffff" 
        title=Label(self.root,text="XYZ Software",bd=12,relief=GROOVE,bg=bg_color,font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        
        #======================variables=================================
        
        #===================Pills Varaibles============================
        self.medicine1 = IntVar()
        self.medicine2 = IntVar()
        self.medicine3 = IntVar()
        self.medicine4 = IntVar()
        self.medicine5 = IntVar()
        
        #===================Injections Varaibles============================
        self.medicine6 = IntVar()
        self.medicine7 = IntVar()
        self.medicine8 = IntVar()
        self.medicine9 = IntVar()
        self.medicine10 = IntVar()
        
        #===================Drinks Varaibles============================
        self.medicine11 = IntVar()
        self.medicine12 = IntVar()
        self.medicine13 = IntVar()
        self.medicine14 = IntVar()
        self.medicine15 = IntVar()
        
        #==================Total Product prices & taxes Varaibles============================
        self.pillsprice = StringVar()
        self.injectionsprice = StringVar()
        self.drinksprice = StringVar()
        
        self.pilltax = StringVar()
        self.injectiontax = StringVar()
        self.drinkstax = StringVar()
        
        #===================customer details Varaibles============================
        self.cusname = StringVar()
        self.cusphn = StringVar()
        self.cusbill = StringVar()
        x=random.randint(1000,9999)
        self.cusbill.set(str(x))
        self.searchbill = StringVar()
        
        #===========customer details=======================================
        F1=LabelFrame(self.root,text="Customer Details",bd=10,relief=GROOVE,bg=bg_color,font=("times new roman",15,"bold"),fg="gold")
        F1.place(x=0,y=80,relwidth=1)
        
    
        cname_lbl=Label(F1,text="Customer Name",bd=12,relief=GROOVE,bg=bg_color,font=("times new roman",18,"bold")).grid(row=0,column=0,pady=5,padx=20)
        cname_txt=Entry(F1,width=15,bd=7,relief=SUNKEN,textvariable=self.cusname,font=("times new roman",12,"bold")).grid(row=0,column=1,pady=5,padx=10)
        
        cphn_lbl=Label(F1,text="Phone No.",bd=12,relief=GROOVE,bg=bg_color,font=("times new roman",18,"bold")).grid(row=0,column=2,pady=5,padx=20)
        cphn_txt=Entry(F1,bd=7,width=15,relief=SUNKEN,textvariable=self.cusphn,font=("times new roman",12,"bold")).grid(row=0,column=3,pady=5,padx=10)
        
        cbill_lbl=Label(F1,text="Bill No.",bd=12,relief=GROOVE,bg=bg_color,font=("times new roman",18,"bold")).grid(row=0,column=4,pady=5,padx=20)
        cbill_lbl=Entry(F1,bd=7,width=15,relief=SUNKEN,textvariable=self.cusbill,font=("times new roman",12,"bold")).grid(row=0,column=5,pady=5,padx=10)
        
        bill_btn=Button(F1,text="Search",command=self.find_bill, width=10, bd=7,font="arial 12 bold").grid(row=0,column=6,pady=10,padx=20)
        bill_btn_lbl=Entry(F1,bd=7,width=15,relief=SUNKEN,textvariable=self.searchbill,font=("times new roman",12,"bold")).grid(row=0,column=7,pady=5,padx=10)
        
        #==========================Medicine Frame=================
       
        F2=LabelFrame(self.root,text="Pills",bd=10,relief=GROOVE,bg=bg_color,font=("times new roman",15,"bold"),fg="gold")
        F2.place(x=5,y=180,width=325,height=380)
        
        mname1_lbl=Label(F2,text="Medicine 1",bd=12,relief=GROOVE,bg=bg_color,font=("times new roman",15,"bold")).grid(row=0,column=0,pady=10,padx=5,sticky="w")
        mname1_txt=Entry(F2,width=15,bd=7,relief=SUNKEN,textvariable=self.medicine1,font=("times new roman",12,"bold")).grid(row=0,column=1,pady=10,padx=5)
        
        mname2_lbl=Label(F2,text="Medicine 2",bd=12,relief=GROOVE,bg=bg_color,font=("times new roman",15,"bold")).grid(row=1,column=0,pady=10,padx=5,sticky="w")
        mname2_txt=Entry(F2,width=15,bd=7,relief=SUNKEN,textvariable=self.medicine2,font=("times new roman",12,"bold")).grid(row=1,column=1,pady=10,padx=5)
        
        mname3_lbl=Label(F2,text="Medicine 3",bd=12,relief=GROOVE,bg=bg_color,font=("times new roman",15,"bold")).grid(row=2,column=0,pady=10,padx=5,sticky="w")
        mname3_txt=Entry(F2,width=15,bd=7,relief=SUNKEN,textvariable=self.medicine3,font=("times new roman",12,"bold")).grid(row=2,column=1,pady=10,padx=5)
        
        mname4_lbl=Label(F2,text="Medicine 4",bd=12,relief=GROOVE,bg=bg_color,font=("times new roman",15,"bold")).grid(row=3,column=0,pady=10,padx=5,sticky="w")
        mname4_txt=Entry(F2,width=15,bd=7,relief=SUNKEN,textvariable=self.medicine4,font=("times new roman",12,"bold")).grid(row=3,column=1,pady=10,padx=5)
        
        mname5_lbl=Label(F2,text="Medicine 5",bd=12,relief=GROOVE,bg=bg_color,font=("times new roman",15,"bold")).grid(row=4,column=0,pady=10,padx=5,sticky="w")
        mname5_txt=Entry(F2,width=15,bd=7,relief=SUNKEN,textvariable=self.medicine5,font=("times new roman",12,"bold")).grid(row=4,column=1,pady=10,padx=5)
       
        #=====================parllel medicine frame=========
        
        F3=LabelFrame(self.root,text="Injections",bd=10,relief=GROOVE,bg=bg_color,font=("times new roman",15,"bold"),fg="gold")
        F3.place(x=335,y=180,width=325,height=380)
        
        mname6_lbl=Label(F3,text="Medicine 6",bd=12,relief=GROOVE,bg=bg_color,font=("times new roman",15,"bold")).grid(row=0,column=0,pady=10,padx=5,sticky="w")
        mname6_txt=Entry(F3,width=15,bd=7,relief=SUNKEN,textvariable=self.medicine6,font=("times new roman",12,"bold")).grid(row=0,column=1,pady=10,padx=5)
        
        mname6_lbl=Label(F3,text="Medicine 7",bd=12,relief=GROOVE,bg=bg_color,font=("times new roman",15,"bold")).grid(row=1,column=0,pady=10,padx=5,sticky="w")
        mname6_txt=Entry(F3,width=15,bd=7,relief=SUNKEN,textvariable=self.medicine7,font=("times new roman",12,"bold")).grid(row=1,column=1,pady=10,padx=5)
        
        mname7_lbl=Label(F3,text="Medicine 8",bd=12,relief=GROOVE,bg=bg_color,font=("times new roman",15,"bold")).grid(row=2,column=0,pady=10,padx=5,sticky="w")
        mname7_txt=Entry(F3,width=15,bd=7,relief=SUNKEN,textvariable=self.medicine8,font=("times new roman",12,"bold")).grid(row=2,column=1,pady=10,padx=5)
        
        mname8_lbl=Label(F3,text="Medicine 9",bd=12,relief=GROOVE,bg=bg_color,font=("times new roman",15,"bold")).grid(row=3,column=0,pady=10,padx=5,sticky="w")
        mname8_txt=Entry(F3,width=15,bd=7,relief=SUNKEN,textvariable=self.medicine9,font=("times new roman",12,"bold")).grid(row=3,column=1,pady=10,padx=5)
        
        mname9_lbl=Label(F3,text="Medicine 10",bd=12,relief=GROOVE,bg=bg_color,font=("times new roman",15,"bold")).grid(row=4,column=0,pady=10,padx=5,sticky="w")
        mname9_txt=Entry(F3,width=15,bd=7,relief=SUNKEN,textvariable=self.medicine10,font=("times new roman",12,"bold")).grid(row=4,column=1,pady=10,padx=5)
        
        #=====================another parllel medicine frame=========
        
        F4=LabelFrame(self.root,text="Drinks",bd=10,relief=GROOVE,bg=bg_color,font=("times new roman",15,"bold"),fg="gold")
        F4.place(x=670,y=180,width=325,height=380)
        
        mname10_lbl=Label(F4,text="Medicine 11",bd=12,relief=GROOVE,bg=bg_color,font=("times new roman",15,"bold")).grid(row=0,column=0,pady=10,padx=5,sticky="w")
        mname10_txt=Entry(F4,width=15,bd=7,relief=SUNKEN,textvariable=self.medicine11,font=("times new roman",12,"bold")).grid(row=0,column=1,pady=10,padx=5)
        
        mname11_lbl=Label(F4,text="Medicine 12",bd=12,relief=GROOVE,bg=bg_color,font=("times new roman",15,"bold")).grid(row=1,column=0,pady=10,padx=5,sticky="w")
        mname11_txt=Entry(F4,width=15,bd=7,relief=SUNKEN,textvariable=self.medicine12,font=("times new roman",12,"bold")).grid(row=1,column=1,pady=10,padx=5)
        
        mname12_lbl=Label(F4,text="Medicine 13",bd=12,relief=GROOVE,bg=bg_color,font=("times new roman",15,"bold")).grid(row=2,column=0,pady=10,padx=5,sticky="w")
        mname12_txt=Entry(F4,width=15,bd=7,relief=SUNKEN,textvariable=self.medicine13,font=("times new roman",12,"bold")).grid(row=2,column=1,pady=10,padx=5)
        
        mname13_lbl=Label(F4,text="Medicine 14",bd=12,relief=GROOVE,bg=bg_color,font=("times new roman",15,"bold")).grid(row=3,column=0,pady=10,padx=5,sticky="w")
        mname13_txt=Entry(F4,width=15,bd=7,relief=SUNKEN,textvariable=self.medicine14,font=("times new roman",12,"bold")).grid(row=3,column=1,pady=10,padx=5)
        
        mname14_lbl=Label(F4,text="Medicine 15",bd=12,relief=GROOVE,bg=bg_color,font=("times new roman",15,"bold")).grid(row=4,column=0,pady=10,padx=5,sticky="w")
        mname14_txt=Entry(F4,width=15,bd=7,relief=SUNKEN,textvariable=self.medicine15,font=("times new roman",12,"bold")).grid(row=4,column=1,pady=10,padx=5)
        
        
        #===============Bill Area==================
        
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1000,y=180,width=530,height=380)
        bill_title=Label(F5,text="Bill Area",bd= 7,relief=GROOVE,font=("times new roman",15,"bold")).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        
        #=============button frame====================
        
        
        F6=LabelFrame(self.root,text="Bill Menu",bd=10,relief=GROOVE,bg=bg_color,font=("times new roman",15,"bold"),fg="gold")
        F6.place(x=0,y=560,relwidth=1,height=240)
        
        m1=Label(F6,text="Total Pills Price",bd=12,bg=bg_color,font=("times new roman",15,"bold")).grid(row=0,column=0,pady=1,padx=5,sticky="w")
        m1_txt=Entry(F6,width=15,bd=7,relief=SUNKEN,textvariable=self.pillsprice,font=("times new roman",12,"bold")).grid(row=0,column=1,pady=1,padx=5)
        
        m2=Label(F6,text="Total Injections Price",bd=12,bg=bg_color,font=("times new roman",15,"bold")).grid(row=1,column=0,pady=1,padx=5,sticky="w")
        m2_txt=Entry(F6,width=15,bd=7,relief=SUNKEN,textvariable=self.injectionsprice,font=("times new roman",12,"bold")).grid(row=1,column=1,pady=1,padx=5)
        
        m3=Label(F6,text="Total Drinks Price",bd=12,bg=bg_color,font=("times new roman",15,"bold")).grid(row=2,column=0,pady=1,padx=5,sticky="w")
        m3_txt=Entry(F6,width=15,bd=7,relief=SUNKEN,textvariable=self.drinksprice,font=("times new roman",12,"bold")).grid(row=2,column=1,pady=1,padx=5)
        
        
        c1=Label(F6,text="Total Pills Tax",bd=12,bg=bg_color,font=("times new roman",15,"bold")).grid(row=0,column=2,pady=1,padx=5,sticky="w")
        c1_txt=Entry(F6,width=15,bd=7,relief=SUNKEN,textvariable=self.pilltax,font=("times new roman",12,"bold")).grid(row=0,column=3,pady=1,padx=5)
        
        c2=Label(F6,text="Total Injections Tax",bd=12,bg=bg_color,font=("times new roman",15,"bold")).grid(row=1,column=2,pady=1,padx=5,sticky="w")
        c2_txt=Entry(F6,width=15,bd=7,relief=SUNKEN,textvariable=self.injectiontax,font=("times new roman",12,"bold")).grid(row=1,column=3,pady=1,padx=5)
        
        c3=Label(F6,text="Total Drinks Tax",bd=12,bg=bg_color,font=("times new roman",15,"bold")).grid(row=2,column=2,pady=1,padx=5,sticky="w")
        c3_txt=Entry(F6,width=15,bd=7,relief=SUNKEN,textvariable=self.drinkstax,font=("times new roman",12,"bold")).grid(row=2,column=3,pady=1,padx=5)
        
        but=Frame(F6,bd=7,relief=GROOVE)
        but.place(x=740,width=750,height=150)
        
        total_btn=Button(but,command=self.total,text="Total",pady=20, width=11,bg="Yellow", bd=7,font="arial 15 bold").grid(row=0,column=0,pady=20,padx=15)
        bill_btn=Button(but,command=self.bill_area,text="Generate Bill", pady=20,width=11,bg="Yellow", bd=7,font="arial 15 bold").grid(row=0,column=1,pady=20,padx=15)
        clear_btn=Button(but,text="Clear",command=self.clrdata, pady=20,width=11,bg="Yellow", bd=7,font="arial 15 bold").grid(row=0,column=2,pady=20,padx=15)
        exit_btn=Button(but,text="Exit",command=self.Exit_app,pady=20, width=11,bg="Yellow", bd=7,font="arial 15 bold").grid(row=0,column=3,pady=20,padx=15)
        self.welcome_bill()
        
         
        
        
        #================================total price work==========================================
        
    def total(self):
        self.m1p=self.medicine1.get()*40
        self.m2p=self.medicine2.get()*50
        self.m3p=self.medicine3.get()*60
        self.m4p=self.medicine4.get()*70
        self.m5p=self.medicine5.get()*80
        
        self.totalpillsprice=float(
                                      self.m1p+
                                      self.m2p+
                                      self.m3p+
                                      self.m4p+
                                      self.m5p 
                                      ) 
        self.pillsprice.set("Rs. "+str(self.totalpillsprice)) 
        self.totalpilltax=self.totalpillsprice*0.125
        self.pilltax.set("Rs. "+str(self.totalpilltax))
        
        self.m6p=self.medicine6.get()*40
        self.m7p=self.medicine7.get()*50
        self.m8p=self.medicine8.get()*60
        self.m9p=self.medicine9.get()*70
        self.m10p=self.medicine10.get()*80
        
        self.totalinjectionsprice=float(
                                      self.m6p+
                                      self.m7p+
                                      self.m8p+
                                      self.m9p+
                                      self.m10p 
                                      ) 
        self.injectionsprice.set("Rs. "+str(self.totalinjectionsprice)) 
        self.totalinjectiontax=self.totalinjectionsprice*0.125
        self.injectiontax.set("Rs. "+str(self.totalinjectiontax))
        
        
        self.m11p=self.medicine11.get()*40
        self.m12p=self.medicine12.get()*50
        self.m13p=self.medicine13.get()*60
        self.m14p=self.medicine14.get()*70
        self.m15p=self.medicine15.get()*80
        
        self.totaldrinksprice=float(
                                      self.m11p+
                                      self.m12p+
                                      self.m13p+
                                      self.m14p+
                                      self.m15p 
                                      ) 
        self.drinksprice.set("Rs. "+str(self.totaldrinksprice))
        self.totaldrinktax=self.totaldrinksprice*0.125
        self.drinkstax.set("Rs. "+str(self.totaldrinktax)) 
        
        self.Totalbill=self.totalpillsprice+self.totalpilltax+self.totalinjectionsprice+self.totalinjectiontax+self.totaldrinksprice+self.totaldrinktax

 #=====================bill area work=======================
    
    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t Welcome Retail Management\n")
        self.txtarea.insert(END,f"\n Bill No. - {self.cusbill.get()}")
        self.txtarea.insert(END,f"\n Customer Name - {self.cusname.get()}")
        self.txtarea.insert(END,f"\n Mobile No. - {self.cusphn.get()}")
        self.txtarea.insert(END,f"\n===============================================")
        self.txtarea.insert(END,f"\n Products \t\t QTY.\t\t Price")
        self.txtarea.insert(END,f"\n===============================================")
        
    def bill_area(self):
        if self.cusname.get()=="" or self.cusphn.get()=="":
            messagebox.showerror("Error","Customer details are must")
        elif self.pillsprice.get()=="Rs. 0.0" and self.injectionsprice.get()=="Rs. 0.0" and self.drinksprice.get()=="Rs. 0.0":
            messagebox.showerror("Error","No products has been purchased")
        else:
            self.welcome_bill()
            if self.medicine1.get()!=0:
                self.txtarea.insert(END,f"\n Medicine 1 \t\t{self.medicine1.get()} \t\tRS. {self.m1p}")
            if self.medicine2.get()!=0:     
                self.txtarea.insert(END,f"\n Medicine 2 \t\t{self.medicine2.get()} \t\tRS. {self.m2p}")
            if self.medicine3.get()!=0:
                self.txtarea.insert(END,f"\n Medicine 3 \t\t{self.medicine3.get()} \t\tRS. {self.m3p}")
            if self.medicine4.get()!=0:    
                self.txtarea.insert(END,f"\n Medicine 4 \t\t{self.medicine4.get()} \t\tRS. {self.m4p}")
            if self.medicine5.get()!=0:    
                self.txtarea.insert(END,f"\n Medicine 5 \t\t{self.medicine5.get()} \t\tRS. {self.m5p}")
                
            if self.medicine6.get()!=0:
                self.txtarea.insert(END,f"\n Medicine 6 \t\t{self.medicine6.get()} \t\tRS. {self.m6p}")
            if self.medicine7.get()!=0:     
                self.txtarea.insert(END,f"\n Medicine 7 \t\t{self.medicine7.get()} \t\tRS. {self.m7p}")
            if self.medicine8.get()!=0:
                self.txtarea.insert(END,f"\n Medicine 8 \t\t{self.medicine8.get()} \t\tRS. {self.m8p}")
            if self.medicine9.get()!=0:    
                self.txtarea.insert(END,f"\n Medicine 9 \t\t{self.medicine9.get()} \t\tRS. {self.m9p}")
            if self.medicine10.get()!=0:    
                self.txtarea.insert(END,f"\n Medicine 10 \t\t{self.medicine10.get()} \t\tRS. {self.m10p}")
            
            if self.medicine11.get()!=0:
                self.txtarea.insert(END,f"\n Medicine 11 \t\t{self.medicine11.get()} \t\tRS. {self.m11p}")
            if self.medicine12.get()!=0:     
                self.txtarea.insert(END,f"\n Medicine 12 \t\t{self.medicine12.get()} \t\tRS. {self.m12p}")
            if self.medicine13.get()!=0:
                self.txtarea.insert(END,f"\n Medicine 13 \t\t{self.medicine13.get()} \t\tRS. {self.m13p}")
            if self.medicine14.get()!=0:    
                self.txtarea.insert(END,f"\n Medicine 14 \t\t{self.medicine14.get()} \t\tRS. {self.m14p}")
            if self.medicine15.get()!=0:    
                self.txtarea.insert(END,f"\n Medicine 15 \t\t{self.medicine15.get()} \t\tRS. {self.m15p}")
            
            
            self.txtarea.insert(END,f"\n-----------------------------------------------")
            
            if self.pilltax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Pills Tax \t\t\t\t {self.pilltax.get()}")
            if self.injectiontax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Injections Tax \t\t\t\t {self.injectiontax.get()}")
            if self.drinkstax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Drinks Tax \t\t\t\t {self.drinkstax.get()}")
            self.txtarea.insert(END,f"\n Total Amount \t\t\t\t Rs. {self.Totalbill}")
            self.txtarea.insert(END,f"\n-----------------------------------------------")
            self.save_bill()
    
    
    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the bill?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("Bills/"+str(self.cusbill.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill No. : {self.cusbill.get()} has been saved sucessfully")
        else:
            return
    
    def find_bill(self):
        present="no"
        for i in os.listdir("Bills/"):
            if i.split('.')[0]==self.searchbill.get():
                f1=open(f"Bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No.")
            
   #====================CLEAR Button===========================

    def clrdata(self):
        op=messagebox.askyesno("Clear","Do you want to clear data?")
        if op>0:
            self.medicine1.set(0)
            self.medicine2.set(0) 
            self.medicine3.set(0)
            self.medicine4.set(0)
            self.medicine5.set(0) 
            
            #===================Injections Varaibles============================
            self.medicine6.set(0) 
            self.medicine7.set(0) 
            self.medicine8.set(0) 
            self.medicine9.set(0) 
            self.medicine10.set(0)
            
            #===================Drinks Varaibles============================
            self.medicine11.set(0)  
            self.medicine12.set(0)  
            self.medicine13.set(0) 
            self.medicine14.set(0) 
            self.medicine15.set(0) 
            
            #==================Total Product prices & taxes Varaibles============================
            self.pillsprice.set("") 
            self.injectionsprice.set("")
            self.drinksprice.set("") 
            
            self.pilltax.set("") 
            self.injectiontax.set("")
            self.drinkstax.set("") 
            
            #===================customer details Varaibles============================
            self.cusname.set("") 
            self.cusphn.set("") 
            self.cusbill.set("")
            x=random.randint(1000,9999)
            self.cusbill.set(str(x))
            self.searchbill.set("")
            self.welcome_bill() 
    
    #=================Exit button=======================================
    
    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.root.destroy()


                
            

     
            
                   
root=Tk()
obj = Bill_App(root)
root.mainloop()
