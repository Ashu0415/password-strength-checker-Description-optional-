import getpass
import re


def check_password_strength(password: str) -> tuple[str, list[str]]:
  """Evaluates password strength and returns a rating alongside improvement tips."""
  score = 0
  feedback = []

  if len(password) >= 12:
    score += 2
  elif len(password) >= 8:
    score += 1
  else:
    feedback.append("Make it at least 8 characters long (12+ is best).")

  if re.search(r"[A-Z]", password):
    score += 1
  else:
    feedback.append("Add at least one uppercase letter (A-Z).")

  if re.search(r"[a-z]", password):
    score += 1
  else:
    feedback.append("Add at least one lowercase letter (a-z).")

  if re.search(r"\d", password):
    score += 1
  else:
    feedback.append("Add at least one number (0-9).")

  if re.search(r"[!@#$%^&*(),.?\":{}|<>_\-+=\[\]\\\/~`]", password):
    score += 1
  else:
    feedback.append("Add at least one special character (e.g., !, @, #, $).")

  common_passwords = {"password", "123456", "qwerty", "admin", "letmein"}
  if password.lower() in common_passwords:
    score = 0
    feedback.append("Avoid commonly used passwords.")

  if score >= 6:
    rating = "Strong"
  elif score >= 4:
    rating = "Moderate"
  else:
    rating = "Weak"

  return rating, feedback


if __name__ == "__main__":
  user_password = getpass.getpass("Enter a password to test: ")
  strength, tips = check_password_strength(user_password)

  print(f"\nPassword Strength: {strength}")
  if tips:
    print("Suggestions to improve:")
    for tip in tips:
      print(f" - {tip}")
