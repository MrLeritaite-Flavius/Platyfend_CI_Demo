from flask import Blueprint, request, render_template_string

main_blueprint = Blueprint('hello', __name__)


@main_blueprint.route("/")
def main_page():
    template = f'''
        <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Meme Keeper</title>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        margin: 0;
                        padding: 0;
                        background-color: #f0f0f0;
                    }}
                    .container {{
                        width: 80%;
                        margin: 200px auto;
                        text-align: center;
                        padding: 4% 0;
                    }}
                    h1 {{
                        color: #333;
                    }}
                    p {{
                        color: #666;
                        margin-bottom: 20px;
                    }}
                    .button {{
                        display: inline-block;
                        padding: 10px 20px;
                        background-color: #007bff;
                        color: #fff;
                        text-decoration: none;
                        border-radius: 5px;
                        transition: background-color 0.3s ease;
                    }}
                    .button:hover {{
                        background-color: #0056b3;
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>Welcome {request.args.get('name', '')}!</h1>
                    <p>We hope you will have a good experience browsing our website! Please feel free to join our family by clicking the button below and start sharing your memes with the world! :D</p>
                    <a href="/register" class="button">Register</a>
                </div>
            </body>
            </html>
    '''
    return render_template_string(template)
