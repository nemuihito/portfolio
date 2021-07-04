from flask import Flask, request
from flask_mail import Mail, Message
from flask_cors import CORS
from PIL import Image
from email import charset

charset.add_charset('utf-8', charset.SHORTEST, charset.BASE64, 'utf-8')

app = Flask(__name__)
mail = Mail(app)
CORS(app)

app.config['MAIL_SERVER']='mail71.onamae.ne.jp'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'info@akaboir-mitsumori.com'
app.config['MAIL_PASSWORD'] = '$sY5rEqS'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/', methods=['POST'])
def index():
    file = request.files['nimotsu-image']
    pil_img = Image.open(file)
    if pil_img.width >= 2000:
        pil_img = pil_img.resize((pil_img.width // 3, pil_img.height // 3))
    pil_img.save('onimotsu.png', quality=70)
    if request.form["item-radio-2"] == "true":
        item2_text = "20km以下"
    else:
        item2_text = request.form["item-number-2"] + "km"
    nimotsu_str = ""
    for counter in range(18):
        try:
            nimotsu_str = nimotsu_str + request.form["nimotsu_name"+str(counter)] + "　"
            nimotsu_str = nimotsu_str + request.form["nimotsu_quantity"+str(counter)] + "<br>"
        except:
            break
    if request.form["street_address_ev"] == "true":
        street_address_ev = "有"
    else:
        street_address_ev = "無"
    if request.form["moving_street_address_ev"] == "true":
        moving_street_address_ev = "有"
    else:
        moving_street_address_ev = "無"
    msg = Message("{0} {1}様お見積りありがとうございます".format(request.form["last_name"], request.form["first_name"]), sender = 'info@akaboir-mitsumori.com', recipients = [request.form["mail_adress"]])
    msg.html = ("このメールは{0} {1}({2} {3})様に送られています。<br>\
        以下の内容でお見積りを承りました。<br><br>\
            お客様の電話番号 {18} ※こちらに後日お電話させていただきます<br><br>\
                作業時間 {8} ￥{4}<br>\
                    運送距離 {9} ￥{5}<br>\
                        合計金額 ￥{6}<br><br>\
                            運びたい荷物<br><br>\
                                {7}<br>\
                                    お荷物の写真<br>\
                                        <img src='cid:Myimage' /><br><br>\
                                            現在お住いの住所<br>\
                                                {10} {11}階 エレベーター{12}<br>\
                                                    建物の形態 {16}<br><br>\
                                                        引っ越し先住所<br>\
                                                            {13} {14}階 エレベーター{15}<br>\
                                                                建物の形態 {17}<br><br>\
                                                                    赤帽アイアール<br>\
                                                                        代表者名  宮本 崇志<br>\
                                                                            会社所在地  〒004-0866 札幌市清田区北野6条１丁目４－８<br>\
                                                                                電話番号  011-886-8646<br>\
                                                                                    FAX  	011-886-8655<br>\
                                                                                        直通番号  090-3772-2627 (至急のご用件の場合はコチラ)".format(request.form["last_name"], request.form["first_name"],\
                                                                                            request.form["last_name_yomi"], request.form["first_name_yomi"],\
                                                                                                request.form["item1_value"], request.form["item2_value"], request.form["total"],\
                                                                                                    nimotsu_str, request.form["item1_text"], item2_text, \
                                                                                                        request.form["street_address"], request.form["street_address_num"], street_address_ev, \
                                                                                                            request.form["moving_street_address"], request.form["moving_street_address_num"], moving_street_address_ev, \
                                                                                                                request.form["build-name-old"], request.form["build-name-new"], \
                                                                                                                    request.form["tel_number"]))
    msg2 = Message("{0} {1}様よりお見積りが届きました。".format(request.form["last_name"], request.form["first_name"]), sender = 'info@akaboir-mitsumori.com', recipients = ['info@akaboir-mitsumori.com'])
    msg2.html = ("お客様氏名 {0} {1}({2} {3}) 様<br>\
        以下の内容でお見積りを承りました。<br><br>\
            お客様の電話番号 {18}<br><br>\
                作業時間 {8} ￥{4}<br>\
                    運送距離 {9} ￥{5}<br>\
                        合計金額 ￥{6}<br><br>\
                            運びたい荷物<br><br>\
                                {7}<br>\
                                    お荷物の写真<br>\
                                        <img src='cid:Myimage' /><br><br>\
                                            現在お住いの住所<br>\
                                                {10} {11}階 エレベーター{12}<br>\
                                                    建物の形態 {16}<br><br>\
                                                        引っ越し先住所<br>\
                                                            {13} {14}階 エレベーター{15}<br>\
                                                                建物の形態 {17}<br><br>\
                                                                    赤帽アイアール<br>\
                                                                        代表者名  宮本 崇志<br>\
                                                                            会社所在地  〒004-0866 札幌市清田区北野6条１丁目４－８<br>\
                                                                                電話番号  011-886-8646<br>\
                                                                                    FAX  	011-886-8655<br>\
                                                                                        直通番号  090-3772-2627 (至急のご用件の場合はコチラ)".format(request.form["last_name"], request.form["first_name"],\
                                                                                            request.form["last_name_yomi"], request.form["first_name_yomi"],\
                                                                                                request.form["item1_value"], request.form["item2_value"], request.form["total"],\
                                                                                                    nimotsu_str, request.form["item1_text"], item2_text, \
                                                                                                        request.form["street_address"], request.form["street_address_num"], street_address_ev, \
                                                                                                            request.form["moving_street_address"], request.form["moving_street_address_num"], moving_street_address_ev, \
                                                                                                                request.form["build-name-old"], request.form["build-name-new"], \
                                                                                                                    request.form["tel_number"]))
    
    with app.open_resource("onimotsu.png") as fp:
        msg.attach("onimotsu.png", 'image/png', fp.read(), 'inline', headers=[['Content-ID', '<Myimage>']])
        msg2.attach("onimotsu.png", 'image/png', fp.read(), 'inline', headers=[['Content-ID', '<Myimage>']])
    with app.app_context():
        mail.send(msg)
        mail.send(msg2)
    # print(request.form)
    return "Sent"

if __name__ == '__main__':
    app.run(debug=True)