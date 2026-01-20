<p align="center">
  <img width="500" height="150" alt="1000190474" src="https://github.com/user-attachments/assets/8b0fabf4-ff9a-44c1-8c6a-5dfdeb6e7128" />
</p>

# pystruct

A lightweight Python CLI tool to automate your project folder structure creation. With one command, you can set up scaffolding for Web, Machine Learning, Data Science, and more.

## Installation

Since this project is in development, you can install it locally:

1. Clone this repository or download the source code.
2. Navigate to the project folder.
3. Run:
   ```bash
   pip install -e .
   

## Usage

Run the following command in your terminal:

```bash
pystruct [type] [name]

```

### Available Templates:

* `pystruct web`: Creates a modern web application structure (src, static, templates, etc.).
* `pystruct ml`: Creates a Machine Learning project structure (Training, Testing, models).
* `pystruct ds`: Creates a Data Science structure (data, notebooks, scripts).
* `pystruct script`: Creates a simple Python script setup with logging.
* `pystruct lib <name>`: Scaffolds a new Python library project.
* `pystruct pract <categories>`: Create a structure to practice or learn programming language.

## Project Structure

This tool follows standard Python packaging practices:

* `main.py`: Core logic for file and folder creation.
* `cli.py`: Command-line interface handling.

## Footage:
<img width="1920" height="1080" alt="Screenshot (1179)" src="https://github.com/user-attachments/assets/c85e2b7a-c4fa-456e-a1e7-d929047c7529" />

## License

This project is licensed under the MIT LICENSE.
