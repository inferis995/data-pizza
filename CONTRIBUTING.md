# 🤝 Contributing to Data Pizza

Thank you for your interest in contributing to Data Pizza! This guide will help you get started.

## 🎯 How to Contribute

We welcome contributions in the following areas:

### 1. **New Agent Templates**
- Create agent templates for specific use cases
- Follow Datapizza AI patterns and conventions
- Include proper error handling and documentation
- Add examples and usage instructions

### 2. **New Tool Patterns**
- Develop @tool functions for common tasks
- Ensure robust error handling and input validation
- Include type hints and comprehensive docstrings
- Test tools with various inputs

### 3. **Documentation Improvements**
- Fix typos and grammatical errors
- Add examples and tutorials
- Improve clarity and structure
- Translate documentation to other languages

### 4. **Bug Reports and Fixes**
- Report bugs with detailed reproduction steps
- Submit pull requests with fixes
- Include tests that verify the fix

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Git
- Familiarity with Datapizza AI framework
- Claude Code with MCP support

### Development Setup
```bash
# 1. Fork and clone the repository
git clone https://github.com/YOUR_USERNAME/data-pizza.git
cd data-pizza

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
pip install -e .

# 4. Create a new branch
git checkout -b feature/your-feature-name
```

## 📝 Contribution Guidelines

### Code Standards
- Follow PEP 8 style guidelines
- Use type hints for all functions
- Include comprehensive docstrings
- Add error handling for all external operations
- Write tests for new functionality

### Agent Template Guidelines
```python
# Use this structure for new agent templates
from datapizza.agents import Agent
from datapizza.clients.openai import OpenAIClient
from datapizza.tools import tool

@tool
def your_custom_tool(param: str) -> str:
    """Tool description.

    Args:
        param: Parameter description

    Returns:
        Return value description
    """
    try:
        # Implementation here
        return result
    except Exception as e:
        return f"Error: {str(e)}"
```

### Tool Pattern Guidelines
```python
# Follow this pattern for new tools
from datapizza.tools import tool

@tool
def tool_function(param: str, optional_param: str = "default") -> str:
    """Clear, concise description of what the tool does.

    Args:
        param: Required parameter description
        optional_param: Optional parameter with default value

    Returns:
        Description of return value

    Example:
        result = tool_function("test_input")
    """
    try:
        # Validate inputs
        if not param:
            return "Error: param is required"

        # Main logic
        result = process_logic(param, optional_param)

        return f"Success: {result}"

    except ValueError as e:
        return f"Validation error: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"
```

## 🧪 Testing

### Running Tests
```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_agent_templates.py

# Run with coverage
pytest --cov=data_pizza
```

### Writing Tests
```python
# Example test structure
import pytest
from your_module import your_function

def test_your_function_normal_case():
    """Test normal operation."""
    result = your_function("valid_input")
    assert "expected_output" in result

def test_your_function_edge_case():
    """Test edge cases."""
    result = your_function("")
    assert "error" in result.lower()

def test_your_function_error_handling():
    """Test error handling."""
    result = your_function(None)
    assert "error" in result.lower()
```

## 📖 Documentation

### Adding New Templates
1. Create the skill file in `skills/`
2. Update `README.md` with:
   - Template description
   - Use case examples
   - Installation instructions
3. Add the template to the documentation site

### Documentation Format
```markdown
# Template Name

## Description
Brief description of what this template does.

## Use Case
When to use this template.

## Requirements
Any additional dependencies or setup.

## Example
```python
# Example usage
```

## Configuration
Any configuration options.
```

## 🔄 Pull Request Process

### Before Submitting
1. Run all tests and ensure they pass
2. Update documentation for any changes
3. Check code formatting with `black` and `flake8`
4. Test your changes with Claude Code

### Pull Request Template
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Breaking change

## Testing
- [ ] All tests pass
- [ ] New tests added for new functionality
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No breaking changes (or documented)
```

## 🏆 Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- Community highlights

## 📞 Getting Help

- Create an issue for questions
- Join our Discord community
- Check existing issues and discussions

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to Data Pizza! 🍕