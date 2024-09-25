## My ecommerce automation project

Automated tests for an online shop. 

The framework uses Playwright/Pytest Framework with Python to test core 
functionalities like login, checkout and payment.

Automation includes report generation, visual testing 
and uses GitHub Actions CI/CD pipeline.

### Requirements
- Python 3.9+
- Playwright
- pytest
#### For all the remaining requirements please see requirements.txt file

### Plugins
Tests are using the following plugins:
- **python-dotenv**: Read key-value pairs from a .env file and set them as environment variables
- **pytest-dot-env**: A py.test plugin that parses environment files before running tests
- **pytest-playwright**: A pytest wrapper with fixtures for Playwright to automate web browsers 
- **pytest-playwright-visual**: A pytest fixture for visual testing in Playwright
- **pixelmatch**: A pixel-level image comparison library.
- **pytest-reporter**: Generate pytest reports with templates
- **pytest-xdist**: pytest dist plugin for distributed testing, most importantly across multiple CPUs

To install Plugins use:
```bash
pip install python-dotenv pip install pytest-dotenv pip install pytest-playwright
pip install pytest-playwright-visual python -m pip install pixelmatch 
pip install pytest-reporter pip install pytest-xdist
```

### Installation
Clone the repository and install dependencies:
```bash
git clone https://github.com/kayziu/SwagShop-automation
cd SwagShop
pip install -r requirements.txt
```



