from flask import Blueprint, render_template, abort, request, jsonify

lab9 = Blueprint('lab9', __name__)

@lab9.route('/lab9/')
def main():
    return render_template('/lab9/index.html')


@lab9.app_errorhandler(404)
def not_found(e):
    return render_template('/lab9/error_404.html'), 404


@lab9.route('/lab9/500')
def server_error():
    # Генерируем ошибку 500, вызывая деление на ноль
    1 / 0


@lab9.app_errorhandler(500)
def internal_server_error(e):
    return render_template('/lab9/error_500.html'), 500
    

@lab9.route('/lab9/card', methods=['GET'])
def greeting_card():
    recipient_name = request.args.get('recipient_name')
    recipient_gender = request.args.get('recipient_gender')
    sender_name = request.args.get('sender_name')

    return render_template('/lab9/card.html', recipient_name=recipient_name, recipient_gender=recipient_gender, sender_name=sender_name)