import random
import time

def display_welcome():
    print("\n" + "=" * 50)
    print("🎮 WELCOME TO THE ULTIMATE QUIZ CHALLENGE! 🎮".center(50))
    print("=" * 50)
    print("\n📜 Instructions:")
    print("- Choose a quiz category")
    print("- Answer multiple-choice questions")
    print("- Each correct answer is worth 10 points")
    print("- See your final score at the end")
    print("- Have fun and learn something new!")

def display_categories():
    print("\n📁 Quiz Categories:")
    print("1. 🌏 General Knowledge")
    print("2. 🎬 Movies and TV Shows")
    print("3. 🔬 Science and Nature")
    print("4. 🎮 Video Games")
    print("5. 🎲 Random Mix (qusetions from all categories)")

def get_user_choice():
    while True:
        try:
            choice = int(input("\nSelect a category (1-5): "))
            if 1 <= choice <= 5:
                return choice
            else:
               print(f"❌ Please enter a number between 1 and 5")
        except ValueError:
            print("❌ Please enter a valid number")

def load_questions():
    general_knowledge = [
        {
            "question": "What is the largest planet in our Solar System?",
            "options": ["A. Earth", "B. Jupiter", "C. Mars", "D. Saturn"],
            "answer": "B"
        },
        {
            "question": "Who wrote the play 'Romeo and Juliet'?",
            "options": ["A. William Shakespeare", "B. Charles Dickens", "C. Mark Twain", "D. Jane Austen"],
            "answer": "A"
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["A. O2", "B. CO2", "C. H2O", "D. NaCl"],
            "answer": "C"
        },
        {
            "question": "Which continent is known as the 'Dark Continent'?",
            "options": ["A. Asia", "B. Africa", "C. South America", "D. Australia"],
            "answer": "B"
        },
        {
            "question": "What is the currency of Japan?",
            "options": ["A. Yuan", "B. Won", "C. Yen", "D. Ringgit"],
            "answer": "C"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A. Mercury", "B. Mars", "C. Venus", "D. Neptune"],
            "answer": "B"
        },
        {
            "question": "Who painted the Mona Lisa?",
            "options": ["A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Michelangelo"],
            "answer": "C"
        },
        {
            "question": "In which country is the Great Pyramid of Giza located?",
            "options": ["A. Mexico", "B. Egypt", "C. Peru", "D. China"],
            "answer": "B"
        },
        {
            "question": "What is the freezing point of water in Celsius?",
            "options": ["A. 0°C", "B. 32°C", "C. 100°C", "D. -10°C"],
            "answer": "A"
        },
        {
            "question": "Which ocean is the largest?",
            "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
            "answer": "D"
        }
    ]

    movies_tv = [
        {
            "question": "Who played Iron Man in the Marvel Cinematic Universe?",
            "options": ["A. Chris Evans", "B. Robert Downey Jr.", "C. Chris Hemsworth", "D. Mark Ruffalo"],
            "answer": "B"
        },
        {
            "question": "Which TV show features the character Walter White?",
            "options": ["A. The Sopranos", "B. Breaking Bad", "C. The Wire", "D. Ozark"],
            "answer": "B"
        },
        {
            "question": "Which movie won Best Picture at the 2020 Oscars?",
            "options": ["A. Joker", "B. 1917", "C. Parasite", "D. Once Upon a Time in Hollywood"],
            "answer": "C"
        },
        {
            "question": "Who directed the movie 'Inception'?",
            "options": ["A. James Cameron", "B. Christopher Nolan", "C. Steven Spielberg", "D. Quentin Tarantino"],
            "answer": "B"
        },
        {
            "question": "Which character is NOT part of the original 'Friends' group?",
            "options": ["A. Rachel", "B. Joey", "C. Monica", "D. Steve"],
            "answer": "D"
        },
        {
            "question": "In 'The Matrix', what color pill does Neo take?",
            "options": ["A. Blue", "B. Green", "C. Red", "D. Yellow"],
            "answer": "C"
        },
        {
            "question": "Which actor voiced Simba in the original 1994 'The Lion King'?",
            "options": ["A. Matthew Broderick", "B. Jonathan Taylor Thomas", "C. Jeremy Irons", "D. James Earl Jones"],
            "answer": "A"
        },
        {
            "question": "What is the name of the fictional continent in 'Game of Thrones'?",
            "options": ["A. Westeros", "B. Narnia", "C. Middle-earth", "D. Panem"],
            "answer": "A"
        },
        {
            "question": "Which animated movie features a robot left to clean Earth?",
            "options": ["A. WALL·E", "B. Big Hero 6", "C. Robots", "D. Astro Boy"],
            "answer": "A"
        },
        {
            "question": "In which movie does the quote 'I am your father' appear?",
            "options": ["A. Star Wars: A New Hope", "B. Star Wars: The Empire Strikes Back", "C. Star Wars: Return of the Jedi", "D. Rogue One"],
            "answer": "B"
        }
    ]

    science_nature = [
        {
            "question": "What is the chemical symbol for gold?",
            "options": ["A. Go", "B. Au", "C. Ag", "D. Gd"],
            "answer": "B"
        },
        {
            "question": "How many bones are there in the adult human body?",
            "options": ["A. 206", "B. 201", "C. 210", "D. 199"],
            "answer": "A"
        },
        {
            "question": "Which planet is closest to the Sun?",
            "options": ["A. Venus", "B. Earth", "C. Mercury", "D. Mars"],
            "answer": "C"
        },
        {
            "question": "What gas do plants absorb from the atmosphere?",
            "options": ["A. Oxygen", "B. Carbon Dioxide", "C. Nitrogen", "D. Hydrogen"],
            "answer": "B"
        },
        {
            "question": "Which part of the plant conducts photosynthesis?",
            "options": ["A. Roots", "B. Stem", "C. Flowers", "D. Leaves"],
            "answer": "D"
        },
        {
            "question": "What is the hardest natural substance on Earth?",
            "options": ["A. Quartz", "B. Diamond", "C. Topaz", "D. Obsidian"],
            "answer": "B"
        },
        {
            "question": "Which organ in the human body is responsible for pumping blood?",
            "options": ["A. Lungs", "B. Liver", "C. Heart", "D. Kidneys"],
            "answer": "C"
        },
        {
            "question": "Which element has the atomic number 1?",
            "options": ["A. Helium", "B. Oxygen", "C. Hydrogen", "D. Carbon"],
            "answer": "C"
        },
        {
            "question": "What is the main gas found in the air we breathe?",
            "options": ["A. Carbon Dioxide", "B. Nitrogen", "C. Oxygen", "D. Hydrogen"],
            "answer": "B"
        },
        {
            "question": "Which celestial body defines a year on Earth?",
            "options": ["A. The Moon", "B. The Sun", "C. Mars", "D. Jupiter"],
            "answer": "B"
        }
    ]

    video_games = [
        {
            "question": "Which video game features a character named Mario?",
            "options": ["A. Call of Duty", "B. Super Mario Bros", "C. Minecraft", "D. Fortnite"],
            "answer": "B"
        },
        {
            "question": "Which company developed the game 'Minecraft'?",
            "options": ["A. Mojang", "B. Epic Games", "C. Ubisoft", "D. EA"],
            "answer": "A"
        },
        {
            "question": "In which game do players compete to be the last one standing on an island?",
            "options": ["A. FIFA", "B. Call of Duty", "C. Fortnite", "D. League of Legends"],
            "answer": "C"
        },
        {
            "question": "What is the name of the main protagonist in 'The Legend of Zelda' series?",
            "options": ["A. Zelda", "B. Ganon", "C. Link", "D. Samus"],
            "answer": "C"
        },
        {
            "question": "Which video game features a battle between the Templars and Assassins?",
            "options": ["A. Assassin's Creed", "B. God of War", "C. Uncharted", "D. Skyrim"],
            "answer": "A"
        },
        {
            "question": "Which game series features locations like San Andreas and Vice City?",
            "options": ["A. Red Dead Redemption", "B. Watch Dogs", "C. Grand Theft Auto", "D. Cyberpunk 2077"],
            "answer": "C"
        },
        {
            "question": "In which game would you find a character named Master Chief?",
            "options": ["A. Halo", "B. Doom", "C. Destiny", "D. Battlefield"],
            "answer": "A"
        },
        {
            "question": "What is the best-selling video game of all time (as of 2024)?",
            "options": ["A. Tetris", "B. Minecraft", "C. GTA V", "D. Wii Sports"],
            "answer": "B"
        },
        {
            "question": "Which company publishes the FIFA video game series?",
            "options": ["A. EA Sports", "B. Konami", "C. Ubisoft", "D. Rockstar Games"],
            "answer": "A"
        },
        {
            "question": "Which game features a city called Rapture and the phrase 'Would you kindly?'?",
            "options": ["A. BioShock", "B. Half-Life", "C. Dishonored", "D. Portal"],
            "answer": "A"
        }
    ]

    return {
        1: {"name": "General Knowledge", "questions": general_knowledge},
        2: {"name": "Movies and TV Shows", "questions": movies_tv},
        3: {"name": "Science and Nature", "questions": science_nature},
        4: {"name": "Video Games", "questions": video_games},
        2: {"name": "Random Mix", "questions": general_knowledge + movies_tv + science_nature + video_games},
    }

def run_quiz(category_data):
    category_name = category_data["name"]
    questions = category_data["questions"]

    random.shuffle(questions)

    print(f"\n🎯 Starting the {category_name} quiz! 🎯")
    print("Answer each question by typing the letter of your choice (A, B, C, or D).")

    score = 0
    correct_answer = 0

    for i, q in enumerate(questions):
        print(f"\n----- Question {i + 1}/{len(questions)} -----")
        print(f"? {q['question']}")

        for option in q["options"]:
            print(option)

        while True:
            user_answer = input("\nYour answer (A/B/C/D): ").upper()
            if user_answer not in ["A", "B", "C", "D"]:
                print("❌ Please enter A, B, C, or D.")
            else:
                break
        
        correct = user_answer == q["answer"]

        if correct:
            score += 10
            correct_answer += 1
            print("✅ Correct! +10 points")
        else:
            print(f"❌ Wrong! The correct answer is {q['answer']}")

        if i < len(questions) - 1:
            print("\nNext question coming up...")
            time.sleep(1.5)

    print("\n" + "=" * 50)
    print("📊 QUIZ RESULTS 📊".center(50))
    print("=" * 50)
    print(f"Category: {category_name}")
    print(f"Correct Answers: {correct_answer}/{len(questions)}")
    print(f"Total Score: {score} points")

    percentage = (score / (len(questions)*10)) * 100

    if percentage == 100:
        print("\n🏆 PERFECT SCORE! You're a quiz master! 🏆")
    elif percentage >= 80:
        print("\n🌟 EXCELLENT! You really know your stuff!")
    elif percentage >= 60:
        print("\n😊 GOOD JOB! You've got decent knowledge!")
    elif percentage >= 40:
        print("\n🤔 NOT BAD! There's room for improvement.")
    else:
        print("\n📚 KEEP LEARNING! Practice makes perfect!")

    return score

def main():
    display_welcome()

    total_score = 0
    play_again = True

    while play_again:
        display_categories()

        category_choice = get_user_choice()

        all_categories = load_questions()
        score = run_quiz(all_categories[category_choice])

        total_score += score

        again = input("\nPlay another round? (yes/no): ").lower()

        while not (again.startswith("y") or again.startswith("n")):
            print("Please type yes or no.")
            again = input("Play amother round? (yes/no): ").lower()

        play_again = again.startswith("y")

    print(f"🎉 Thanks for playing! Your total score from all rounds: {total_score} points 🎉")

main()