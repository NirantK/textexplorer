# Contributing to TextExplorer

First off, thank you for considering contributing to TextExplorer! It's people like you that make TextExplorer such a great tool.

## Code of Conduct

By participating in this project, you are expected to uphold our Code of Conduct:

- Use welcoming and inclusive language
- Be respectful of differing viewpoints and experiences
- Gracefully accept constructive criticism
- Focus on what is best for the community
- Show empathy towards other community members

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, please include as many details as possible:

- A clear and descriptive title
- Exact steps to reproduce the problem
- Expected behavior
- Actual behavior
- Code samples and/or test files (if applicable)
- Your environment details (OS, Python version, package versions)

### Suggesting Enhancements

If you have a suggestion for a new feature or enhancement:

1. Check the issues list to see if it's already been suggested
2. Create a new issue with the label "enhancement"
3. Clearly describe the feature and its potential benefits
4. If possible, outline how you think it could be implemented

### Pull Requests

1. Fork the repository
2. Create a new branch for your feature (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Update documentation if needed
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to your branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

#### Pull Request Guidelines

- Follow the existing code style (we use ruff for formatting and linting)
- Update documentation for any changed functionality
- Keep commits focused and atomic
- Write clear, descriptive commit messages

## Development Setup

1. Clone the repository
```bash
git clone https://github.com/yourusername/textexplorer.git
cd textexplorer
```

2. Install Poetry if you haven't already
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

3. Install dependencies and create virtual environment
```bash
poetry install
```

4. Activate the virtual environment
```bash
poetry shell
```

## Documentation

- Document all new functions, classes, and modules
- Use Google-style docstrings
- Update the README.md if needed
- Add examples for new features

## Style Guide

We use ruff for code formatting and linting. The configuration can be found in pyproject.toml. Key style points:

- Line length: 88 characters
- Use double quotes for strings
- Use trailing commas in multi-line structures
- Follow import sorting rules defined in ruff configuration

## Getting Help

If you need help, you can:

- Open an issue with the label "question"
- Comment on relevant issues or pull requests
- Check existing documentation and issues

## Recognition

Contributors will be recognized in our release notes. Thank you for your contributions! 