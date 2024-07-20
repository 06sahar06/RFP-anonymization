import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

chat = ChatGroq(
    temperature=0,
    model="llama3-70b-8192",
    api_key="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" 
)

system = "You will be provided with RFP texts (job descriptions) from a client, and your task is to anonymize the content by removing any details related to the company, such as the company's name, department, and contact information. The anonymized text should retain all essential job requirements, qualifications, and responsibilities while ensuring that no identifying company-specific information"
human = "{text}"
prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])

chain = prompt | chat

st.title("ChatGroq Assistant")

user_input = st.text_input("Enter an RFP text:")

# Button to invoke the chain
if st.button("Get Response"):
    if user_input:
        # Invoke the chain with the user's input
        response = chain.invoke({"text": user_input})
        content = response.content

        st.write("Response:", content)
    else:
        st.write("Please enter some text.")

