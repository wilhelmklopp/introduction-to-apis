# introduction-to-apis
Introduction to APIs Workshop at CopenHacks 2017

## Pre-workshop instructions
- If you don't already have a twitter account, create one [here](https://twitter.com)
- If you haven't already got Python 3 installed, get it [here](https://www.python.org/downloads/). You can see what your python version is by opening a shell and running `python -V` or `python3 -V`
- Download and install Postman. It's a really cool tool for playing around with APIs. Get it [here](https://www.getpostman.com/)
- Create your own personal Slack team for testing at https://slack.com. (You can choose any team name and username you want. You'll be the only one using this Slack team.)

## Setup Instructions for the demo code
** Don't worry about these steps for now. We'll do them together in the workshop.**
- clone this directory by running `git clone https://github.com/wilhelmklopp/introduction-to-apis.git`
- Run `cd introduction-to-apis`
- Run `cd twitter-streaming`  

- Install the dependencies by running `pip install -r requirements.txt` (this can also be `pip3 install -r requirements.txt` depending on your setup)
- Run `cp .env.example .env`
- Open the `.env` file and input the relevant values, which you can obtain from https://apps.twitter.com after you create an app.  

- Run `demo.py`
