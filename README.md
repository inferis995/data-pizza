# 🍕 Data Pizza - Datapizza AI Skills for Claude Code

<div align="center">

![Data Pizza](https://img.shields.io/badge/Data-Pizza-orange?style=for-the-badge)
![Claude Code](https://img.shields.io/badge/Claude-Code-orange?style=for-the-badge)
![Datapizza AI](https://img.shields.io/badge/Datapizza-AI-blue?style=for-the-badge)

**Build powerful AI agents and tools for Datapizza AI framework with Claude Code**

[Installation](#-installation) • [Documentation](#-documentation) • [Examples](#-examples) • [Contributing](#-contributing)

</div>

## 🎯 About Data Pizza

Data Pizza is a collection of specialized skills for Claude Code that accelerate development with the [Datapizza AI](https://github.com/datapizza-labs/datapizza-ai) framework.

> **Datapizza AI**: A no-fluff GenAI framework to build reliable Gen AI solutions without overhead. Get your agents from dev to prod, fast.

Our skills help you create production-ready AI agents and custom tools that integrate seamlessly with the Datapizza AI ecosystem.

## 🚀 Features

### 🤖 Agent Creator (`datapizza-agent-creator`)
- **5+ Agent Templates**: Customer service, e-commerce, research, RAG, multi-agent systems
- **Multi-Provider Support**: OpenAI, Anthropic, Google, Mistral, Azure
- **Production-Ready**: Proper error handling, logging, and monitoring
- **Quick Setup**: Generate agents in seconds, not hours

### 🛠️ Tool Builder (`datapizza-tool-builder`)
- **Custom @tool Functions**: Database, API, file system, business logic tools
- **Best Practices**: Type hints, error handling, input validation
- **Framework Integration**: Seamless integration with Datapizza AI agents
- **Template Library**: 5+ pre-built tool patterns

## 📦 Installation

### Prerequisites
- Python 3.8+
- Claude Code with MCP support
- Datapizza AI framework

### 1. Clone the Repository
```bash
git clone https://github.com/inferis995/data-pizza.git
cd data-pizza
```

### 2. Install Dependencies
```bash
# Core Datapizza AI framework
pip install datapizza-ai

# Official tools
pip install datapizza-ai-tools-sqldatabase
pip install datapizza-ai-tools-duckduckgo
pip install datapizza-ai-tools-filesystem
pip install datapizza-ai-tools-web-fetch

# Vector stores (for RAG capabilities)
pip install qdrant-client
pip install chromadb
```

### 3. Configure Claude Code
Add the Data Pizza skills to your Claude Code configuration:

```json
{
  "skills": [
    {
      "name": "datapizza-agent-creator",
      "path": "C:\\Users\\Utente\\Desktop\\data_pizza\\skills\\datapizza-agent-creator\\SKILL.md"
    },
    {
      "name": "datapizza-tool-builder",
      "path": "C:\\Users\\Utente\\Desktop\\data_pizza\\skills\\datapizza-tool-builder\\SKILL.md"
    }
  ]
}
```

### 4. Set Up API Keys
```bash
# Set your preferred AI provider API key
export OPENAI_API_KEY="your-openai-key"
# or
export ANTHROPIC_API_KEY="your-anthropic-key"
```

## 🎯 Quick Start

### Create Your First Agent
```bash
# Using Claude Code
/skill datapizza-agent-creator --type basic --name assistant --provider openai
```

### Create Custom Tools
```bash
# Using Claude Code
/skill datapizza-tool-builder --type database --function get_customer_data
```

### Example Generated Agent
```python
from datapizza.agents import Agent
from datapizza.clients.openai import OpenAIClient

# Create client
client = OpenAIClient(api_key="YOUR_API_KEY", model="gpt-4o-mini")

# Create agent
agent = Agent(
    name="assistant",
    system_prompt="You are a helpful AI assistant.",
    client=client
)

# Use the agent
response = agent.run("Hello! How can you help me today?")
```

## 📚 Documentation

### Skills Overview
- [Agent Creator Documentation](skills/datapizza-agent-creator/README.md)
- [Tool Builder Documentation](skills/datapizza-tool-builder/README.md)

### Agent Templates
| Template | Use Case | Tools | Complexity |
|----------|----------|-------|------------|
| Customer Service | Support automation | Database, API | Medium |
| E-commerce | Shopping assistant | Product catalog, inventory | Medium |
| Research Assistant | Information gathering | Web search, fetch | Medium |
| Document Processor | Document analysis | File system, parsing | Medium |
| Multi-Agent System | Complex workflows | Agent communication | High |

### Tool Patterns
| Type | Examples | Integration |
|------|----------|-------------|
| Database | CRUD operations, queries | SQLDatabase tool |
| API | REST calls, webhooks | requests library |
| File System | Document processing | FileSystem tool |
| Business Logic | Calculations, validation | Custom functions |
| Utility | Hashing, validation | Standard library |

## 🎨 Examples

### Customer Service Agent
```python
from datapizza.agents import Agent
from datapizza.clients.openai import OpenAIClient
from datapizza.tools import tool

@tool
def get_customer_info(customer_id: str) -> str:
    """Get customer information from database."""
    # Implementation here
    return customer_data

# Create agent with tools
client = OpenAIClient(api_key="YOUR_API_KEY")
agent = Agent(
    name="customer_service",
    system_prompt="You are a helpful customer service assistant.",
    client=client,
    tools=[get_customer_info]
)
```

### RAG Agent
```python
from datapizza.agents import Agent
from datapizza.clients.openai import OpenAIClient
from datapizza.tools.qdrant import QdrantTool

# Set up vector store
vector_store = QdrantTool(
    collection_name="knowledge_base",
    embedding_model="text-embedding-ada-002"
)

# Create RAG agent
client = OpenAIClient(api_key="YOUR_API_KEY")
agent = Agent(
    name="rag_assistant",
    system_prompt="You are a knowledge assistant. Use the provided context to answer questions.",
    client=client,
    tools=[vector_store.search]
)
```

## 🔧 Configuration

### Environment Variables
```bash
# AI Providers
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
GOOGLE_API_KEY=your_google_key
MISTRAL_API_KEY=your_mistral_key

# Database
DATABASE_URL=sqlite:///your_database.db

# Vector Stores
QDRANT_URL=http://localhost:6333
QDRANT_API_KEY=your_qdrant_key
```

### Claude Code Setup
1. Install Claude Code with MCP support
2. Add Data Pizza skills to your configuration
3. Restart Claude Code
4. Start using `/skill datapizza-agent-creator` and `/skill datapizza-tool-builder`

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Development Setup
```bash
# Clone the repository
git clone https://github.com/inferis995/data-pizza.git
cd data-pizza

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .
```

### Contributing Guidelines
- Follow the [Datapizza AI](https://github.com/datapizza-labs/datapizza-ai) patterns and conventions
- Ensure all code includes proper error handling
- Add type hints and docstrings
- Test your contributions thoroughly
- Update documentation

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Datapizza AI](https://github.com/datapizza-labs/datapizza-ai) - The core framework
- [Build with Claude](https://www.buildwithclaude.com) - Inspiration for the documentation style
- [Claude Code](https://claude.ai/code) - AI-powered development environment

## 📞 Support

- 📧 Email: [your-email@example.com]
- 💬 Discord: [Join our community]
- 📖 Documentation: [Full documentation site]
- 🐛 Issues: [GitHub Issues](https://github.com/inferis995/data-pizza/issues)

---

<div align="center">

**⭐ Star this repository if it helped you!**

Made with ❤️ by [Poola Ai](https://github.com/inferis995)

</div>