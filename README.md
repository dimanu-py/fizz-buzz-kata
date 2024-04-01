# 🐝 FizzBuzz Kata 🐝

[![Python](https://img.shields.io/badge/Python-3.11+-yellow?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)](https://python.org)

## Resources

These requirements and the step to step on how to start applying TDD can be found in Codurance website linked below.

[![Web](https://img.shields.io/badge/Codurance-Website-14a1f0?style=for-the-badge&logo=web&logoColor=white&labelColor=101010)](https://www.codurance.com/katas/fizzbuzz)

## Description
  
Write a function that:
- Takes numbers from 1 to 100 
- Outputs them as strings
- For multiples of 3, it returns "Fizz" instead of the number
- For multiples of 5, it returns "Buzz" instead of the number
- For numbers that are multiples of both 3 and 5, it returns "FizzBuzz"

## Objective

The main objective of this kata is to learn how to apply TDD. The following concepts will be applied:

- Red-Green-Refactor cycle
- Baby steps
- Test parametrization

## Configuration

The project can be configured either by using `pip` or `pipenv`. Both ways will be explained.

<details><summary>Using pip</summary>

1. Create a virtual environment:
    ```bash
    python -m venv .venv
    ```
2. Activate the virtual environment:
    ```bash
    source .venv/bin/activate # Linux / Mac
    .venv\Scripts\activate # Windows
    ```
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
</details>

<details><summary>Using pipenv</summary>

1. Install pipenv:
    ```bash
    pip install pipenv
    ```
2. Create a virtual environment with desire python version
    ```bash
    pipenv --python 3.11
    ```
   
    By default it will create the virtual environment outside the project. To create it inside the project, use the following command:
    ```bash
    PIPENV_VENV_IN_PROJECT=1 pipenv --python 3.11
    ```
3. Install the dependencies:
    ```bash
    pipenv install
    ```
</details>

## Running the tests

To run the tests, execute one of the following commands:

```bash
pytest
```

or

```bash
pipenv run test
```

### Visit my GitHub profile for more projects 🚀

[![Web](https://img.shields.io/badge/GitHub-Dimanu.py-14a1f0?style=for-the-badge&logo=github&logoColor=white&labelColor=101010)](https://github.com/dimanu-py)

