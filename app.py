import openai
import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template


# load the api key
load_dotenv()
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

#add this openai key inside my openai key
openai.api_key=OPENAI_API_KEY


#initialize the flask
app = Flask(__name__)


# audio will be upload in static folder
app.config["UPLOAD_FOLDER"]="static"


#create the route look for 2 kinds of req get and post
@app.route("/", methods=["GET","POST"])

#if this match then it will execute this main function
def main():
    # if the req is post then
    if request.method =="POST":
        #take the language input 
        language= request.form["language"]

        #get the file
        file= request.files["file"]

        # if file is present or not check
        if file:  # save in static folder
            filename=file.filename   #give the file name
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))

           # load the audio
            audio_file =open("static/recorded.mp3","rb")
            transcript=openai.Audio.translate("whisper-1",audio_file)


            # now using the gpt-4 model convert to the transilation 
            response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages = [{ "role": "system", "content": f"You will be provided with a sentence in English, and your task is to translate it into {language}" }, 
                                { "role": "user", "content": transcript.text }],
                    temperature=0,
                    max_tokens=256
                  )
            
            return jsonify(response)
    

    # if it is get req then noly render the web app
    return render_template("index.html")



#run on that post
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8080)
        
    

