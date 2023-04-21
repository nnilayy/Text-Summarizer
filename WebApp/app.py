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


# https://www.youtube.com/watch?v=3KuA3DrnZNQ
# https://www.youtube.com/watch?v=prjMJtXCR-g
# https://www.youtube.com/watch?v=fhje9idm8V4
# https://www.youtube.com/watch?v=z-RywG7Xfk8
# https://www.producthunt.com/products/coolify
# https://coolify.io/
# https://www.youtube.com/watch?v=lPJVi797Uy0
# https://www.youtube.com/watch?v=hv0rNxr1XXk