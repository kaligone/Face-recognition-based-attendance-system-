from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #College Image
        img=Image.open(r"C:\Users\user\Desktop\FACE-REGONITION\College_Image\6.jpg")
        img=img.resize((2000,700),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=40,width=2000,height=700)

        #title
        title_lbl=Label(text="STUDENT DETAILS",font=("times new roman",35,"bold"),bg="Chocolate",fg="Black")
        title_lbl.place(x=0,y=0,width=1450,height=45)


      
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=0,y=0,width=1500,height=650)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=660,height=580)

        #current course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="CURRENT COURSE INFORMATION",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=50,width=650,height=200)

        #Department 
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),width=25,state="readonly")
        dep_combo["values"]=("SELECT DEPARTMENT","COMPUTER","IT","EXTC","CIVIL","MECHNICAL")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10)

        course_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),width=25,state="readonly")
        course_combo["values"]=("SELECT COURSE","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Semester
        semester_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=0,padx=10)

        semester_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),width=25,state="readonly")
        semester_combo["values"]=("SELECT SEMESTER","SEM 1","SEM 2","SEM 3","SEM 4","SEM 5","SEM 6","SEM 7","SEM 8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


        #Class Student course
        class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="CLASS STUDENT INFORMATION",font=("times new roman",12,"bold"))
        class_Student_frame.place(x=5,y=250,width=650,height=300)

        #student Id
        studentID_label=Label(class_Student_frame,text="StudentID",font=("times new roman",12,"bold"),bg="white")
        studentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_Student_frame,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #student Name
        studentName_label=Label(class_Student_frame,text="Student Name",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_Student_frame,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)


        #class division
        class_div_label=Label(class_Student_frame,text="Division",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        class_div_entry=ttk.Entry(class_Student_frame,font=("times new roman",12,"bold"))
        class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Roll No
        roll_no_label=Label(class_Student_frame,text="Roll No.",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_Student_frame,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Gender
        gender_label=Label(class_Student_frame,text="Gender",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_entry=ttk.Entry(class_Student_frame,font=("times new roman",12,"bold"))
        gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #DOB
        dob_label=Label(class_Student_frame,text="DOB",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_Student_frame,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #EmailID
        email_label=Label(class_Student_frame,text="EmailID",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_Student_frame,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #Phone no.
        phone_label=Label(class_Student_frame,text="Phone No.",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_Student_frame,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #ADDRESS
        address_label=Label(class_Student_frame,text="Address",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_Student_frame,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)


        #radio buttons
        radiobtn1=ttk.Radiobutton(class_Student_frame,text="TAKE PHOTO SAMPLE",value="YES")
        radiobtn1.grid(row=5,column=0)

        radiobtn2=ttk.Radiobutton(class_Student_frame,text="NO PHOTO SAMPLE",value="YES")
        radiobtn2.grid(row=5,column=1)

        #buttons frame
        btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=440,height=35)

        save_btn=Button(btn_frame,text="SAVE",width=11,font=("times new roman",12,"bold"),bg="chocolate")
        save_btn.grid(row=0,column=0,padx=2)

        delete_btn=Button(btn_frame,text="DELETE",width=11,font=("times new roman",12,"bold"),bg="chocolate")
        delete_btn.grid(row=0,column=1,padx=2)

        update_btn=Button(btn_frame,text="UPDATE",width=11,font=("times new roman",12,"bold"),bg="chocolate")
        update_btn.grid(row=0,column=2,padx=2)

        reset_btn=Button(btn_frame,text="RESET",width=11,font=("times new roman",12,"bold"),bg="chocolate")
        reset_btn.grid(row=0,column=3)

        
        btn_frame_1=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame_1.place(x=0,y=235,width=420,height=35)

        take_photo_btn=Button(btn_frame_1,text="TAKE PHOTO SAMPLE",width=22,font=("times new roman",12,"bold"),bg="chocolate")
        take_photo_btn.grid(row=0,column=0,padx=2)

        update_photo_btn=Button(btn_frame_1,text="UPDATE PHOTO SAMPLE",width=22,font=("times new roman",12,"bold"),bg="chocolate")
        update_photo_btn.grid(row=0,column=1)


        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",12,"bold"))
        Right_frame.place(x=680,y=10,width=660,height=580)

        #Search system
        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="SEARCH SYSTEM",font=("times new roman",12,"bold"))
        Search_frame.place(x=5,y=10,width=650,height=100)

        search_label=Label(Search_frame,text="Search By:",font=("times new roman",15,"bold"),bg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(Search_frame,font=("times new roman",12,"bold"),width=15,state="readonly")
        search_combo["values"]=("SELECT","ROLL_NO","PHONE_NO")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(Search_frame,width=16,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(Search_frame,text="SEARCH",width=11,font=("times new roman",12,"bold"),bg="chocolate")
        search_btn.grid(row=0,column=3,padx=3)

        showALL_btn=Button(Search_frame,text="SHOW ALL",width=11,font=("times new roman",12,"bold"),bg="chocolate")
        showALL_btn.grid(row=0,column=4)

        #table frame
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=100,width=650,height=450)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","phone","address","photo","email"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone_No")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.pack(fill=BOTH,expand=1)

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("photo",width=100)



        

if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
