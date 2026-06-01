import streamlit as st
import random

st.set_page_config(page_title="Uwais Portfolio", page_icon="🔥")

# orange colour for headings
st.markdown("""
<style>
h1, h2, h3 { color: #ff6600; }
</style>
""", unsafe_allow_html=True)

# ── SIDEBAR NAVIGATION ──
page = st.sidebar.radio("Go to", ["🏠 Home", "👤 About Me", "🖼️Gallery", "🎮 Fun Zone", "📬 Contact"])

# ══════════════════════
# 🏠 HOME
# ══════════════════════
if page == "🏠 Home":
   st.title("Welcome to My Website! 👋")
   st.write("Hi! My name is **Uwais Ruzali Rustam Aziz** and this is my personal website.")
   st.write("I made this as a school project to share a little bit about myself.")
   st.write("Use the sidebar on the left to explore the different pages! 😊")
   st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Abu_Dhabi_Skyline.jpg/1280px-Abu_Dhabi_Skyline.jpg",
            caption="Abu Dhabi - where I live 🇦🇪", use_container_width=True)

# ══════════════════════
# 👤 ABOUT ME
# ══════════════════════
elif page == "👤 About Me":
   st.title("About Me")

   st.subheader("Basic Info")
   st.write("- **Name:** Uwais Ruzali Rustam Aziz")
   st.write("- **Age:** 13 years old")
   st.write("- **Birthday:** January 1, 2013 🎂")
   st.write("- **School:** Al Manara School, MBZ, Abu Dhabi")
   st.write("- **Grade:** Grade 7")

   st.subheader("My Hobbies")
   st.write("I like a mix of a lot of things! Here are some of them:")
   st.write("- 🎬 Watching documentaries (especially from Fern on YouTube)")
   st.write("- 💻 Coding — I sometimes just randomly start a project")
   st.write("- ⚡ Arduino and ESP electronics")
   st.write("- 🔧 Figuring out how things work")



# ══════════════════════
# 🖼️ GALLERY
# ══════════════════════
elif page == "🖼️ Gallery":
   st.title("Gallery 🖼️")
   st.write("Here are some pictures from my life!")

   uploaded = st.file_uploader("Upload your photos here",
type=["jpg", "jpeg", "png"], accept_multiple_files=True)

   if uploaded:
       cols = st.columns(2)
       for i, f in enumerate(uploaded):
           with cols[i % 2]:
               st.image(f, use_container_width=True)
   else:
       st.info("No photos uploaded yet. Use the uploader above to add your pictures! 📸")

# ══════════════════════
# 🎮 FUN ZONE
# ══════════════════════
elif page == "🎮 Fun Zone":
   st.title("Fun Zone 🎮")
   st.write("Some fun stuff to do on my website!")

   # Quiz
   st.subheader("🧠 Quiz - How well do you know me?")

   questions = [
       {"q": "What city do I live in?", "opts": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"], "ans": "Abu Dhabi"},
       {"q": "What grade am I in?", "opts": ["Grade 5", "Grade 6",
"Grade 7", "Grade 8"], "ans": "Grade 7"},
       {"q": "When is my birthday?", "opts": ["Dec 31", "Jan 1", "Feb 14", "March 3"], "ans": "Jan 1"},
       {"q": "What type of videos do I like?", "opts": ["Pranks",
"Documentaries", "Cooking", "Sports"], "ans": "Documentaries"},
       {"q": "What electronics do I like?", "opts": ["Raspberry Pi",
"Arduino & ESP", "Only LEDs", "Nothing"], "ans": "Arduino & ESP"},
   ]

   score = 0
   for i, q in enumerate(questions):
       answer = st.radio(q["q"], q["opts"], index=None, key=f"q{i}")
       if answer == q["ans"]:
           st.success("✅ Correct!")
           score += 1
       elif answer is not None:
           st.error(f"❌ Wrong! The answer is {q['ans']}")

   st.write(f"**Your score: {score} / {len(questions)}**")

   st.divider()

   # Random fact
   st.subheader("⚡ Random Fact About Me")
   facts = [
       "I was born on New Year's Day 🎉",
       "My full name has 4 parts: Uwais Ruzali Rustam Aziz",
       "I once got an ESP board to work on my first try ⚡",
       "I can spend hours watching documentaries without getting bored",
       "I started coding just randomly one day and never stopped",
       "My dream is to be rich, happy and help others 💜",
       "I go to Al Manara School in Mohammed Bin Zayed City",
   ]
   if st.button("Show me a random fact!"):
       st.info(random.choice(facts))

# ══════════════════════
# 📬 CONTACT
# ══════════════════════
elif page == "📬 Contact":
   st.title("Contact 📬")
   st.write("Want to say hi or ask me something? Fill in the form below!")

   name = st.text_input("Your Name")
   message = st.text_area("Your Message")

   if st.button("Send Message"):
       if name and message:
           st.success(f"Thanks {name}! I got your message 😊")
       else:
           st.warning("Please fill in your name and message first!")

   st.divider()
   st.write("**About me:**")
   st.write("📍 Abu Dhabi, UAE")
   st.write("🏫 Al Manara School, Grade 7")
