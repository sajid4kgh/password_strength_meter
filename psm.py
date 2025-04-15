import re
import random
import string
import streamlit as st

def generate_strong_password(length):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(characters) for _ in range(length))


def check_password_strength(password):
    score = 0
    common_passwords = ["password123", "12345678", "qwerty", "letmein", "admin", "welcome"]
    
    if password in common_passwords:
        return "❌ This password is too common. Choose a more unique one.", "Weak"
    
    feedback = []
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔹 Password should be at least 8 characters long.")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("🔹 Include both uppercase and lowercase letters.")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("🔹 Add at least one number (0-9).")
    
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("🔹 Include at least one special character (!@#$%^&*).")
    
    if score == 4:
        return "✅ Strong Password!", "Strong"
    elif score == 3:
        return "⚠️ Moderate Password - Consider adding more security features.", "Moderate"
    else:
        return "\n".join(feedback), "Weak"


st.title("🔐 Password Strength Meter")
st.write("Enter your password below to check its strength:")

password = st.text_input("Enter your password:", type="password")

if st.button("Check Strength"):
    if password:
        result, strength = check_password_strength(password)
        if strength == "Strong":
            st.success(result)
            st.balloons()
        elif strength == "Moderate":
            st.warning(result)
        else:
            st.error("Weak Password - Improve it using these tips:")
            for tip in result.split("\n"):
                st.write(tip)
    else:
        st.warning("⚠️ Please enter a password to check.")

password_length = st.number_input("Choose password length:", min_value=8, max_value=20, value=12)
if st.button("Generate Strong Password"):
    strong_password = generate_strong_password(password_length)
    st.success(f"Suggested Strong Password: {strong_password}")
    