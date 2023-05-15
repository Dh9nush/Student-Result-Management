import streamlit as st
import functions as f


from streamlit_option_menu import option_menu
st.set_page_config(page_title="Result Management System")



if "login_state" not in st.session_state:
    st.session_state["login_state"]=False

st.title("Result Management System")
with st.sidebar:
    choice=option_menu("ROLES",("ADMIN","TEACHER","STUDENT"))
if choice=="ADMIN":
    st.session_state.role="admin"
    f.admin_login()
if choice=="TEACHER":
    st.session_state.role="teacher"
    f.teacher_login()
if choice=="STUDENT":
    st.session_state.role="student"
    f.student_login()




    







# def main():
#     menu = st.sidebar.selectbox("options",("Admin","Teacher","Student"),key="Choice")
#     st.write(st.session_state)

#     if menu =="Admin":
#             name=["admin"]
#             username=["admin"]
#             password=["admin@123"]
#             hash_pass=stauth.Hasher(password).generate()
#             authenticator = stauth.Authenticate(name,username,hash_pass,"Test1","abcde",cookie_expiry_days=0)
#             name,authentication_status,username =authenticator.login("Login","main")
#             if authentication_status==False:
#                 st.error("wrong password")

#             elif authentication_status == None:
#                 st.warning("Enter something")

#             elif authentication_status:


                    # st.title("Admin Page")
                    # option=option_menu(None,["Teacher","Student"],icons=["person","book"],menu_icon="cast",orientation="horizontal")
                    # if option=="Teacher": 
                    #     option_menu(None,["Update Course","Add Teacher","Performance"],icons=["","",""],menu_icon="cast",orientation="horizontal")
                    #     pass
                    # else:
                    #     option_menu(None,["View Results","Update Result","Delete Student"],icons=["","",""],menu_icon="cast",orientation="horizontal")
                    #     pass
                    # authenticator.logout("Logout","main")
#     elif menu== "Teacher":
#             username=["vineeta","malkeet","amar"]
#             password=["vine","malk","amar"]
#             hash_pass=stauth.Hasher(password).generate()
#             authenticator = stauth.Authenticate(username,username,hash_pass,"Test2","abcd",cookie_expiry_days=0)
#             name,authentication_status,username =authenticator.login("Login","main")
#             if authentication_status==False:
#                 st.error("wrong password")

#             elif authentication_status == None:
#                 st.warning("Enter something")

#             elif authentication_status:
#                     st.title("Teacher Page")
                    # option=option_menu(None,["Add Result","View Result"],icons=["person","book"],menu_icon="cast",orientation="horizontal")
                    # if option=="Add Result":
                    #     pass
                    # elif option=="View Result":
                    #     pass
                    # authenticator.logout("Logout","main")
#     elif menu=="Student":
#             username=["dhanush","nitesh","mahesh"]
#             password=["dha","nit","mah"]
#             hash_pass=stauth.Hasher(password).generate()
#             authenticator = stauth.Authenticate(username,username,hash_pass,"Test3","ab",cookie_expiry_days=0)
#             name,authentication_status,username =authenticator.login("Login","main")
#             if authentication_status==False:
#                 st.error("wrong password")

#             elif authentication_status == None:
#                 st.warning("Enter something")

#             elif authentication_status:
#                     st.title("Student Page")
#                     st.input( )
                    
                    
         
         
         
# main()
    # elif menu == "Teacher":
    #     st.title("Login Admin")
    #     user_name
    #     password=st.text_input("Password :",type="Password")
    #     if password ==cnx.execute(f"select password from credentials where password={password} and user_name ={user_name}")
    #         hash_pass=stauth.Hasher([password]).generate()
    #         st.set_page_config(page_title="Test")
    #         authenticator = stauth.Authenticate(username,username,hash_pass,"Test","abcd")
    #         name,authentication_status,username =authenticator.login("Login","main")
