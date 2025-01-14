import streamlit as st
import pandas as pd
import datetime

# Title and description
st.title("Workplace Placement Application Use For Reverse Engineering and Fast Prototyping For Design Of Workplace Job Placement Services Automation")
st.markdown("Welcome to the Workplace Placement Application. Please fill in the form below to apply for your desired placement.")
st.markdown("\n**CareerForce Overview**\n\nCareerForce is the State of Minnesota's official resource for career exploration and job search assistance. It offers a variety of services aimed at helping individuals find meaningful employment and develop their careers.\n\n**Services Provided:**\n- **Job Search Assistance:** One-on-one guidance, access to job listings, and employer connections.\n- **Career Counseling:** Personalized advice for youth (14-24) and others to achieve work or education goals.\n- **Training Programs:** Free career training, technical skill development, and workshops on job search strategies.\n- **Networking Opportunities:** Career fairs, events, and professional networking sessions.\n- **Specialized Programs:** Support for dislocated workers, veterans, and individuals with employment barriers.\n- **Support Services:** Assistance with childcare, housing, transportation, and access to labor market information.\n- **Virtual and In-Person Services:** Accessible both online and at various locations across Minnesota.\n\nCareerForce empowers individuals with the tools and support to secure long-term, family-sustaining wages through effective job placement and career development strategies.")

# Form for user input
with st.form(key="placement_form"):
    st.header("Application Form")

    # Personal Details
    full_name = st.text_input("Full Name", placeholder="Enter your full name")
    email = st.text_input("Email", placeholder="Enter your email address")
    phone = st.text_input("Phone Number", placeholder="Enter your phone number")

    # Skills and Interests
    skills = st.text_area("Skills", placeholder="List your relevant skills (e.g., Python, Data Analysis, Communication)")
    placement_type = st.selectbox(
        "Type of Placement", 
        ["Internship", "Part-Time", "Full-Time", "Project-Based"]
    )

    # Availability
    start_date = st.date_input("Start Date", min_value=datetime.date.today())
    end_date = st.date_input("End Date", min_value=start_date)

    # Additional Information
    additional_info = st.text_area("Additional Information", placeholder="Share any other details or preferences for your placement.")

    # Submit Button
    submit_button = st.form_submit_button(label="Submit Application")

# Process the form submission
if submit_button:
    if not full_name or not email or not phone or not skills:
        st.error("Please fill in all the required fields.")
    else:
        st.success("Thank you for your application! We will review your details and get back to you.")

        # Save application details (example: displaying it as a dataframe)
        application_data = {
            "Full Name": [full_name],
            "Email": [email],
            "Phone Number": [phone],
            "Skills": [skills],
            "Placement Type": [placement_type],
            "Start Date": [start_date],
            "End Date": [end_date],
            "Additional Information": [additional_info]
        }

        df = pd.DataFrame(application_data)
        st.dataframe(df)
