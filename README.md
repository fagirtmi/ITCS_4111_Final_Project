# ITCS 4111 Final Project
**Developers:** 

`Fatih Agirtmis` * Email: fagirtmi@uncc.edu

`Jacqueline White` * Email: jwhit241@uncc.edu 

**Description:** This repository contains the codebase and instructions on how to run BOT_49 locally on your machine. If you have any questions please reach out to Fatih or Jacqueline

## Hosted Web App: 

The application is hosted using Heroku and can be visted from this link <https://chatbot-49.herokuapp.com/>

## Running it Locally:

**Project Structure:**

**Virtual:** 
Folder contains the packages and libraries needed to run the chatbot. 

**Templates:**  
Folder contains the html for the bot

**Intents:**  
Folder contains the python classes used to interact with Google's API and DialogFlow

`directions_intent:` responsible for getting the directions from Google's Map API

`picture_intent:` responsible for getting pictures from Google's Map API

**Static:**  Folder contains several classes

`custom.js` - javascript class which is responsible for the front-end

`style.cc` - stylesheet that is responsible for the styling on the front-end 

`images` - folder that is responsible for containing the images used in the front-end

**Other Notable Files:**

`env.sh` - file contains important enviromental variables needed to run the bot and connect to DialogFlow & Google's Map API

`index.py` - main python file that is responsible for redirecting the server side to load pages, get data, and return events

### Step 1:

Download and unzip the project to a location of your choosing. 

### Step 2:

Change into the project root directiory and run the command `. env.sh ` to set the enviromental variables on your machine 

### Step 3:

Run the command `source virtual/bin/activate` to get into your virtual enviroment 

### Step 4:

Once you are into the virtual enviroment, run the command `pip install -r requirements.txt` to download all your dependicies 

### Step 5:

After the dependencies have been installed, run `flask run` to run the app locally 





