# Dashboard IDT

## Introduction

This application has been developed using **Python**, mainly the **Dash Framework**. We suggest to deploy it in a **RHEL ** **based operating system**, however it is possible to deploy it using other O.S, this guide and the elements provided to make this process easier may not work that well.

## Setup

We provided a nice **bash** script to initialize the *production environment* for the application, this file is *setup* and in order to run it use the code below.

```bash
# Move to the project's folder
cd DS4A-T9 # You need to place your path

# Give execution permission
chmod +x setup

# Run the script
./setup
```

Once you have done this, it's pretty important that before launching the application you launch the *virtual environment* using `source venv/bin/activate`, otherwise the application will not find the required dependencies.

## Running

### Manual deployment

Now that you have already set up the environment for the application to run properly, we provided a script *deploy_app*, just run `./deploy_app.sh` and it will launch instantly.

### Cloud based assistant

The application has a *Procfile* that defines properties that tools used by cloud providers can easily use to launch the application. With that said, below you can find how to deploy the application using different providers.

* [Heroku](https://dash.plotly.com/deployment)
  * Be aware to initialize a complete new repository when using this alternative
* [AWS](https://austinlasseter.medium.com/deploying-a-dash-app-with-elastic-beanstalk-console-27a834ebe91d)
  * *You might have to meet costs.*

## Authors

### DS4A Cohort 5 - Team 9

* Alberto Cortes
* Elizabeth Rendon
* Kelly Garcia
* Paul Moros
* Sergio Rairan



