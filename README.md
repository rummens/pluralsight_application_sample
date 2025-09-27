# Pluralsight Application Sample

Sample Python application wrapped in a container to show the benefits containers can bring in terms of portability.

## Features

- Simple Flask web app that displays:
    - A greeting message
    - A toggleable list of installed Python packages (using `pip freeze`)
    - The build timestamp of the container image (from `/app/timestamp.txt`)
    - An error message if the timestamp file is missing

## How It Works

- The app is built into a container using a `Containerfile`.
- On build, the current date/time is written to `/app/timestamp.txt`.
- When running, the app reads and displays this timestamp.
- All dependencies are installed from `requirements.txt`.

## Running the App in a Container

1. Build the container image: `docker build -t pluralsight-app -f Containerfile .`
2. Run the container: `docker run -d -p 8080:8080 pluralsight-app`
3. Access the app at `http://localhost:8080`

## Purpose

This project demonstrates how containers can package Python applications with all dependencies and metadata, making them
easy to run anywhere.