import sys
from pathlib import Path

def ml():
    train_c = """
# Training entry point.

def main():
    pass  #training logic here

if __name__ == "__main__":
    main()
"""
    eval_c = """
# Evaluation entry point.

def main():
    pass  #evaluation logic here
    
if __name__ == "__main__":
    main()
"""
    test_c = """

# Testing entry point.

def main():
    pass  #testing logic here
    
if __name__ == "__main__":
    main()
"""
    model_c = """# Model definition file.
"""
    tr_folder = Path("Training")
    ts_folder = Path("Testing")
    tr_folder.mkdir(exist_ok=True)
    ts_folder.mkdir(exist_ok=True)

    files_ml = ["data.csv", "model.pkl", "train.py", "evaluate.py", "test.py"]
    for file in files_ml:
        Path(file).touch()

    train_path = Path("train.py")
    eval_path = Path("evaluate.py")
    test_path = Path("test.py")
    model_path = Path("model.py")

    model_path.write_text(model_c)
    train_path.write_text(train_c)
    eval_path.write_text(eval_c)
    test_path.write_text(test_c)

    print("Successfully created Machine Learning project structure.")
        
def web():
    app_c = """
# Main application entry point.

def main():
    print("Application started.")
    pass  #application logic here
    
if __name__ == "__main__":
    main()
"""
    readme_c = """# # Project Name

Short description.

## Usage
"""
    requirements_c = """# Add dependencies here
"""
    env_c = """# Environment variables
"""
    gitignore_c = """__pycache__/
.env
*.pyc
"""
    style_c = """/* Add your CSS styles here */
.body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
}
    """
    js_c = """// Add your JavaScript code here
console.log("JavaScript loaded.");
"""
    html_c = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>--pystruct--</h1>
</body>
</html>"""

    files = ["requirements.txt", "README.md", ".env", ".gitignore"]
    for f in files:
        Path(f).touch()

    Path("tests").mkdir(exist_ok=True)

    src_path = Path("src") / "my_app"
    sub_folders = ["api", "models", "services", "static", "templates", "utils"]
    
    for folder in sub_folders:
        (src_path / folder).mkdir(parents=True, exist_ok=True)

    for f in ["__init__.py", "app.py"]:
        (src_path / f).touch()

    static_path = src_path / "static"
    static_subfolders = ["css", "js", "images"]
    for folder in static_subfolders:
        (static_path / folder).mkdir(parents=True, exist_ok=True)

    style_path = static_path / "css"
    files_css = ("style.css")
    (style_path / files_css).touch()
    css_path = style_path / "style.css"
    css_path.write_text(style_c)

    js_path = static_path / "js"
    js_files = ("script.js")
    (js_path / js_files).touch()
    js_file_path = js_path / "script.js"
    js_file_path.write_text(js_c)

    templates_path = src_path / "templates"
    html_files = ("index.html")
    (templates_path / html_files).touch()
    html_file_path = templates_path / "index.html"
    html_file_path.write_text(html_c)

    app_path = src_path / "app.py"
    readme_path = Path("README.md")
    req_path = Path("requirements.txt")
    env_path = Path(".env")
    gitignore_path = Path(".gitignore")

    app_path.write_text(app_c)
    readme_path.write_text(readme_c)
    req_path.write_text(requirements_c)
    env_path.write_text(env_c)
    gitignore_path.write_text(gitignore_c)

    print("Successfully created Web project structure.")

def ds():
    data_collection_c = """# Data Collection Script
"""
    data_cleaning_c = """# Data Cleaning Script
"""
    data_analysis_c = """# Data Analysis Script
"""
    visualization_c = """# Data Visualization Script

"""
    
    Path("data").mkdir(exist_ok=True)
    Path("notebooks").mkdir(exist_ok=True)
    files = ["data_collection.py", "data_cleaning.py", "data_analysis.py", "visualization.py"]
    for f in files:
        Path(f).touch()

    dc_path = Path("data_collection.py")
    dcl_path = Path("data_cleaning.py")
    da_path = Path("data_analysis.py")
    vz_path = Path("visualization.py")

    dc_path.write_text(data_collection_c)
    dcl_path.write_text(data_cleaning_c)
    da_path.write_text(data_analysis_c)
    vz_path.write_text(visualization_c)

    print("Successfully created Data Science project structure.")

def script():
    main_c = """
Main script entry point.

def main():
    pass

if __name__ == "__main__":
    main()
"""
    main_path = Path("main.py")
    main_path.write_text(main_c)

    Path("logs").mkdir(exist_ok=True)
    files = ["main.py", "requirements.txt"]
    for f in files:
        Path(f).touch()

    print("Successfully created Script project structure.")

def lib(name):
    toml_c = f"""[project]
name = "{name}"
version = "0.1.0"
description = "Write your library description here."
dependencies = []

[project.scripts]
{name} = "{name}.cli:main" 
"""
    cli_c = """
def main():
    print("Library CLI entry point")

if __name__ == "__main__":
    main()
"""
    init_c = """__version__ = "0.1.0"
"""
    readme_c = f"# {name}\n\nWrite your library description here.\n"
    main_c = """
# Main library functionality."""

    name = str(name)
    Path(name).mkdir(exist_ok=True)
    lib_path = Path(name)
    for f in ["__init__.py", "main.py", "cli.py"]:
        (lib_path / f).touch()

    cli_path = lib_path / "cli.py"
    init_path = lib_path / "__init__.py"
    main_path = lib_path / "main.py"
    pyproject_toml = Path("pyproject.toml")
    readme_path = Path("README.md")
    
    readme_path.write_text(readme_c)
    cli_path.write_text(cli_c)
    pyproject_toml.write_text(toml_c)
    init_path.write_text(init_c)
    main_path.write_text(main_c)

    print("Successfully created Library project structure.")