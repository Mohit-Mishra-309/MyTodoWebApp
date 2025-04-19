import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["todos"].title() + '\n'
    todos.append(todo)
    functions.write_todos(todos)


st.title("ZapList")
st.subheader("Strike through your day—one task at a time.")

for index , todo in enumerate(todos):
    checkbox = st.checkbox(todo , key = todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(placeholder="Enter a todo...",
              on_change= add_todo, key="todos")