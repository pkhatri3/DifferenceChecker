from flask import Flask, render_template, request, jsonify
import difflib
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare', methods=['POST'])
def compare():
    data = request.get_json()
    text1 = data['text1']
    text2 = data['text2']
    
    # Split texts into lines
    text1_lines = text1.splitlines()
    text2_lines = text2.splitlines()
    
    # Generate diff
    differ = difflib.HtmlDiff()
    diff_table = differ.make_table(text1_lines, text2_lines)
    
    return jsonify({'diff': diff_table})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Get PORT from environment variable
    app.run(host='0.0.0.0', port=port, debug=False)