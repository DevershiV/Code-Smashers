import streamlit as st

st.set_page_config(page_title='Code Smashers', layout="wide")

with open("designing.css") as source_des:
    st.markdown(f"<style>{source_des.read()}</style>",unsafe_allow_html=True)

st.title('Code Smashers')

col1, col2, col3 = st.columns([3,2,2])

with col1:
    st.header("Upload file")
    uploaded_file = st.file_uploader("Upload file",label_visibility="collapsed")
    if uploaded_file is not None:
        pass

with col2:
    st.header("Convert")
    if st.button('Convert 🔄'):
        if uploaded_file is not None:
            pass
        else:
            st.warning('Please Upload a file to convert', icon="⚠️")
    else:
        pass

with col3:
    st.header("Download file")
    text_contents = '''This is some text'''
    st.download_button('Download 📥', text_contents)