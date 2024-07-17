import streamlit as st
import sqlite3
from langchain.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


st.title("TEXT-2-SQL using DB 🔁")
text = st.text_area("Please enter/paste your sql query in natural language to convert that into SQL Query:",height=100)

def sql_connection(sql,db):
    connection = sqlite3.connect(db,timeout=10)
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        cursor.commit()
        row = cursor.fetchall()
        print("row",row)
        for data in row:
            print(data)
    except sqlite3.Error as e:
        print("error",e)
    finally:
        cursor.close()
    
    

prompts = """
You are an expert in SQL and your task is to convert natural language queries into precise SQL code. Given the following natural language query, generate the corresponding SQL statement. The output should only include the SQL code without any additional text.
these are the table column name available in the employee table emp_name,emp_id,salary,bonus,dept_id.
Natural Language Query: "{text}"

SQL Code:

"""
    
def convertor(text,prompt):
    prompt_template = PromptTemplate.from_template(template=prompt)
    prompt = prompt_template.format(text=text)
    llm = Ollama(model='llama2',temperature = 0.5)
    response = llm(prompt)
    print("response",response)
    return response


convert = st.button("Convert")
if convert:
    response1 = convertor(text,prompts)
    response2 = sql_connection(response1,"data.db")
    for row in response2:
        print(row)
        st.header(row)

