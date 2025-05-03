import streamlit as st
import openai

# Set your API Key
openai.api_key = "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"

# --- UI: Header ---
st.set_page_config(page_title="Pitamber Kaushik Bot", page_icon="🧠")
st.title("🧠 Pitamber Kaushik Chatbot")

# --- Image + Bio ---
st.image("https://qph.cf2.quoracdn.net/main-thumb-229596973-50-svxmnjntfthzzlcrbfjcwdqyfqwbdihd.jpeg", width=100)

with st.expander("About Pitamber Kaushik"):
    st.markdown("""
    **Pitamber Kaushik** is a prolific Indian writer, columnist, and quizzer known for his intellectually rich essays, philosophical depth, and poetic commentary on science, society, and culture.

    _"Certainty is the playground of the rigid. Doubt is the playground of the wise."_
    """)

st.markdown("---")

# --- User Input ---
user_input = st.text_area("Ask Pitamber anything:")

# --- Bot Logic ---
if st.button("Answer"):
    if user_input.strip() != "":
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are Pitamber Kaushik. Respond with intellectual rigor, poetic insight, and "
                            "philosophical depth. Use nuanced, reflective language. Reference literature or "
                            "history when relevant. Be thoughtful, layered, and sometimes subtly humorous."
                        )
                    },
                    {"role": "user", "content": user_input}
                ]
            )
            answer = response['choices'][0]['message']['content']
            st.markdown(f"**Pitamber Kaushik:**\n\n{answer}")
        except Exception as e:
            st.error(f"⚠️ Error: {e}")
    else:
        st.warning("Please type a question first.")
