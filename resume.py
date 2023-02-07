import streamlit as st
from PIL import Image 

from pathlib import Path
import pandas as pd
import plotly.express as px


current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()




ines_visage_path = current_dir / "files" / "ines_face.jpeg"
python_path = current_dir / "files" / "python2.png"
sql_path = current_dir / "files" / "sql2.png"

ines_visage = Image.open(ines_visage_path)
python_logo = Image.open(python_path)
sql_logo = Image.open(sql_path)

st.set_page_config(layout="wide", page_icon=ines_visage, page_title="Inès Resume")



css_file=current_dir / "styles" / "main.css"
with open(css_file) as f:
   st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)



st.sidebar.info(
    """
    If you are looking for a curious and enthusiast data analyst, don't hesitate to 
    [email](mailto:ines.mebarki@essec.edu) me or reach out on [LinkedIn](https://www.linkedin.com/in/inès-mebarki/)""")



def space(num_lines=1):
    """Adds empty lines to the Streamlit app."""
    for _ in range(num_lines):
        st.write("")
    pass


col1,col2 = st.columns(2,gap="small")
with col1:
    st.title('Mebarki Inès')
    st.write(':e-mail:','ines.mebarki@essec.edu')
    st.write(':phone: ',' +33 7 50 08 49 36')

    social_media={'LinkedIn':'www.linkedin.com/in/inès-mebarki'}
    for key,value in social_media.items():
        st.write(f":necktie: [{key}]({value})")



    space(3)
    st.header('Profesionnal Experience')
    st.markdown('<p style="font-family:roboto; color:#2E5984;">2021 - July 2023, MON PETIT PLACEMENT - Data Analyst/Scientist, Apprentice</p>',unsafe_allow_html=True)
    st.write("""
    Data Visualization:
    - Data extractions from a relational database (PostgreSQL) and data analysis for C-level positions
    - Automation of most frequents extracts through Pyhton and visualisation as excel files
    - Development of dashboards for decision support and KPI follow-up (Grafana and Streamlit)
    - Development of an algorithm that forecast upcoming billing given the dynamic billing model of the company (based on high water mark)

    Machine Learning: 
    - Descriptive algorithms to cluster the database for marketing purposes (design of personas)
    - Predictive algorithm to estimate the likelihood of a prospect to become client
    - Prescriptive algorithm advising human consultant on portfolio allocation according to customer risk profile""")
    space(2)
    st.markdown('<p style="font-family:roboto; color:#2E5984;">2020, MON PETIT PLACEMENT - Project manager for the CEO - 6 months, Intern</p>',unsafe_allow_html=True)

    st.write("""
        - Various reporting for the CEO : performance indicators, benchmark of the competitive environment
        - Organized events (webinars, competitions) with clients, partners schools
        - Advanced use of HubSpotCRM (Designing workflows)
        - Wrote out financial content for the Sales team(report of funds performances, macro economic notes, pedagogical articles for clients)""")
    space(2)
    st.markdown('<p style="font-family:roboto; color:#2E5984;">2019, GREENFURN - Consultant for an entrepreneurial project, Part-time</p>',unsafe_allow_html=True)
    st.write("""
        - Junior consultant for a business creation project of eco-design furniture in a team of five students
        - “Wasterial” furniture market study, investigating the cradle-to-cradle market trends""")
    
    space(3)
    st.header('Education')
    st.markdown('<p style="font-family:roboto; color:#2E5984;">2019-2023, ESSEC Business School - MSc in Management and Business Administration</p>',unsafe_allow_html=True)
    st.markdown('<p style="font-family:roboto; color:#2E5984;">Exepected Graduation in October 2023</p>',unsafe_allow_html=True)

    st.write("""
    Major in Business Analytics, Electives in Finance, Entrepreneurship, Accounting""")
    space(2)
    st.markdown('<p style="font-family:roboto; color:#2E5984;">Jan 2022 - June 2022, Gothenburg University, SWEDEN </p>',unsafe_allow_html=True)
    st.markdown('<p style="font-family:roboto; color:#2E5984;">International Exchange Program</p>',unsafe_allow_html=True)

    st.write("""
    Courses in Project Management & Management across cultures """)
    space(2)
    st.markdown('<p style="font-family:roboto; color:#2E5984;">2017 - 2019, Lycée Henri IV, FRANCE</p>',unsafe_allow_html=True)
    st.markdown('<p style="font-family:roboto; color:#2E5984;">Intensive preparatory classes for competitive national examination</p>',unsafe_allow_html=True)
    st.write("""
    Mathematics, Economics, Geopolitics, Philosophy, English, German""")


with col2:
    st.image(ines_visage,width=200)
    st.write('Junior Data Analyst, I am eager to learn and help decision making through the power of analytics !')
    st.write('Expecting graduation from Essec Business School in Oct 2023')


    cv_pdf = current_dir / "files" / "INES MEB RESUME.pdf"
    with open(cv_pdf, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    st.download_button(label="Download my resume :rocket:",
                    data=PDFbyte,
                    file_name="INES_MEBARKI.pdf",
                    mime='application/octet-stream')


    space(1)
    st.header('IT Skills')
    st.write("""Python (Pandas, Plotly, Scikit Learn), SQL, Grafana, Streamlit, Office Suite, HubSpot, APIs manipulation""")
    st.image([python_logo,sql_logo],width=100)
    
    space(1)
    
    st.header('Languages')

    df_lang = pd.DataFrame(data={'Language': ["French", "English","German","Spanish","Chinese"],'Level': [5, 4,3,1,1],'Proficiency':['Native','Fluent','Advanced','Notions','Notions']})
    fig = px.bar(df_lang, x="Language", y="Level", color="Language",hover_data=['Proficiency'], width=400, height=300)
    fig.update_traces(width=0.5)
    st.plotly_chart(fig)
    
    space(1)
    
    st.header('Soft Skills')
    st.write("Comfortable with agile methodology")
    st.write("Excellent interpersonal skills (active listening, cultural intelligence, team leadership, empathy...)")
    st.write("Proficiency in problem-solving")

    space(1)

    st.header('Interests')
    st.write("Strong interest in innovation and entrepreneurship: fintech & insurtech environment follow up")
    st.write("Participation in the professional integration program for refugees EACH ONE (Support in finding work and housing, sharing cultures)")
    st.write("Midfield player in the Essec Women's Football Team (EFF)")
    st.write("Travels : Norway, Sweden, Denmark, Brazil, Spain, Germany, Slovenia, Hungary... ")