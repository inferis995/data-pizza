# Datapizza AI Agent Creator Skill

**Category**: Datapizza AI Agent Development
**Description**: Creates Datapizza AI agents with proper syntax and best practices
**Usage**: `/skill datapizza-agent-creator`

## 🎯 Purpose

This skill helps create production-ready Datapizza AI agents following official patterns and best practices. It ensures agents are properly configured, have the right tools, and follow Datapizza AI conventions.

## 🛠️ What This Skill Does

### Agent Creation Patterns
- **Simple Agent**: Basic agent with system prompt and client
- **Agent with Tools**: Agent with custom @tool functions
- **Multi-Agent System**: Multiple collaborating agents
- **RAG Agent**: Agent with retrieval-augmented generation
- **API Integration Agent**: Agent that connects to external systems

### Configuration Options
- **AI Provider Selection**: OpenAI, Anthropic, Google, Mistral
- **Tool Integration**: Official tools + custom tools
- **Memory Setup**: Conversation persistence
- **Performance Optimization**: Caching, timeouts, error handling

## 🚀 Usage Examples

### Basic Agent Creation
```bash
/skill datapizza-agent-creator --type basic --name assistant --provider openai
```

### Agent with Tools
```bash
/skill datapizza-agent-creator --type with-tools --name ecommerce --provider openai --tools database,search
```

### Multi-Agent System
```bash
/skill datapizza-agent-creator --type multi-agent --agents researcher,writer --provider openai
```

### RAG Agent
```bash
/skill datapizza-agent-creator --type rag --name knowledge --provider openai --vector-store qdrant
```

## 📋 Agent Templates

### Template 1: Customer Service Agent
```python
from datapizza.agents import Agent
from datapizza.clients.openai import OpenAIClient
from datapizza.tools import tool
from datapizza.tools.SQLDatabase import SQLDatabase

# Database setup
db = SQLDatabase(db_uri="sqlite:///customer_data.db")

# Custom tools
@tool
def get_customer_info(customer_id: str) -> str:
    """Get customer information from database."""
    return db.run_sql_query(f"SELECT * FROM customers WHERE id = {customer_id}")

@tool
def update_customer_status(customer_id: str, status: str) -> str:
    """Update customer status."""
    db.run_sql_query(f"UPDATE customers SET status = '{status}' WHERE id = {customer_id}")
    return f"Customer {customer_id} status updated to {status}"

# Agent creation
client = OpenAIClient(api_key="YOUR_API_KEY", model="gpt-4o-mini")
agent = Agent(
    name="customer_service",
    system_prompt="You are a helpful customer service assistant. You can access customer information and update their status.",
    client=client,
    tools=[get_customer_info, update_customer_status]
)
```

### Template 2: E-commerce Assistant
```python
from datapizza.agents import Agent
from datapizza.clients.openai import OpenAIClient
from datapizza.tools import tool

@tool
def get_product_catalog() -> str:
    """Get complete product catalog."""
    return fetch_product_catalog()

@tool
def check_inventory(product_id: str) -> str:
    """Check product availability."""
    return check_product_stock(product_id)

@tool
def place_order(items: list, customer_info: dict) -> str:
    """Place new order."""
    return process_order(items, customer_info)

# Create e-commerce agent
client = OpenAIClient(api_key="YOUR_API_KEY")
agent = Agent(
    name="ecommerce_assistant",
    system_prompt="You are an e-commerce assistant. You can help customers browse products, check inventory, and place orders.",
    client=client,
    tools=[get_product_catalog, check_inventory, place_order]
)
```

### Template 3: Document Intelligence Agent
```python
from datapizza.agents import Agent
from datapizza.clients.openai import OpenAIClient
from datapizza.tools import tool
from datapizza.tools.filesystem import FileSystem

# File system setup
fs = FileSystem()

@tool
def read_document(file_path: str) -> str:
    """Read document content."""
    return fs.read_file(file_path)

@tool
def analyze_document(content: str) -> str:
    """Analyze document content."""
    # Extract key information
    return extract_key_info(content)

@tool
def generate_summary(content: str) -> str:
    """Generate document summary."""
    return create_summary(content)

# Create document processor
client = OpenAIClient(api_key="YOUR_API_KEY")
agent = Agent(
    name="document_processor",
    system_prompt="You are a document processor. You can read, analyze, and summarize documents.",
    client=client,
    tools=[read_document, analyze_document, generate_summary]
)
```

### Template 4: Research Agent
```python
from datapizza.agents import Agent
from datapizza.clients.openai import OpenAIClient
from datapizza.tools.duckduckgo import DuckDuckGoSearch
from datapizza.tools.web_fetch import WebFetchTool

# Research tools
search = DuckDuckGoSearch()
web_tool = WebFetchTool()

@tool
def search_information(query: str) -> str:
    """Search for information online."""
    return search.search(query)

@tool
def fetch_webpage(url: str) -> str:
    """Fetch and analyze webpage."""
    return web_tool.fetch(url)

@tool
def compile_research(results: list) -> str:
    """Compile research findings."""
    return create_research_report(results)

# Create research agent
client = OpenAIClient(api_key="YOUR_API_KEY")
agent = Agent(
    name="research_agent",
    system_prompt="You are a research assistant. You can search the web, fetch information, and compile research reports.",
    client=client,
    tools=[search_information, fetch_webpage, compile_research]
)
```

### Template 5: Multi-Agent System
```python
from datapizza.agents import Agent
from datapizza.clients.openai import OpenAIClient

# Create different specialist agents
client = OpenAIClient(api_key="YOUR_API_KEY")

researcher = Agent(
    name="researcher",
    system_prompt="You research information and provide detailed analysis.",
    client=client
)

writer = Agent(
    name="writer",
    system_prompt="You write content based on research provided.",
    client=client
)

analyst = Agent(
    name="analyst",
    system_prompt="You analyze data and provide insights.",
    client=client
)

# Enable agent communication
researcher.can_call(["writer", "analyst"])
writer.can_call(["analyst"])

# Example usage
# The researcher can now call the writer and analyst
response = researcher.run("Research market trends for electric vehicles and have the writer create a summary, then have the analyst provide insights.")
```

## ⚙️ Configuration Parameters

### Basic Parameters
- `--name`: Agent name (required)
- `--provider`: AI provider (openai, anthropic, google, mistral)
- `--model`: Model name (gpt-4o-mini, claude-3-haiku, gemini-pro, etc.)
- `--system-prompt`: Custom system prompt

### Tool Parameters
- `--tools`: Comma-separated list of tools to include
- `--database`: Database connection string
- `--vector-store`: Vector store configuration
- `--file-path`: File system path for file operations

### Advanced Parameters
- `--memory`: Enable conversation memory
- `--temperature`: Response creativity (0.0-1.0)
- `--max-tokens`: Maximum response length
- `--timeout`: Request timeout in seconds

## 📦 Required Dependencies

### **Official Installation**
```bash
# Core framework
pip install datapizza-ai

# Official tools (from repository)
pip install datapizza-ai-tools-sqldatabase
pip install datapizza-ai-tools-duckduckgo
pip install datapizza-ai-tools-filesystem
pip install datapizza-ai-tools-web-fetch

# Vector stores (for RAG)
pip install qdrant-client
pip install chromadb
```

### **Repository Ufficiale Tools**
GitHub: https://github.com/datapizza-labs/datapizza-ai/tree/main/datapizza-ai-tools

**Tools Disponibili:**
- ✅ **SQLDatabase** - Database operations
- ✅ **DuckDuckGo** - Web search
- ✅ **FileSystem** - File operations
- ✅ **WebFetch** - Web content extraction

## 🎯 Best Practices

### ✅ DO:
- Use clear, descriptive agent names
- Write specific system prompts
- Include proper error handling in tools
- Use type hints for tool functions
- Add docstrings to all tools
- Test agents with sample inputs

### ❌ DON'T:
- Create overly complex agents
- Skip error handling
- Use vague system prompts
- Forget to set API keys
- Mix unrelated functionality in one agent

## 🔧 Troubleshooting

### Common Issues
1. **API Key Not Found**: Ensure environment variables are set
2. **Tool Not Working**: Check tool syntax and imports
3. **Agent Not Responding**: Verify client configuration
4. **Database Connection**: Check connection string format

### Debug Mode
```python
# Enable debug logging
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 📚 Additional Resources

- [Datapizza AI Documentation](https://docs.datapizza.ai)
- [Official Examples](https://github.com/datapizza-labs/datapizza-ai/tree/main/examples)
- [API Reference](https://docs.datapizza.ai/api-reference)

## 🚀 Getting Started

1. **Install Dependencies**: `pip install datapizza-ai`
2. **Set API Key**: `export OPENAI_API_KEY="your-key"`
3. **Create Agent**: Use this skill to generate agent code
4. **Test Agent**: Run with sample inputs
5. **Deploy**: Integrate into your application

---

*This skill ensures your Datapizza AI agents follow best practices and are production-ready!* 🍕