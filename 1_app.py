from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__, template_folder='3_html', static_folder='4_static')

# Define supported languages
LANGUAGES = {
    'en': 'English',
    'hi': 'Hindi',
    'fr': 'French',
    'es': 'Spanish',
    'de': 'German',
    'zh-cn': 'Chinese (Simplified)',
    'ja': 'Japanese',
    'ko': 'Korean'
}

@app.route('/', methods=['GET', 'POST'])
def home():
    translated_text = ""
    error = ""
    if request.method == 'POST':
        try:
            text = request.form['text']
            source_lang = request.form['source_lang']
            target_lang = request.form['target_lang']
            translator = Translator()
            translated = translator.translate(text, src=source_lang, dest=target_lang)
            translated_text = translated.text
        except Exception as e:
            error = "Something went wrong. Please try again."

    return render_template('3_home.html', languages=LANGUAGES, translated_text=translated_text, error=error)

if __name__ == '__main__':
    app.run(debug=True)
