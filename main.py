from gtts import gTTS
from PyPDF2 import PdfReader


def text_to_audio(text, name):
    tts = gTTS(text=text, lang='en', tld='co.uk')
    filename = f"{name}.mp3"
    tts.save(filename)
    print("success")


### PUT PDF FILE IN WORKING DIRECTORY OR CHANGE PATCH ###
content = ""
reader = PdfReader("example.pdf")
number_of_pages = len(reader.pages)
for number in range(number_of_pages):
    pages = reader.pages[number-1]
    content += pages.extract_text()

text_to_audio(content, "sample")
