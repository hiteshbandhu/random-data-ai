import openai
import streamlit as st
import os
openai.api_key = st.secrets['pass']

st.header("Generate Random Data, Powered by AI !")

st.set_page_config(page_title="RanData😶")

extension = st.selectbox("Pick Extension",["JSON","CSV","MD"])
columns = st.text_input("Enter Keys/Columns To Be Included : ")
number = st.text_input("Enter Sample Size (<=100) : ")

system_prompt = f""" Don't output any explanations, only output the code. I want to make a project, for which i require random user data. Generate me random user data, the format for which will be given below. Make sure, the data is really random and is recyclable, that is, i can use it in another project also. Output only the below,nothing more, not even explanations or supportive sentences :

Extension : ```extension```
Keys/Columns : ```columns```

Generate me data for ```number``` users. Don't output code to generate, i need raw data. I will provide the format and keys in the user prompt."""

prompt = f"Extension : {extension}, Keys : {columns}, Number : {number}"

def code_gen(prompt,temperature=0) :
    response= openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt}
    ],
    temperature = 0.5
    )
    return response.choices[0].message.content

if st.button("Generate Data"):
    with st.spinner("Generating..."):
        final_code = code_gen(prompt)
        st.success("Done Generating !")

    st.text_area("Your Dataset", final_code,
                     height=500)


        



