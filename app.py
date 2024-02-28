import streamlit as st
import pandas as pd  # Add this import statement

# Options in the sidebar for navigation
option = st.sidebar.selectbox(
    "Select an option", 
    ["Personal Information", "Education", "My Certificates", "Projects", "Skills"]
)

import streamlit as st
import pandas as pd

# Set page title
st.set_page_config(page_title="Resume Dashboard", page_icon="🚀", layout="wide")
# Custom sidebar title with border and box shadow using markdown
st.sidebar.markdown("""
    <h1 style="
        text-align: center; 
        color: #FFFFFF; 
        margin-bottom: 1rem; 
        border: 2px solid #FFD700; 
        padding: 10px; 
        border-radius: 10px; 
        box-shadow: 0 4px 8px 0 rgba(255, 215, 0, 0.2), 0 6px 20px 0 rgba(255, 215, 0, 0.19);
        background-color: #000000;
        ">
        Digital Resume 
    </h1>
""", unsafe_allow_html=True)

# Custom HTML and CSS for the header
header_html = """
    <div style="
        background-color: #333333; 
        padding: 10px 20px; 
        border-bottom: 4px solid #007BFF;
        border-top: 4px solid #007BFF;
        margin-bottom: 25px;
        text-align: center;
        box-shadow: 0 4px 8px rgba(255, 255, 255, 0.4);
        ">
        <h1 style="
            color: #FFFFFF; 
            margin: 0;
            padding: 0;
            font-size: 36px;
            font-weight: bold;
            ">Digital Resume Dashboard</h1>
    </div>
"""
# Display the custom header
st.markdown(header_html, unsafe_allow_html=True)

# Add your photo in a round shape with a border using HTML and CSS
st.sidebar.markdown(
    """
    <style>
        /* Apply circular shape and border to the image */
        img {
            border-radius: 50%;
            width: 100px;
            height: px;
            object-fit: cover;
            border: 3px solid #FFD700;
            box-shadow: 0 4px 8px 0 rgba(255, 215, 0, 0.2), 0 6px 20px 0 rgba(255, 215, 0, 0.19);
        }
    </style>
    """
    , unsafe_allow_html=True
)
# st.sidebar.image("my.jpg", use_column_width=True)

#this diff
st.sidebar.markdown(
    """
    <style>
        .info-div {
            text-align: center;
            padding: 20px;
            color: #FFFFFF;
            border: 2px solid #FFD700;
            background-color: #000000;
            margin-bottom: 25px;
            border-radius: 10px;
            box-shadow: 0 4px 8px 0 rgba(255, 215, 0, 0.2), 0 6px 20px 0 rgba(255, 215, 0, 0.19);
        }
        .name {
            font-size: 22px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .role {
            font-size: 18px;
            font-weight: normal;
            font-style: normal;
            margin-top: 10px;
        }
    </style>
    <div class="info-div">
        <div class="name">VATS BALAR</div>
        <div class="role">AI & ML Developer <br> MLOps Enthusiast</div>
    </div>
    """,
    unsafe_allow_html=True
)


st.subheader("Welcome to my personal webpage")

#this diff
# Options in the sidebar for navigation
option = st.sidebar.selectbox(
    "Select an option", 
    ["Personal Information", "Education", "My Certificates", "Projects", "Skills"]
)

# Apply CSS styling to mimic the provided style for the sidebar selectbox
st.markdown(
    """
    <style>
        /* General styling for the sidebar select box, attempting to mimic the .info-div style */
        div[data-baseweb="select"] {
            color: #FFFFFF !important; /* White text color */
            background-color: #000000 !important; /* Black background color */
            border: 2px solid #FFD700 !important; /* Yellow border */
            border-radius: 10px !important;
            padding: 20px !important;
            box-shadow: 0 4px 8px 0 rgba(255, 215, 0, 0.2), 0 6px 20px 0 rgba(255, 215, 0, 0.19) !important;
        }
        
        /* Attempting to style the dropdown items, though direct access may be limited */
        div[data-baseweb="select"] > div {
            background-color: #000000 !important; /* Black background for items */
            color: #FFFFFF !important; /* White text color for items */
        }
    </style>
    """,
    unsafe_allow_html=True
)


# Assuming 'option' is your variable from the sidebar selection
if option == "Personal Information":
    st.header("Personal Information")
    st.write("Location: Surat, Gujrat")
    st.write("Contact No: +91 8306662624")
    st.write("Gmail: balarvats3@gmail.com")

    st.markdown(
        """
        <style>
            .personal-info {
                margin-bottom: 20px;
                padding: 15px;
                border: 2px solid #007BFF; /* Blue border */
                border-radius: 10px;
                background-color: #333333; /* Dark background */
                color: #FFFFFF; /* Text color */
                box-shadow: 0 4px 8px rgba(255, 255, 255, 0.4); /* White shadow */
            }
            .personal-info a {
                color: #007BFF; /* Link color */
                text-decoration: none;
            }
            .personal-info a:hover {
                color: #0056b3; /* Darker shade for hover effect */
            }
        </style>

        <div class="personal-info">
            <div style="margin-top: 10px;">
                <p><strong>Social Media Accounts:</strong></p>
                <ul style="list-style-type: none; padding-left: 0;">
                    <li><strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/vatsbalar/" target="_blank">Your LinkedIn Profile</a></li>
                    <li><strong>GitHub:</strong> <a href="https://github.com/vatsbalar22" target="_blank">Your GitHub Profile</a></li>
                    <li><strong>Instagram:</strong> <a href="https://www.instagram.com/l_______.b.a.l.a.r._______l/" target="_blank">Your Instagram Profile</a></li>
                    <li><strong>Snapchat:</strong>vats_balar</li>
                </ul>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


elif option == "Education":
    st.header("Education")

    # University Education
    st.markdown(
        """
        <div class="education-container">
            <h3>University Education</h3>
            <p>B.Tech in CSE with a specialization in ML and AI</p>
            <p>Graduated from P.P. Savani University in 2024</p>
        </div>
        """, unsafe_allow_html=True
    )

    # High School Education
    st.markdown(
        """
        <div class="education-container">
            <h3>High School Education</h3>
            <p>Science A Group</p>
            <p>Ashadeep Vidhyalay, Class of 2020</p>
        </div>
        """, unsafe_allow_html=True
    )

    # Apply CSS styling to the education section
    st.markdown(
        """
        <style>
            .education-container {
                margin-bottom: 20px;
                padding: 10px;
                border: 2px solid #007BFF; /* Blue border */
                border-radius: 10px;
                background-color: #333333; /* Dark background */
                color: #FFFFFF; /* Text color */
                box-shadow: 0 4px 8px rgba(255, 255, 255, 0.4); /* White shadow */
            }
            .education-container h3 {
                color: #FFD700; /* Gold color for subheaders */
            }
        </style>
        """, unsafe_allow_html=True
    )



elif option == "My Certificates":
    st.header("My Certificates")

    # Custom CSS for styling the certificates section
    st.markdown(
        """
        <style>
            .certificate-container {
                margin-bottom: 20px;
                padding: 10px;
                border: 2px solid #007BFF; /* Blue border */
                border-radius: 10px;
                background-color: #333333; /* Dark background */
                color: #FFFFFF; /* Text color */
                box-shadow: 0 4px 8px rgba(255, 255, 255, 0.4); /* White shadow */
            }
            .certificate-container h3 {
                color: #FFFFFF; /* Gold color for subheaders */
            }
            .certificate-container p, .certificate-container a {
                color: #FAEA4E; /* White text color */
            }
            .certificate-container a {
                color: #81F7EE; /* Green color for links */
            }
        </style>
        """, unsafe_allow_html=True
    )

    # Certificate in Machine Learning
    st.markdown(
        """
        <div class="certificate-container">
            <h3>DevOps, DataOps, MLOps</h3>
            <p>Organization: Duke University | Coursera</p>
            <p><a href="https://coursera.org/share/6966f774a463df5121ab9de42bfb4955" target="_blank">Certificate link</a></p>
        </div>
        """, unsafe_allow_html=True
    )

    # AWS Certified Developer - Associate
    st.markdown(
        """
        <div class="certificate-container">
            <h3>Deep Learning Specialization</h3>
            <p>Organization: DeepLearning.AI</p>
            <p><a href="https://coursera.org/share/5846ca0e1e35ec3d4f132dbd250732b1" target="_blank">Certificate link</a></p>
        </div>
        """, unsafe_allow_html=True
    )
    st.markdown(
        """
        <div class="certificate-container">
            <h3>IBM Data Science Specialization</h3>
            <p>Organization: IBM</p>
            <p><a href="https://www.coursera.org/account/accomplishments/specialization/AS2V6MF64432" target="_blank">Certificate link</a></p>
        </div>
        """, unsafe_allow_html=True
    )
    st.markdown(
        """
        <div class="certificate-container">
            <h3>AI For Everyone </h3>
            <p>Organization: DeepLearning.AI</p>
            <p><a href="https://coursera.org/share/46b8fb8a19237581129a7382632a4f30" target="_blank">Certificate link</a></p>
        </div>
        """, unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="certificate-container">
            <h3>Excel for Data Analysis Course</h3>
            <p>Organization: LearnVern</p>
            <p><a href="https://drive.google.com/file/d/1eS1nL849CPBaM0s0QNjdVrxxOTwyi0-q/view?usp=sharing" target="_blank">Certificate link</a></p>
        </div>
        """, unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="certificate-container">
            <h3>AWS Academy Graduate - AWS Academy Cloud Foundations</h3>
            <p>Organization: Amazon Web Services (AWS)</p>
            <p><a href="https://drive.google.com/file/d/1L2HtUXGlbg_7fu1xIrmgMAnm6YG_9-Wj/view?usp=sharing" target="_blank">Certificate link</a></p>
        </div>
        """, unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="certificate-container">
            <h3>Extended Reality for Everybody</h3>
            <p>Organization: University of Michigan</p>
            <p><a href="https://coursera.org/share/7268d4ea894ec810b74212576eb2bcc3" target="_blank">Certificate link</a></p>
        </div>
        """, unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="certificate-container">
            <h3>Tableau for Beginners</h3>
            <p>Organization: Great Learning</p>
            <p><a href="https://drive.google.com/file/d/1Kx26RLpVQW42PPiJ2-O87vKtMRvV1ztC/view?usp=sharing" target="_blank">Certificate link</a></p>
        </div>
        """, unsafe_allow_html=True
    )
    # Add more certificates here using the same div structure


elif option == "Projects":
    st.header("Projects")

    projects_data = [
        {"Project Name": "Stock-prediction-ML-DL-MLOps-Flask ", "Description": "Stock price prediction model", "GitHub Link": "https://github.com/vatsbalar22/Stock-prediction-ML-DL-MLOps-Flask"},
        {"Project Name": "MLOps-function-from-zero ", "Description": "MLOps make pipline of CI and CD", "GitHub Link": "https://github.com/vatsbalar22/MLOps-function-from-zero"},
        {"Project Name": "MLOps-function-FastAPI-docker", "Description": "Model deployement using Dockerfile in AWS", "GitHub Link": "https://github.com/vatsbalar22/MLOps-function-FastAPI-docker"},
        # Add more projects as needed
        # {"Project Name": "Project 4", "Description": "Your project description.", "GitHub Link": "[Project 4](https://github.com/your-username/project-4)"},
    ]

    # Custom CSS for styling the projects table
    st.markdown(
        """
        <style>
            .project-container {
                margin-bottom: 20px;
                padding: 10px;
                border: 2px solid #007BFF; /* Blue border */
                border-radius: 10px;
                background-color: #333333; /* Dark background */
                color: #FFFFFF; /* Text color */
                box-shadow: 0 4px 8px rgba(255, 255, 255, 0.4); /* White shadow */
            }
            .project-container h3 {
                color: #FFFFFF; /* Gold color for subheaders */
            }
            .project-container p, .project-container a {
                color: #FAEA4E; /* White text color */
            }
            .project-container a {
                color: #81F7EE; /* Green color for links */
            }
        </style>
        """, unsafe_allow_html=True
    )

    # Display each project in a container
    for project in projects_data:
        st.markdown(
            f"""
            <div class="project-container">
                <h3>{project['Project Name']}</h3>
                <p>{project['Description']}</p>
                <p><a href="{project['GitHub Link']}" target="_blank">GitHub Link</a></p>
            </div>
            """, unsafe_allow_html=True
        )

elif option == "Skills":
    st.header("Skills")

    skills_data = [
        {"Category": "Programming Languages", "Skills": "Python, Java, C++"},
        {"Category": "Machine Learning", "Skills": "Scikit-learn, TensorFlow, PyTorch"},
        {"Category": "Web Technologies", "Skills": "HTML, CSS, JavaScript"},
        {"Category": "Database", "Skills": "SQL, MongoDB"},
        # Add more skills categories as needed
        # {"Category": "Category Name", "Skills": "Skill1, Skill2, Skill3"},
    ]

    # Apply CSS styling to the skills table with a red border and shadow box
    st.markdown(
        """
        <style>
            table {
                border-collapse: collapse;
                width: 100%;
                margin-top: 15px;
                border: 2px solid #FF0000; /* Red border */
                border-radius: 10px;
                box-shadow: 0 4px 8px 0 rgba(255, 0, 0, 0.2), 0 6px 20px 0 rgba(255, 0, 0, 0.19); /* Red shadow box */
            }
            th, td {
                border: 1px solid #FFFFFF; /* Table border color */
                padding: 10px;
                text-align: left;
                background-color: #1E1E1E; /* Dark background color */
                color: #FFFFFF; /* Text color */
            }
            tr:nth-child(even) {
                background-color: #333333; /* Darker background color for even rows */
            }
            tr:hover {
                background-color: #2E2E2E; /* Darker background color for hovered row */
            }
        </style>
        """, unsafe_allow_html=True
    )

    # Display skills in a table without the index column
    st.table(pd.DataFrame(skills_data).set_index('Category'))





