from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')


@app.route('/upload/', methods=['GET', 'POST'])
def upload():
    return render_template('index.html')
    # try:
    #     imagefile = request.files.get('imagefile', '')
    #     #create byte stream from uploaded file
    #     file = request.files['imagefile'].read() ## byte file
    #     img = Image.open(imagefile)
    #     img1 = img.convert('LA')
    #     print("Before reducing",img1.size)
    #     imgsize=len(file) >> 20
    #     if imgsize>2:
    #         x, y = img1.size
    #         x *= REDUCTION_COEFF
    #         y *= REDUCTION_COEFF
    #         img1 = img1.resize((floor(x),floor(y)), Image.BICUBIC)
    #         print("Img reduced",img1.size)
    #     ext = "jpeg"
    #     if "." in imagefile.filename:
    #         ext = imagefile.filename.rsplit(".", 1)[1]
    #     text = pytesseract.image_to_string(img1)
    #     #Base64 encoding the uploaded image 
    #     img_base64 = base64.b64encode(file)
    #     img_base64_str = str(img_base64)
    #     #final base64 encoded string
    #     img_base64_str = "data:image/"+ ext +";base64,"+img_base64_str.split('\'',1)[1][0:-1]
    #     f = open("sample.txt", "a")
    #     f.truncate(0)
    #     f.write(text)
    #     f.close()
    #     return render_template('result.html', var=text,img=img_base64_str)
    # except Exception as e:
    #     print(e) 
    #     return render_template('error.html')