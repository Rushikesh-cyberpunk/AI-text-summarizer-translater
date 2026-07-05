# AI Text Summarizer & Translator

A Python-based AI application that summarizes text into exactly three key bullet points and translates those bullet points into a user-selected language using Google's Gemini AI model.

## Features

* Read text from a file or paste text directly into the terminal
* Generate concise summaries in exactly 3 bullet points
* Translate summaries into any user-selected language
* Save results to a Markdown file (`summary_translated.md`)
* Simple command-line interface
* Powered by Google Gemini 1.5 Flash

## Technologies Used

* Python
* Google Generative AI (Gemini API)
* File Handling
* Markdown Output

## How It Works

1. The user chooses whether to load text from a file or paste text manually.
2. The application sends the text to the Gemini AI model.
3. Gemini generates a summary in exactly three bullet points.
4. The summary is translated into the language selected by the user.
5. The result is displayed in the terminal.
6. The user can optionally save the output as a Markdown file.

## Installation

1. Clone the repository.
2. Install the required package:

```bash
pip install google-generativeai
```

3. Add your Gemini API key in the code.
4. Run the application:

```bash
python app.py
```

## Example Output

SUMMARY:

* Point 1
* Point 2
* Point 3

TRANSLATION (Spanish):

* Punto 1
* Punto 2
* Punto 3

## Future Improvements

* Support PDF and DOCX files
* Add a graphical user interface (GUI)
* Export results in multiple formats
* Support custom summary lengths
* Improve error handling and validation

## Purpose

This project was developed as part of an AI internship task to demonstrate the use of Generative AI for text summarization and multilingual translation.


