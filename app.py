import streamlit as st
import numpy as np
from PIL import Image

from ocr import extract_text
from embedding import create_embeddings
from attention import calculate_attention


st.set_page_config(
    page_title="AI Attention Visualizer",
    layout="wide"
)


st.title("AI Attention Visualizer")

st.write(
    "Upload an image to extract text and visualize "
    "word-level attention scores."
)


# Sidebar

with st.sidebar:

    st.header("About")

    st.write(
        "This application extracts text from an image "
        "using OCR and calculates attention scores "
        "using word embeddings."
    )

    st.divider()

    st.subheader("Process")

    st.write("1. Upload Image")
    st.write("2. Extract Text using OCR")
    st.write("3. Create Word Embeddings")
    st.write("4. Calculate Attention Scores")
    st.write("5. Display Results")


# Image Upload

st.header("Upload Image")

file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)


if file:

    image = Image.open(file)

    # Image and OCR result

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Input Image")

        st.image(
            image,
            use_container_width=True
        )

    with col2:

        st.subheader("Extracted Text")

        with st.spinner("Extracting text..."):

            text = extract_text(image)

        if not text.strip():

            st.error("No text found in the image.")

            st.stop()

        st.text_area(
            "OCR Result",
            text,
            height=250
        )


    st.divider()


    # Process words

    words = text.split()

    words = [
        word.strip(".,!?;:()[]{}")
        for word in words
    ]

    words = [
        word
        for word in words
        if len(word) > 2
    ]

    words = words[:20]


    if not words:

        st.warning("No suitable words found.")

        st.stop()


    # Create embeddings

    with st.spinner("Creating word embeddings..."):

        embeddings = create_embeddings(words)


    # Calculate attention

    with st.spinner("Calculating attention scores..."):

        scores = calculate_attention(embeddings)


    # Normalize scores

    if scores.max() != 0:

        display_scores = scores / scores.max()

    else:

        display_scores = scores


    # Attention results

    st.header("Word Attention")

    st.write(
        "The progress bar represents the relative "
        "attention score of each word."
    )


    for word, score in zip(words, display_scores):

        percentage = float(score) * 100

        st.write(
            f"{word} - {percentage:.2f}%"
        )

        st.progress(float(score))


    # Highest attention

    top_index = np.argmax(scores)

    top_word = words[top_index]

    top_score = float(display_scores[top_index]) * 100


    st.divider()

    st.header("Attention Summary")


    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Highest Attention Word",
            top_word
        )

    with col2:

        st.metric(
            "Attention Score",
            f"{top_score:.2f}%"
        )

    with col3:

        st.metric(
            "Total Words",
            len(words)
        )


else:

    st.info(
        "Upload an image to start the attention visualization."
    )