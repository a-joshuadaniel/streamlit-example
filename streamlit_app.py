
# joshua Daniel
# version 1 with front end
# CS50 Problem Set 0
#Problem link :https://cs50.harvard.edu/python/2022/psets/0/einstein
# step 1: Start
# Step 2: Prompt User For input bill amt in $
# Step 3: prompt user for tip perecntage in %
# Step 4: remove $
# Step 5: remove %
# Step 6: calculate tip
# Step 7: print tip amt

import streamlit as st
from google.oauth2 import service_account
from gsheetsdb import connect

# Create a connection object.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
    ],
)
conn = connect(credentials=credentials)

# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows

sheet_url = st.secrets["private_gsheets_url"]
rows = run_query(f'SELECT * FROM "{sheet_url}"')

# Print results.
for row in rows:
    st.write(f"{row.name} has a :{row.pet}:")

def main():
    st.title('tip calculator')
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    return float(d.replace('$',''))


def percent_to_float(p):
    p=float(p.replace('%',''))
    p1 = p/100
    return p1

main()
