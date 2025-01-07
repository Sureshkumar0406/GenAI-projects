**Text-to-SQL-to-Text Streamlit Application**

This repository demonstrates how to implement a Text-to-SQL model using Langchain and deploy it on a Streamlit interface.
Basically, it contains a Streamlit-based application that enables natural language interaction with a SQLite database where data has been stored.
Users can ask questions in plain English, and the app generates SQL queries to retrieve data from the database. 
The responses are then presented in user-friendly text format.
The solution leverages the LangChain ecosystem for handling text-to-SQL generation and integrates LangSmith for tracking and debugging purposes.

## Project Structure

- **app.py**: The main Streamlit app that deploys the model interface for user interaction.
- **chinook-db.db**: SQLite database used to store data for querying. It serves as the backend for the SQL generation process.
- **create_db.py**: Contains code for creating the SQLite database (`chinook-db.db`) and loading sample data into it.
- **database_table_descriptions.csv**: A CSV file containing a list of tables and their descriptions, providing context for the tables in the database.
- **examples.py**: Includes sample code for few-shot prompt templates to generate SQL queries based on example inputs.
- **langchain_utils.py**: Code that handles connecting to the database, rephrasing the output from the LLM, and adding chat history to the LLM to provide more accurate responses to user queries.
- **prompts.py**: Contains the few-shot prompt templates, examples, and final prompts used to guide the model in generating SQL queries.
- **table_details.py**: Implements logic to fetch relevant tables for a given query and assist in constructing the appropriate SQL query.

## Features

- **Natural Language Input**: Users can interact with the model by typing natural language queries into the Streamlit interface.
- **SQL Query Generation**: The LLM (Language Model) processes the natural language input and generates an SQL query.
- **Database Interaction**: SQL queries are executed on an SQLite database (Chinook), and results are displayed to the user.
- **Few-Shot Learning**: The model leverages few-shot prompt engineering to generate accurate SQL queries for diverse use cases.
- **Chat History**: The model considers previous interactions to improve its responses and generate more contextually relevant SQL queries.

**Technology Stack**

Python: Core programming language.

Streamlit: Frontend framework for building the interactive web app.

LangChain: Framework for LLM-based applications.

LangSmith: Monitoring and debugging toolkit for LangChain applications.

SQLite: Example database used (Chinook DB).

**Prerequisites**

Python 3.8+: Ensure Python is installed on your system.

Chinook Database: Download the Chinook SQLite database (chinook.db).

OpenAI API Key: Required for using the LLM for SQL generation.

**Installation**

Clone the Repository:

git clone https://github.com/Sureshkumar0406/GenAI-projects.git
cd text-to-sql-app

**Create a Virtual Environment:**

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

**Install Dependencies:**

pip install -r requirements.txt

**Set Environment Variables:**
Create a .env file in the root directory and add the following:

OPENAI_API_KEY=your_openai_api_key
LANGSMITH_API_KEY=your_langsmith_api_key

**Place the Chinook Database:**
Ensure the chinook.db file is in the root directory of the project.

Usage

**Run the Application:**

streamlit run app.py

**Interact with the App:**

Enter your natural language question in the input box.

The app generates a SQL query, executes it, and displays the result.

**Track Queries Using LangSmith:**

Access the LangSmith dashboard to monitor chain performance, inspect logs, and debug issues.
