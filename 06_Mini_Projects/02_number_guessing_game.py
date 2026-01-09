"""
MINI PROJECT 2: NUMBER GUESSING GAME
=====================================

A fun game where the computer picks a random number and you have to guess it!
The game gives hints if your guess is too high or too low.
"""

import random

def play_game():
    """Main game function"""
    print("\n" + "=" * 50)
    print("🎮 WELCOME TO NUMBER GUESSING GAME! 🎮")
    print("=" * 50)
    print("\nI'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?")
    print("=" * 50 + "\n")
    
    # Computer picks a random number
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    print(f"You have {max_attempts} attempts to guess the number.\n")
    
    # Game loop
    while attempts < max_attempts:
        attempts += 1
        remaining = max_attempts - attempts + 1
        
        # Get player's guess
        try:
            guess = int(input(f"Attempt {attempts}/{max_attempts} - Enter your guess: "))
        except ValueError:
            print("❌ Invalid input! Please enter a number.\n")
            attempts -= 1  # Don't count invalid attempts
            continue
        
        # Check if guess is in valid range
        if guess < 1 or guess > 100:
            print("❌ Please guess a number between 1 and 100!\n")
            attempts -= 1  # Don't count invalid attempts
            continue
        
        # Check the guess
        if guess == secret_number:
            print("\n" + "=" * 50)
            print("🎉 CONGRATULATIONS! YOU WON! 🎉")
            print("=" * 50)
            print(f"You guessed the number in {attempts} attempts!")
            print(f"The secret number was: {secret_number}")
            
            # Calculate score based on attempts
            score = ((max_attempts - attempts + 1) * 10)
            print(f"Your score: {score} points")
            print("=" * 50)
            return True
        
        elif guess < secret_number:
            print(f"📈 Too low! Try a higher number.")
            if remaining > 0:
                print(f"You have {remaining} attempts remaining.\n")
        
        else:
            print(f"📉 Too high! Try a lower number.")
            if remaining > 0:
                print(f"You have {remaining} attempts remaining.\n")
    
    # Player ran out of attempts
    print("\n" + "=" * 50)
    print("😢 GAME OVER!")
    print("=" * 50)
    print(f"You've used all {max_attempts} attempts.")
    print(f"The secret number was: {secret_number}")
    print("Better luck next time!")
    print("=" * 50)
    return False

def play_multiple_rounds():
    """Play multiple rounds and keep track of score"""
    print("\n" + "🌟" * 25)
    print("MULTI-ROUND NUMBER GUESSING GAME")
    print("🌟" * 25 + "\n")
    
    total_wins = 0
    total_games = 0
    
    while True:
        total_games += 1
        won = play_game()
        
        if won:
            total_wins += 1
        
        # Ask if player wants to play again
        print("\n" + "-" * 50)
        play_again = input("Do you want to play again? (yes/no): ")
        
        if play_again.lower() not in ['yes', 'y']:
            break
    
    # Display final statistics
    print("\n" + "=" * 50)
    print("GAME STATISTICS")
    print("=" * 50)
    print(f"Games Played: {total_games}")
    print(f"Games Won: {total_wins}")
    print(f"Games Lost: {total_games - total_wins}")
    
    if total_games > 0:
        win_percentage = (total_wins / total_games) * 100
        print(f"Win Rate: {win_percentage:.1f}%")
    
    print("=" * 50)
    print("\nThank you for playing! 👋")

# ============================================
# DEMONSTRATION MODE
# ============================================

def demo_game():
    """Demonstrates the game with automated guesses"""
    print("\n" + "=" * 50)
    print("GAME DEMONSTRATION (Automated)")
    print("=" * 50 + "\n")
    
    secret_number = 47  # Fixed number for demo
    print(f"Secret number: {secret_number}")
    print("Watch the computer try to guess it!\n")
    
    # Simulate guesses
    guesses = [50, 25, 37, 43, 45, 47]
    
    for i, guess in enumerate(guesses, 1):
        print(f"Attempt {i}: Guessed {guess}")
        
        if guess == secret_number:
            print(f"✓ Correct! Found it in {i} attempts!\n")
            break
        elif guess < secret_number:
            print(f"  → Too low! Try higher.\n")
        else:
            print(f"  → Too high! Try lower.\n")

# Run demonstration
demo_game()

# ============================================
# HOW TO PLAY
# ============================================

print("=" * 50)
print("HOW TO PLAY")
print("=" * 50)
print("""
To play the game:

1. Uncomment ONE of these lines:
   # play_game()              # Play single round
   # play_multiple_rounds()   # Play multiple rounds

2. Run the program again

3. Follow the instructions:
   - Guess a number between 1 and 100
   - Get hints (too high or too low)
   - Try to guess in as few attempts as possible!

Scoring:
- Fewer attempts = Higher score
- Each remaining attempt is worth 10 points
""")

# Uncomment one of these lines to play:
# play_game()              # Single round
# play_multiple_rounds()   # Multiple rounds with statistics

# ============================================
# ENHANCEMENT IDEAS
# ============================================

print("\n" + "=" * 50)
print("ENHANCEMENT IDEAS")
print("=" * 50)
print("""
Try adding these features:

1. Difficulty Levels:
   - Easy: 1-50, 15 attempts
   - Medium: 1-100, 10 attempts
   - Hard: 1-200, 7 attempts

2. Hints System:
   - "Hot/Warm/Cold" based on proximity
   - Reveal if number is even or odd
   - Show range narrowing (e.g., "between 30-60")

3. Time Challenge:
   - Add timer for each guess
   - Bonus points for quick guesses

4. Two-Player Mode:
   - Players take turns guessing
   - First to guess wins

5. Save High Scores:
   - Keep track of best scores
   - Save to a file
   - Display leaderboard

6. Advanced Features:
   - Multiple number ranges
   - Guess decimals
   - Binary search hints
   - Sound effects (using libraries)
""")

print("\n🎮 Have fun coding and playing! 🎮\n")
