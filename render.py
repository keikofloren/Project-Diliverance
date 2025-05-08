from flask import Flask, render_template
import os

app = Flask(__name__)

def render_and_save(template_name, filename):
    html = render_template(template_name)
    with open(os.path.join('output', filename), 'w') as f:
        f.write(html)

if __name__ == "__main__":
    output_dir = './output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    templates = [
        ('index.html', 'index.html'),
        ('about.html', 'about.html'),
        ('events.html', 'events.html'),
        ('team.html', 'team.html'),
        ('donate.html', 'donate.html')
    ]

    with app.app_context():
        for template, filename  in templates:
            render_and_save(template, filename)