# import streamlit as st 
# st.set_page_config(page_title="Task Manager", page_icon="📋", layout="centered")
# st.title("📋 Task Manager App")
# st.write("Welcom ! choose a page from below 👇")

# #navigation (routers)

# page = st.sidebar.radio(
#     "Go to",
#     ["login", "Register", "Tasks"]
# )
# if page =="Login":
#     st.switch_page("page/login.py")
# elif page =="Register":
#     st.switch_page("page/register.py")
# elif page == "Tasks":
#     st.switch_page("page/tasks.py")



from fastapi import FastAPI

from auth import router as auth_router
from tasks import router as task_router

app = FastAPI(
    title="Task Manager API"
)

app.include_router(auth_router)
app.include_router(task_router)


@app.get("/")
def home():

    return {
        "message": "Task Manager Backend Running"
    }