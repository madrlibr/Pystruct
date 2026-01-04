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
import pandas as pd
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
import pandas as pd
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


#lib variables has parameter on it's value so i'm still working on it

#pract
comment_c = """# This is a practice exercise file.
"""
files_py = ["exercise1.py", "exercise2.py", "exercise3.py", "exercise4.py", "exercise5.py",
              "exercise6.py", "exercise7.py", "exercise8.py", "exercise9.py", "exercise10.py",
              "exercise11.py", "exercise12.py", "exercise13.py", "exercise14.py", "exercise15.py"]
files_js = ["exercise1.js", "exercise2.js", "exercise3.js", "exercise4.js", "exercise5.js",
              "exercise6.js", "exercise7.js", "exercise8.js", "exercise9.js", "exercise10.js",
              "exercise11.js", "exercise12.js", "exercise13.js", "exercise14.js", "exercise15.js"]
note = """# you can add other files hear such as dataset, images, etc."""

#script
main_c = """
Main script entry point.

def main():
    pass


if __name__ == "__main__":
main()
"""

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
    }
}