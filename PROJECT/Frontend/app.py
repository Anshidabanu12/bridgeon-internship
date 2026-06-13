
import streamlit as st
import pandas as pd
from datetime import date

st.markdown("""
<style>

/* Main Background */
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
}

/* Content Width */
.block-container {
    max-width: 1000px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Text */
h1, h2, h3, label, p {
    color: white !important;
}

/* Cards */
[data-testid="stMetric"] {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 15px;
    padding: 15px;
}

/* Text Inputs */
div[data-testid="stTextInput"] input {
    background: white;
    color: black;
    border-radius: 10px;
    height: 45px;
}

/* Text Area */
textarea {
    background: white !important;
    color: black !important;
    border-radius: 10px !important;
}

/* Select Box */
div[data-baseweb="select"] {
    background: white;
    border-radius: 10px;
}

/* Date Input */
div[data-testid="stDateInput"] input {
    background: white;
    color: black;
    border-radius: 10px;
}

/* Buttons */
.stButton button {
    background-color: #2563eb;
    color: white;
    border-radius: 10px;
    height: 45px;
    width: 100%;
    font-weight: bold;
    border: none;
}

.stButton button:hover {
    background-color: #1d4ed8;
}

/* Dataframe */
[data-testid="stDataFrame"] {
    background: white;
    border-radius: 12px;
    overflow: hidden;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #111827;
}

/* Divider */
hr {
    border-color: rgba(255,255,255,0.2);
}

</style>
""", unsafe_allow_html=True)

# ===================================
# SESSION STATE
# ===================================
if "users" not in st.session_state:
    st.session_state.users = {}

if "tasks" not in st.session_state:
    st.session_state.tasks = {}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "current_user" not in st.session_state:
    st.session_state.current_user = None


# ===================================
# REGISTER
# ===================================
def register():

    # st.header("Register")
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)

    st.markdown(
    "<h2 style='text-align:center;color:#4F46E5'>Create Account</h2>",
    unsafe_allow_html=True
)

    st.markdown(
    "<p style='text-align:center'>Start Managing Your Tasks</p>",
    unsafe_allow_html=True
)



    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Register"):

        if not username or not email or not password:
            st.error("Please fill all fields")

        elif username in st.session_state.users:
            st.error("Username already exists")

        else:
            st.session_state.users[username] = {
                "email": email,
                "password": password
            }

            st.session_state.tasks[username] = []

            st.success("Registration Successful!")
            st.info("Please Login")


# ===================================
# LOGIN
# ===================================
def login():

    st.header("Login")
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown(
    '<div class="main-title">📋 Task Manager</div>',
    unsafe_allow_html=True
)

    st.markdown(
    '<div class="sub-title">Welcome Back</div>',
    unsafe_allow_html=True
)




    username = st.text_input(
        "Username",
        key="login_user"
    )

    password = st.text_input(
        "Password",
        type="password",
        key="login_pass"
    )

    if st.button("Login"):

        if (
            username in st.session_state.users
            and
            st.session_state.users[username]["password"] == password
        ):

            st.session_state.logged_in = True
            st.session_state.current_user = username

            st.rerun()

        else:
            st.error("Invalid Username or Password")


# ===================================
# DASHBOARD
# ===================================
def dashboard():

    user = st.session_state.current_user

    # st.title("📋 Task Manager Dashboard")

    st.markdown("""
<div class='custom-card'>
<h1 style='text-align:center;color:#4F46E5'>
📋 Task Manager
</h1>
<p style='text-align:center'>
Manage Your Daily Tasks
</p>
</div>
""", unsafe_allow_html=True)

    st.success(f"Welcome {user}")

    # Metrics
    tasks = st.session_state.tasks[user]

    total_tasks = len(tasks)

    completed_tasks = sum(
        1 for task in tasks
        if task["completed"]
    )

    pending_tasks = total_tasks - completed_tasks

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Tasks", total_tasks)

    with col2:
        st.metric("Completed", completed_tasks)

    with col3:
        st.metric("Pending", pending_tasks)

    st.divider()

    # Create Task
    st.subheader("Create Task")

    with st.form("task_form"):

        title = st.text_input("Title")

        description = st.text_area(
            "Description"
        )

        priority = st.selectbox(
            "Priority",
            ["Low", "Medium", "High"]
        )

        due_date = st.date_input(
            "Due Date",
            min_value=date.today()
        )

        submit_task = st.form_submit_button(
            "Create Task"
        )

    if submit_task:

        if title:

            task_id = len(
                st.session_state.tasks[user]
            ) + 1

            st.session_state.tasks[user].append(
                {
                    "id": task_id,
                    "title": title,
                    "description": description,
                    "priority": priority,
                    "due_date": str(due_date),
                    "completed": False
                }
            )

            st.success(
                f"Task '{title}' created successfully!"
            )

            st.rerun()

        else:
            st.error("Task Title is required")

    st.divider()

    # My Tasks
    st.subheader("My Tasks")

    tasks = st.session_state.tasks[user]

    if tasks:

        df = pd.DataFrame(
            [
                {
                    "ID": task["id"],
                    "Title": task["title"],
                    "Description": task["description"],
                    "Priority": task["priority"],
                    "Due Date": task["due_date"],
                    "Completed":
                        "Yes" if task["completed"]
                        else "No"
                }
                for task in tasks
            ]
        )

        st.dataframe(
            df,
            use_container_width=True
        )

        st.divider()

        st.subheader(
            "Update Task Status"
        )

        for index, task in enumerate(tasks):

            col1, col2, col3 = st.columns(
                [4, 2, 1]
            )

            with col1:
                st.write(
                    f"**{task['title']}**"
                )

            with col2:

                if task["completed"]:
                    st.success("Completed")

                else:
                    if st.button(
                        "Complete",
                        key=f"complete_{index}"
                    ):
                        task["completed"] = True
                        st.rerun()

            with col3:

                if st.button(
                    "Delete",
                    key=f"delete_{index}"
                ):
                    st.session_state.tasks[user].pop(
                        index
                    )
                    st.rerun()

    else:
        st.info("No Tasks Available")

    st.divider()

    if st.button("Logout"):

        st.session_state.logged_in = False
        st.session_state.current_user = None

        st.rerun()


# ===================================
# MAIN APP
# ===================================
if st.session_state.logged_in:

    dashboard()

else:

    st.title("📋 Task Manager")

    option = st.sidebar.selectbox(
        "Menu",
        [
            "Login",
            "Register"
        ]
    )

    if option == "Login":
        login()
    else:
        register()