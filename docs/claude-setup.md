# Claude Code Setup Guide

This guide will help you set up Data Pizza skills with Claude Code for seamless AI agent and tool development.

## 🎯 Prerequisites

1. **Claude Code** with MCP (Model Context Protocol) support
2. **Python 3.8+** installed on your system
3. **Git** for cloning the repository
4. **API Keys** for your preferred AI provider

## 📋 Step-by-Step Installation

### Step 1: Install Claude Code

If you haven't already, install Claude Code:

```bash
# Install via npm (recommended)
npm install -g @anthropic-ai/claude-code

# Or download from the official website
# https://claude.ai/code
```

Verify installation:
```bash
claude --version
```

### Step 2: Clone Data Pizza Repository

```bash
# Clone the repository
git clone https://github.com/inferis995/data-pizza.git

# Navigate to the project directory
cd data-pizza

# Verify the structure
ls -la
```

You should see:
```
data-pizza/
├── skills/
│   ├── datapizza-agent-creator/
│   │   └── SKILL.md
│   └── datapizza-tool-builder/
│       └── SKILL.md
├── examples/
├── docs/
├── README.md
└── ...
```

### Step 3: Install Python Dependencies

```bash
# Create a virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install Datapizza AI framework
pip install datapizza-ai

# Install official tools
pip install datapizza-ai-tools-sqldatabase
pip install datapizza-ai-tools-duckduckgo
pip install datapizza-ai-tools-filesystem
pip install datapizza-ai-tools-web-fetch

# Install vector stores for RAG capabilities
pip install qdrant-client
pip install chromadb

# Additional dependencies
pip install requests sqlalchemy pandas python-dotenv
```

### Step 4: Configure API Keys

Set up environment variables for your preferred AI provider:

**Option A: OpenAI**
```bash
# Windows (Command Prompt)
set OPENAI_API_KEY=your-openai-api-key-here

# Windows (PowerShell)
$env:OPENAI_API_KEY="your-openai-api-key-here"

# macOS/Linux
export OPENAI_API_KEY="your-openai-api-key-here"
```

**Option B: Anthropic**
```bash
# Windows (Command Prompt)
set ANTHROPIC_API_KEY=your-anthropic-api-key-here

# Windows (PowerShell)
$env:ANTHROPIC_API_KEY="your-anthropic-api-key-here"

# macOS/Linux
export ANTHROPIC_API_KEY="your-anthropic-api-key-here"
```

**Option C: Google AI**
```bash
# Set Google API key
export GOOGLE_API_KEY="your-google-api-key-here"
```

### Step 5: Configure Claude Code

Create or update your Claude Code configuration file to include Data Pizza skills:

**Windows Configuration Location:**
```
%APPDATA%\Claude\claude_config.json
```

**macOS/Linux Configuration Location:**
```
~/.config/claude/claude_config.json
```

**Configuration Content:**
```json
{
  "skills": [
    {
      "name": "datapizza-agent-creator",
      "path": "C:\\Users\\Utente\\Desktop\\data_pizza\\skills\\datapizza-agent-creator\\SKILL.md",
      "description": "Creates Datapizza AI agents with proper syntax and best practices",
      "category": "development"
    },
    {
      "name": "datapizza-tool-builder",
      "path": "C:\\Users\\Utente\\Desktop\\data_pizza\\skills\\datapizza-tool-builder\\SKILL.md",
      "description": "Creates custom @tool functions for Datapizza AI agents",
      "category": "development"
    }
  ],
  "mcpServers": {
    "datapizza": {
      "command": "python",
      "args": ["-m", "datapizza.mcp_server"],
      "env": {
        "OPENAI_API_KEY": "%OPENAI_API_KEY%",
        "ANTHROPIC_API_KEY": "%ANTHROPIC_API_KEY%"
      }
    }
  }
}
```

⚠️ **Important:** Update the `path` values to match your actual file paths.

### Step 6: Restart Claude Code

After configuring the skills, restart Claude Code to load the new configuration:

```bash
# Stop any running Claude Code instances
# Then restart
claude
```

### Step 7: Verify Installation

Test that the skills are properly installed by running:

```bash
# In Claude Code, type:
/skill datapizza-agent-creator --help

# And test the tool builder:
/skill datapizza-tool-builder --help
```

You should see help messages and usage instructions for both skills.

## 🚀 Quick Start Examples

### Create Your First Agent

In Claude Code, run:

```bash
/skill datapizza-agent-creator --type basic --name assistant --provider openai
```

This will generate a basic agent template that you can use immediately.

### Create Custom Tools

```bash
/skill datapizza-tool-builder --type database --function get_customer_data
```

This will generate a database tool function with proper error handling.

## 🔧 Troubleshooting

### Common Issues

#### 1. Skills Not Found
**Error:** `Skill not found: datapizza-agent-creator`

**Solution:**
- Verify the file paths in your configuration are correct
- Ensure Claude Code has been restarted after configuration
- Check that the SKILL.md files exist in the specified locations

#### 2. API Key Issues
**Error:** `API key not found or invalid`

**Solution:**
- Verify your API key is correctly set in environment variables
- Check that the API key is valid and active
- Ensure you're using the correct environment variable name

#### 3. Module Import Errors
**Error:** `ModuleNotFoundError: No module named 'datapizza'`

**Solution:**
- Verify all dependencies are installed: `pip install datapizza-ai`
- Check you're using the correct Python environment
- Try installing in development mode: `pip install -e .`

#### 4. Permission Issues
**Error:** `Permission denied` when accessing files

**Solution:**
- Run Claude Code with appropriate permissions
- Check file permissions on the Data Pizza directory
- On Windows, try running as administrator

### Debug Mode

Enable debug logging to troubleshoot issues:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Getting Help

If you encounter issues:

1. **Check the logs:** Look for error messages in Claude Code output
2. **Verify configuration:** Double-check file paths and environment variables
3. **Test dependencies:** Ensure all Python packages are installed correctly
4. **Check GitHub Issues:** [Data Pizza Issues](https://github.com/inferis995/data-pizza/issues)
5. **Join the community:** Ask for help in discussions

## 📚 Advanced Configuration

### Custom Skills Directory

If you want to store skills in a different location, update your configuration:

```json
{
  "skills": [
    {
      "name": "datapizza-agent-creator",
      "path": "D:\\my-skills\\datapizza-agent-creator\\SKILL.md"
    }
  ]
}
```

### Multiple AI Providers

Configure multiple providers in your environment:

```bash
export OPENAI_API_KEY="your-openai-key"
export ANTHROPIC_API_KEY="your-anthropic-key"
export GOOGLE_API_KEY="your-google-key"
```

Then specify the provider when creating agents:

```bash
/skill datapizza-agent-creator --type basic --name assistant --provider anthropic
```

### Custom Tool Integration

To use custom tools with your agents:

1. Create the tool using `/skill datapizza-tool-builder`
2. Save the generated tool code to a Python file
3. Import and use the tool in your agent code

## 🎯 Best Practices

### Development Workflow

1. **Start Simple:** Begin with basic agent templates
2. **Iterate:** Gradually add custom tools and complexity
3. **Test:** Test agents thoroughly before deployment
4. **Document:** Keep track of custom tools and their purposes

### Security Considerations

- Never commit API keys to version control
- Use environment variables for sensitive configuration
- Validate inputs in custom tools
- Follow the principle of least privilege

### Performance Optimization

- Use appropriate model sizes for your use case
- Implement caching for frequently accessed data
- Monitor agent performance and token usage
- Use streaming responses for long-running tasks

## 🎉 You're Ready!

Congratulations! You now have Data Pizza skills configured with Claude Code. You can:

- ✅ Create AI agents with `/skill datapizza-agent-creator`
- ✅ Build custom tools with `/skill datapizza-tool-builder`
- ✅ Integrate with Datapizza AI framework
- ✅ Deploy production-ready AI solutions

Start building amazing AI agents! 🍕