# Brainrot Fighters

A local two-player 2D fighting game built with Python and Pygame, starring characters from the "Italian brainrot" meme universe.

Made as the final programming project of my first year of SMX (*Sistemas Microinformáticos y Redes*), April–May 2025.

## Features

- **5 playable characters**, each with a basic, an elemental and an ultimate skill
- **Map roulette** that randomly picks the arena before each fight
- **Character selection** for two players on the same keyboard
- **Round timer**, health bars and skill cooldown HUD
- **Pause menu** during fights (Esc)
- **Settings menu**: music/SFX volume, resolution (720p to 4K), FPS cap, fullscreen and FPS counter, saved to `data.json`
- Resolution-independent layout: every element is positioned as a percentage of the screen

## Characters

| Character | Basic | Elemental | Ultimate |
|---|---|---|---|
| **Tralalero Tralala** | Bite (melee) | Homing bubbles | Wave that slows the enemy |
| **Bombardiro Crocodilo** | Homing missile | Flight for 7 s | Barrage of 5–10 missiles |
| **Tung Tung Tung Sahur** | Bat hit (melee) | Thrown stick | Spin attack for 7 s |
| **Brr Brr Patapim** | Melee hit | Vines that slow the enemy | Takes half damage for 10 s |
| **Lirilì Larilà** | Stand that chases and punches | Homing steamroller | Stops time for 12 s |

## Getting started

Requires Python 3.9–3.13 (the versions pygame 2.6.1 publishes wheels for).

```bash
git clone https://github.com/davidcastillocruz/BrainrotFighters.git
cd BrainrotFighters
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python game.py
```

Run it from the project root: asset and `data.json` paths are relative.

## Controls

| Action | Player 1 | Player 2 |
|---|---|---|
| Move / jump | `W` `A` `S` `D` | `I` `J` `K` `L` |
| Basic skill | `Q` | `U` |
| Elemental skill | `E` | `O` |
| Ultimate skill | `R` | `P` |
| Confirm character | `E` | `O` |
| Pause menu | `Esc` | `Esc` |

`S` / `K` move down while Bombardiro is flying. Menus are used with the mouse.

## Project structure

```
game.py              Entry point: window, main loop and scene switching
functions.py         Layout helpers, settings persistence and image utilities
SoundManager.py      Loads and plays music and sound effects
data.json            User settings
characters/
  Character.py       Base class: movement, physics, animations and skill cooldowns
  Projectile.py      Generic homing/targeted projectile used by the skills
  *.py               One subclass per fighter
components/          Reusable UI widgets (button, slider, dropdown, checkbox, HUD...)
scenarios/           Scenes: main menu, settings, map roulette, character selection, fight
assets/              Sprites, backgrounds, sounds and font
```

### How it works

- **Scenes.** `Game` holds one instance of each scene. Each scene has a `status` flag, and the main loop updates and draws whichever one is active. Switching scenes means toggling flags.
- **Characters.** `Character` handles input, gravity, walking/idle animations and a generic skill system. Skill state is looked up by name (`doing_basic_skill`, `basic_skill_cooldown`, `basic_skill_left_animation`...), so a new fighter only has to load its sprites and implement `basic_skill()`, `elemental_skill()` and `ultimate_skill()`.
- **Projectiles.** `Proyectile` covers every ranged attack: it homes in on the enemy or flies to a fixed point, animates, optionally rotates to face its direction, and applies damage and debuffs (such as a slow) on hit.
- **Frame-rate independence.** Movement and timers are scaled by delta time, so the game plays the same at 30 or 144 FPS.

## Credits

Programming by David Castillo. Characters and sounds come from the "Italian brainrot" internet meme. This is a non-commercial student project.
