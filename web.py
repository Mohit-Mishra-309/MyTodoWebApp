import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo= st.session_state["todos"].capitalize().strip()
    if todo:
        todos.append(todo + '\n')
        functions.write_todos(todos)
        st.session_state["todos"] = ""


st.title("ZapList")
st.subheader("Strike through your day—one task at a time.")

for index , todo in enumerate(todos):
    checkbox = st.checkbox(todo , key = todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="Enter a task", label_visibility = "hidden",
              placeholder="Enter a todo...", key="todos" )

st.button("Add Task", on_click=add_todo)