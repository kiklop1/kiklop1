from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def menu():
    return '''
    <h1>Select an Option:</h1>
    <ul>
        <li><a href="/equity">Equity Analysis</a></li>
        <li><a href="/credit">Credit Analysis</a></li>
    </ul>
    '''

@app.route('/equity', methods=['GET', 'POST'])
def equity():
    if request.method == 'POST':
        analysis_type = request.form['analysis_type']
        return f'You selected {analysis_type} analysis'
    return '''
    <h1>Equity Analysis</h1>
    <form method="POST">
        <label for="analysis_type">Select analysis type:</label>
        <select id="analysis_type" name="analysis_type">
            <option value="technical">Technical Analysis</option>
            <option value="fundamental">Fundamental Analysis</option>
        </select>
        <br><br>
        <input type="submit" value="Submit">
    </form>
    '''

@app.route('/credit', methods=['GET', 'POST'])
def credit():
    if request.method == 'POST':
        analysis_type = request.form['analysis_type']
        return f'You selected {analysis_type} analysis'
    return '''
    <h1>Credit Analysis</h1>
    <form method="POST">
        <label for="analysis_type">Select analysis type:</label>
        <select id="analysis_type" name="analysis_type">
            <option value="default">Default Risk Analysis</option>
            <option value="credit_rating">Credit Rating Analysis</option>
        </select>
        <br><br>
        <input type="submit" value="Submit">
    </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)