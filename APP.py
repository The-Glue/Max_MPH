import streamlit as st
import pandas as pd
import random
import os

# Function to calculate points based on guess accuracy
def calculate_points(guess, actual):
    if guess == actual:
        return 5
    elif abs(guess - actual) <= 0.5:
        return 3
    elif abs(guess - actual) <= 1:
        return 2
    elif abs(guess - actual) <= 1.5:
        return 1
    else:
        return 0

# Load the data with caching
@st.cache_data
def load_data():
    return pd.read_csv('finally_with_headshots.csv')

# Function to select a new pitcher
def select_new_pitcher():
    available_pitchers = df_combined[~df_combined['player_name'].isin(st.session_state.used_pitchers)]
    if available_pitchers.empty:
        st.session_state.game_over = True  # Set game over if no pitchers are available
        return None
    random_pitcher = available_pitchers.sample().iloc[0]
    st.session_state.used_pitchers.add(random_pitcher['player_name'])
    st.session_state.current_pitcher = random_pitcher

# Function to reset the game
def reset_game():
    st.session_state.total_points = 0
    st.session_state.round_num = 1
    st.session_state.used_pitchers = set()
    st.session_state.feedback_statements = []
    st.session_state.current_pitcher = None
    st.session_state.game_over = False

# Load data
df_combined = load_data()

# Initialize session state variables
if "total_points" not in st.session_state:
    st.session_state.total_points = 0
    st.session_state.round_num = 1
    st.session_state.used_pitchers = set()
    st.session_state.feedback_statements = []
    st.session_state.current_pitcher = None
    st.session_state.game_over = False

rounds = 10  # Total number of rounds in the game

# Main game logic
if st.session_state.round_num > rounds or st.session_state.game_over:
    st.subheader("Game Summary")
    for statement in st.session_state.feedback_statements:
        st.write(statement)
    st.write(f"**Total Points: {st.session_state.total_points}**")
    
    if st.button("Play Again"):
        reset_game()
        select_new_pitcher()
    st.stop()

# If no current pitcher is selected, select one
if st.session_state.current_pitcher is None:
    select_new_pitcher()

# Get current pitcher details
pitcher = st.session_state.current_pitcher
pitcher_name = pitcher['player_name']
actual_speed = pitcher['release_speed']
headshot_url = pitcher['headshot_url']

# Determine the headshot folder based on player name
if pitcher_name >= "Luis Frias":
    headshot_path = os.path.join("headshots2", headshot_url)
else:
    headshot_path = os.path.join("headshots", headshot_url)

# Display the pitcher's name and headshot
st.subheader(f"Round {st.session_state.round_num}/{rounds} - Pitcher: {pitcher_name}")
if os.path.exists(headshot_path) and headshot_url != 'Not Found':
    st.image(headshot_path, width=200)
else:
    st.write(f"No headshot found for {pitcher_name}.")

# User input for guessing
with st.form(key=f"guess_form_{st.session_state.round_num}"):
    user_guess = st.text_input("Guess the fastest pitch speed (e.g., '95.3')", key=f"guess_input_{st.session_state.round_num}")
    submit_button = st.form_submit_button("Submit Guess")

# Process the guess
if submit_button:
    try:
        # Ensure valid format with one decimal place
        if not (user_guess and user_guess.count('.') == 1 and len(user_guess.split('.')[-1]) == 1):
            raise ValueError("Invalid format")
        
        user_guess_float = float(user_guess)  # Convert to float

        # Calculate points for the guess
        points = calculate_points(user_guess_float, actual_speed)
        st.session_state.total_points += points

        # Store and display feedback for the current (just completed) round
        feedback = (
            f"Round {st.session_state.round_num}/{rounds} - Pitcher: {pitcher_name} - "
            f"Your Guess: {user_guess_float}, Actual Speed: {actual_speed}, Points Awarded: {points}"
        )
        st.session_state.feedback_statements.append(feedback)
        st.success(feedback)

        # Increment the round number after processing the guess
        st.session_state.round_num += 1

        # Clear current_pitcher to select a new one in the next iteration
        st.session_state.current_pitcher = None

        # Force a rerun to update the UI with the new round
        st.rerun()

    except ValueError:
        st.error("Invalid input. Please enter a speed like '90.0' with exactly one decimal place.")

# Display all feedback statements from previous rounds
if st.session_state.feedback_statements:
    st.subheader("Feedback So Far:")
    for statement in st.session_state.feedback_statements:
        st.write(statement)
