from flask import Flask, request, redirect, jsonify
import secrets

app = Flask(__name__)
url_mapping = {}

def generate_short_url():
    # Generate a unique short code
    return secrets.token_urlsafe(6)

@app.route('/shorten', methods=['POST'])
def shorten_url():
    long_url = request.form.get('long_url')
    if not long_url:
        return jsonify({'error': 'Invalid request. Please provide a valid long_url parameter.'}), 400
    
    short_url = generate_short_url()
    url_mapping[short_url] = long_url
    return jsonify({'short_url': f'http://your_domain/{short_url}'})

@app.route('/<short_url>')
def redirect_to_long_url(short_url):
    long_url = url_mapping.get(short_url)
    if not long_url:
        return jsonify({'error': 'Short URL not found'}), 404
    
    return redirect(long_url)

if __name__ == '__main__':
    app.run(debug=True)
