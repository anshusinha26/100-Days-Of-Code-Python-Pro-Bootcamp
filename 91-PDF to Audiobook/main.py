import PyPDF2
import pyttsx3


def pdf_to_speech(pdf_path):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set properties before starting
    engine.setProperty('rate', 150)  # Speed percent (default is 200)
    engine.setProperty('volume', 0.9)  # Volume 0-1

    # Open the PDF file
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Initialize an empty string to store all text from the PDF
        all_text = ""

        # Loop through each page of the PDF
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            page_text = page.extract_text()
            all_text += page_text + "\n"

        # Use the engine to speak the text
        engine.say(all_text)
        engine.runAndWait()


# Replace 'sample.pdf' with the path to your PDF file
pdf_to_speech('sample.pdf')
