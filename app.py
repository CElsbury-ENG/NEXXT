from flask import Flask, render_template, redirect, url_for, request
from itsdangerous import URLSafeSerializer
from forms import ResponseForm
from excel_utils import append_response

app = Flask(__name__)
app.config['SECRET_KEY'] = 'replace_with_random_secret'

serializer = URLSafeSerializer(app.config['SECRET_KEY'], salt='form-link')

@app.route('/')
def index():
    # Generate a one-time form link token
    token = serializer.dumps({'sheet': 'Sheet1'})
    form_url = url_for('fill_form', token=token, _external=True)
    return f'<a href="{form_url}">Fill Out the Form</a>'

@app.route('/form/<token>', methods=['GET', 'POST'])
def fill_form(token):
    try:
        data = serializer.loads(token)
    except Exception:
        return "Invalid or expired link", 400

    form = ResponseForm()
    if form.validate_on_submit():
        resp = {
            'name': form.name.data,
            'email': form.email.data,
            'comments': form.comments.data
        }
        append_response(resp)
        return "Thank you! Your response has been recorded."
    return render_template('form.html', form=form)