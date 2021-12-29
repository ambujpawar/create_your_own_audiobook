from gtts import gTTS

input_data = open('/path/to/article.txt', "r")
text_str = input_data.read()
speech = gTTS(text=text_str, lang='en', slow=False)
speech.save('/path/to/save.mp3')
