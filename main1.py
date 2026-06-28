import sys

def sanitize_input(raw_text):
    """
    Phase 1: Input Sanitization & Normalization
    Converts to lowercase and cleans outer spaces to prevent rule bypasses.
    """
    return raw_text.strip().lower()

def get_chatbot_response(cleaned_text):
    """
    Phase 2 & 3: Process Skeleton & Feedback Response Loop
    Pure deterministic logic matching user intents with zero hallucination.
    """
    if cleaned_text in ['hello', 'hi', 'hey', 'greetings', 'wassup']:
        return "Hello Intern! Welcome to the DecodeLabs Artificial Intelligence program."
    
    elif 'project 1' in cleaned_text or 'chatbot' in cleaned_text:
        return "Project 1 focuses on foundational control flow, decision-making logic, and deterministic architectures."
    
    elif 'project 2' in cleaned_text or 'classification' in cleaned_text:
        return "Project 2 covers Supervised Learning pipelines using feature engineering, scaling, and classification models."
    
    elif 'badge' in cleaned_text or 'qualification' in cleaned_text:
        return "You must successfully complete and verify each project to unlock subsequent modules and earn your official badge."
    
    elif cleaned_text in ['exit', 'quit', 'bye', 'stop']:
        return "EXIT"
        
    else:
        return "Intent not identified. Please ask about greetings, Project 1, Project 2, or qualifying badges."

def main():
    print("==================================================")
    print("      DECODELABS RULE-BASED AI ENGINE LOOP        ")
    print("==================================================")
    print("Type 'exit' or 'bye' to terminate the session.\n")
    
    while True:
        try:
            user_raw = input("You: ")
         
            clean_text = sanitize_input(user_raw)
            
            if not clean_text:
                continue
            bot_response = get_chatbot_response(clean_text)
            
            if bot_response == "EXIT":
                print("Bot: Goodbye Intern! Structural session terminated safely.")
                break
                
            print(f"Bot: {bot_response}\n")
            
        except (KeyboardInterrupt, EOFError):
            print("\nBot: Session interrupted. Exiting clean loop.")
            break

if __name__ == "__main__":
    main()