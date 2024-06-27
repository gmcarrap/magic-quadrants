from flask import Flask, jsonify, request, render_template
from main import main

app = Flask(__name__, template_folder='/Volumes/Transcend/Magic Quadrants/magic-quadrants/')

@app.route('/magic-quadrants-json', methods=['POST'])
def get_magic_quadrants():
    """
    Endpoint to calculate magic quadrants from JSON input.

    Accepts JSON with a parameter N, calculates magic quadrants using 'main' function.

    Returns:
        JSON: Magic quadrants calculated based on input N.

    Raises:
        ValueError: If N is not provided or is not a valid integer.
    """
    
    data = request.json
    N = data.get('N')
    
    if N is None:
        return jsonify({"error": "Parameter N not provided"}), 400
    
    try:
        N = int(N)
    except ValueError:
        return jsonify({"error": "The value of N must be an integer."}), 400
    
    magic_quadrants = main(N)
    return jsonify(magic_quadrants)

@app.route('/magic-quadrants', methods=['GET', 'POST'])
def magic_quadrants_form():
    """
    Endpoint to render HTML form for inputting N and displaying magic quadrants.

    Renders 'form.html' template for GET requests. Processes POST requests,
    validates N, calculates magic quadrants using 'main' function, and renders 'index.html'.

    Returns:
        str: Rendered HTML page with magic quadrants or error message.

    Raises:
        ValueError: If N is not provided or is not a valid integer.
    """
    if request.method == 'POST':
        N = request.form.get('N')
        
        if not N:
            return "Please enter a value for N."
        
        try:
            N = int(N)
        except ValueError:
            return "N must be an integer."
        
        magic_quadrants = main(N)
        return render_template('index.html', magic_quadrants=magic_quadrants, N=N)
    
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
