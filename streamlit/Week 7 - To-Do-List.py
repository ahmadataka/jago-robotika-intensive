import streamlit as st

st.set_page_config(page_title="My Productivity App", layout="centered")

st.title("My Productivity App")
st.write("Habit Tracker + To-Do List")

# =========================
# INIT STATE
# =========================
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# =========================
# INPUT SECTION
# =========================
st.subheader("Tambah Task / Habit")

new_task = st.text_input("Nama task atau habit")

col1, col2 = st.columns(2)

with col1:
    add_btn = st.button("Tambah")

with col2:
    clear_btn = st.button("Hapus Semua")

# =========================
# ADD TASK
# =========================
if add_btn:
    if new_task.strip() != "":
        st.session_state.tasks.append({
            "name": new_task,
            "done": False
        })
        st.success("Task ditambahkan")
    else:
        st.warning("Masukkan nama task terlebih dahulu")

# =========================
# CLEAR ALL
# =========================
if clear_btn:
    st.session_state.tasks = []
    st.warning("Semua task dihapus")

# =========================
# DISPLAY TASKS
# =========================
st.subheader("Daftar Task")

if len(st.session_state.tasks) == 0:
    st.info("Belum ada task")
else:
    completed = 0

    for i, task in enumerate(st.session_state.tasks):
        checked = st.checkbox(task["name"], value=task["done"], key=i)

        st.session_state.tasks[i]["done"] = checked

        if checked:
            completed += 1

# =========================
# METRICS
# =========================
total = len(st.session_state.tasks)

if total > 0:
    st.subheader("Progress")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Task", total)

    with col2:
        st.metric("Selesai", completed)

    progress = completed / total
    st.progress(progress)

# =========================
# FEEDBACK
# =========================
if total > 0:
    if completed == total:
        st.success("Semua task selesai! Keren!")
    elif completed > 0:
        st.write("Tetap semangat, lanjutkan!")
    else:
        st.write("Ayo mulai kerjakan task kamu!")