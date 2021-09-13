import streamlit as st

## Title
st.title("This is the title.")

## Header
st.header("This is a header.")
st.subheader("This is a subheader.")

# Text
st.text("This is some text. Hello, Streamlit!")

# Markdown
st.markdown("### This is a markdown H3.")
st.markdown("*This is italic text.*")
st.markdown("**This is bold text.**")

# Colored Boxes
st.info("This is an info box.")
st.success("Great success!")
st.warning("This is a warning box.")
st.error("This is an error box.")
st.exception("NameError('Name not defined').")

# Get Help About Python Functions
st.help(range)

# Write Plain Text
st.write("This is plain text. Not markdown, just plain text.")
st.write(range(10))

# Widgets
if st.checkbox("Show/Hide"):
	st.text("Showing or Hiding Widget")

# Radio Buttons
status = st.radio("What is your status?", ("Active", "Inactive"))

if status == "Active":
	st.success("You're active!")
else:
	st.warning("You're not active!")

# Select Box
location = st.selectbox("Where do you work?", ("London", "New York", "Chicago", "Houston", "Mexico"))
st.write("You selected:", location)

# Multiselect
occupation = st.multiselect("Your occupation", ("Programmer", "Data Scientist", "Financial Analyst"))
st.write("You selected", len(occupation), "occupations.")

# Slider
level = st.slider("What is your level?",1,5)

# Buttons
st.button("Sample Button")
if st.button("About"):
	st.text("Streamlit is cool!")

# Text Inputs
firstname = st.text_input("Enter first name...", "Type here.")
if st.button("Submit1"):
	result1 = firstname
	st.success(result1)

# Text Areas
message = st.text_area("Enter your message.","Type here.")
if st.button("Submit2"):
	result2 = message
	st.success(result2)

# Date Input
import datetime
today = st.date_input("Today is:", datetime.datetime.now())

# Time Input
my_time = st.time_input("The time is:", datetime.time())

# Display JSON
st.text("Display JSON")
st.json("{'name':'Jo', 'Gender':'male'}")

# Display Raw Code
## Note: this is not execued code-- just a display of code!
st.code("import numpy as np\nimport pandas as pd")

# Display Raw Code (Part 2)
with st.echo():
	import pandas as pd
	df = pd.DataFrame()

# Progress Bars
import time
my_bar = st.progress(0)
for p in range(50):
	my_bar.progress(p+1)

# Spinnner
with st.spinner("Waiting ..."):
	time.sleep(5)

# Sidebar
st.sidebar.header("This is a header in the sidebar.")
st.sidebar.text("This is text in the sidebar.")