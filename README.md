# Welcome to the Warp Design Challenge for Engineering Week 2025!

## Challenge Description

**Oh no! We found this jumbled up Github Repo and it seems to be a website locked down by a (very secure) password. Can you help us crack it?**</br>

Get ready for takeoff as we travel through this repository and correct all the errors which prevent our journey. This repository used to host a website using a Express.js frontend and Flask backend that shows you the Engineering Week 2025 logo when you gave it the right password, but invaders from Spartaverse have came in and wreaked havoc! Using the power of [Warp](https://www.warp.dev/) and your engineering mindset, fix up this repository so we can blast off to new horizons!</br> 

You will find many bugs in this repository preventing you from accessing the goal. This can be anything up to and including:</br>
- *merge conflicts between 'main' and 'dev' branches*</br>
- *syntax errors*</br>
- *misnamed functions and variables*</br>
*and more!*</br>
</br>
Additionally, in order to show the Engineering Week logo at the end, you're going to need to enter a password which is lost in space! Fortunately, when you access the webpage being hosted by the Flask backend, you will be directed to a page full of riddles to solve to get the password!

## The Goal
***Debug the entire repository so that you're able to <ins>properly merge main and dev</ins>, <ins>see the riddles on the backend</ins>, and <ins>get the Engineering Week logo to show up when accessing the webpage!</ins>***</br>
In order to win, you must show us both <ins>the website itself working</ins> (see below) and <ins>what you have set as your password</ins> (`PW` in `app.py`).

**IMPORTANT NOTE:** The only files you'll need to fix are `app.py`, `index.html`, and `server.js`! <ins>NOTHING</ins> is wrong with the other files in this repository. :)

![What you need to show us to show that you won!](/proof.png)

## Instructions
*Before you begin, make sure you have an <ins>IDE</ins> ([VS Code](https://code.visualstudio.com/download)), <ins>[Git](https://git-scm.com/downloads)</ins>, and <ins>[Python 3.13.1](https://www.python.org/downloads/release/python-3131/)</ins> set up on your device. You will be needing these to clone this repository and debug the programs!*

### Clone the repository.
Open up VS Code and open a new terminal (``Ctrl+Shift+` ``in VS Code on Windows). Navigate to a directory that you want to store the repository files in. For sake of ease, we'll navigate to the Desktop:
```
cd Desktop
```
Next, we'll clone the repository into this directory using the following:
```
git clone https://github.com/Wag-Jack/EW_DC_2025.git
```
Now you can open the cloned repository through a folder on your Desktop! To open this folder in VS Code, type `Ctrl+K` `Ctrl+O`, find the folder in your Desktop folder, and hit `Select Folder`. Now you have the repository on your local machine, and we can set up everything else to get you debugging! Make sure you keep this terminal open, as we're going to need it for the next steps!

### Python (Flask) / Backend Setup
Start by ensuring you are running a virtual environment in the backend directory. In your terminal, type the following to go to the backend directory:
```
cd backend
```
Next, run the following to create your virtual environment:
```
python -m venv venv
```
Then, depending on what you system is, use the following script to activate the virtual environment:</br>
**Windows:**
```
.\venv\Scripts\activate
```
*If you're having any issues running the virtual environment on Windows, execute the following command to change your terminal's execution policy:*
```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```
**macOS/Linux:**
```
source venv/bin/activate
```
Now we're able to install everything we need to get rolling! All of our Python libraries (including Flask) are included in `requirements.txt`, so we'll install them all at once:
```
pip install -r requirements.txt
```
Once this is done, you should be able to import from `flask` and `flask-cors`. This means that your backend is configured! (minus the bugs...)

### Express.js / Frontend Setup
Ensure that you downloaded and ran the Node.js installer from their [official website](https://nodejs.org/en/download). Once this is done, **open a new terminal** and enter the `frontend` directory:
```
cd frontend
```
To initialize your dependencies, run the following command once in the `frontend` directory:
```
npm init -y
```
You should now have a package.json file with all the dependencies needed! Now, run the following to get the necessary requirements downloaded:
```
npm install
```
Now that you have everything installed, it's time to start debugging!

### Running The Website
When testing to see if everything works, you need to run the Flask (`backend`) server and the Express.js (`frontend`) servers at the same time so they are communicating with one another. To run these scripts, do the following ***in seperate terminals:***</br>
**In your `backend` directory, execute this script in your terminal:**
```
python app.py
```
You should get the following output:
```
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead. a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```
Accessing `https://127.0.0.1:5000` (`Ctrl + Click` on the address) will let you see the riddles you need to solve for the password!</br>

**In your `frontend` directory, execute this script in your terminal:**
```
node server.js
```
You should get the following output:
```
Express server running at http://localhost:3000
```
Accessing `https://localhost:3000` (`Ctrl + Click` on the address) will let you access the password submission screen. Here you can enter the password and, if correct, the Engineering Week logo will show up!</br>
</br>
**Good luck, and happy hacking!**