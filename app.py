from flask import Flask
from flask import request
from flask import render_template
from transformers import pipeline

app = Flask(__name__)

pt_model_sa = pipeline('sentiment-analysis', 'distilbert-base-uncased-finetuned-sst-2-english')
# analysis = pt_model_sa('i love you')

def analyze(phrase):
  analysis = pt_model_sa(phrase)
  return analysis

# print(analysis);

@app.route("/")
def display_form():
  return """
    <div>
      <h1>sentiment analysis</h1>
      <h2>enter a phrase</h2>
      <form action="analyze">
        <label for="phrase">phrase</label>
        <input type="text" id="phrase" name="phrase">
        <button>analyze</button>
      </form>
    </div>
  """

@app.route("/analyze")
def run_analyze():
  phrase = request.args.get('phrase')
  analysis = analyze(phrase)
  label = analysis[0]["label"]
  print(label)
  return render_template('analysis.html', label=label)