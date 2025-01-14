import streamlit as st
import pandas as pd
import datetime

# Title and description
st.title("Workplace Placement Application")
st.markdown("Welcome to the Workplace Placement Application. Please fill in the form below to apply for your desired placement.")
st.markdown(
    """
    **CareerForce Overview**

    CareerForce is the State of Minnesota's official resource for career exploration and job search assistance. 
    It offers a variety of services aimed at helping individuals find meaningful employment and develop their careers.

    **Services Provided:**
    - **Job Search Assistance:** One-on-one guidance, access to job listings, and employer connections.
    - **Career Counseling:** Personalized advice for youth (14-24) and others to achieve work or education goals.
    - **Training Programs:** Free career training, technical skill development, and workshops on job search strategies.
    - **Networking Opportunities:** Career fairs, events, and professional networking sessions.
    - **Specialized Programs:** Support for dislocated workers, veterans, and individuals with employment barriers.
    - **Support Services:** Assistance with childcare, housing, transportation, and access to labor market information.
    - **Virtual and In-Person Services:** Accessible both online and at various locations across Minnesota.

    CareerForce empowers individuals with the tools and support to secure long-term, family-sustaining wages 
    through effective job placement and career development strategies.
    """
)

# CareerForce services and sub-options
careerforce_services = {
    "Job Search Assistance": [
        "One-on-one guidance",
        "Access to job listings",
        "Employer connections"
    ],
    "Career Counseling": [
        "Personalized advice for youth (14-24)",
        "Help to achieve work goals",
        "Help to achieve education goals"
    ],
    "Training Programs": [
        "Free career training",
        "Technical skill development",
        "Workshops on job search strategies"
    ],
    "Networking Opportunities": [
        "Career fairs",
        "Events",
        "Professional networking sessions"
    ],
    "Specialized Programs": [
        "Support for dislocated workers",
        "Support for veterans",
        "Support for individuals with employment barriers"
    ],
    "Support Services": [
        "Assistance with childcare",
        "Assistance with housing",
        "Assistance with transportation",
        "Access to labor market information"
    ],
    "Virtual and In-Person Services": [
        "Accessible online",
        "Services at various locations in Minnesota"
    ]
}

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

    # CareerForce Parent Services
    parent_selection = st.multiselect(
        "Select CareerForce Services of Interest:",
        list(careerforce_services.keys())
    )

    # CareerForce Sub-Options
    selected_services = {}
    if parent_selection:
        st.subheader("Select Specific Sub-Options for Chosen Services:")
        for parent in parent_selection:
            sub_options = st.multiselect(
                f"Select sub-options for {parent}:",
                careerforce_services[parent]
            )
            selected_services[parent] = sub_options

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

        # Combine selected services into a formatted string
        formatted_services = {
            parent: ", ".join(subs) for parent, subs in selected_services.items()
        }

        # Save application details (example: displaying it as a dataframe)
        application_data = {
            "Full Name": [full_name],
            "Email": [email],
            "Phone Number": [phone],
            "Skills": [skills],
            "Placement Type": [placement_type],
            "Selected Services": [str(formatted_services)],
            "Start Date": [start_date],
            "End Date": [end_date],
            "Additional Information": [additional_info]
        }

        df = pd.DataFrame(application_data)
        st.dataframe(df)
