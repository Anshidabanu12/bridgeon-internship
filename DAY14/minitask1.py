import streamlit as st

st.title("GREETING APP")
if "name" not in st.session_state:
    st.session_state["name"] = ""

#text inpute
name = st.text_input("Enter your name")
# st.write("hello",name) 
  
if st.button("greet"):
    # st.write ("button pressed") 
       st.session_state["name"] = name
#display greeting 
if st.session_state["name"]:
      st.success(f"hello, {st.session_state['name']}!")

