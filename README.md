#  AI Attention Visualizer

A beginner-friendly AI application that extracts text from study-note images using OCR, converts the extracted words into numerical embeddings, applies a simple scaled dot-product attention mechanism, and visualizes the relative attention received by each word.

 Project Overview

The AI Attention Visualizer combines multiple AI concepts into one simple application:

Image → OCR → Words → Embeddings → Attention → Visualization

The project is designed to help students understand how OCR, embeddings, and attention can work together in an AI application.

Main Components

- OCR – Extracts text from an uploaded image.
- Embeddings – Converts words into numerical vectors.
- Attention – Calculates relationships between word representations.
- Streamlit – Provides an interactive web interface.
- Visualization – Displays relative attention scores using progress bars.

---

 Project Objective

The main objective is to build a simple AI application that can:

1. Read text from a study-notes image.
2. Convert the extracted text into individual words.
3. Generate numerical embeddings for the words.
4. Apply scaled dot-product attention.
5. Calculate relative attention scores.
6. Display the scores visually using Streamlit.

---

Problem Statement

Students often learn OCR, embeddings, and attention as separate concepts.

This project combines these concepts into one small application. The user uploads an image containing study notes, the application extracts the text, processes the words, calculates attention scores, and displays the results visually.

---

Learning Outcomes

After completing this project, students can understand:

- The basic purpose of OCR.
- How text can be converted into numerical embeddings.
- The purpose of Query, Key, and Value.
- The concept of scaled dot-product attention.
- How attention weights can be visualized.
- How to create a simple Streamlit application.
- How multiple Python modules can work together.
- How to run an AI application locally using VS Code.

---

Project Flow

Study Notes Image
        ↓
      OCR
        ↓
  Extracted Text
        ↓
   Word Processing
        ↓
     Embeddings
        ↓
Scaled Dot-Product Attention
        ↓
 Attention Scores
        ↓
 Streamlit Visualization

---

🧠 What is OCR?

OCR stands for Optical Character Recognition.

OCR converts text present inside an image into machine-readable text.

For example:

Image:
"Artificial Intelligence"

        ↓ OCR

Text:
Artificial Intelligence

This project uses Tesseract OCR through the Python library pytesseract.

---

 Embedding

An embedding is a numerical representation of text.

Instead of representing a word only as characters, an AI model converts it into a vector of numbers.

This project uses:

all-MiniLM-L6-v2

The model produces 384-dimensional embeddings.

Important Note

"all-MiniLM-L6-v2" is primarily designed for sentence embeddings. In this project, it is applied to individual words for educational simplicity.

Therefore, these embeddings should not be considered the same as the internal token representations or attention maps of a trained Transformer model.

---
Attention

Attention is a mechanism that helps a model calculate relationships between different representations.

The basic scaled dot-product attention formula is:

Attention(Q, K, V)
=
softmax(QKᵀ / √dₖ)V

Where:

- Q = Query
- K = Key
- V = Value
- dₖ = dimension of the Key vectors
- Softmax = converts scores into attention weights

In this project, the attention weights are averaged to produce one display score for each word.

---

 System Architecture

Stage| Technology| Input| Output
Image Upload| Streamlit + Pillow| JPG/PNG| Image object
OCR| Tesseract + pytesseract| Image| Extracted text
Word Processing| Python| Text| Clean word list
Embeddings| Sentence Transformers| Words| 384-D vectors
Attention| NumPy| Embeddings| Attention weights
Visualization| Streamlit| Scores| Progress bars

---

 Technologies Used

Technology / Library| Purpose
Python| Main programming language
Streamlit| Web interface
Pillow| Image processing
pytesseract| Python interface for Tesseract
Tesseract OCR| Text extraction
Sentence Transformers| Text embeddings
NumPy| Matrix and attention calculations

---

 Project Structure

AI-Attention-Visualizer/
│
├── app.py
├── ocr.py
├── embedding.py
├── attention.py
├── requirements.txt
└── README.md

---

Prerequisites

Before running the project, install:

- Python 3.x
- VS Code
- Tesseract OCR
- Internet connection for the first model download
- Basic Python knowledge

---

Installation

1. Clone the Repository

git clone <your-github-repository-url>

2. Open the Project

Open the project folder in VS Code.

AI-Attention-Visualizer

3. Install Python Packages

Open the VS Code terminal and run:

pip install streamlit numpy pillow pytesseract sentence-transformers

Or use the requirements file:

pip install -r requirements.txt

---

requirements.txt

streamlit
numpy
pillow
pytesseract
sentence-transformers

---

Tesseract OCR Setup

"pytesseract" is only a Python wrapper. The actual Tesseract OCR application must also be installed.

A common Windows installation path is:

C:\Program Files\Tesseract-OCR\tesseract.exe

The path is configured in "ocr.py".

If Tesseract is installed in another location, update the path accordingly.

---

 Running the Application

Open the project folder in VS Code.

Open:

Terminal → New Terminal

Run:

streamlit run app.py

Streamlit will provide a local web address.

Open that address in your browser to use the application.

---

 Features

- Upload study-note images.
- Extract text using OCR.
- Clean and process extracted words.
- Generate 384-dimensional embeddings.
- Apply scaled dot-product attention.
- Display relative attention scores.
- Identify the word with the highest calculated score.
- Simple and beginner-friendly Streamlit interface.

---
Application Workflow

Step 1 — Upload Image

The user uploads a JPG, JPEG, or PNG image containing study notes.

Step 2 — OCR

Tesseract extracts the text from the image.

Step 3 — Word Processing

The extracted text is split into individual words.

Words are cleaned and words shorter than three characters are removed.

The application uses a maximum of 20 words for the demonstration.

Step 4 — Embeddings

Each selected word is converted into a numerical representation using:

all-MiniLM-L6-v2

Step 5 — Attention

Query, Key, and Value representations are generated and scaled dot-product attention is calculated.

Step 6 — Visualization

The attention scores are normalized and displayed using Streamlit progress bars.

Step 7 — Highest Attention

The application displays the word with the highest calculated attention score.

---

Example

Suppose OCR extracts:

Artificial Intelligence uses machine learning to analyze data.

The application may display:

Artificial       ██████████
Intelligence     ███████████████
uses             █████
machine          █████████
learning         █████████████
analyze          ███████
data             █████████

The exact values depend on the generated embeddings and attention calculation.

---
Important Technical Note

This project is designed primarily for learning the mechanics of attention.

The Q, K, and V projection matrices used in this classroom implementation are randomly initialized.

Therefore:

«The highest-attention word should not be interpreted as the word that the AI model truly considers most important.»

The visualization demonstrates how attention calculations work, rather than showing the actual learned attention maps of a pretrained Transformer.

---

 Testing

The application can be tested using:

Test 1

Upload a clear image containing a short paragraph.

Test 2

Upload an image containing a heading and body text.

Test 3

Upload handwritten notes and observe OCR limitations.

Test 4

Upload an image containing no readable text.

Expected result:

No text found in the image.

Test 5

Upload an image containing more than 20 words.

Expected result:

Only the first 20 cleaned words are visualized.

---
Common Errors

Error| Solution
"python is not recognized"| Install Python and add it to PATH
"No module named streamlit"| Run "pip install streamlit"
"No module named sentence_transformers"| Run "pip install sentence-transformers"
"No module named pytesseract"| Run "pip install pytesseract"
"TesseractNotFoundError"| Install Tesseract and check its path
No text found| Use a clearer image with printed text
Model download is slow| Wait for the first-time model download
Progress bar error| Ensure the value passed to "st.progress()" is between 0 and 1

---
Project Limitations

- OCR accuracy depends on image quality.
- Handwritten text may not be recognized correctly.
- Only the first 20 cleaned words are processed.
- MiniLM is primarily a sentence-embedding model.
- The project applies the model to individual words for demonstration.
- Q, K, and V projection matrices are randomly initialized.
- The attention score does not represent reliable semantic importance.
- The project does not extract the actual internal attention maps of a pretrained Transformer.

---

Future Enhancements

Possible improvements include:

- Use a Transformer model that exposes actual token-level attention.
- Highlight important words directly in the extracted text.
- Highlight OCR words on the original image.
- Add support for Tamil and other languages.
- Add keyword extraction.
- Add topic classification.
- Add study-note summarization.
- Add question-answering from uploaded notes.
- Allow users to download an attention report.
- Add a more advanced attention heatmap.

---

📈 Learning Pipeline

Image Processing
       ↓
      OCR
       ↓
 Text Processing
       ↓
   Embeddings
       ↓
   Attention
       ↓
 Visualization

This pipeline demonstrates how different AI concepts can be connected to create a complete beginner-friendly AI application.

---

📝 Conclusion

The AI Attention Visualizer is an educational AI project that combines image processing, OCR, text embeddings, attention mechanisms, and Streamlit into one application.

It provides a simple way for students to understand the flow:

Image → Text → Embeddings → Attention → Visualization

The project focuses on understanding the basic working of attention rather than reproducing the internal attention mechanisms of a large pretrained Transformer model.