
def cricket_scoring_app():
    print("=" * 40)
    print("       CRICKET SCORING APP")
    print("=" * 40)

    batting_team = input("Enter batting team name: ")
    bowling_team = input("Enter bowling team name: ")
    max_overs = int(input("Enter number of overs: "))

    runs = 0
    wickets = 0
    legal_balls = 0
    extras = 0

    while wickets < 10 and legal_balls < max_overs * 6:
        overs = f"{legal_balls // 6}.{legal_balls % 6}"

        print("\n" + "-" * 40)
        print(f"{batting_team}: {runs}/{wickets}")
        print(f"Overs: {overs}/{max_overs}")
        print(f"Run rate: {runs / (legal_balls / 6):.2f}"
              if legal_balls else "Run rate: 0.00")
        print("-" * 40)

        print("1. Dot ball")
        print("2. Score runs (1, 2, 3, 4, 6)")
        print("3. Wicket")
        print("4. Wide (+1 run)")
        print("5. No-ball (+1 run)")
        print("6. Bye / Leg bye")
        print("7. End innings")

        choice = input("Choose an option: ")

        if choice == "1":
            legal_balls += 1

        elif choice == "2":
            try:
                scored = int(input("Runs scored: "))
                if scored not in [1, 2, 3, 4, 6]:
                    print("Enter 1, 2, 3, 4, or 6.")
                    continue
                runs += scored
                legal_balls += 1
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "3":
            wickets += 1
            legal_balls += 1
            print("Wicket taken!")

        elif choice == "4":
            runs += 1
            extras += 1
            print("Wide ball! One extra run.")

        elif choice == "5":
            runs += 1
            extras += 1
            print("No-ball! One extra run.")

        elif choice == "6":
            try:
                bye_runs = int(input("Enter bye/leg-bye runs: "))
                if bye_runs < 0:
                    print("Runs cannot be negative.")
                    continue
                runs += bye_runs
                extras += bye_runs
                legal_balls += 1
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "7":
            break

        else:
            print("Invalid choice. Try again.")

    print("\n" + "=" * 40)
    print("           INNINGS SUMMARY")
    print("=" * 40)
    print(f"Batting team : {batting_team}")
    print(f"Bowling team : {bowling_team}")
    print(f"Final score  : {runs}/{wickets}")
    print(f"Overs        : {legal_balls // 6}.{legal_balls % 6}")
    print(f"Extras       : {extras}")
    print(f"Run rate     : {runs / (legal_balls / 6):.2f}"
          if legal_balls else "Run rate     : 0.00")

    print(f"\n{bowling_team} needs {runs + 1} runs to win.")


if __name__ == "__main__":
    cricket_scoring_app()
