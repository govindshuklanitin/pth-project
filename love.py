from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Special message for Divya
message = """Divya, tum meri zindagi ka woh hissa ho jo har din ko roshan aur har lamhe ko khaas bana deta hai.
Tumhari muskurahat meri duniya ka sabse haseen nazara hai, aur tumhari awaaz ek aisi madhur dhun jo mere dil ko sukoon deti hai.
Tum sirf meri mohabbat nahi, meri rooh ka ek hissa ho. Har pal, har saans tumhare naam hai.
Tum jo ho, bas waise hi hamesha raho, kyunki tumse behtar kuch ho hi nahi sakta."""

@app.route('/', methods=['GET', 'POST'])
def love_message():
    if request.method == 'POST':
        user_input = request.form.get('love_input')
        if user_input.lower() == "nitin ka dill":
            return render_template('result.html', message=message)
        else:
            return render_template('result.html', message="😔 Lagta hai tumhe meri yaad nahi aayi 😔")
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=5000, debug=True)

 
