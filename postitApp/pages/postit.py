import streamlit as st 
import json
import pandas as pd

st.write("# Post it")

@st.cache_data
def get_tags(data: dict) -> list:
    
    tags = set()
    for d in data.values():
        for tag in d["tags"]:
            tags.add(tag)

    return sorted(tags)

file_upload = st.file_uploader("Uploadez votre fichier json")

if file_upload:
    
    data = json.load(file_upload)
    tags = get_tags(data)
    
    tags_checked = {tag: st.checkbox(tag, value=True) for tag in tags}

    keys = []
    for key, val in data.items():
        for tag in val["tags"]:
            if tags_checked[tag] and key not in keys:
                keys.append(key)
                with st.expander(key):
                    val["description"]
    
    df = pd.DataFrame(data)
    st.dataframe(df.T)

    json_str = json.dumps(data)
    st.download_button(
        label="Télécharger votre fichier mis à jour",
        file_name="data.json",
        mime="application/json",
        data=json_str,
    )
    