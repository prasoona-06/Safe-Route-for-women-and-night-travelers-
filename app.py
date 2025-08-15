import streamlit as st
from speech_to_text import recognize_speech
from language_detection import detect_language
from response_generator import generate_response
from police_lookup import find_nearby_police

st.title("SafeRoute - Online")

if st.button("🎤 Speak Now"):
    query = recognize_speech()
    st.write("You said:", query)

    lang = detect_language(query)
    st.write("Language Detected:", lang)

    response = generate_response(query)
    st.write("Response:", response)

    if "location" in query.lower():
        st.write("🔍 Searching for nearby police stations...")
        # Example: hardcoded location; replace with live GPS or user input
        results = find_nearby_police(17.3850, 78.4867)
        for r in results[:3]:
            st.markdown(f"**{r['name']}** - {r['vicinity']}")
