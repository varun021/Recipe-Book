# Recipe Book

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Setup and Installation](#setup-and-installation)
5. [Usage](#usage)
6. [API Integration](#api-integration)
7. [Frontend](#frontend)
8. [Backend](#backend)
9. [Error Handling](#error-handling)
10. [Future Enhancements](#future-enhancements)
11. [Contributing](#contributing)
12. [License](#license)

## Introduction

Recipe Book is a web application that allows users to search for recipes using an external API. Users can view detailed recipe information, including ingredients, nutritional facts, and cooking instructions. The application also provides features like recipe deletion and social media sharing.

## Features

- Recipe search functionality
- Detailed recipe view with ingredients and nutritional information
- Delete recipe option
- Responsive design for various screen sizes
- Social media integration in footer
- Dynamic content loading

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python with Flask framework
- **API**: Edamam Recipe Search API
- **Additional Libraries**: Font Awesome for icons

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/recipe-book.git
   ```

2. Navigate to the project directory:
   ```
   cd recipe-book
   ```

3. Install required Python packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the root directory
   - Add your API credentials:
     ```
     API_ID=your_api_id
     API_KEY=your_api_key
     API_URL=https://api.edamam.com/search
     ```

5. Run the application:
  
   python app.py
  

6. Open a web browser and go to `http://localhost:5000`

## Usage

1. On the homepage, enter a recipe name or ingredients in the search bar.
2. Click the "Search" button or press Enter.
3. Browse through the search results.
4. Click on a recipe card to view more details.
5. Use the delete button (X) to remove a recipe from the results.

## API Integration

This application uses the Edamam Recipe Search API. To use the API:

1. Sign up for an account at [Edamam](https://developer.edamam.com/edamam-recipe-api)
2. Obtain your API ID and API Key
3. Replace the placeholder credentials in the `.env` file with your actual credentials

## Frontend

The frontend is built with HTML, CSS, and JavaScript. Key components include:

- Responsive design using CSS flexbox
- Dynamic content loading with JavaScript
- Font Awesome icons for enhanced UI

## Backend

The backend is powered by Flask, a Python web framework. It handles:

- API requests to Edamam
- Routing and serving HTML templates
- Processing form submissions
- Implementing the delete functionality

## Error Handling

- The application includes basic error handling for API requests
- User-friendly messages are displayed when no results are found
- Console logging for debugging purposes

## Future Enhancements

- User accounts and recipe saving functionality
- Advanced search filters (dietary restrictions, cuisine type, etc.)
- Recipe rating system
- Implement proper logging instead of print statements
- Add unit tests for backend functionality

## Contributing

Contributions to improve Recipe Book are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` file for more information.
