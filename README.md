## My ecommerce tests
Automated tests for an online shop. The framework uses Playwright/Pytest Framework with Python to test core 
functionalities like login, checkout and payment.

Automation includes report generation and visual testing.

### Requirements
- Python 3.9+
- Playwright
- pytest

### Plugins
Tests are using the following plugins:
- **python-dotenv**: Read key-value pairs from a .env file and set them as environment variables
- **pytest-dot-env**: A py.test plugin that parses environment files before running tests
- **pytest-playwright**: A pytest wrapper with fixtures for Playwright to automate web browsers 
- **pytest-playwright-visual**: A pytest fixture for visual testing in Playwright
- **pixelmatch**: A pixel-level image comparison library.
- **pytest-reporter**: Generate pytest reports with templates
- **pytest-xdist**: pytest dist plugin for distributed testing, most importantly across multiple CPUs
