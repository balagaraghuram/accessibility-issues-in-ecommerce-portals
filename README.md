# Accessibility Analysis Web Application

This Flask-based web application performs accessibility analysis using a TensorFlow model and a simple logistic regression model. It allows users to input features related to accessibility and provides predictions based on the trained models.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Models](#models)
- [Routes](#routes)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project implements a web application for accessibility analysis. It uses Flask as the web framework and integrates a TensorFlow model for predictions based on input features related to accessibility. Additionally, a simple logistic regression model is used to provide statistical insights into the data.

## Installation

To run this project locally, follow these steps:

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. **Install Required Packages:**
    ```bash
    pip install -r requirements.txt
    ```

   Make sure to replace `requirements.txt` with the actual file containing necessary dependencies.

## Usage

1. **Run the Flask Application:**
    ```bash
    python app.py
    ```

   This command starts the Flask development server. Navigate to `http://localhost:5000` in your web browser to access the application.

2. **Input Data for Analysis:**

   - Visit the main page (`/`) to input features related to accessibility.
   - Submit the form to `/analyze` for predictions.

## Models

- **TensorFlow Model:**
    - The TensorFlow model (`your_model_path`) is loaded using `tf.keras.models.load_model()`. This model is used to predict accessibility based on user input.

- **Statistical Model:**
    - A logistic regression model is trained using `sklearn.linear_model.LogisticRegression()` on dummy data (`accessibility_data` and `accessibility_labels`). It provides additional statistical insights into the data.

## Routes

- **`/` (Main Page):**
    - Renders `index.html` where users can input features for accessibility analysis.

- **`/analyze` (POST Method):**
    - Processes user input from the form on the main page.
    - Uses the TensorFlow model to predict accessibility.
    - Uses the statistical model to provide additional predictions and insights.
    - Renders `result.html` with the predictions.

## Contributing

Contributions are welcome! If you have any improvements or suggestions, please fork this repository, make your changes, and submit a pull request. Ensure your code adheres to the existing style and includes relevant documentation.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
