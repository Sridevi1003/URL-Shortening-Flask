from flask import Flask, render_template, request, redirect
import random
import string

app = Flask(__name__)
url_mapping = {}


def generate_alias():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.form['long_url']
    custom_alias = request.form['custom_alias']

    if custom_alias:
        alias = custom_alias
    else:
        alias = generate_alias()

    url_mapping[alias] = long_url

    return render_template('result.html', alias=alias)


@app.route('/<alias>')
def redirect_to_original(alias):
    if alias in url_mapping:
        return redirect(url_mapping[alias])
    else:
        return render_template('not_found.html')


if __name__ == '__main__':
    app.run(debug=True)
