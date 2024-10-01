## My ecommerce automation project

Automated tests for an online shop. 

UI testing framework verifies the functionality, usability, and visual correctness of the user interface. 
It automates the process of interacting with the application's UI elements, such as buttons, forms, and navigation menus,
to ensure they behave as expected.

The framework uses Playwright/Pytest with Python. 
Automation includes report generation, visual testing 
and uses GitHub Actions CI/CD pipeline.

### Requirements
- Python 3.9+
- Playwright
- pytest

For all the remaining requirements please see _requirements.txt_ file.

### Installation
Clone the repository and install dependencies:
```bash
git clone https://github.com/kayziu/SwagShop-automation
cd SwagShop
pip install -r requirements.txt
```

### Plugins
Tests are using the following plugins:
- **python-dotenv**: Read key-value pairs from a .env file and set them as environment variables
- **pytest-dot-env**: A py.test plugin that parses environment files before running tests
- **pytest-playwright**: A pytest wrapper with fixtures for Playwright to automate web browsers 
- **pytest-playwright-visual**: A pytest fixture for visual testing in Playwright
- **pixelmatch**: A pixel-level image comparison library.
- **pytest-reporter**: Generate pytest reports with templates
- **pytest-xdist**: pytest dist plugin for distributed testing, most importantly across multiple CPUs

To install Plugins (if not already installed with _requirements.txt_ file) use:
```bash
pip install python-dotenv pip install pytest-dotenv pip install pytest-playwright
pip install pytest-playwright-visual python -m pip install pixelmatch 
pip install pytest-reporter pip install pytest-xdist
```

### Test data
Before running the tests, add test data:
* create .env file in the root directory of the project
* write in it _PASSWORD=pass_ and from https://www.saucedemo.com/ copy "Password for all users"
as 'pass'.





