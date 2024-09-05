# Recipe Search Application

This is a Flask-based web application that allows users to search for recipes using a third-party API. The application takes a user query (e.g., "chicken pasta") and displays a list of recipe results fetched from the API. The application also includes a route to simulate the deletion of a recipe.

## Features
- Search for recipes by entering a query.
- Display a list of recipes fetched from a public recipe API.
- Simulate recipe deletion with an API route.
  
## Table of Contents
- [Features](#features)
- [Technologies](#technologies)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Clone the Repository](#clone-the-repository)
  - [Setting up Environment Variables](#setting-up-environment-variables)
  - [Installing Dependencies](#installing-dependencies)
  - [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [API](#api)
- [License](#license)

## Technologies
- **Python**: Flask, Requests
- **HTML**: For the frontend rendering of search results
- **API**: A third-party recipe API (e.g., Edamam)

## Prerequisites
Before running the project, make sure you have the following installed:
- Python 3.x
- pip (Python package manager)
- A GitHub account (to clone the repository)


### Explanation of the Key Sections:

1. **Project Overview**: Briefly describes what the project does and its features.
   
2. **Technologies**: Lists the major technologies used, including Python (Flask and Requests), HTML for templates, and the third-party recipe API.

3. **Getting Started**: 
   - Instructions on how to set up the project (cloning the repo, setting up API keys, installing dependencies, and running the application).
   - Specific instructions for environment variables and `config.py`.

4. **Project Structure**: Provides an overview of how the files are organized within the project.

5. **API**: Describes the available API endpoints for searching and deleting recipes.

6. **License**: Specifies the license under which the project is released (MIT in this case, but you can change it).

### Before Committing:
- Make sure to create a `.gitignore` file to exclude sensitive files like `config.py`.
- If your project does not yet have a `requirements.txt`, you can create it using:
   ```bash
   pip freeze > requirements.txt


## Getting Started

### Clone the Repository
First, clone the project repository from GitHub to your local machine:
```bash
git clone https://github.com/varun021/Recipe-Book.git
cd Recipe-Book
