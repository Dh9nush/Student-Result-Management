import streamlit as st 
import mysql.connector 
import pandas as pd
from streamlit_option_menu import option_menu


    
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="student_results"
)
cnx=mydb.cursor()

def add_result(Id,Student_name,Lab,McQ,Module,Instructor):
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Dhanush@123",
    database="student_results"
    )
    cnx=mydb.cursor()
    st.subheader("ADD STUDENT")
    cnx.execute(f"insert into results values ({int(Id)},'{Student_name}',{int(Lab)},{int(McQ)},{int(Module)},'{Instructor}'); ")
    mydb.commit()
    mydb.close()
    return 1
    

                                            
def add_teacher(tname,pswd):
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="student_results"
    )
    cnx=mydb.cursor()
    cnx.execute(f"insert into teacher_cred(teacher_name,password_) values ('{tname}','{pswd}');")
    mydb.commit()
    mydb.close()
    return 1

def add_course(mod,course_name,cname,tname):
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="student_results"
    )
    cnx=mydb.cursor()
    cnx.execute(f"insert into course_details values ({int(mod)},'{course_name}','{cname}','{tname}');")
    mydb.commit()
    mydb.close()
    return 1

def remove_teacher(tname):
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="student_results"
    )
    cnx=mydb.cursor()
    cnx.execute(f"delete from  teacher_cred where teacher_name like '{tname}';")
    mydb.commit()
    mydb.close()
    return 1

def view_results():
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="student_results"
    )
    cnx=mydb.cursor()
    st.subheader("View results")
    
    cnx.execute("SELECT * FROM results")
    data=pd.DataFrame(cnx.fetchall(),columns=["Roll_number","Name","Lab","Practical","Module","Instructor"]).sort_values("Roll_number")    
    st.write(data)
    cnx.close()

def view_course():
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="student_results"
    )
    cnx=mydb.cursor()
    cnx.execute(f"Select * from course_details")
    data=cnx.fetchall()
    st.dataframe(pd.DataFrame(data,columns=["Module","Course Name","Course Coordinator","Teacher"]),use_container_width=False)
    mydb.commit()
    mydb.close()

def view_student():
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="student_results"
    )
    cnx=mydb.cursor()
    cnx.execute(f"Select * from student_cred")
    data=cnx.fetchall()
    st.dataframe(pd.DataFrame(data,columns=["Roll_Number","Date_Of_Birth"]),use_container_width=False)
    mydb.commit()
    mydb.close()
    
  
def update_result():
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="student_results"
    )
    cnx=mydb.cursor()
    rn=st.text_input("Enter Roll Number")
    field=st.text_input("What field name (Lab,McQ) to Update")
    value=st.text_input("Enter Marks")
    confirm=st.text_input("Enter Confirm ")
    if rn !="" and confirm=="confirm" and field!="":
        cnx.execute(f"SELECT id FROM results WHERE id like {rn}  ;")
        stu_tab = cnx.fetchall()
        if stu_tab:
            cnx.execute(f"Update results set {field}={int(value)} where id={int(rn)}")
            mydb.commit()
            mydb.close()
            st.success("Student record Deleted Successfully")
        else:
            st.error("Roll number not found ")
    
def delete_student_results():
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="student_results"
    )
    cnx=mydb.cursor()
    rn=st.text_input("Enter Roll Number")
    confirm=st.text_input("Enter confirm ")
    if rn !="" and confirm=="confirm":
        cnx.execute(f"SELECT id FROM results WHERE id like {rn}  ;")
        stu_tab = cnx.fetchall()
        if stu_tab:
            cnx.execute(f"delete from results where id={int(rn)}")
            mydb.commit()
            mydb.close()
            st.success("Student record Updated Successfully")
        else:
            st.error("Roll number not found ")
    
    
      
def get_student_detail(id):
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="student_results"
    )
    cnx=mydb.cursor()
    # Add a title
    st.title("Results") 

    # Execute a MySQL query to retrieve the student details based on the ID
    cnx.execute(f"SELECT * FROM results WHERE id = {int(id)}")
    stu_tab = cnx.fetchall()
            
    # Show the student details
    if stu_tab:
        data=pd.DataFrame(stu_tab,columns=["Roll_number","Student_Name","Lab","Practical","Module","Instructor"]).sort_values("Roll_number")
        st.write(data)
    mydb.close()



def check_student(id,dob):
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="student_results"
    )
    cnx=mydb.cursor()
    cnx.execute(f"SELECT id FROM student_cred WHERE id like {id} and dob  like '{dob}' ;")
    stu_tab = cnx.fetchall()
    mydb.close()
    return stu_tab

def add_student(id,dob):
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="student_results"
    )
    cnx=mydb.cursor()
    st.write(id,dob)
    cnx.execute(f"insert into student_cred values ({int(id)},'{dob}');")
    mydb.commit()
    mydb.close()
    return 1

    


def admin_login():
    pswd=st.text_input("Enter Password",type="password")
    if pswd=="admin@123":
        st.title("Admin Page")
        with st.sidebar:
            option=option_menu(None,["Teacher","Student"],icons=["person","book"],menu_icon="cast",orientation="horizontal")
        if option=="Teacher": 
            tmenu=option_menu(None,["View Course","Add Course","Add Teacher","Delete Teacher"],icons=["","",""],menu_icon="cast",orientation="horizontal")
            if tmenu=="View Course":
                view_course()
            if tmenu=="Add Course":
                mod = st.text_input("Enter Module ")
                course_name = st.text_input("Enter Course Name ")
                cname = st.text_input("Enter Course-coordinator ")
                tname = st.text_input("Enter Teacher name ")
                if mod!="" and course_name!="" and cname!="" and tname != "":
                    if add_course(mod,course_name,cname,tname):
                        st.success("Course Added")
                    else:
                        st.error("Course Added")
                

            if tmenu=="Add Teacher":
                tname=st.text_input("Name of Teacher")
                pswd=st.text_input("Password for that Teacher ",type ='password')
                if tname!="" and pswd!="":
                    if add_teacher(tname,pswd):
                        st.success("Added Teacher")
                    else:
                        st.error("Failed to Add Teacher")
                
            if tmenu=="Delete Teacher":
                tname=st.text_input("Name of Teacher")
                if tname!="":
                    if remove_teacher(tname):
                        st.success("Teacher Removed")
                    else:
                        st.error("Teacher Not Found")
                
        else:
            smenu=option_menu(None,["View Results","Add Result","Update Results","View Student","Add Student","Delete Student"],icons=["","",""],menu_icon="cast",orientation="horizontal")
            if smenu=="View Results":
                view_results()
            if smenu=="Add Result":
                    Id = st.text_input("Enter ID")
                    Student_name = st.text_input(f"Enter ID:{Id} Name ")
                    Lab = st.text_input(f"Enter {Student_name} Lab Marks ")
                    McQ = st.text_input(f"Enter {Student_name} McQ MArks ")
                    Module = st.text_input(f"Enter Module")
                    Instructor = st.text_input(f"Enter module {Module} Instructor ")
                    if Id!="" and Student_name!="" and Lab!="" and McQ!="" and Instructor!="":
                        if add_result(Id,Student_name,Lab,McQ,Module,Instructor):
                            st.success("Student Added ")
                        else:
                            st.error("Error Occured ")
            if smenu=="View Student":
                view_student()
            if smenu=="Update Results":
                update_result()
            if smenu=="Add Student":
                roll_no=st.text_input("Enter Your roll number")
                dob=st.text_input("Enter Your Date Of Birth ",placeholder="yyyy-mm-dd")
                if dob!="" :
                    if add_student(roll_no,dob):
                        st.success("Student added")
                    else:
                        st.error("Error Found")
            if smenu=="Delete Student":
                delete_student()
        st.session_state.role=None

def teacher_login():
    tname=st.text_input("Enter User name")
    pswd=st.text_input("Enter Password",type="password")
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="student_results"
    )
    cnx=mydb.cursor()
    if tname!="" and pswd!="":
        cnx.execute(f"select teacher_name from teacher_cred where teacher_name like '{tname}' and password_ like '{pswd}' ")
        if cnx.fetchone():
            st.title("Teacher Page")
            st.subheader(f"Welcome {tname}")
            option=option_menu(None,["Add Result","View Result"],icons=["person","book"],menu_icon="cast",orientation="horizontal")
            if option=="Add Result":
                Id = st.text_input("Enter ID")
                Student_name = st.text_input(f"Enter ID:{Id} Name ")
                Lab = st.text_input(f"Enter {Student_name} Lab Marks ")
                McQ = st.text_input(f"Enter {Student_name} McQ MArks ")
                Module = st.text_input(f"Enter Module")
                Instructor = st.text_input(f"Enter module {Module} Instructor ")
                if Id!="" and Student_name!="" and Lab!="" and McQ!="" and Instructor!="":
                    if add_result(Id,Student_name,Lab,McQ,Module,Instructor):
                        st.success("Student Added ")
                    else:
                        st.error("Error Occured ")
            elif option=="View Result":
                view_results()
            st.session_state.role=None
        else:
            st.error("Wrong Password")
             

    

def student_login():
    roll_no=st.text_input("Enter Your roll number")
    dob=st.text_input("Enter Your Date Of Birth ",placeholder="yyyy-mm-dd")
    if dob!="":
        if check_student(roll_no,dob):
            get_student_detail(roll_no)
        else:
            st.error("Not Found")

    st.session_state.role=None

