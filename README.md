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

## Getting Started

### Clone the Repository
First, clone the project repository from GitHub to your local machine:
```bash
git clone https://github.com/varun021/Recipe-Book.git
cd Recipe-Book
