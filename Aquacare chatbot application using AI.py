#!/usr/bin/env python3
"""
AquaCare Chatbot System
A complete conversational AI assistant for water-related topics
"""

import os
import sys
import time
import random
from datetime import datetime

class AquaCareChatbot:
    """Main chatbot class for AquaCare"""
    
    def __init__(self):
        self.user_name = None
        self.conversation_history = []
        self.session_start = datetime.now()
        
        # Knowledge base with patterns and responses
        self.knowledge_base = {
            'greeting': {
                'patterns': ['hello', 'hi', 'hey', 'good morning', 'good afternoon', 'good evening', 'greetings'],
                'responses': [
                    "Hello! I'm AquaCare, your water conservation assistant. How can I help you today?",
                    "Hi there! Welcome to AquaCare. What water-related questions do you have?",
                    "Greetings! I'm here to help with all things water-related. What would you like to know?"
                ]
            },
            'water_conservation': {
                'patterns': [
                    'save water', 'conservation', 'how to save water', 'reduce water usage',
                    'water saving tips', 'conserve water', 'save water at home'
                ],
                'responses': [
                    "Here are some water conservation tips:\n"
                    "🏠 At Home:\n"
                    "• Fix leaking taps and pipes immediately\n"
                    "• Take shorter showers (5 minutes or less)\n"
                    "• Turn off tap while brushing teeth\n"
                    "• Run washing machine with full loads only\n"
                    "• Install water-efficient fixtures\n\n"
                    "🌱 Outdoors:\n"
                    "• Water plants in early morning or evening\n"
                    "• Use mulch to retain soil moisture\n"
                    "• Collect rainwater for gardening\n"
                    "• Choose drought-resistant plants",
                    
                    "Did you know?\n"
                    "• A dripping tap can waste 20 gallons per day\n"
                    "• Turning off tap while brushing saves 4 gallons/minute\n"
                    "• Fixing leaks can save 10% on water bills"
                ]
            },
            'water_quality': {
                'patterns': [
                    'water quality', 'safe water', 'drinking water', 'water testing',
                    'water purity', 'is water safe', 'water contamination'
                ],
                'responses': [
                    "Water Quality Indicators:\n"
                    "✅ Good water should be:\n"
                    "• Clear (not cloudy or colored)\n"
                    "• No unusual taste (metallic, salty)\n"
                    "• No unpleasant odor (rotten eggs, chlorine)\n\n"
                    "📊 Key Parameters:\n"
                    "• pH level: 6.5-8.5 (ideal)\n"
                    "• Total Dissolved Solids: <500 ppm\n"
                    "• No bacteria (E. coli, coliform)\n\n"
                    "💡 Tips:\n"
                    "• Test water annually\n"
                    "• Use certified water filters\n"
                    "• Contact local water authority for reports",
                    
                    "Signs of poor water quality:\n"
                    "• Cloudy appearance\n"
                    "• Metallic or bitter taste\n"
                    "• Rotten egg smell (sulfur)\n"
                    "• Stains on sinks/clothes"
                ]
            },
            'water_footprint': {
                'patterns': [
                    'water footprint', 'water usage', 'daily water use',
                    'how much water do i use', 'water consumption', 'virtual water'
                ],
                'responses': [
                    "Understanding Your Water Footprint:\n\n"
                    "💧 Direct Water Use (Daily):\n"
                    "• Shower (8 min): 17 gallons\n"
                    "• Toilet flush: 1.6-3.5 gallons\n"
                    "• Dishwasher: 6-16 gallons/load\n"
                    "• Washing machine: 15-30 gallons/load\n\n"
                    "🌍 Indirect Water (Virtual Water):\n"
                    "• 1 apple: 33 gallons\n"
                    "• 1 cup of coffee: 37 gallons\n"
                    "• 1 burger: 660 gallons\n"
                    "• 1 pair jeans: 2,900 gallons\n\n"
                    "Average US daily footprint: 2,000 gallons",
                    
                    "Reduce your water footprint:\n"
                    "• Eat less meat (especially beef)\n"
                    "• Choose sustainable products\n"
                    "• Reduce food waste\n"
                    "• Buy second-hand items\n"
                    "• Support water-efficient companies"
                ]
            },
            'water_treatment': {
                'patterns': [
                    'water treatment', 'water purification', 'water filtration',
                    'how is water treated', 'clean water', 'purify water'
                ],
                'responses': [
                    "Water Treatment Process:\n\n"
                    "🏭 Municipal Treatment:\n"
                    "1. Coagulation: Chemicals bind to dirt\n"
                    "2. Sedimentation: Heavy particles settle\n"
                    "3. Filtration: Pass through sand/gravel\n"
                    "4. Disinfection: Chlorine/UV kills germs\n"
                    "5. Storage: Clean water ready for use\n\n"
                    "🏠 Home Treatment Options:\n"
                    "• Boiling (kills bacteria/viruses)\n"
                    "• Activated carbon filters (improves taste)\n"
                    "• Reverse osmosis (removes contaminants)\n"
                    "• UV purifiers (destroys microorganisms)\n"
                    "• Distillation (produces pure water)",
                    
                    "Emergency Water Purification:\n"
                    "1. Boil vigorously for 1 minute\n"
                    "2. Add 8 drops bleach per gallon\n"
                    "3. Use water purification tablets\n"
                    "4. Filter through clean cloth first"
                ]
            },
            'water_crisis': {
                'patterns': [
                    'water crisis', 'water scarcity', 'water shortage',
                    'drought', 'water stress', 'world water crisis'
                ],
                'responses': [
                    "Global Water Crisis Facts:\n\n"
                    "📊 Statistics:\n"
                    "• 2.2 billion people lack safe drinking water\n"
                    "• 4 billion face severe water scarcity (1 month/year)\n"
                    "• By 2025, half of world population in water-stressed areas\n"
                    "• 80% of wastewater returns to environment untreated\n\n"
                    "🌡️ Causes:\n"
                    "• Climate change\n"
                    "• Population growth\n"
                    "• Pollution\n"
                    "• Poor infrastructure\n"
                    "• Over-extraction of groundwater",
                    
                    "Solutions to Water Crisis:\n"
                    "• Rainwater harvesting\n"
                    "• Water recycling and reuse\n"
                    "• Desalination plants\n"
                    "• Efficient irrigation\n"
                    "• Protect wetlands and watersheds\n"
                    "• Fix leaking infrastructure"
                ]
            },
            'water_recycling': {
                'patterns': [
                    'water recycling', 'reuse water', 'greywater',
                    'wastewater treatment', 'reclaim water', 'recycled water'
                ],
                'responses': [
                    "Water Recycling Methods:\n\n"
                    "🔄 Types of Reclaimed Water:\n"
                    "• Greywater: From sinks, showers, laundry\n"
                    "• Blackwater: From toilets (requires treatment)\n"
                    "• Stormwater: Rain runoff\n\n"
                    "🌿 Uses for Recycled Water:\n"
                    "• Landscape irrigation\n"
                    "• Agricultural irrigation\n"
                    "• Industrial processes\n"
                    "• Toilet flushing\n"
                    "• Groundwater recharge\n\n"
                    "💡 Benefits:\n"
                    "• Reduces freshwater demand\n"
                    "• Decreases pollution\n"
                    "• Saves money\n"
                    "• Provides drought resilience",
                    
                    "Simple Greywater Systems:\n"
                    "• Laundry-to-landscape direct use\n"
                    "• Branched drain gravity systems\n"
                    "• Pumped systems for higher use\n"
                    "• Use biodegradable soaps only"
                ]
            },
            'aquatic_life': {
                'patterns': [
                    'aquatic life', 'ocean animals', 'freshwater animals',
                    'water animals', 'marine life', 'fish', 'water ecosystems'
                ],
                'responses': [
                    "Aquatic Ecosystems:\n\n"
                    "🌊 Marine (Salt Water):\n"
                    "• Oceans cover 71% of Earth\n"
                    "• Coral reefs: Rainforests of the sea\n"
                    "• Home to: whales, dolphins, sharks, fish\n\n"
                    "💧 Freshwater:\n"
                    "• Rivers, lakes, wetlands\n"
                    "• Only 2.5% of Earth's water\n"
                    "• Home to: fish, frogs, turtles, insects\n\n"
                    "⚠️ Threats:\n"
                    "• Pollution (plastic, chemicals)\n"
                    "• Overfishing\n"
                    "• Climate change\n"
                    "• Habitat destruction",
                    
                    "Protect Aquatic Life:\n"
                    "• Reduce plastic use\n"
                    "• Proper chemical disposal\n"
                    "• Sustainable seafood choices\n"
                    "• Participate in cleanups\n"
                    "• Support marine protected areas"
                ]
            },
            'water_fun_facts': {
                'patterns': [
                    'fun facts', 'interesting facts', 'water facts',
                    'did you know', 'amazing water facts'
                ],
                'responses': [
                    "💧 Amazing Water Facts:\n\n"
                    "• 60% of human body is water\n"
                    "• Water can dissolve more substances than any other liquid\n"
                    "• Hot water freezes faster than cold water (Mpemba effect)\n"
                    "• Only 0.5% of Earth's water is usable freshwater\n"
                    "• A person can survive weeks without food, but only days without water\n"
                    "• Water is the only substance found naturally in solid, liquid, and gas\n"
                    "• 70% of the human brain is water\n"
                    "• There's the same amount of water now as when Earth was formed",
                    
                    "🌍 More Water Wonders:\n"
                    "• Clouds aren't weightless - they can weigh millions of tons\n"
                    "• Antarctica has 90% of world's ice\n"
                    "• The average water molecule stays in the ocean for 3,000 years\n"
                    "• Humans use 4 trillion cubic meters of freshwater annually"
                ]
            },
            'help': {
                'patterns': ['help', 'what can you do', 'commands', 'options', 'menu'],
                'responses': [
                    "I can help you with these water topics:\n\n"
                    "💧 Water Conservation - Tips to save water\n"
                    "🔬 Water Quality - Safety and testing info\n"
                    "📊 Water Footprint - Understanding water usage\n"
                    "🏭 Water Treatment - Purification methods\n"
                    "🌍 Water Crisis - Global water issues\n"
                    "♻️ Water Recycling - Reusing water\n"
                    "🐠 Aquatic Life - Water ecosystems\n"
                    "✨ Fun Facts - Interesting water facts\n\n"
                    "Type 'history' to see our conversation\n"
                    "Type 'stats' to see session statistics\n"
                    "Type 'exit' or 'bye' to end chat"
                ]
            },
            'history': {
                'patterns': ['history', 'conversation history', 'previous messages', 'chat history'],
                'responses': []  # Will be handled separately
            },
            'stats': {
                'patterns': ['stats', 'statistics', 'session info', 'conversation stats'],
                'responses': []  # Will be handled separately
            },
            'goodbye': {
                'patterns': ['bye', 'goodbye', 'exit', 'quit', 'see you', 'farewell'],
                'responses': [
                    "Thank you for using AquaCare! Remember: every drop counts! 💧",
                    "Goodbye! Stay hydrated and help conserve water! 🌊",
                    "Take care! Feel free to return with more water questions! 🌍",
                    "See you later! Keep saving water! 💙"
                ]
            },
            'thanks': {
                'patterns': ['thanks', 'thank you', 'appreciate it', 'helpful'],
                'responses': [
                    "You're welcome! Happy to help! 😊",
                    "Glad I could assist! Any other water questions?",
                    "My pleasure! Remember to save water! 💧"
                ]
            }
        }
        
        # Fallback responses when no match found
        self.fallback_responses = [
            "I'm not sure about that. Could you ask about water conservation, quality, or treatment?",
            "I don't have information on that specific topic. Try asking about water-related subjects like conservation or quality.",
            "I'm here to help with water topics. What would you like to know about water?",
            "That's outside my knowledge area. I specialize in water-related topics. Try asking something like 'how to save water'?"
        ]
    
    def preprocess_text(self, text):
        """Clean and normalize text input"""
        # Convert to lowercase
        text = text.lower().strip()
        # Remove punctuation
        text = ''.join(c for c in text if c.isalnum() or c.isspace())
        return text
    
    def calculate_similarity(self, text1, text2):
        """Calculate simple similarity between two texts"""
        # Convert to sets of words
        words1 = set(text1.split())
        words2 = set(text2.split())
        
        if not words1 or not words2:
            return 0
        
        # Calculate Jaccard similarity
        intersection = words1.intersection(words2)
        union = words1.union(words2)
        
        return len(intersection) / len(union)
    
    def find_best_intent(self, user_input):
        """Find the best matching intent for user input"""
        processed_input = self.preprocess_text(user_input)
        best_intent = 'fallback'
        best_score = 0
        
        # Check each intent's patterns
        for intent, data in self.knowledge_base.items():
            for pattern in data['patterns']:
                processed_pattern = self.preprocess_text(pattern)
                score = self.calculate_similarity(processed_input, processed_pattern)
                
                # Bonus for exact word matches
                if processed_pattern in processed_input:
                    score += 0.3
                
                if score > best_score:
                    best_score = score
                    best_intent = intent
        
        # Check for common words as fallback
        water_keywords = ['water', 'save', 'quality', 'treatment', 'conservation', 
                         'footprint', 'recycle', 'crisis', 'aquatic']
        
        for keyword in water_keywords:
            if keyword in processed_input:
                best_score += 0.1
        
        # Return best intent if score is above threshold
        return best_intent if best_score > 0.2 else 'fallback'
    
    def get_response(self, intent, user_input):
        """Get response based on intent"""
        if intent == 'history':
            return self.show_history()
        elif intent == 'stats':
            return self.show_statistics()
        elif intent in self.knowledge_base:
            responses = self.knowledge_base[intent]['responses']
            return random.choice(responses) if responses else self.get_fallback()
        else:
            return self.get_fallback()
    
    def get_fallback(self):
        """Get random fallback response"""
        return random.choice(self.fallback_responses)
    
    def show_history(self):
        """Show conversation history"""
        if not self.conversation_history:
            return "No conversation history yet."
        
        history_text = "\n📝 Recent Conversations:\n" + "=" * 40 + "\n"
        for i, exchange in enumerate(self.conversation_history[-10:], 1):
            history_text += f"{i}. You: {exchange['user'][:80]}\n"
            history_text += f"   AquaCare: {exchange['bot'][:80]}\n"
            if i < len(self.conversation_history[-10:]):
                history_text += "-" * 40 + "\n"
        
        return history_text
    
    def show_statistics(self):
        """Show session statistics"""
        duration = datetime.now() - self.session_start
        minutes = int(duration.total_seconds() / 60)
        
        stats_text = f"\n📊 Session Statistics:\n"
        stats_text += f"• Session duration: {minutes} minutes\n"
        stats_text += f"• Messages exchanged: {len(self.conversation_history)}\n"
        
        if self.conversation_history:
            # Count intents
            intent_counts = {}
            for exchange in self.conversation_history:
                intent = exchange['intent']
                intent_counts[intent] = intent_counts.get(intent, 0) + 1
            
            stats_text += "• Topics discussed:\n"
            for intent, count in intent_counts.items():
                if intent != 'fallback':
                    stats_text += f"  - {intent.replace('_', ' ').title()}: {count} time(s)\n"
        
        stats_text += f"\n• Session started: {self.session_start.strftime('%I:%M %p')}"
        
        return stats_text
    
    def print_colored(self, text, color='white', end='\n'):
        """Print colored text (simple version without colorama)"""
        # Simple color codes for terminals that support them
        colors = {
            'blue': '\033[94m',
            'green': '\033[92m',
            'yellow': '\033[93m',
            'cyan': '\033[96m',
            'white': '\033[97m',
            'bold': '\033[1m',
            'end': '\033[0m'
        }
        
        if color in colors:
            print(f"{colors[color]}{text}{colors['end']}", end=end)
        else:
            print(text, end=end)
    
    def welcome_message(self):
        """Display welcome message"""
        welcome = """
╔══════════════════════════════════════════════════════════════╗
║                    🌊 AquaCare Chatbot 🌊                    ║
║           Your Personal Water Conservation Assistant         ║
╚══════════════════════════════════════════════════════════════╝
        """
        self.print_colored(welcome, 'cyan')
        print("\nI'm here to help with all things water-related!")
        print("Type 'help' to see what I can do, or just ask me anything about water.\n")
    
    def get_user_name(self):
        """Ask for user's name"""
        self.print_colored("\nWhat's your name? ", 'yellow')
        name = input().strip()
        if name:
            self.user_name = name.title()
            self.print_colored(f"\nNice to meet you, {self.user_name}! ", 'green')
            print("Feel free to ask me about water conservation, quality, or any water topics.\n")
    
    def process_input(self, user_input):
        """Process user input and return response"""
        # Check for empty input
        if not user_input.strip():
            return "Please type a message or ask a question."
        
        # Find intent
        intent = self.find_best_intent(user_input)
        
        # Get response
        response = self.get_response(intent, user_input)
        
        # Add to history
        self.conversation_history.append({
            'user': user_input,
            'bot': response,
            'intent': intent,
            'time': datetime.now().strftime('%H:%M')
        })
        
        return response
    
    def run(self):
        """Main chatbot loop"""
        # Clear screen
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Show welcome
        self.welcome_message()
        
        # Get user name
        self.get_user_name()
        
        # Main conversation loop
        while True:
            try:
                # Get user input
                if self.user_name:
                    self.print_colored(f"\n{self.user_name}: ", 'green', end='')
                else:
                    self.print_colored("\nYou: ", 'green', end='')
                
                user_input = input().strip()
                
                # Check for exit
                if user_input.lower() in ['exit', 'quit', 'bye', 'goodbye']:
                    response = random.choice(self.knowledge_base['goodbye']['responses'])
                    if self.user_name:
                        response = f"{response} Take care, {self.user_name}!"
                    
                    self.print_colored(f"\nAquaCare: {response}\n", 'cyan')
                    
                    # Show final stats
                    print("\n" + "=" * 50)
                    print(self.show_statistics())
                    print("=" * 50 + "\n")
                    break
                
                # Process input
                if user_input:
                    # Show typing indicator
                    print("AquaCare: ", end='')
                    time.sleep(0.5)
                    
                    response = self.process_input(user_input)
                    
                    # Print response with typing effect
                    words = response.split()
                    for i, word in enumerate(words):
                        print(word, end=' ')
                        if i % 5 == 0:  # Small delay every few words
                            time.sleep(0.05)
                    print()
                
            except KeyboardInterrupt:
                self.print_colored("\n\nAquaCare: Goodbye! Thanks for chatting! 👋\n", 'cyan')
                break
            except EOFError:
                break
            except Exception as e:
                self.print_colored(f"\nAquaCare: I encountered an error. Please try again.\n", 'red')
                if 'DEBUG' in os.environ:
                    print(f"Error details: {e}")


def main():
    """Main function to run the chatbot"""
    print("Starting AquaCare Chatbot...")
    
    try:
        # Create and run chatbot
        chatbot = AquaCareChatbot()
        chatbot.run()
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Please try running the script again.")
        sys.exit(1)


if __name__ == "__main__":
    main()