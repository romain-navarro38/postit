import streamlit as st 
import json
import pandas as pd

st.write("# Post it")

@st.cache_data
def get_tags(data):
    
    tags = []
    for d in data.values():
        for tag in d["tags"]:
            if tag not in tags:
                tags.append(tag) 
    
    return tags

file_upload = st.file_uploader("Uploadez votre fichier json")

if file_upload:
    
    data = json.load(file_upload)
    tags = get_tags(data)
    
    tags_checked = {tag:st.checkbox(tag, value=True) for tag in tags}
    
    for key, val in data.items():
        for tag in val["tags"]:
            if tags_checked[tag]:
                with st.expander(key):
                    val["description"]
    
    df = pd.DataFrame(data)
    st.dataframe(df.T)
    