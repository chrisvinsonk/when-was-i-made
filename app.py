import streamlit as st
from datetime import datetime
import dateutil.relativedelta

# Set the title of the app
st.title("When did my parents fuck?")

# Brief description
st.write("When did my parents fuck?")

# Input for user's birthday with min and max values
today = datetime.today().date()
min_date = datetime(1900, 1, 1)  # Minimum date allowed
user_birthday = st.date_input("Enter your birthday", value=None, min_value=min_date, max_value=today)

if user_birthday:
    # Calculate the date 9 months before the birthday
    due_date = user_birthday - dateutil.relativedelta.relativedelta(months=9)

    # Format the output date
    formatted_date = due_date.strftime('%d %B %Y')  # e.g., "17 October 2023"

    # Display the result
    st.title("Your parents fucked on:")
    st.title(f"**{formatted_date}**")
