**Text-to-SQL-to-Text Streamlit Application**

This repository contains a Streamlit-based application that enables natural language interaction with a database. 
Users can ask questions in plain English, and the app generates SQL queries to retrieve data from the database. 
The responses are then presented in user-friendly text format.
The solution leverages the LangChain ecosystem for handling text-to-SQL generation and integrates LangSmith for tracking and debugging purposes.

**Features**

Natural Language to SQL Conversion: Convert plain English questions into SQL queries.

Streamlit Interface: A user-friendly and interactive web application for querying and visualizing data.

LangChain Integration: Utilize LangChain components for LLM-based SQL generation.

LangSmith Tracking: Track and debug queries, responses, and chain performance.

Database Support: Designed to work with the Chinook sample database, but extensible to other SQL databases.

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

Directory Structure

.
├── app.py                  # Main Streamlit application
├── langchain_utils.py      # Helper functions for LangChain operations
├── requirements.txt        # Python dependencies
├── chinook.db              # Sample SQLite database
├── .env                    # Environment variables
└── README.md               # Project documentation

**Key Components**

LangChain SQL Chain: Handles the conversion of natural language to SQL queries.

LangSmith Integration: Tracks each query, allowing you to debug and improve model performance.

Streamlit UI: Provides an easy-to-use interface for users to interact with the database.

**Example**

Input:

How many employees are there in the database?

SQL Query:

SELECT COUNT(EmployeeId) AS EmployeeCount FROM Employee;

Output:

There are 8 employees in the database.

**Troubleshooting**

Slow App Performance:

Ensure @st.cache_resource is used for resource-intensive operations.

Optimize database queries and embeddings.

**LangSmith Integration Errors:**

Verify the LANGSMITH_API_KEY is set correctly in the .env file.

Ensure you have the latest version of LangSmith installed.

**Database Connection Issues:**

Confirm that chinook.db is in the correct location.

Check for proper database driver installation.


**Acknowledgments**

LangChain Documentation

Streamlit Documentation

Chinook Database
