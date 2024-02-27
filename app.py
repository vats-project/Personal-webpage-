import streamlit as st
from PIL import Image

def display_personal_details():
    st.subheader("Personal Details")
    # Display your photo. Replace 'your_photo.png' with the path to your image file.
    st.image("your_photo.png", caption='Vats Balar', width=150)
    st.write("**Name:** Vats Balar")
    st.write("**Age:** 21")
    st.write("**Field of Interest:** AI")

def display_social_links():
    st.subheader("Social Accounts")
    st.markdown("[Instagram](https://www.instagram.com/your_instagram_username/)")
    st.markdown("[Snapchat](https://www.snapchat.com/add/your_snapchat_username)")
    st.markdown("[GitHub](https://github.com/your_github_username)")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/your_linkedin_username)")

def display_education_and_courses():
    st.subheader("Education & Courses")
    st.write("- Bachelor's degree in Computer Science")
    st.write("- Machine Learning Specialization, Coursera")
    st.write("- Deep Learning Specialization, Coursera")

def display_skills_and_projects():
    st.subheader("Skills & Projects")
    st.write("**Skills:** Python, Machine Learning, Deep Learning, NLP, Computer Vision")
    st.write("**Projects:**")
    st.markdown("1. **Sentiment Analysis with Machine Learning:** Analyzed sentiments from text data.")
    st.markdown("2. **Image Classification using CNNs:** Implemented a CNN model to classify images.")
    st.markdown("3. **Chatbot Development with NLP:** Built a conversational AI chatbot.")

def main():
    st.title("👨‍💻 Vats Balar - AI Enthusiast")

    # Sidebar for navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Personal Details", "Social Accounts", "Education & Courses", "Skills & Projects"])

    if page == "Personal Details":
        display_personal_details()
    elif page == "Social Accounts":
        display_social_links()
    elif page == "Education & Courses":
        display_education_and_courses()
    elif page == "Skills & Projects":
        display_skills_and_projects()

    st.sidebar.markdown("---")
    st.sidebar.info("Thank you for visiting my app. Feel free to connect with me through the social links provided.")

if __name__ == "__main__":
    main()
