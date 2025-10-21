"""
Data Pizza - Interactive Demo
This script demonstrates the capabilities of Data Pizza skills
with Datapizza AI framework in an interactive way.
"""

import os
import sys
from typing import Dict, Any

# Add the parent directory to the path so we can import our examples
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def print_banner():
    """Print the demo banner."""
    print("🍕" * 50)
    print(" " * 15 + "DATA PIZZA INTERACTIVE DEMO")
    print(" " * 20 + "Datapizza AI Skills for Claude Code")
    print("🍕" * 50)
    print()

def show_menu():
    """Display the main menu."""
    print("What would you like to explore today?")
    print()
    print("1. 🤖 Agent Creator - Generate AI agents")
    print("2. 🛠️  Tool Builder - Create custom tools")
    print("3. 📚 Knowledge Base - RAG agent demo")
    print("4. 🛒 E-commerce - Customer service demo")
    print("5. 📖 Documentation - View setup guide")
    print("6. 🔧 Configuration - Check setup")
    print("0. 🚪 Exit")
    print()

def demo_agent_creator():
    """Demonstrate agent creator capabilities."""
    print("\n🤖 AGENT CREATOR DEMO")
    print("=" * 40)
    print()

    print("The Agent Creator skill helps you generate production-ready AI agents.")
    print("Here are some examples of what you can create:")
    print()

    agent_types = {
        "1": {
            "name": "Customer Service Agent",
            "description": "Handles customer inquiries, order status, and support tickets",
            "command": "/skill datapizza-agent-creator --type customer-service --name support_bot --provider openai",
            "features": ["Database integration", "Order lookup", "Ticket creation", "Status updates"]
        },
        "2": {
            "name": "Research Assistant",
            "description": "Conducts web research and compiles comprehensive reports",
            "command": "/skill datapizza-agent-creator --type research --name researcher --provider openai --tools web-search,document-analysis",
            "features": ["Web search", "Document analysis", "Source citation", "Report generation"]
        },
        "3": {
            "name": "E-commerce Assistant",
            "description": "Helps customers with shopping, recommendations, and orders",
            "command": "/skill datapizza-agent-creator --type ecommerce --name shop_assistant --provider openai",
            "features": ["Product catalog", "Inventory check", "Order processing", "Recommendations"]
        },
        "4": {
            "name": "RAG Knowledge Agent",
            "description": "Retrieval-augmented generation for knowledge-based answers",
            "command": "/skill datapizza-agent-creator --type rag --name knowledge_bot --provider openai --vector-store qdrant",
            "features": ["Vector search", "Context awareness", "Knowledge integration", "Source attribution"]
        }
    }

    print("Available Agent Templates:")
    for key, agent in agent_types.items():
        print(f"\n{key}. {agent['name']}")
        print(f"   Description: {agent['description']}")
        print(f"   Command: {agent['command']}")
        print(f"   Features: {', '.join(agent['features'])}")

    print("\n💡 Pro Tip: Each agent template includes proper error handling,")
    print("   logging, and follows Datapizza AI best practices!")

    input("\nPress Enter to continue...")

def demo_tool_builder():
    """Demonstrate tool builder capabilities."""
    print("\n🛠️ TOOL BUILDER DEMO")
    print("=" * 40)
    print()

    print("The Tool Builder skill creates custom @tool functions for your agents.")
    print("Here are the types of tools you can create:")
    print()

    tool_types = {
        "1": {
            "type": "Database Tools",
            "description": "CRUD operations and data management",
            "examples": [
                "get_customer_data(customer_id: str) -> str",
                "update_inventory(product_id: str, quantity: int) -> str",
                "search_products(category: str, price_range: str) -> str"
            ],
            "command": "/skill datapizza-tool-builder --type database --function manage_customers"
        },
        "2": {
            "type": "API Integration Tools",
            "description": "REST API calls and web service integration",
            "examples": [
                "fetch_weather_data(city: str) -> str",
                "send_slack_notification(webhook: str, message: str) -> str",
                "process_payment(payment_data: dict) -> str"
            ],
            "command": "/skill datapizza-tool-builder --type api --function weather_service"
        },
        "3": {
            "type": "File System Tools",
            "description": "File operations and document processing",
            "examples": [
                "process_json_file(file_path: str, operation: str) -> str",
                "extract_pdf_text(pdf_path: str) -> str",
                "create_backup(source_dir: str, backup_dir: str) -> str"
            ],
            "command": "/skill datapizza-tool-builder --type file --function document_processor"
        },
        "4": {
            "type": "Business Logic Tools",
            "description": "Custom business rules and calculations",
            "examples": [
                "calculate_discount(price: float, tier: str, quantity: int) -> str",
                "generate_invoice(order_data: dict) -> str",
                "validate_shipping_address(address: dict) -> str"
            ],
            "command": "/skill datapizza-tool-builder --type business --function pricing_calculator"
        }
    }

    for key, tool in tool_types.items():
        print(f"\n{key}. {tool['type']}")
        print(f"   Description: {tool['description']}")
        print(f"   Examples:")
        for example in tool['examples']:
            print(f"     • {example}")
        print(f"   Command: {tool['command']}")

    print("\n🔧 All tools include:")
    print("   • Type hints and validation")
    print("   • Comprehensive error handling")
    print("   • Clear documentation")
    print("   • Integration examples")

    input("\nPress Enter to continue...")

def demo_rag_agent():
    """Demonstrate RAG agent capabilities."""
    print("\n📚 RAG KNOWLEDGE AGENT DEMO")
    print("=" * 40)
    print()

    print("RAG (Retrieval-Augmented Generation) agents combine vector search with AI generation.")
    print("They can maintain and query a knowledge base while providing context-aware answers.")
    print()

    # Simulate knowledge base operations
    print("🔍 Simulating Knowledge Base Operations:")
    print()

    knowledge_samples = [
        {
            "topic": "Datapizza AI Framework",
            "content": "Datapizza AI is a Python framework for building production-ready AI agents with multi-provider support.",
            "source": "Official Documentation"
        },
        {
            "topic": "Data Pizza Skills",
            "content": "Data Pizza provides specialized Claude Code skills for rapid agent and tool development.",
            "source": "GitHub Repository"
        },
        {
            "topic": "Best Practices",
            "content": "Always include proper error handling, type hints, and documentation in agent tools.",
            "source": "Development Guide"
        }
    ]

    print("1. Adding information to knowledge base:")
    for i, sample in enumerate(knowledge_samples, 1):
        print(f"   ✓ Added: {sample['topic']} from {sample['source']}")

    print("\n2. Sample queries and responses:")

    queries = [
        "What is Datapizza AI?",
        "How can Data Pizza help with agent development?",
        "What are the best practices for creating tools?"
    ]

    for i, query in enumerate(queries, 1):
        print(f"\n   Query {i}: {query}")
        relevant_info = [k for k in knowledge_samples if k['topic'].lower() in query.lower() or any(word in k['content'].lower() for word in query.lower().split() if len(word) > 3)]

        if relevant_info:
            info = relevant_info[0]
            print(f"   🎯 Found relevant information: {info['topic']}")
            print(f"   📄 Source: {info['source']}")
            print(f"   💡 Answer: Based on the knowledge base, {info['content'].lower()}")
        else:
            print(f"   ❓ No specific information found. Would you like me to search the web?")

    print("\n🚀 Key Features of RAG Agents:")
    print("   • Context-aware responses")
    print("   • Source attribution")
    print("   • Continuous learning")
    print("   • Web content integration")
    print("   • Knowledge base management")

    input("\nPress Enter to continue...")

def demo_ecommerce():
    """Demonstrate e-commerce customer service agent."""
    print("\n🛒 E-COMMERCE DEMO")
    print("=" * 40)
    print()

    print("Experience a customer service interaction with an AI agent!")
    print("This agent can help with orders, accounts, and support issues.")
    print()

    # Simulate customer scenarios
    scenarios = [
        {
            "customer": "Sarah Johnson",
            "issue": "Order status inquiry",
            "conversation": [
                "Agent: Hello! How can I help you today?",
                "Customer: Hi, I'm checking on order #12345",
                "Agent: Let me look that up for you... [searches database]",
                "Agent: I found your order! It's currently 'In Transit' and should arrive in 2-3 days.",
                "Customer: Great! Can you tell me what's in it?",
                "Agent: Your order contains: 2x Python Programming Book, 1x Wireless Mouse",
                "Customer: Perfect, thank you!",
                "Agent: You're welcome! Is there anything else I can help with?"
            ]
        },
        {
            "customer": "Mike Chen",
            "issue": "Technical support",
            "conversation": [
                "Agent: Hello! How can I assist you today?",
                "Customer: I'm having trouble logging into my account",
                "Agent: I'm sorry to hear that. Let me help you resolve this issue.",
                "Agent: Can you confirm your email address so I can locate your account?",
                "Customer: mike.chen@email.com",
                "Agent: Thanks! I found your account. I'll create a support ticket for this issue.",
                "Agent: Support ticket #TKT789 created. Our technical team will contact you within 24 hours.",
                "Customer: Thank you for your help!",
                "Agent: You're welcome! We'll get this resolved for you quickly."
            ]
        }
    ]

    print("Sample Customer Interactions:")
    print()

    for i, scenario in enumerate(scenarios, 1):
        print(f"Scenario {i}: {scenario['customer']} - {scenario['issue']}")
        print("-" * 40)

        for line in scenario['conversation']:
            if line.startswith("Customer:"):
                print(f"👤 {line}")
            elif line.startswith("Agent:"):
                print(f"🤖 {line}")
            else:
                print(f"   {line}")

        print()
        print("✅ Issue resolved successfully!")
        print()

    print("🛠️ Tools Used in This Demo:")
    print("   • Database queries (order lookup)")
    print("   • Customer account management")
    print("   • Support ticket creation")
    print("   • Status updates and notifications")

    input("\nPress Enter to continue...")

def show_documentation():
    """Display documentation links."""
    print("\n📖 DOCUMENTATION")
    print("=" * 40)
    print()

    docs = {
        "Setup Guide": "docs/claude-setup.md",
        "Agent Creator": "skills/datapizza-agent-creator/SKILL.md",
        "Tool Builder": "skills/datapizza-tool-builder/SKILL.md",
        "Examples": "examples/",
        "Main README": "README.md",
        "Contributing": "CONTRIBUTING.md"
    }

    print("Available Documentation:")
    for title, path in docs.items():
        print(f"   📄 {title}: {path}")

    print("\n🌐 Online Resources:")
    print("   🍕 Data Pizza GitHub: https://github.com/inferis995/data-pizza")
    print("   🤖 Datapizza AI: https://github.com/datapizza-labs/datapizza-ai")
    print("   💬 Claude Code: https://claude.ai/code")

    input("\nPress Enter to continue...")

def check_configuration():
    """Check if the environment is properly configured."""
    print("\n🔧 CONFIGURATION CHECK")
    print("=" * 40)
    print()

    checks = [
        {
            "name": "Python Version",
            "check": lambda: sys.version_info >= (3, 8),
            "message": "Python 3.8+ is required"
        },
        {
            "name": "Data Pizza Directory",
            "check": lambda: os.path.exists("skills"),
            "message": "skills directory not found"
        },
        {
            "name": "Agent Creator Skill",
            "check": lambda: os.path.exists("skills/datapizza-agent-creator/SKILL.md"),
            "message": "datapizza-agent-creator skill file not found"
        },
        {
            "name": "Tool Builder Skill",
            "check": lambda: os.path.exists("skills/datapizza-tool-builder/SKILL.md"),
            "message": "datapizza-tool-builder skill file not found"
        },
        {
            "name": "Example Files",
            "check": lambda: os.path.exists("examples"),
            "message": "examples directory not found"
        }
    ]

    print("Running configuration checks...")
    print()

    all_passed = True
    for check in checks:
        try:
            if check["check"]():
                print(f"✅ {check['name']}: OK")
            else:
                print(f"❌ {check['name']}: FAILED - {check['message']}")
                all_passed = False
        except Exception as e:
            print(f"⚠️  {check['name']}: ERROR - {str(e)}")
            all_passed = False

    print()

    # Check environment variables
    env_vars = ["OPENAI_API_KEY", "ANTHROPIC_API_KEY", "GOOGLE_API_KEY"]
    print("Environment Variables:")
    for var in env_vars:
        value = os.getenv(var)
        if value:
            masked = value[:8] + "*" * (len(value) - 8) if len(value) > 8 else "*" * len(value)
            print(f"✅ {var}: {masked}")
        else:
            print(f"⚠️  {var}: Not set (optional)")

    print()

    if all_passed:
        print("🎉 Configuration looks good! You're ready to use Data Pizza skills.")
    else:
        print("⚠️  Some configuration issues were found. Please review the failed checks.")
        print("   Refer to the setup guide for assistance: docs/claude-setup.md")

    input("\nPress Enter to continue...")

def main():
    """Main demo loop."""
    print_banner()

    while True:
        show_menu()
        choice = input("Enter your choice (0-6): ").strip()

        if choice == "0":
            print("\nThank you for trying Data Pizza! 🍕")
            print("Visit us at: https://github.com/inferis995/data-pizza")
            break
        elif choice == "1":
            demo_agent_creator()
        elif choice == "2":
            demo_tool_builder()
        elif choice == "3":
            demo_rag_agent()
        elif choice == "4":
            demo_ecommerce()
        elif choice == "5":
            show_documentation()
        elif choice == "6":
            check_configuration()
        else:
            print("\n❌ Invalid choice. Please enter a number between 0 and 6.")
            input("Press Enter to continue...")

        print("\n" + "="*50)

if __name__ == "__main__":
    main()