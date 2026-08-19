# 🎮 Catch the Falling Objects

A simple 2D arcade game developed using **Python** and **Pygame**.

The player controls a character at the bottom of the screen and tries to catch falling food objects while avoiding bombs. The game includes a score system, countdown timer, collision detection, and a restart/quit system.

---

<img width="1235" height="736" alt="Screenshot 2026-06-25 022719" src="https://github.com/user-attachments/assets/80c36335-973b-459e-b6e0-db1fc6c050fe" />

## 🎯 Game Overview

The main objective is to catch as many falling food objects as possible before the timer runs out.

Different objects have different effects:

- 🍓 Strawberry
- 🍎 Apple
- 🥕 Carrot
- 🍇 Grapes
- 💣 Bomb

Catching a food object increases the score by **1 point**.

Catching a bomb decreases the score by **1 point**.

The game ends when:

- ⏱️ The 60-second timer expires.
- 💣 The score becomes negative.
- ❌ The player closes the game.

---

## ✨ Features

- 🎮 Keyboard-controlled player movement
- ⬅️➡️ Left and right movement
- 🍎 Multiple falling food objects
- 💣 Randomly generated bombs
- 💥 Collision detection
- 🏆 Real-time score system
- ⏱️ 60-second countdown timer
- 🔄 Restart option
- 🚪 Quit option
- 🖼️ Custom game images and background
- 🎲 Random falling object types and speeds

---

## 🕹️ Controls

| Key | Action |
|---|---|
| `←` | Move left |
| `A` | Move left |
| `→` | Move right |
| `D` | Move right |
| `R` | Restart after Game Over |
| `Q` | Quit after Game Over |

---

## 📊 Scoring System

| Object | Effect |
|---|---:|
| 🍓 Strawberry | +1 |
| 🍎 Apple | +1 |
| 🥕 Carrot | +1 |
| 🍇 Grapes | +1 |
| 💣 Bomb | -1 |

The game ends immediately if the score becomes less than zero.

---

## ⏱️ Game Timer

Each game lasts for **60 seconds**.

The remaining time is displayed in the top-right corner:

```text
Time Left: 00:60

📌 Project Status

Completed Prototype

The current version includes the main gameplay mechanics:

Player movement
Falling objects
Random object generation
Food and bomb objects
Collision detection
Score system
Countdown timer
Game Over state
Restart functionality

👥 Contributors
This project was developed as a collaborative academic project with Dina
