import streamlit as st
import pandas as pd
import os

# Set the title of the app
st.title("Community Shapers Feedback Form")

# Add a description or introduction
st.write("Welcome to the Community Shapers Feedback Form. Please fill out the form below to provide your valuable feedback.")

# Define the questions and their corresponding options
questions = [
    "This training is relevant to my needs and/or interests.",
    "I have learnt new skills and/or knowledge through this training.",
    "I can describe and explain what I learnt at this training to others.",
    "I can apply what I have learnt to improve my work and/or my organisation.",
    "This training will enable me to make positive changes to my organisation.",
    "Are you a repeat participant?",
    "When I apply what I learn, my clients and/or my community experience positive change.",
    "I am satisfied with the administrative and logistical support provided.",
    "I am satisfied with the quality of this training.",
    "My trainers were knowledgeable and professional.",
    "The training formats and learning activities were engaging and effective.",
    "The programme has been useful for building cross-cultural understanding through the sharing of perspectives, insights, know-how and/or experiences.",
    "The programme has been useful for building networks, connections and friendships with people from around the world.",
    "The programme has been useful for inspiring or bringing people around the world together to collaborate for good.",
    "I would recommend this programme to others.",
    "This programme has helped me gain a better understanding of Singapore or Singaporeans.",
    "This programme has inspired my interest in partnering with Singaporeans or Singapore institutions on collaborative initiatives and ventures.",
    "This programme has inspired my interest to visit Singapore."
]

# Options for the Likert scale questions
options = ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"]

def feedback_form():
    # Collect user inputs
    name = st.text_input("Name", key="name")
    email = st.text_input("Email", key="email")
    
    # Store responses in a dictionary
    responses = {}
    
    # Display the questions and collect responses
    for question in questions:
        if question == "Are you a repeat participant?":
            responses[question] = st.radio(question, ("Yes", "No"), key=question)
        else:
            responses[question] = st.radio(question, options, key=question)
    
    # Submit button
    if st.button("Submit", key="submit"):
        # Create a DataFrame to store the responses
        data = {
            "Name": [name],
            "Email": [email]
        }
        for question, response in responses.items():
            data[question] = [response]
        
        df = pd.DataFrame(data)
        
        # Save to CSV
        if not os.path.isfile("feedback.csv"):
            df.to_csv("feedback.csv", mode='a', index=False, header=True)
        else:
            df.to_csv("feedback.csv", mode='a', index=False, header=False)
        
        st.write("Thank you for your feedback!")
        
        # Clear form fields after submission
        st.experimental_rerun()

feedback_form()
