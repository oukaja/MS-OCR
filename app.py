import os

from flask import Flask, render_template, request, jsonify

from utils.ocr_card import ocr_id_card
from utils.ocr_pay import ocr_pay
from utils.ocr_paie import ocr_paie


UPLOAD_FOLDER = '/static/uploads/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'cin_front' not in request.files or 'cin_back' not in request.files or 'pay' not in request.files or 'paie' not in request.files:
            return render_template('upload.html', msg='No file selected')
        cin_front = request.files['cin_front']
        cin_back = request.files['cin_back']
        pay_sheet = request.files['pay']
        paie_sheet = request.files['paie']

        # if user does not select file, browser also
        # submit a empty part without filename
        if cin_front.filename == '' or cin_back.filename == '' or pay_sheet.filename == '' or paie_sheet.filename == '':
            return render_template('upload.html', msg='No file selected')

        if cin_front and allowed_file(cin_front.filename) and cin_back and allowed_file(cin_back.filename) and pay_sheet and allowed_file(pay_sheet.filename) and  paie_sheet and allowed_file(paie_sheet.filename):
            cin_front.save(os.path.join(os.getcwd() + UPLOAD_FOLDER, cin_front.filename))
            cin_back.save(os.path.join(os.getcwd() + UPLOAD_FOLDER, cin_back.filename))
            pay_sheet.save(os.path.join(os.getcwd() + UPLOAD_FOLDER, pay_sheet.filename))
            paie_sheet.save(os.path.join(os.getcwd() + UPLOAD_FOLDER, paie_sheet.filename))

            # call the OCR function on it
            id_card = ocr_id_card(os.getcwd() + UPLOAD_FOLDER, cin_front, cin_back)
            pay = ocr_pay(os.getcwd() + UPLOAD_FOLDER, pay_sheet)
            paie = ocr_paie(os.getcwd() + UPLOAD_FOLDER, paie_sheet)

            # extract the text and display it
            return render_template('upload.html',
                                   msg='Successfully processed',
                                   id_card=id_card,
                                   pay=pay,
                                   paie = paie,
                                   cin_front_img=UPLOAD_FOLDER + cin_front.filename,
                                   cin_back_img=UPLOAD_FOLDER + cin_back.filename,
                                   pay_img=UPLOAD_FOLDER + pay_sheet.filename,
                                   paie_img=UPLOAD_FOLDER + paie_sheet.filename)
    elif request.method == 'GET':
        return render_template('upload.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
