from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        a = request.form.get("Name")
        b = request.form.get("S/o")
        c = request.form.get("Address")
        d = request.form.get("Email")
        f = request.form.get("phone")
        g = request.form.get("Education")
        h = request.form.get("Skills")
        i = request.form.get("Experience")
        j = request.form.get("Hobbies")
        k = request.form.get("lks")
        l = request.form.get("lkw")

        return render_template("resume.html", name=a, S=b, Address=c, Email=d, Phone_number=f,
                               EQ=g, Skills=h, Experience=i, Hobbies=j, LCS=k, LCW=l)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
