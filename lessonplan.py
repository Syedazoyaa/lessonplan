import streamlit as st
import google.generativeai as genai

# Google Gemini API setup
genai.configure(api_key="AIzaSyDl2nIaYT9ef8vJ6NDhXnIOUj-Z_UmYfXU")
model = genai.GenerativeModel("gemini-1.0-pro")
chat = model.start_chat(history=[])

# Function to generate lesson plan using Gemini model
def generate_lesson_plan(topic, grade_level):
    msg = (f"Create a simple and practical lesson plan for the topic '{topic}' "
           f"for {grade_level} students. The plan should include: "
           f"1. A brief introduction to the topic, "
           f"2. The main learning objectives, "
           f"3. Key concepts to cover, "
           f"4. Teaching methods to use, "
           f"5. Suggested activities and assignments, "
           f"6. Ways to assess student understanding, "
           f"7. Additional resources with hyperlinks for further reading.")
    response = chat.send_message(msg, stream=True)
    return ''.join([chunk.text for chunk in response])  # Extract the text content from the response

# Streamlit UI
st.title("📚 Lesson Plan Generator")

st.markdown("### Enter the details below to generate a lesson plan:")

topic = st.text_input("Topic")
grade_level = st.selectbox("Class/Grade Level", ["Kindergarten", "1st Grade", "2nd Grade", "3rd Grade", "4th Grade", "5th Grade", "6th Grade", "7th Grade", "8th Grade", "High School", "College"])

if st.button("Generate Lesson Plan"):
    if topic and grade_level:
        lesson_plan = generate_lesson_plan(topic, grade_level)
        st.markdown("### 📝 Generated Lesson Plan")
        st.markdown(lesson_plan, unsafe_allow_html=True)
    else:
        st.error("Please enter both the topic and grade level.")
