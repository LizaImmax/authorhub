# app.py
from flask import Flask, render_template,request, redirect, url_for, session, flash 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about' , methods=['GET', 'POST'])
def about():
    return render_template('about.html')

@app.route('/books' , methods=['GET', 'POST'])
def books():
    return render_template('books.html')

@app.route('/book_detail/<int:book_id>')
def book_detail(book_id):
    # Logic to fetch book details based on book_id
    return render_template('book_detail.html')

@app.route('/blog' , methods=['GET', 'POST'])
def blog():
    return render_template('blog.html')

@app.route('/contact' , methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')

@app.route('/events' , methods=['GET', 'POST'])
def events():
    return render_template('events.html')

@app.route('/media_kit' , methods=['GET', 'POST'])
def media_kit():
    return render_template('media_kit.html')

@app.route('/testimonials' , methods=['GET', 'POST'])
def testimonials():
    return render_template('testimonials.html')

@app.route('/newsletter_signup' , methods=['GET', 'POST'])
def newsletter_signup():
    return render_template('newsletter_signup.html')

@app.route('/404' , methods=['GET', 'POST'])
def page_not_found():
    return render_template('404.html'), 404

@app.route('/privacy_policy' , methods=['GET', 'POST'])
def privacy_policy():
    return render_template('privacy_policy.html')

@app.route('/terms_of_service' , methods=['GET', 'POST'])
def terms_of_service():
    return render_template('terms_of_service.html')

@app.route('/shop' , methods=['GET', 'POST'])
def shop():
    return render_template('shop.html')  # You can implement this page for merchandise listings

@app.route('/bookclub_signup' , methods=['GET', 'POST'])
def bookclub_signup():
    return render_template('bookclub_signup.html')

if __name__ == '__main__':
    app.run(debug=True)
