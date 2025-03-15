import streamlit as st
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from portfolio_classification import main

# Set page config
st.set_page_config(page_title="Portfolio Classification", layout="wide")

# Run the main function from portfolio_classification
main() 