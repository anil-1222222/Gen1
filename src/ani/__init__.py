import os
from dotenv import load_dotenv

# Load environment variables from .env file for the whole project
load_dotenv()

def main() -> None:
    print("Hello from ani!")
    
    # Check configured API keys
    keys = {
        "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY"),
        "GROQ_API_KEY": os.getenv("GROQ_API_KEY"),
        "GOOGLE_API_KEY": os.getenv("GOOGLE_API_KEY"),
    }
    
    configured = []
    for key_name, key_val in keys.items():
        if key_val and not key_val.startswith("your_") and not key_val.endswith("_here"):
            # Mask key for secure display
            masked = key_val[:7] + "..." + key_val[-4:] if len(key_val) > 12 else "***"
            configured.append(f"  [+] {key_name}: {masked}")
    
    if configured:
        print("Configured API Keys:")
        for line in configured:
            print(line)
    else:
        print("No valid API keys detected in .env file.")

if __name__ == "__main__":
    main()
