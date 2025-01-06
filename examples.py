
examples = [
    {
        "input": "Count of customerID where total >20",
        "query": "select count(*) from Invoice where Total >20;"
    },
    {
        "input": "List out the customerID from Brazil",
        "query": "select CustomerId from Customer where country = 'Brazil';"
    },
    {
        "input": "Total number of Albhums",
        "query": "select count(*) from Album;"
    },
    {
        "input": "List out the firstName & LastName of the employees belongs to IT-Staff",
        "query": "select FirstName,LastName from Employee where Title = 'IT Staff';"
    },
    {
        "input": "How many number of Media types are available",
        "query": "select count(*) from MediaType;"
    },
    {
     'input':"List of customer's first name belongs to Germany",
     "query": "select  DISTINCT a.FirstName from Customer a, Invoice b where a.CustomerId = b.CustomerId and b.BillingCountry ='Germany';"
    }
]


from langchain_community.vectorstores import Chroma
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain_openai import OpenAIEmbeddings
import streamlit as st

@st.cache_resource
def get_example_selector():
    example_selector = SemanticSimilarityExampleSelector.from_examples(
        examples,
        OpenAIEmbeddings(),
        Chroma,
        k=2,
        input_keys=["input"],
    )
    return example_selector