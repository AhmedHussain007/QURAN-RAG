import streamlit as st
import requests

# Define base URL
BASE_URL = "http://127.0.0.1:8000"

# Configure page layout with reduced margins
st.set_page_config(layout="wide")

# Add custom CSS to reduce margins and set proper spacing
st.markdown("""
<style>
.main .block-container {
    padding-left: 5%;
    padding-right: 5%;
    max-width: 100%;
}
</style>
""", unsafe_allow_html=True)

# Create two columns with 65% and 35% width distribution
col1, col2 = st.columns([0.65, 0.35])


# Left column: Hadith Validation using Quran
with col1:
    st.header("Hadith Validation using Quran")
    st.write("Enter a Hadith in English to validate it using similar Quranic ayahs.")

    query = st.text_area("Enter your Hadith", height=150, key="hadith_validation_input")

    if st.button("Validate Hadith", key="validate_hadith_button"):
        if not query.strip():
            st.warning("Please enter a Hadith.")
        else:
            url = f"{BASE_URL}/api/quran/validate"
            payload = {"query": query}
            try:
                response = requests.post(url, json=payload)
                if response.status_code == 200:
                    data = response.json()
                    results = data["results"]

                    st.success("Similar Ayahs Founded!")

                    st.markdown(f"### Matching Quranic Ayahs")
                    for ayah in results:
                        st.markdown(f"*Surah:* {ayah['surah_name_english']} - Ayah {ayah['aya_number']}")
                        st.markdown(f"*Score:* {ayah['score']:.4f}")
                        st.markdown(f"*Arabic:* {ayah['arabic_diacritics']}")
                        st.markdown(f"*English Translation:* {ayah['english_translation']}")
                        st.markdown("---")

                else:
                    st.error(f"Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"Failed to connect to backend: {e}")


# Right column: Hadith Narrator Chain Extractor
with col2:
    st.header("LLM-based Hadith Analyzer")
    st.write("Enter a hadith. Extract narrators, hadith content, or both using a language model.")

    hadith_text = st.text_area("Hadith Text", height=150, key="hadith_llm_input")

    if st.button("Get Narrators Only", key="get_narrators_only"):
        if not hadith_text.strip():
            st.warning("Please enter a hadith text.")
        else:
            url = f"{BASE_URL}/api/quran/get_naraters"
            payload = {"query": hadith_text}
            try:
                response = requests.post(url, json=payload)
                if response.status_code == 200:
                    data = response.json()
                    st.success("Narrators extracted successfully!")
                    st.json(data)
                else:
                    st.error(f"Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"Failed to connect to backend: {e}")

    if st.button("Get Hadith Content Only", key="get_hadith_only"):
        if not hadith_text.strip():
            st.warning("Please enter a hadith text.")
        else:
            url = f"{BASE_URL}/api/quran/get_hadith"
            payload = {"query": hadith_text}
            try:
                response = requests.post(url, json=payload)
                if response.status_code == 200:
                    data = response.json()
                    st.success("Hadith content extracted successfully!")
                    st.json(data)
                else:
                    st.error(f"Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"Failed to connect to backend: {e}")

    if st.button("Get Both Hadith & Narrators", key="get_both"):
        if not hadith_text.strip():
            st.warning("Please enter a hadith text.")
        else:
            url = f"{BASE_URL}/api/quran/get_hadith_and_narators"
            payload = {"query": hadith_text}
            try:
                response = requests.post(url, json=payload)
                if response.status_code == 200:
                    data = response.json()
                    st.success("Hadith and narrators extracted successfully!")
                    st.json(data)
                else:
                    st.error(f"Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"Failed to connect to backend: {e}")
