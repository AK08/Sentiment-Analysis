import streamlit as st
import textPage
# import audioPage
# import videoPage
# import twitterAnalysisPage

# st.title("Hello")
page = "Text"

if page=="Text":
    textPage.renderPage()
# elif page=="Audio":
#     audioPage.renderPage()

# elif page=="Video":
#     videoPage.main()
# elif page=="Twitter Data":
#     twitterAnalysisPage.renderPage()