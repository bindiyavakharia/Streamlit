import streamlit as st
from PIL import Image
import pandas as pd
import altair as alt
#st.balloons()
#st.snow()
#Your name
st.title("Bindiya Vakharia")
#Elevator Pitch
st.subheader("Python")

col1, col2= st.columns([3,1])
with col1:
    st.subheader("About Me")
    st.text("Passionate about power of data to drive insights and\ninnovation")
with col2:
    #Add an image
    image = Image.open('dp.png')
    st.image(image, width = 250)
# Sidebar w/ download
st.sidebar.caption('Wish to connect?')
st.sidebar.write('xyz@gamil.com')
#rb means converting pdf file to raw binary format
pdf_file = open('Resume_BindiyaVakharia.pdf', 'rb')
st.sidebar.download_button('Download Resume', pdf_file, file_name='Resume_BindiyaVakharia.pdf', mime='pdf')

## Getting everything in tabs
#tab_exp, tab_pro,tab_skills,tab_cont,tab_pic = st.table(['Experience','Projects','Skills','Contact Me','Take a Picture'])
##with tab_exp:
        # New subheader for experience in  a table
st.subheader('Relevant Experience')
experience_table= pd.DataFrame({
    "Job Title": ["Business Analyst","Administrator"],
    "Company": ["XYZ", "ABC"],
    "Job Description": ["Provided expertise in data analytics, data storage structures, mining and data cleaning","Data Cleaninga and Visulizing"]
})
experience_table = experience_table.set_index('Job Title')
st.table(experience_table)
#Projects GRID
#with tab_pro:
st.subheader("Projects")
titanic_data = pd.read_csv('titanic.csv')
interval = alt.selection_interval()
bar_chart = alt.Chart(titanic_data).mark_bar().encode(
    x = 'sum(Survived):Q',
    y = 'Pclass:N',
    color = 'Pclass:N',
).properties(
    width = 300
    )
scatter_plot = alt.Chart(titanic_data).mark_point().encode(
    x = 'Age:Q',
    y = 'Fare:Q',
    color = alt.condition(interval, 'Sex', alt.value('lightgray')),
).properties(
    width = 500,
    height = 400
    ).add_selection(
        interval
        ).interactive()
    # Define a selection to filter the scatter plot based on the selected passenger 
selection = alt.selection_single(fields=['Pclass'], empty = 'none')
bar_chart = bar_chart.add_selection(selection)
scatter_plot = scatter_plot.transform_filter(selection)
#put any jupiter chart in streamlit just add st.altair_chart()
st.altair_chart(bar_chart | scatter_plot)
#Skills section - In the form of a bar chart
#with tab_skills:
skill_data = pd.DataFrame(
    {
    "Skills Level":[90,60,60,40],
    "Skills":['Python','Tableau','mySQL','Rstudio']
    })
skill_data = skill_data.set_index('Skills')
with st.container():
    st.header("Skills")
    st.bar_chart(skill_data)
with st.expander("See More Skills"):
    st.write("I have lot of more skills such as .....")

#Streamlit form
#with tab_cont:
form = st.form('my_form')
fullname = form.text_input(label='Enter your Full Name', value = '')
age = st.slider("Select your age")
gender = st.radio("Select your gender",('Male','Female','Other'))
message = form.text_area(label = 'Your Message', value = '', height = 100)
terms = st.checkbox('Accept terms and conditions')
submit = form.form_submit_button(label = 'Submit')
    #Handle form submission
if submit:
    if terms:
        st.success('Form Completed: Thank You for visiting')
    else:
        st.success('Please accept the terms and conditions')
st.write('Name:', fullname, "Age:", age,"Gender:", gender, "Message:", message)

#Add a map
#Create a Dataframe with lat and long columns
data = {
    'Location':['Kitchener','Waterloo','Guelph','Cambridge'],
    'LAT':[43.451639,43.46258,43.5467,43.3616],
    'LON':[-80.492533,-80.520410,-80.2482,-80.3144]
    }
df=pd.DataFrame(data)
st.map(df)
#Using Camera
#with tab_pic:
picture = st.camera_input('Take a picture with me')
if picture:
    st.image(picture)

