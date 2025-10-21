// Data Pizza ChatBot Configuration
// Questo file contiene la configurazione avanzata per il chatbot

const CHATBOT_CONFIG = {
    // API Configuration
    API: {
        BASE_URL: 'https://api.mistral.ai/v1',
        MODEL: 'magistral-medium-2507',
        API_KEY: 'JHoFOzDdRZOV483zX2xpfRkQXQYO0XDX',
        MAX_TOKENS: 1000,
        TEMPERATURE: 0.7,
        TOP_P: 0.9
    },

    // Web Search Configuration
    WEB_SEARCH: {
        ENABLED: false,
        PROVIDERS: [
            {
                name: 'DuckDuckGo',
                url: 'https://api.duckduckgo.com/',
                priority: 1
            },
            {
                name: 'Brave Search',
                url: 'https://api.search.brave.com/',
                priority: 2
            }
        ],
        TRIGGER_KEYWORDS: [
            'ultimo', 'recente', 'attuale', 'nuovo', 'aggiornamento',
            'versione', 'notizie', 'news', 'latest', 'release'
        ]
    },

    // Conversation Management
    CONVERSATION: {
        MAX_HISTORY_LENGTH: 20,
        CONTEXT_WINDOW: 10,
        AUTO_SUMMARIZE: true,
        PERSISTENCE: false // In futuro: salvare conversazioni
    },

    // UI Configuration
    UI: {
        POSITION: 'bottom-right',
        WIDTH: '384px',
        HEIGHT: '600px',
        ANIMATION_DURATION: '300ms',
        TYPING_DELAY: 100,
        SCROLL_BEHAVIOR: 'smooth'
    },

    // Features
    FEATURES: {
        VOICE_INPUT: false, // Coming soon
        CODE_HIGHLIGHTING: true,
        MARKDOWN_RENDERING: true,
        EMOJI_SUPPORT: true,
        FILE_UPLOAD: false, // Coming soon
        EXPORT_CHAT: false // Coming soon
    },

    // Analytics
    ANALYTICS: {
        ENABLED: true,
        TRACK_EVENTS: [
            'chat_opened',
            'message_sent',
            'web_search_toggled',
            'minimize_chat',
            'error_occurred'
        ]
    }
};

// Enhanced Knowledge Base for Data Pizza
const DATA_PIZZA_KNOWLEDGE = {
    framework: {
        name: "Datapizza AI",
        description: "Framework GenAI Python con design 'less abstraction, more control'",
        url: "https://github.com/datapizza-labs/datapizza-ai",
        version: "Latest",
        license: "MIT",
        language: "Python"
    },

    quick_start: {
        installation: "pip install datapizza-ai",
        basic_example: `
from datapizza.agents import Agent
from datapizza.clients.openai import OpenAIClient
from datapizza.tools import tool

@tool
def get_weather(city: str) -> str:
    return f"The weather in {city} is sunny"

client = OpenAIClient(api_key="YOUR_API_KEY")
agent = Agent(name="assistant", client=client, tools=[get_weather])
response = agent.run("What is the weather in Rome?")`
    },

    core_concepts: {
        agents: {
            definition: "Entità AI con capacità di utilizzare strumenti per compiti specifici",
            use_cases: ["Customer service", "Research assistant", "Code generation", "Data analysis"],
            key_features: ["Tool integration", "Multi-provider support", "Observability"]
        },
        tools: {
            definition: "Funzioni che gli agenti possono chiamare per interagire con sistemi esterni",
            available_tools: [
                "SQLDatabase - Operazioni database",
                "DuckDuckGo - Ricerca web",
                "FileSystem - Operazioni file",
                "WebFetch - Contenuti web"
            ]
        },
        rag: {
            definition: "Retrieval-Augmented Generation",
            components: ["Vector stores", "Embeddings", "Rerankers"],
            vector_stores: ["Qdrant", "ChromaDB"],
            use_cases: ["Knowledge base", "Document Q&A", "Research"]
        }
    },

    providers: {
        openai: {
            models: ["gpt-4", "gpt-4-turbo", "gpt-3.5-turbo"],
            client: "OpenAIClient",
            features: ["Chat completions", "Function calling", "Embeddings"]
        },
        anthropic: {
            models: ["claude-3-opus", "claude-3-sonnet", "claude-3-haiku"],
            client: "AnthropicClient",
            features: ["Chat completions", "Vision"]
        },
        google: {
            models: ["gemini-pro", "gemini-pro-vision"],
            client: "GoogleClient",
            features: ["Chat completions", "Vision", "Function calling"]
        },
        mistral: {
            models: ["mistral-7b", "mixtral-8x7b", "magistral-medium-2507"],
            client: "MistralClient",
            features: ["Chat completions", "Function calling", "OCR"]
        },
        azure: {
            models: ["gpt-4", "gpt-35-turbo"],
            client: "AzureOpenAIClient",
            features: ["Chat completions", "Enterprise features"]
        }
    },

    integrations: {
        document_parsers: [
            "Azure AI Document Intelligence",
            "Docling",
            "Custom parsers"
        ],
        caching: [
            "Redis integration",
            "In-memory caching"
        ],
        monitoring: [
            "OpenTelemetry tracing",
            "Performance metrics",
            "Error tracking"
        ]
    },

    best_practices: {
        development: [
            "Use type hints for tool functions",
            "Include proper error handling",
            "Add comprehensive docstrings",
            "Test tools with various inputs",
            "Use environment variables for API keys"
        ],
        production: [
            "Implement logging and monitoring",
            "Use connection pooling",
            "Set appropriate timeouts",
            "Implement rate limiting",
            "Use proper error handling"
        ]
    },

    troubleshooting: {
        common_issues: [
            {
                problem: "API Key not found",
                solution: "Check environment variables and API key format"
            },
            {
                problem: "Tool not working",
                solution: "Verify tool syntax and imports"
            },
            {
                problem: "Agent not responding",
                solution: "Check client configuration and network connectivity"
            }
        ]
    },

    resources: {
        documentation: "https://docs.datapizza.ai",
        examples: "https://github.com/datapizza-labs/datapizza-ai/tree/main/examples",
        api_reference: "https://docs.datapizza.ai/api-reference",
        community: "https://github.com/datapizza-labs/datapizza-ai/discussions"
    },

    data_pizza_skills: {
        agent_creator: {
            description: "Skill per creare agenti AI con Claude Code",
            features: [
                "5+ pre-built templates",
                "Multi-provider support",
                "Production-ready error handling",
                "Quick setup"
            ],
            templates: [
                "Customer service agent",
                "E-commerce assistant",
                "Research assistant",
                "Document processor",
                "RAG agent",
                "Multi-agent system"
            ]
        },
        tool_builder: {
            description: "Skill per creare tools personalizzati",
            features: [
                "Database tools",
                "API integration tools",
                "File system tools",
                "Business logic tools",
                "Utility tools"
            ],
            patterns: [
                "CRUD operations",
                "REST API calls",
                "File operations",
                "Calculations and validation"
            ]
        }
    }
};

// System prompts for different contexts
const SYSTEM_PROMPTS = {
    general: `Sei un assistente AI esperto di Data Pizza AI framework.
Informazioni chiave su Data Pizza:
${JSON.stringify(DATA_PIZZA_KNOWLEDGE, null, 2)}

Rispondi sempre in italiano. Sii preciso, utile e professionale.
Usa le informazioni fornite per rispondere alle domande.
Se non conosci la risposta, suggerisci dove trovare l'informazione.`,

    with_web_search: `Sei un assistente AI esperto di Data Pizza AI framework con accesso alla ricerca web.
Informazioni chiave su Data Pizza:
${JSON.stringify(DATA_PIZZA_KNOWLEDGE, null, 2)}

Rispondi sempre in italiano. Sii preciso, utile e professionale.
Usa le informazioni fornite e i risultati della ricerca web per rispondere alle domande.
Quando usi informazioni dalla ricerca, cita le fonti.
Se non conosci la risposta, suggerisci dove trovare l'informazione.`,

    technical_help: `Sei un assistente tecnico specializzato in Data Pizza AI framework.
Fornisci soluzioni tecniche dettagliate, codice di esempio e best practices.
Usa le informazioni fornite per dare risposte tecniche precise.
Rispondi sempre in italiano.`,

    beginner_friendly: `Sei un assistente AI che spiega Data Pizza AI framework in modo semplice e chiaro.
Usa analogie e esempi pratici per aiutare i principianti.
Rispondi sempre in italiano con un tono amichevole e incoraggiante.`
};

// Export configurations
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        CHATBOT_CONFIG,
        DATA_PIZZA_KNOWLEDGE,
        SYSTEM_PROMPTS
    };
}

// Make available globally for browser
if (typeof window !== 'undefined') {
    window.CHATBOT_CONFIG = CHATBOT_CONFIG;
    window.DATA_PIZZA_KNOWLEDGE = DATA_PIZZA_KNOWLEDGE;
    window.SYSTEM_PROMPTS = SYSTEM_PROMPTS;
}