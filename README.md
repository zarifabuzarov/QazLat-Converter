# QazContext-Latiner 🇰🇿

A context-aware Cyrillic-to-Latin transliterator for the Kazakh language, implemented in Python.

## 🚀 Overview

Unlike simple character-to-character mapping tools, **QazContext-Latiner** uses phonetic logic to handle the complexities of the Kazakh language. It analyzes the surrounding characters of each vowel to determine the correct Latin representation, ensuring high accuracy for linguistic conversion.

## ✨ Key Features

* **Vowel Harmony Detection:** Automatically identifies if a word is "soft" or "hard" (`issoft`) to choose the correct vowel variants (e.g., `o` vs `ö`).
* **Complex Diphthong Handling:** Intelligent processing for letters like **У, И, Ю, Я, Ё** based on their position (start of word, between consonants, etc.).
* **Case Sensitivity:** Perfectly preserves the original text's casing (Sentence case, UPPERCASE, lowercase, or Title Case).
* **Smart Tokenization:** Separates words from punctuation and symbols, processes them individually, and reassembles the text without breaking formatting.
* **Phonetic Mapping:** Uses a custom `mapvocal` system to categorize sounds into consonants, vowels, and special diphthongs for precise conversion.

## 🛠 How It Works

The algorithm follows a multi-step pipeline:
1.  **Split:** Segments the input string into words and non-word characters.
2.  **Analysis:** Maps each word into a phonetic structure (e.g., `cvvc` for "book").
3.  **Context Check:** Determines word harmony (soft/hard).
4.  **Transformation:** Replaces characters based on the harmony and the type of neighbors (vowel-consonant proximity).
5.  **Reconstruction:** Restores the original casing and joins the tokens back together.

## 💻 Usage

Simply import the `convert_text` function into your project:

```python
from qaz_latiner import convert_text

# Example input
cyrillic_text = "Ассалаумағалейкум, достар!"

# Convert
latin_text = convert_text(cyrillic_text)

print(latin_text)
# Output: Assalavumağaleykuvm, dostar!
