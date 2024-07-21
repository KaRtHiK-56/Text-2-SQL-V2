## Natural Language to SQL: AI-Powered Text-to-SQL Query Engine

### Table of Contents
1. **Introduction**
2. **Problem Statement**
3. **Problem Outline**
4. **Business Solution**
5. **Technical Solution**
   - Architecture
   - Components
   - Implementation Details
6. **Usage Instructions**
   - Prerequisites
   - Setup
   - Running the Application
7. **Future Enhancements**
8. **Conclusion**

---

### 1. Introduction
This documentation provides a comprehensive overview of the generative AI text-to-SQL solution developed to facilitate seamless database querying using natural language. Leveraging cutting-edge technologies such as Streamlit, LangChain, Python, and Llama 3, this solution converts user queries into SQL statements and retrieves the relevant data from the database.

### 2. Problem Statement
Business users often require access to data stored in databases but lack the technical skills to write complex SQL queries. This gap creates a dependency on technical teams and delays the decision-making process.

### 3. Problem Outline
- **Non-technical Users:** Difficulty in writing SQL queries.
- **Dependency:** Relying on technical staff for data retrieval.
- **Efficiency:** Time-consuming process for data extraction.
- **Decision-making:** Delayed business insights due to the above challenges.

### 4. Business Solution
The generative AI text-to-SQL solution addresses these issues by enabling non-technical users to query databases using natural language. This reduces dependency on technical teams, accelerates data retrieval, and enhances the decision-making process.

### 5. Technical Solution

#### Architecture
The solution architecture comprises the following components:
- **User Interface:** Streamlit application for user interaction.
- **Query Analyzer:** LangChain model to interpret natural language queries.
- **SQL Generator:** Llama 3 model to convert analyzed queries into SQL statements.
- **Database Connector:** Python module to execute SQL queries on the database.
- **Response Handler:** Displays the retrieved data to the user.

#### Components
1. **Streamlit:** Provides an interactive web interface for users to input queries and view results.
2. **LangChain:** Analyzes the user's natural language query.
3. **Llama 3:** Generates the corresponding SQL query.
4. **Python:** Facilitates the integration and execution of components.
5. **Database:** Stores the data and processes SQL queries.

#### Implementation Details
- **Query Input:** Users input their natural language query via the Streamlit interface.
- **Query Analysis:** LangChain model interprets the query's intent and key entities.
- **SQL Generation:** Llama 3 converts the analyzed query into a valid SQL statement.
- **Query Execution:** Python module executes the SQL query against the database.
- **Data Retrieval:** Retrieved data is displayed to the user via the Streamlit interface.

### 6. Usage Instructions

#### Prerequisites
- Python 3.8 or higher
- Streamlit
- LangChain
- Llama 3
- Database connection details (e.g., PostgreSQL, MySQL)


### 7. Future Enhancements
- **Enhanced Natural Language Understanding:** Improving the LangChain model for better query interpretation.
- **Support for Multiple Databases:** Extending support to various database systems.
- **Advanced Query Handling:** Including support for complex queries involving joins, subqueries, and aggregations.
- **User Authentication:** Adding user authentication and authorization mechanisms.

### 8. Conclusion
The generative AI text-to-SQL solution bridges the gap between non-technical users and database querying, providing a robust, efficient, and user-friendly interface for data retrieval. By leveraging advanced AI models, this solution significantly enhances business operations and decision-making processes.

## Acknowledgements

 - [Langchain](https://www.langchain.com/)
 - [Ollama](https://ollama.com/)
 - [Llama-3](https://ollama.com/library/llama3)


## Authors

- [@Github](https://www.github.com/KaRtHiK-56)
- [@LinkedIn](https://www.linkedin.com/in/l-karthik/)


## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)

![MIT License](https://img.shields.io/badge/License-MIT-green.svg)


## Demo

https://github.com/KaRtHiK-56/Text-2-SQL-V2


## Documentation

 - [Langchain](https://www.langchain.com/)
 - [Ollama](https://ollama.com/)
 - [Llama-3](https://ollama.com/library/llama3)

## Technology used

### Backend
- **LangChain:** For chaining together various AI models and processing workflows.
- **Llama 3 Model:** A state-of-the-art language model used for generating human-like text.
- **Python:** The primary programming language for implementing the application logic.

### Frontend
- **Streamlit:** An open-source app framework used for creating the web interface.

## Installation

#### Setup
1. **Clone the Repository:**
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```
2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure Database Connection:**
   Update the database connection settings in the `config.py` file.

#### Running the Application
1. **Start the Streamlit Application:**
   ```bash
   streamlit run app.py
   ```
2. **Enter Query:**
   Navigate to the Streamlit URL, enter your natural language query, and click "Submit".
3. **View Results:**
   The application will display the retrieved data.
