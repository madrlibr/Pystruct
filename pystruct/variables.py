#ml
train_c = """# Training entry point.

# import necessary libraries
import pandas as pd
import numpy as np
import sklearn as sk
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    pass  #training logic here

if __name__ == "__main__":
    main()
"""
eval_c = """# Evaluation entry point.

# import necessary libraries
import pandas as pd
import numpy as np
import sklearn as sk
from sklearn.metrics import accuracy_score, classification_report 
import joblib 
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    pass  #evaluation logic here
    
if __name__ == "__main__":
    main()
"""
predict_c = """# Testing entry point.

# import necessary libraries
import pandas as pd
import numpy as np
import sklearn as sk
from sklearn.metrics import accuracy_score, classification_report 
import joblib 
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    pass  #testing logic here
    
if __name__ == "__main__":
    main()
"""
model_c = """# Model definition file.
"""

#web
app_c = """
# Main application entry point.

def main():
    print("Application started.")
    pass  #application logic here
    
if __name__ == "__main__":
    main()
"""
readme_c = """# # Project 

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
    <meta ="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>--pystruct--</h1>
</body>
</html>"""

#ds
data_collection_c = """# Data Collection Script

#import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn as sk

"""
data_cleaning_c = """# Data Cleaning Script
#import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn as sk
"""
data_analysis_c = """# Data Analysis Script
#import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn as sk
"""
visualization_c = """# Data Visualization Script

#import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn as sk

"""

#lib
main_c = """
Main script entry point.

def main():
    pass

if __name__ == "__main__":
    main()
"""
toml_c = f"""[project]
 = ""
version = "0.1.0"
description = "Write your library description here."
dependencies = []

[project.scripts]
 = ".cli:main" 
"""
cli_c = """
def main():
    print("Library CLI entry point")

if __name__ == "__main__":
    main()
"""
init_c = """__version__ = "0.1.0"
"""
readme_c = f"# \n\nWrite your library description here.\n"
main_c = """# Main library functionality."""


#pract
comment_c = """# This is a practice exercise file.
"""
files_py = ["exercise1.py", "exercise2.py", "exercise3.py", "exercise4.py", "exercise5.py",
              "exercise6.py", "exercise7.py", "exercise8.py", "exercise9.py", "exercise10.py",
              "exercise11.py", "exercise12.py", "exercise13.py", "exercise14.py", "exercise15.py"]
files_js = ["exercise1.js", "exercise2.js", "exercise3.js", "exercise4.js", "exercise5.js",
              "exercise6.js", "exercise7.js", "exercise8.js", "exercise9.js", "exercise10.js",
              "exercise11.js", "exercise12.js", "exercise13.js", "exercise14.js", "exercise15.js"]
note = """# you can add other files here such as dataset, images, etc."""

#script
main_c = """
#Main script entry point.

def main():
    pass

if __name__ == "__main__":
    main()
"""



#gitcom
license_c = """
MIT License

Copyright (c) 2025 yourname

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
readme_c = """# Project Title

A concise description of the project, its purpose, and the problem it solves.

## Features

- Feature one description.
- Feature two description.
- Feature three description.

## Tech Stack

- **Frontend**: Framework/Library (e.g., React, Vue, Angular)
- **Backend**: Language/Runtime (e.g., Node.js, Python, Go)
- **Database**: Type (e.g., PostgreSQL, MongoDB)
- **Infrastructure**: Platforms (e.g., AWS, Docker, Vercel)

## Getting Started

### Prerequisites

List the software and versions required to run the project:
- Node.js (version 18.x or higher)
- npm or yarn
- Docker (optional)

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com
   cd repo-name

## Usage

Run the following command in your terminal:

```bash
*your project usage*

```

## License
This project is licensed under the MIT LICENSE.
"""
gitignore_c = """#add yout files/folder to ignore"""


#dicting
dict_vars = {
    "ml": {
        "train_c": train_c,
        "eval_c": eval_c,
        "predict_c": predict_c,
        "model_c": model_c
    },
    "web": {
        "app_c": app_c,
        "readme_c": readme_c,
        "requirements_c": requirements_c,
        "env_c": env_c,
        "gitignore_c": gitignore_c,
        "style_c": style_c,
        "js_c": js_c,
        "html_c": html_c
    },
    "ds": {
        "data_collection_c": data_collection_c,
        "data_cleaning_c": data_cleaning_c,
        "data_analysis_c": data_analysis_c,
        "visualization_c": visualization_c
    },
    "pract": {
        "comment_c": comment_c,
        "files_py": files_py,
        "files_js": files_js,
        "note": note
    },
    "script": {
        "main_c": main_c
    },
    "lib": {
        "main_c": main_c,
        "toml_c": toml_c,
        "cli_c": cli_c,
        "init_c": init_c,
        "readme_c": readme_c,
        "main_C": main_c

    }
}