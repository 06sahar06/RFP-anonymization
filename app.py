import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

chat = ChatGroq(
    temperature=0,
    model="llama3-70b-8192",
    api_key="insert your api key here" 
)

system = '''Your task is to anonymize Request for Proposal (RFP) text containing job descriptions. Follow these guidelines:

                                    Remove all identifying information, including but not limited to:

                                    Company name and any variations or abbreviations
                                    Department names
                                    Contact information (email addresses, phone numbers, physical addresses)
                                    Names of specific individuals or teams
                                    Proprietary product names or trademarked terms
                                    Industry-specific jargon that could identify the company
                                    Unique company initiatives or programs


                                    Retain all essential job-related information, such as:

                                    Job title (unless it's company-specific)
                                    Required qualifications and skills
                                    Job responsibilities and duties
                                    Experience requirements
                                    Education requirements
                                    Desired soft skills


                                    Replace specific identifiers with generic terms:

                                    Use "[Company]" instead of the actual company name
                                    Use "[Department]" for department names
                                    Use "[Product]" for specific product names


                                    Maintain the overall structure and flow of the original text.
                                    Ensure the anonymized version remains coherent and professionally worded.
                                    If certain details are crucial but potentially identifying, generalize them. For example, "Fortune 500 tech company" instead of the specific company name.
                                    Review the final text to confirm all identifying information has been removed while preserving the essence of the job description.
                                    If you're unsure about a particular detail, err on the side of caution and remove or generalize it.
                                    Don't start with any introductory phrase, just start with the anonymized text.

                                    Please process the provided RFP text according to these guidelines and present the anonymized version.'''
human = "{text}"
prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])

chain = prompt | chat

st.title("ChatGroq Assistant")

user_input = st.text_input("Enter an RFP text:")

if st.button("Get Response"):
    if user_input:
        response = chain.invoke({"text": user_input})
        content = response.content

        st.write("Response:", content)
    else:
        st.write("Please enter some text.")

