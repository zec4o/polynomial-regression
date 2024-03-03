# Polynomial Regression Model - Salary Predictions 💰

This repository is a project focused on studying Polynomial Regressions and Machine Learning, using Python and some libraries such as Pandas, Seaborn, Pingouin, Streamlit, FastAPI and more... The model aims to provide a salary prediction for professionals based on some independent variables (months_of_service and seniority). Also, the model was trained and tested from a dataset in ./datasets/salary_dataset.csv, from it I've created an API using FastAPI and a basic front-end using streamlit.

## Features

- Data Loading and Cleaning ✨
- Exploratory Data Analysis 📊
- Model Training and Testing ⚙️
- Model Evaluation 📈

## Technologies Used

- Python: A popular programming language known for its simplicity and versatility. It is widely used in data analysis, machine learning, and web development.
- Pandas: A powerful data manipulation library in Python. It provides data structures and functions to efficiently analyze and manipulate structured data.
- Seaborn: A data visualization library based on Matplotlib. It provides a high-level interface for creating informative and attractive statistical graphics.
- Matplotlib: A comprehensive plotting library in Python. It allows users to create a wide variety of static, animated, and interactive visualizations.
- Sklearn: Also known as scikit-learn, it is a machine learning library in Python. It provides a wide range of algorithms and tools for data preprocessing, model selection, and evaluation.
- Pingouin: A statistical package in Python that offers a wide range of statistical tests and functions for analyzing data.
- FastAPI: A modern, fast (high-performance), web framework for building APIs with Python. It is easy to use, highly efficient, and supports asynchronous programming.
- Streamlit: A Python library for building interactive web applications and dashboards for data science and machine learning projects. It simplifies the process of creating and sharing data-driven applications.


## Getting Started

To get started with this project, follow the steps below:

1. Clone the repository:

```bash
git clone https://github.com/zec4o/polynomial-regression.git
```

2. Set-up your python environment:

   - Start by installing [Pipenv](https://pipenv.pypa.io/en/latest/) in your machine.
   - Install the dependencies: 
```bash
pipenv install scikit-learn scipy pandas matplotlib seaborn ipykernel pingouin fastapi pydantic streamlit uvicorn requests
```

3. Start the API:

   - Open your Pipenv shell by running: ```pipenv shell```
   - Run the following command:
     ```bash
     uvicorn api_salary_model:app --reload
     ```

     This command will setup the API in `127.0.0.1:8000`
     </br>
     You'll be able to see the API documentation in `127.0.0.1:8000/docs`

4. Start the Streamlit front-end:

   - In another terminal instance, open you Pipenv shell by running: ```pipenv shell```
   - Run the following command:
    ```bash
    streamlit run front_salary.py
    ```
    This command will setup the front-end in `localhost:8501`

## Contributing

Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, please open an issue on the GitHub repository.

## License

This project was designed based on a Rocketseat class and it's licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code for personal or commercial purposes.
