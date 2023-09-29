from flask import Flask, render_template, redirect

app = Flask(__name__)
socials = {
    "github": "https://github.com/obosky",
    "organization": "https://coconut.or.id",
    "website": "https://obosky.githib.io",
    "discord": "https://discord.gg/K2u3BVJs",
    "email": "obococonut@gmail.com"
}

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/<string:social>")
def media(social: str):
    print(1)
    return redirect(socials.get(social, "https://obosky.githib.io"))

if __name__ == "__main__":
    app.run(debug = True)