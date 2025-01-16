import streamlit as st
from scrape import (scrape_website, clean_body_content,extract_body_content, split_dom_content)
from parse import parse_with_gemini

st.title("AI web scrapin tool")
url = st.text_input("Enter the URL you want to scrape:")

if st.button("Start scraping"):
    st.write("Scraping...")
    result = scrape_website(url)
    
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)

    st.session_state.dom_content = cleaned_content

    with st.expander("View DOM content"):
        st.text_area("DOM content", cleaned_content, height= 300)

if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe the details that you want to extract from the site")

    if st.button("Start extraction"):
        if parse_description:
            st.write("Extracting content...")

            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse_with_gemini(dom_chunks, parse_description)
            st.write(result)

