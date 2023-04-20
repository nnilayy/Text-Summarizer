from flask import Flask, render_template, request
from summarizer import summarizer

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['POST','GET'])
def analyze():
    if request.method=='POST':
        rawtext=request.form['rawtext']
        doc, doc_length, summary, summary_length=summarizer(rawtext)
    return render_template('summary.html', summary=summary,doc=doc,doc_length=doc_length,summary_length=summary_length)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=int("3000"), debug=True)



