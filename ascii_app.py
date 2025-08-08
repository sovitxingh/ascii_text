import streamlit as st

def ascii_to_text(binary_data):
    return ''.join(chr(int(b, 2)) for b in binary_data.split())

def text_to_ascii(text):
    return ' '.join(format(ord(c), '08b') for c in text)

st.title("ASCII ⇆ Text Converter")

mode = st.radio("Select mode:", ["ASCII to Text", "Text to ASCII"])

if mode == "ASCII to Text":
    binary_data = st.text_area("Enter binary (8-bit, space separated):")
    if st.button("Convert"):
        st.write(ascii_to_text(binary_data))
else:
    text = st.text_area("Enter text:")
    if st.button("Convert"):
        st.write(text_to_ascii(text))
