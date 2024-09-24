# Team7CENProject

## Overview
**Wear & Share** is a peer-to-peer marketplace connecting individuals who are looking to rent costumes, unique outfits, or formal attire with those who own them. The platform allows users to list their outfits for short-term rental, providing a cost-effective and sustainable solution for people attending themed parties or special events.
This project is structured to run automated tests (both unit and integration) using **GitHub Actions**. It includes security checks, dependency management, and Python code testing to ensure the stability and security of the application.

### Team Members
- Chloe Crews, Nikhil Anantha, Gabriel De Brito, and Arwen Dowers

### Project Vision
- **For**: Individuals who need to attend themed parties or special events.
- **Who**: Do not want to spend an excessive amount of money on an outfit they will only wear once or twice.
- **The product is**: A web-based marketplace that allows users to rent outfits.
- **Unlike**: Traditional retail stores or online marketplaces that only sell outfits and costumes.
- **Our product**: Offers a peer-to-peer platform that facilitates short-term rentals, promoting sustainability and cost-effectiveness.

### Features
- **Unit Testing**: Automated testing of individual components of the application.
- **Integration Testing**: Tests to ensure multiple components work together as expected.
- **Security Checks**: Using Bandit to catch security vulnerabilities in the code.
- **Continuous Integration**: Every push or pull request to the `master` branch triggers the test suite via GitHub Actions.
- **Dependency Management**: Automated checks for any vulnerabilities in project dependencies.

---

## Project Structure

```markdown
Team7CENProject/
├── tests/                     # Directory containing all test files
│   ├── unit/                  # Directory for unit test files
│   │   └── test_basic.py      # Example of a basic unit test file
│   └── integration/           # Directory for integration test files
│       └── test_integration.py # Example of a basic integration test file
├── .github/                   # Directory containing GitHub-specific files
│   └── workflows/             # Directory for GitHub Actions workflow files
│       └── status_checks.yml  # The GitHub Actions workflow configuration file
├── requirements.txt           # File that lists Python dependencies for the project
├── README.md                  # Project documentation 
└── <source code files>        # Placeholder for main application code 
```

---

## Setting Up the Project

To work with this project locally, follow these steps:

### 1. Clone the Repository
```bash
git clone https://github.com/chloe-crews/Team7CENProject.git
cd Team7CENProject
```

### 2. Set up your Virtual Environment
```bash
# On Linux/MacOS
python3 -m venv venv
source venv/bin/activate
# On Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install the dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Tests Locally
```bash
# Run all unit and integration tests
pytest tests
```

---

## Branch Naming Conventions
To maintain consistency and ensure a smooth development process, please follow these branch naming conventions:

- **Feature Branches**: For new features, create branches named <your-name>/feature/<description>. Example:
```bash
git checkout -b chloe-crews/feature/user-authentication
```
- **Bug Fix Branches**: For bug fixes, use bugfix/<description>. Example:
```bash
git checkout -b chloe-crews/bugfix/fix-login-issue
```
- **Hotfix Branches**: For critical fixes, use hotfix/<description>. Example:
```bash
git checkout -b chloe-crews/hotfix/critical-deployment-fix
```
- **Naming Guidelines**:
    - Use lowercase letters.
    - Separate words with hyphens (-).
    - Be descriptive but concise.

### Master Branch Protection Rules
- **No Direct Commits**: Do not commit directly to the master branch. All changes must go through a pull request.
- **Code Reviews**: Before merging into the master branch, your code must be reviewed and approved by at least one other team member.
- **Testing Requirements**: Ensure all tests pass and the GitHub Actions checks are successful before merging.

---

## Commit Messages
When making changes to the repository, it is important to use clear and descriptive commit messages. A good commit message helps others (and your future self) understand what changes were made and why. Follow these guidelines when writing a commit message:

### Structure of a Commit Message:
- Short summary (50 characters or less):
    - Summarize the change in a few words.
    - Example: "Fix login issue when using Facebook authentication"


### Commit Guidelines:
- **Use the imperative mood**: Write the summary as if you’re commanding the code to make the change. For example: "Add new payment method", "Fix typo in README".
- **Keep it concise**: The summary should be brief and to the point.
- **Explain why when necessary**: If the reason for the change is not obvious, explain why the change was made in the longer description.
- **Reference issues if applicable**: If the commit fixes a specific issue, reference it in the message. Example: "Fixes #123".

### Example Commit Message:
```bash
git commit -m "Add validation to rental form to prevent empty submissions"
```

---

## Running the Tests

### Unit Tests
- Unit tests focus on individual components or functions.
- They are located in the tests/unit/ directory.
To run only the unit tests:
```bash
pytest tests/unit
```

### Integration Tests
- Integration tests check how different components work together.
- They are located in the tests/integration/ directory.
To run only the integration tests:
```bash 
pytest tests/integration
```

---

## Adding New Tests

### Adding Unit Tests
1. Create a new test file in the tests/unit/ directory. Name it something descriptive, following the naming convention: test_<name>.py.
2. Write your test functions inside this file. Each test function MUST start with test_ to be detected by pytest.
Example of a basic unit test:
```python
# tests/unit/test_example.py
def test_addition():
    assert 1 + 1 == 2

def test_subtraction():
    assert 2 - 1 == 1
```
3. Run your new unit tests with:
```bash
pytest tests/unit
```

### Adding Integration Tests
1. Create a new test file in the tests/integration/ directory. Name it something descriptive, following the naming convention test_<name>.py.
2. Write your test functions to check the interaction between components.
Example of a basic integration test:
```python
# tests/integration/test_example_integration.py
def test_integration_example():
    result = "Hello" + " World"
    assert result == "Hello World"
```
3. Run your new integration tests with:
```bash
pytest tests/integration
```

---

## Continuous Integration (CI) Workflow
This repository uses GitHub Actions for continuous integration. Each time you push code or open a pull request to the master branch, the following actions are automatically triggered:

- **Unit Tests**: Tests the individual components.
- **Integration Tests**: Ensures multiple components work together as expected.
- **Security Check**: Runs Bandit to check for any potential security vulnerabilities in the code.
- **Dependency Check**: Ensures the project's dependencies are secure and up to date.

### How to Trigger the Workflow
Every time you push to master or submit a pull request, the GitHub Actions CI will automatically run:
- Unit and Integration Tests.
- Security Vulnerability Checks.
- Compilation Checks.
- Dependency Checks.
To monitor the status of the CI, navigate to the Actions tab.

---

## Security Scans
We use Bandit for security scans to ensure that the code adheres to security best practices. If a security vulnerability is detected, the CI pipeline will fail.

If Bandit flags something in your test files that is safe to ignore (ie. the use of assert in tests), you can add # nosec to the flagged line.

Example:
```python
# tests/unit/test_example.py

def test_addition():
    assert 1 + 1 == 2  # nosec
```

## Team 7 Contribution Rules
1. Fork the repository.
2. Create a new branch for your feature or bug fix following the Branch Naming Conventions mentioned above.
3. Write your code and add relevant unit/integration tests.
4. Ensure all tests pass locally by running pytest.
5. Submit a pull request for review.
