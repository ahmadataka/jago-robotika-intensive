import streamlit as st
import random

st.set_page_config(page_title="Student Dashboard", layout="centered")

st.title("Student Score Dashboard")

print(random.randint(0, 10))

data = [
    {"Nama": "Ataka", "Math": 90, "Science": 70, "History": 80, "Religion": 100},
    {"Nama": "Uwais", "Math": 100, "Science": 80, "History": 90, "Religion": 100},
    {"Nama": "Hamizan", "Math": 100, "Science": 85, "History": 85, "Religion": 100},
    ]
st.subheader("Nilai Akademik")
st.dataframe(data)

names = [d["Nama"] for d in data]
selected = st.selectbox("Pilih siswa", names)

for d in data:
    if d["Nama"] == selected:
        st.write("Nama:", d["Nama"])
        st.write("Math:", d["Math"])
        st.write("Science:", d["Science"])
        st.write("History:", d["History"])
        st.write("Religion:", d["Religion"])

selected = st.selectbox("Pilih Pelajaran", ["Math", "Science", "History", "Religion"])

nama_pelajaran = str(selected)
pelajaran = [d[nama_pelajaran] for d in data]
data_baru = {"Nama": names,
            nama_pelajaran: pelajaran}

st.bar_chart(data_baru, x="Nama", y=nama_pelajaran)

st.write("Jumlah siswa:", len(names))

jumlah_nilai = sum(pelajaran)
ratarata = jumlah_nilai/len(names)

st.write("Rata-rata nilai "+nama_pelajaran+"=", ratarata)

min_score = st.slider("Nilai minimum", 0, 50, 100)    

filtered = [d for d in data if d[nama_pelajaran] >= min_score]
st.dataframe(filtered)



 
# 
# # =========================
# # FILTER DATA
# # =========================
# st.subheader("Filter Nilai")
# 
# min_score = st.slider("Minimum nilai math", 0, 100, 70)
# 
# filtered = [d for d in data if d["math"] >= min_score]
# 
# st.write("Siswa dengan nilai math di atas batas:")
# st.dataframe(filtered)
# 
# # =========================
# # FEEDBACK
# # =========================
# if len(filtered) == 0:
#     st.warning("Tidak ada siswa yang memenuhi kriteria")
# else:
#     st.success(f"{len(filtered)} siswa ditemukan")


# 
# avg_math = sum([d["math"] for d in data]) / len(data)
# st.metric("Rata-rata Math", round(avg_math, 1))