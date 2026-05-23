import streamlit as st
import random

st.set_page_config(page_title="AI Image Caption Generator", layout="centered")

st.title("AI Image Caption Generator")
st.write("Upload gambar, pilih kategori, lalu buat caption otomatis.")

uploaded_file = st.file_uploader(
    "Upload gambar",
    type=["jpg", "jpeg", "png"]
)

category = st.selectbox(
    "Pilih kategori gambar",
    ["Cat", "Dog", "Food", "Nature", "Robot", "School", "Other"]
)

caption_style = st.selectbox(
    "Pilih gaya caption",
    ["Funny", "Cool", "Simple", "Motivational"]
)

captions = {
    "Cat": {
        "Funny": [
            "Kucing ini sepertinya sedang merencanakan sesuatu.",
            "Bos kecil berbulu sedang mengawasi dunia."
        ],
        "Cool": [
            "Seekor kucing dengan aura misterius.",
            "Tenang, fokus, dan penuh gaya."
        ],
        "Simple": [
            "Seekor kucing sedang berpose.",
            "Kucing lucu terlihat di gambar ini."
        ],
        "Motivational": [
            "Tetap tenang seperti kucing ini.",
            "Percaya diri dimulai dari sikap yang santai."
        ]
    },
    "Dog": {
        "Funny": [
            "Anjing ini siap menjadi sahabat terbaikmu.",
            "Wajahnya bilang: ayo main sekarang!"
        ],
        "Cool": [
            "Seekor anjing penuh energi dan semangat.",
            "Loyal, berani, dan ceria."
        ],
        "Simple": [
            "Seekor anjing terlihat di gambar.",
            "Anjing ini tampak sangat ramah."
        ],
        "Motivational": [
            "Semangat seperti anjing yang selalu siap bermain.",
            "Kesetiaan dan energi positif terlihat di sini."
        ]
    },
    "Food": {
        "Funny": [
            "Makanan ini berbahaya karena terlalu menggoda.",
            "Kalau lapar, gambar ini bukan ide yang baik."
        ],
        "Cool": [
            "Sajian yang terlihat menarik dan menggugah selera.",
            "Komposisi makanan yang tampak lezat."
        ],
        "Simple": [
            "Ini adalah gambar makanan.",
            "Makanan terlihat siap dinikmati."
        ],
        "Motivational": [
            "Energi hari ini dimulai dari makanan yang baik.",
            "Setiap karya hebat butuh bahan bakar."
        ]
    },
    "Nature": {
        "Funny": [
            "Alam sedang pamer keindahan.",
            "Tempat ini terlihat cocok untuk kabur dari tugas."
        ],
        "Cool": [
            "Pemandangan alam yang menenangkan.",
            "Keindahan sederhana dari dunia sekitar."
        ],
        "Simple": [
            "Gambar ini menunjukkan pemandangan alam.",
            "Alam terlihat indah dan tenang."
        ],
        "Motivational": [
            "Seperti alam, terus tumbuh perlahan.",
            "Ketenangan adalah kekuatan."
        ]
    },
    "Robot": {
        "Funny": [
            "Robot ini sepertinya butuh update software.",
            "Calon penguasa dunia sedang latihan."
        ],
        "Cool": [
            "Teknologi dan kreativitas bertemu di sini.",
            "Robot ini menunjukkan masa depan yang menarik."
        ],
        "Simple": [
            "Ini adalah gambar robot.",
            "Robot terlihat dalam gambar ini."
        ],
        "Motivational": [
            "Masa depan dibuat oleh mereka yang berani mencoba.",
            "Setiap robot besar dimulai dari ide kecil."
        ]
    },
    "School": {
        "Funny": [
            "Tempat penuh tugas, teman, dan cerita.",
            "Sekolah: tempat ide dan PR bertemu."
        ],
        "Cool": [
            "Lingkungan belajar yang penuh peluang.",
            "Tempat tumbuhnya generasi kreatif."
        ],
        "Simple": [
            "Ini adalah gambar tentang sekolah.",
            "Suasana belajar terlihat di gambar ini."
        ],
        "Motivational": [
            "Belajar hari ini, memimpin esok hari.",
            "Setiap pelajaran adalah langkah maju."
        ]
    },
    "Other": {
        "Funny": [
            "Gambar ini misterius, tapi tetap menarik.",
            "AI bingung, tapi tetap percaya diri."
        ],
        "Cool": [
            "Sebuah gambar dengan cerita tersendiri.",
            "Visual yang menarik untuk diamati."
        ],
        "Simple": [
            "Ini adalah gambar yang diupload pengguna.",
            "Gambar berhasil ditampilkan."
        ],
        "Motivational": [
            "Setiap gambar punya cerita.",
            "Hal sederhana bisa menjadi inspirasi."
        ]
    }
}

if uploaded_file is not None:
    st.subheader("Preview Gambar")
    st.image(uploaded_file, use_container_width=True)

    if st.button("Generate Caption"):
        result = random.choice(captions[category][caption_style])

        st.subheader("Generated Caption")
        st.success(result)

else:
    st.warning("Silakan upload gambar terlebih dahulu.")