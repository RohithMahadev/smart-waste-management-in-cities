import streamlit as st
import Data_etl
import streamlit.components.v1 as components
import prediction
import analytics




def app():
    def col(url):
        st.markdown(f'<b><center><p style="color:#332FD0;font-size:40px;border-radius:2%;">{url}</p></center></b>', unsafe_allow_html=True)

    col('Smart Waste Management System in cities')

    db = st.sidebar.radio('View',['Analytics','GarbageCollection','Live Dashboard','Dustbin Data','Location','Table'])

  
    if db =='Live Dashboard':
        page = Data_etl
        page.dataetl()
      
    if db == 'Table':
        st.subheader('House no:1')
        st.write("House ID:001")
        page = Data_etl
        page.table()
    if db == 'Dustbin Data':
        st.write("House ID:001")
        page = Data_etl
        page.dustbindata()
    
    if db == 'Location':
        page = Data_etl
        page.location()
    if db == 'Analytics':
        page = analytics
        page.analytics()
    if db == 'GarbageCollection':
        page = prediction
        page.pred()


