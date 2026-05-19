import streamlit as st

# Title
st.title("🤖 HRM Expert Chatbot")

st.write("Ask me anything about Human Resource Management!")

# HRM Knowledge Base
hrm_data = {
    "recruitment": "Recruitment is the process of attracting, screening, and selecting qualified candidates for jobs.",

    "training": "Training improves employee knowledge, skills, productivity, and performance.",

    "performance appraisal": "Performance appraisal evaluates employee performance and helps in promotions, rewards, and development.",

    "compensation": "Compensation includes salary, incentives, bonuses, allowances, and benefits.",

    "employee engagement": "Employee engagement is the emotional commitment employees have toward their organization.",

    "hr analytics": "HR Analytics uses employee data and technology to improve HR decision-making.",

    "leadership": "Leadership is the ability to guide and influence employees toward organizational goals.",

    "talent management": "Talent management focuses on attracting, developing, and retaining talented employees.",

    "human resource management": "HRM is the strategic management of employees in an organization."
}

# User Input
user_input = st.text_input("Ask HR Question")

# Response Logic
if user_input:

    response = "Sorry, I currently answer only HRM-related topics."

    for topic in hrm_data:
        if topic in user_input.lower():
            response = hrm_data[topic]
            break

    st.success(response)