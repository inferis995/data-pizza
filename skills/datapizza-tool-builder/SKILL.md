# Datapizza AI Tool Builder Skill

**Category**: Datapizza AI Tool Development
**Description**: Creates custom @tool functions for Datapizza AI agents with proper patterns and error handling
**Usage**: `/skill datapizza-tool-builder`

## 🎯 Purpose

This skill helps create production-ready @tool functions for Datapizza AI agents. It ensures tools follow proper syntax, include error handling, and integrate seamlessly with Datapizza AI agent systems.

## 🛠️ What This Skill Does

### Tool Creation Patterns
- **Database Tools**: SQL queries and data operations
- **API Integration Tools**: REST API calls and web services
- **File System Tools**: File operations and document processing
- **Business Logic Tools**: Custom business functions
- **Utility Tools**: Helper functions and calculations

### Tool Features
- **Error Handling**: Robust exception management
- **Type Safety**: Proper type hints and validation
- **Documentation**: Clear docstrings and examples
- **Testing**: Input validation and edge case handling
- **Integration**: Seamless agent integration

## 🚀 Usage Examples

### Database Tool Creation
```bash
/skill datapizza-tool-builder --type database --function get_customer_data --table customers
```

### API Integration Tool
```bash
/skill datapizza-tool-builder --type api --function fetch_weather --service openweathermap
```

### File Processing Tool
```bash
/skill datapizza-tool-builder --type file --function process_pdf --format pdf
```

### Business Logic Tool
```bash
/skill datapizza-tool-builder --type business --function calculate_discount --logic pricing
```

## 📋 Tool Templates

### Template 1: Database Operations Tool
```python
from datapizza.tools import tool
from datapizza.tools.SQLDatabase import SQLDatabase

# Initialize database connection
db = SQLDatabase(db_uri="sqlite:///your_database.db")

@tool
def get_customer_data(customer_id: str) -> str:
    """Retrieve customer data from database.

    Args:
        customer_id: The ID of the customer to retrieve

    Returns:
        Formatted customer information as string
    """
    try:
        query = f"SELECT * FROM customers WHERE id = {customer_id}"
        result = db.run_sql_query(query)

        if not result:
            return f"Customer with ID {customer_id} not found"

        customer = result[0]
        return f"""
        Customer Information:
        ID: {customer['id']}
        Name: {customer['name']}
        Email: {customer['email']}
        Phone: {customer['phone']}
        Status: {customer['status']}
        """

    except Exception as e:
        return f"Error retrieving customer data: {str(e)}"

@tool
def update_customer_status(customer_id: str, status: str) -> str:
    """Update customer status in database.

    Args:
        customer_id: The ID of the customer
        status: New status value

    Returns:
        Confirmation message
    """
    try:
        valid_statuses = ['active', 'inactive', 'pending', 'suspended']
        if status.lower() not in valid_statuses:
            return f"Invalid status. Valid options: {', '.join(valid_statuses)}"

        query = f"UPDATE customers SET status = '{status}' WHERE id = {customer_id}"
        db.run_sql_query(query)

        return f"Customer {customer_id} status updated to '{status}'"

    except Exception as e:
        return f"Error updating customer status: {str(e)}"
```

### Template 2: API Integration Tool
```python
from datapizza.tools import tool
import requests
import json

@tool
def fetch_weather_data(city: str) -> str:
    """Fetch weather data from OpenWeatherMap API.

    Args:
        city: Name of the city to get weather for

    Returns:
        Weather information as formatted string
    """
    try:
        api_key = os.getenv("OPENWEATHER_API_KEY")
        if not api_key:
            return "OpenWeatherMap API key not configured"

        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,
            "appid": api_key,
            "units": "metric"
        }

        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]

        return f"""
        Weather in {city}:
        Temperature: {temp}°C
        Feels like: {feels_like}°C
        Conditions: {description}
        Humidity: {humidity}%
        """

    except requests.exceptions.RequestException as e:
        return f"Network error fetching weather: {str(e)}"
    except KeyError as e:
        return f"Error parsing weather data: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"

@tool
def send_slack_notification(webhook_url: str, message: str, channel: str = None) -> str:
    """Send notification to Slack channel.

    Args:
        webhook_url: Slack webhook URL
        message: Message to send
        channel: Optional channel override

    Returns:
        Success/failure message
    """
    try:
        payload = {"text": message}
        if channel:
            payload["channel"] = channel

        response = requests.post(webhook_url, json=payload, timeout=10)
        response.raise_for_status()

        return f"Slack notification sent successfully"

    except requests.exceptions.RequestException as e:
        return f"Error sending Slack notification: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"
```

### Template 3: File System Tool
```python
from datapizza.tools import tool
import os
import json
from datetime import datetime

@tool
def process_json_file(file_path: str, operation: str, data: dict = None) -> str:
    """Process JSON files with various operations.

    Args:
        file_path: Path to the JSON file
        operation: Operation to perform (read, write, append, validate)
        data: Data to write (for write/append operations)

    Returns:
        Operation result message
    """
    try:
        if operation == "read":
            with open(file_path, 'r') as f:
                json_data = json.load(f)
            return f"JSON data read from {file_path}: {len(json_data)} items"

        elif operation == "write":
            if not data:
                return "No data provided for write operation"

            with open(file_path, 'w') as f:
                json.dump(data, f, indent=2)
            return f"JSON data written to {file_path}"

        elif operation == "append":
            if not data:
                return "No data provided for append operation"

            # Read existing data
            existing_data = {}
            if os.path.exists(file_path):
                with open(file_path, 'r') as f:
                    existing_data = json.load(f)

            # Merge data
            existing_data.update(data)

            # Write back
            with open(file_path, 'w') as f:
                json.dump(existing_data, f, indent=2)
            return f"Data appended to {file_path}"

        elif operation == "validate":
            with open(file_path, 'r') as f:
                json.load(f)  # Will raise exception if invalid JSON
            return f"JSON file {file_path} is valid"

        else:
            return f"Invalid operation: {operation}. Valid options: read, write, append, validate"

    except FileNotFoundError:
        return f"File not found: {file_path}"
    except json.JSONDecodeError as e:
        return f"Invalid JSON in file {file_path}: {str(e)}"
    except Exception as e:
        return f"Error processing JSON file: {str(e)}"

@tool
def create_log_entry(log_file: str, level: str, message: str) -> str:
    """Create a log entry in specified format.

    Args:
        log_file: Path to the log file
        level: Log level (INFO, WARNING, ERROR, DEBUG)
        message: Log message

    Returns:
        Confirmation message
    """
    try:
        valid_levels = ["INFO", "WARNING", "ERROR", "DEBUG"]
        if level.upper() not in valid_levels:
            return f"Invalid log level. Valid options: {', '.join(valid_levels)}"

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {level.upper()}: {message}\n"

        # Ensure directory exists
        os.makedirs(os.path.dirname(log_file), exist_ok=True)

        with open(log_file, 'a') as f:
            f.write(log_entry)

        return f"Log entry added to {log_file}"

    except Exception as e:
        return f"Error creating log entry: {str(e)}"
```

### Template 4: Business Logic Tool
```python
from datapizza.tools import tool
import datetime
from typing import List, Dict, Any

@tool
def calculate_discount(price: float, customer_tier: str, quantity: int = 1) -> str:
    """Calculate discount based on customer tier and quantity.

    Args:
        price: Original price
        customer_tier: Customer tier (bronze, silver, gold, platinum)
        quantity: Order quantity

    Returns:
        Discount calculation result
    """
    try:
        # Validate inputs
        if price <= 0:
            return "Price must be greater than 0"
        if quantity <= 0:
            return "Quantity must be greater than 0"

        # Customer tier discounts
        tier_discounts = {
            "bronze": 0.05,    # 5%
            "silver": 0.10,    # 10%
            "gold": 0.15,      # 15%
            "platinum": 0.20   # 20%
        }

        # Quantity discounts
        quantity_discounts = {
            range(1, 5): 0,        # No discount for 1-4 items
            range(5, 11): 0.05,     # 5% discount for 5-10 items
            range(11, 21): 0.10,   # 10% discount for 11-20 items
            range(21, 51): 0.15,   # 15% discount for 21-50 items
            range(51, 101): 0.20,  # 20% discount for 51-100 items
        }

        # Calculate tier discount
        tier_discount = tier_discounts.get(customer_tier.lower(), 0)

        # Calculate quantity discount
        quantity_discount = 0
        for qty_range, discount in quantity_discounts.items():
            if quantity in qty_range:
                quantity_discount = discount
                break

        # Total discount (don't exceed 30%)
        total_discount = min(tier_discount + quantity_discount, 0.30)

        # Calculate final price
        discounted_price = price * (1 - total_discount)
        total_savings = (price - discounted_price) * quantity

        return f"""
        Discount Calculation:
        Original Price: ${price:.2f}
        Customer Tier: {customer_tier.title()} ({tier_discount*100:.0f}%)
        Quantity: {quantity} ({quantity_discount*100:.0f}%)
        Total Discount: {total_discount*100:.0f}%
        Final Price per Unit: ${discounted_price:.2f}
        Total Savings: ${total_savings:.2f}
        Total Cost: ${discounted_price * quantity:.2f}
        """

    except Exception as e:
        return f"Error calculating discount: {str(e)}"

@tool
def generate_invoice(order_data: dict) -> str:
    """Generate a formatted invoice from order data.

    Args:
        order_data: Dictionary containing order information

    Returns:
        Formatted invoice as string
    """
    try:
        required_fields = ["order_id", "customer_name", "items", "order_date"]
        for field in required_fields:
            if field not in order_data:
                return f"Missing required field: {field}"

        invoice = f"""
        ╔══════════════════════════════════════════════════════════════╗
        ║                        INVOICE                             ║
        ╠══════════════════════════════════════════════════════════════╣
        ║ Invoice Number: {order_data['order_id']}                      ║
        ║ Customer: {order_data['customer_name']}                      ║
        ║ Date: {order_data['order_date']}                             ║
        ║ Status: {order_data.get('status', 'Pending')}                ║
        ╠══════════════════════════════════════════════════════════════╣
        ║                                                         ║
        ║ ITEMS:                                                  ║
        """

        total = 0.0
        for item in order_data['items']:
            item_total = item['price'] * item['quantity']
            total += item_total

            invoice += f"""
        ║ {item['name']}                                          ║
        ║   {item['quantity']} x ${item['price']:.2f} = ${item_total:.2f}        ║
        """

        tax = total * 0.10  # 10% tax
        grand_total = total + tax

        invoice += f"""
        ║                                                         ║
        ╠══════════════════════════════════════════════════════════════╣
        ║                                                         ║
        ║ Subtotal:                                             ║
        ║    ${total:.2f}                                            ║
        ║ Tax (10%):                                             ║
        ║    ${tax:.2f}                                            ║
        ║                                                         ║
        ║ GRAND TOTAL:                                          ║
        ║    ${grand_total:.2f}                                    ║
        ║                                                         ║
        ╚══════════════════════════════════════════════════════════════╝
        """

        return invoice

    except Exception as e:
        return f"Error generating invoice: {str(e)}"
```

### Template 5: Utility Tool
```python
from datapizza.tools import tool
import hashlib
import base64
import re

@tool
def generate_hash(text: str, algorithm: str = "sha256") -> str:
    """Generate hash of text using specified algorithm.

    Args:
        text: Text to hash
        algorithm: Hash algorithm (md5, sha1, sha256, sha512)

    Returns:
        Generated hash as string
    """
    try:
        if algorithm.lower() not in ["md5", "sha1", "sha256", "sha512"]:
            return f"Invalid algorithm: {algorithm}. Valid options: md5, sha1, sha256, sha512"

        hash_object = hashlib.new(algorithm.lower())
        hash_object.update(text.encode())
        return f"{algorithm.upper()} hash: {hash_object.hexdigest()}"

    except Exception as e:
        return f"Error generating hash: {str(e)}"

@tool
def validate_email(email: str) -> str:
    """Validate email address format.

    Args:
        email: Email address to validate

    Returns:
        Validation result with details
    """
    try:
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if not email:
            return "Email cannot be empty"

        if len(email) > 254:
            return "Email address is too long (max 254 characters)"

        if not re.match(email_pattern, email):
            return f"Invalid email format: {email}"

        # Additional checks
        local_part, domain = email.split('@')

        if len(local_part) > 64:
            return "Local part is too long (max 64 characters)"

        if domain.startswith('.') or domain.endswith('.'):
            return "Domain cannot start or end with a dot"

        return f"✅ Valid email address: {email}"

    except Exception as e:
        return f"Error validating email: {str(e)}"

@tool
def format_currency(amount: float, currency: str = "USD", locale: str = "en_US") -> str:
    """Format currency amount according to locale.

    Args:
        amount: Amount to format
        currency: Currency code (USD, EUR, GBP, etc.)
        locale: Locale for formatting

    Returns:
        Formatted currency string
    """
    try:
        if amount < 0:
            return f"Amount cannot be negative: {amount}"

        currency_symbols = {
            "USD": "$",
            "EUR": "€",
            "GBP": "£",
            "JPY": "¥",
            "CNY": "¥"
        }

        symbol = currency_symbols.get(currency.upper(), currency)

        # Simple formatting (in production, use locale module)
        formatted = f"{symbol}{amount:,.2f}"

        return f"Formatted currency ({currency}): {formatted}"

    except Exception as e:
        return f"Error formatting currency: {str(e)}"
```

## ⚙️ Configuration Parameters

### Basic Parameters
- `--type`: Tool type (database, api, file, business, utility)
- `--function`: Function name
- `--table`: Database table (for database tools)
- `--service`: API service (for api tools)
- `--format`: File format (for file tools)

### Advanced Parameters
- `--error-handling`: Error handling strategy
- `--validation`: Input validation rules
- `--logging`: Enable logging
- `--testing`: Include test cases

## 📦 Required Dependencies

```bash
# Core framework
pip install datapizza-ai

# Additional dependencies (as needed)
pip install requests  # For API tools
pip install sqlalchemy # For database tools
pip install pandas    # For data processing
pip install python-dotenv  # For environment variables
```

## 🎯 Best Practices

### ✅ DO:
- Always include proper error handling
- Use type hints for function parameters
- Write clear, descriptive docstrings
- Validate inputs before processing
- Handle edge cases gracefully
- Include logging for debugging
- Write unit tests for tools

### ❌ DON'T:
- Skip error handling
- Use vague parameter names
- Write tools that do too many things
- Return unstructured data
- Hardcode configuration values
- Forget to document tool purpose

## 🔧 Testing Tools

### Unit Test Template
```python
def test_tool_function():
    """Test the tool function."""
    # Test normal case
    result = your_tool_function("test_input")
    assert "expected_output" in result

    # Test edge cases
    result = your_tool_function("")
    assert "error" in result.lower()

    # Test error handling
    result = your_tool_function(None)
    assert "error" in result.lower()
```

## 📚 Integration Examples

### Using Tools with Agents
```python
from datapizza.agents import Agent
from datapizza.clients.openai import OpenAIClient

# Import custom tools
from your_tools import custom_tool_1, custom_tool_2

# Create agent with tools
client = OpenAIClient(api_key="YOUR_API_KEY")
agent = Agent(
    name="assistant",
    system_prompt="You are a helpful assistant with access to custom tools.",
    client=client,
    tools=[custom_tool_1, custom_tool_2]
)

# Use agent
response = agent.run("Help me with something using your tools")
```

## 🚀 Getting Started

1. **Define Requirements**: What should the tool do?
2. **Choose Template**: Select appropriate template
3. **Customize Logic**: Add business-specific logic
4. **Add Error Handling**: Make tool robust
5. **Test Thoroughly**: Validate with various inputs
6. **Integrate with Agent**: Add to Datapizza AI agent

---

*This skill ensures your Datapizza AI tools are robust, well-documented, and production-ready!* 🛠️