# ⚾️ Max Velocity Leaderboard & PitchGuesser Game

This repository addresses a gap in available Statcast data by compiling a **Max Velocity Leaderboard** for every MLB pitcher in the 2024 and 2025 seasons.

While Statcast easily highlights a hitter's hardest-hit ball (the 'red/blue bubbles' we frequently see), finding a pitcher's max pitch velocity required building a custom database.

The leaderboard was constructed via a combination of Baseball Savant searches and calls to the **MLB Stats API**, initially creating a database of every fastball-type pitch thrown in those seasons, then filtering it down to each pitcher's single fastest pitch.

### 🎮 The PitchGuesser Game

An accompanying **Streamlit** application allows users to guess the Max MPH for 10 randomly selected 2024 pitchers.

* **Play the Game:** [HERE (Link to your Streamlit App)]
* **Contact:** Let me know your high score and any feedback on Twitter **[@BarrisHax]**.

All code is written in Python and performed in Jupyter Notebooks.

---

## ⚙️ Data Pipeline: From Scratch to API

This project showcases the evolution of data sourcing between the 2024 and 2025 seasons, highlighting the power of the MLB Stats API.

### 2024 Database Creation: The Hard Way

In 2024, the MLB Stats API hackathon documentation was not yet available to me, requiring a painstaking manual process:

* I manually stitched together the outputs of **30 different Baseball Savant searches**.
* Each search targeted every fastball, sinker, or cutter thrown by a *single team* during the entire regular season.
* The final result was a complete database of every fastball-type pitch thrown during the 2024 season.

### 2025 Database Creation: The Elegant Way

Armed with the knowledge of the official MLB Stats API, the process for 2025 was far more efficient:

* The API allowed elegant access to every play event of every game during the regular season.
* Any event labeled with a fastball pitch type was added to the database, leaving us with a comprehensive list of every fastball thrown during the 2025 season.

### Building the Final Leaderboard

For both years, a simple, quick block of Python code was run on the complete database to perform a group-by and filter, isolating each individual pitcher's fastest pitch.

* This process yielded the final **Max MPH Leaderboard** for both the 2024 and 2025 seasons.
* The final leaderboard CSV files are provided in this repository.
* *Note: The entire database of fastballs was too large to upload to GitHub.*

---

## 📸 Headshots and The Streamlit App

### Pitcher Headshots

Gathering headshots for the game was initially a manual and time-consuming process.

Moving forward, the MLB Stats API provides a reliable and scalable solution for obtaining player images:
