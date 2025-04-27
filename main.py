import pygame
import random
import numpy as np

# Initialize Pygame
pygame.init()

# Constants
BASE_WIDTH, BASE_HEIGHT = 1600, 960
SCALE_FACTOR = 1
WIDTH, HEIGHT = BASE_WIDTH * SCALE_FACTOR, BASE_HEIGHT * SCALE_FACTOR
INFO_WIDTH = 1000 * SCALE_FACTOR
BATTLE_WIDTH = WIDTH - INFO_WIDTH
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RPG Game")

# Load fonts
try:
    FONT = pygame.font.SysFont("Arial", int(24 * SCALE_FACTOR))
    SMALL_FONT = pygame.font.SysFont("Arial", int(18 * SCALE_FACTOR))
    VS_FONT = pygame.font.SysFont("Arial", int(60 * SCALE_FACTOR))
except:
    print("Could not load Arial font. Falling back to default system font.")
    FONT = pygame.font.SysFont(None, int(24 * SCALE_FACTOR))
    SMALL_FONT = pygame.font.SysFont(None, int(18 * SCALE_FACTOR))
    VS_FONT = pygame.font.SysFont(None, int(60 * SCALE_FACTOR))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GRAY = (200, 200, 200)
LIGHT_GRAY = (230, 230, 230)

# Themes
THEMES = {
    "Light": {
        "battle_background": (240, 240, 255),
        "text_box_bg": (255, 255, 255),
        "text_box_border": (50, 50, 50),
        "info_bg": (220, 220, 255),
        "info_text": (0, 0, 0),
        "text": (0, 0, 0),
        "button_idle": (180, 180, 180),
        "button_hover": (200, 200, 200),
        "button_border": (50, 50, 50),
        "player_color": (0, 150, 255),
        "enemy_color": (255, 50, 50),
        "hp_bar": GREEN,
        "status_glow": YELLOW,
        "progress_bar": (0, 255, 100),
        "progress_bg": (100, 150, 100),
        "menu_border": (0, 200, 0),
        "vs_color": (0, 0, 0),
        "heal_glow": (0, 255, 100),
        "particle_color": (255, 255, 0),
    },
    "Dark": {
        "battle_background": (40, 40, 60),
        "text_box_bg": (60, 60, 90),
        "text_box_border": (0, 255, 255),
        "info_bg": (60, 60, 90),
        "info_text": (0, 255, 255),
        "text": (0, 255, 255),
        "button_idle": (80, 80, 120),
        "button_hover": (100, 100, 140),
        "button_border": (0, 255, 255),
        "player_color": (0, 180, 255),
        "enemy_color": (255, 80, 80),
        "hp_bar": GREEN,
        "status_glow": YELLOW,
        "progress_bar": (0, 200, 200),
        "progress_bg": (50, 80, 80),
        "menu_border": (0, 150, 150),
        "vs_color": (0, 255, 255),
        "heal_glow": (0, 200, 200),
        "particle_color": (0, 255, 255),
    },
    "Retro": {
        "battle_background": (120, 200, 120),
        "text_box_bg": (255, 255, 255),
        "text_box_border": (0, 0, 0),
        "info_bg": (200, 255, 200),
        "info_text": (0, 0, 0),
        "text": (0, 0, 0),
        "button_idle": (0, 180, 0),
        "button_hover": (0, 220, 0),
        "button_border": (0, 0, 0),
        "player_color": (0, 200, 255),
        "enemy_color": (255, 100, 100),
        "hp_bar": GREEN,
        "status_glow": YELLOW,
        "progress_bar": (0, 255, 0),
        "progress_bg": (0, 150, 0),
        "menu_border": (0, 200, 0),
        "vs_color": (0, 0, 0),
        "heal_glow": (0, 255, 0),
        "particle_color": (255, 255, 0),
    },
    "Cyberpunk": {
        "battle_background": (30, 60, 90),
        "text_box_bg": (40, 80, 120),
        "text_box_border": (0, 255, 255),
        "info_bg": (40, 80, 120),
        "info_text": (0, 255, 255),
        "text": (0, 255, 255),
        "button_idle": (60, 120, 180),
        "button_hover": (80, 140, 200),
        "button_border": (0, 255, 255),
        "player_color": (0, 200, 255),
        "enemy_color": (255, 100, 150),
        "hp_bar": GREEN,
        "status_glow": YELLOW,
        "progress_bar": (0, 255, 255),
        "progress_bg": (40, 80, 120),
        "menu_border": (0, 100, 200),
        "vs_color": (0, 255, 255),
        "heal_glow": (0, 255, 255),
        "particle_color": (255, 0, 255),
    },
    "Fantasy": {
        "battle_background": (180, 140, 100),
        "text_box_bg": (220, 200, 160),
        "text_box_border": (120, 100, 60),
        "info_bg": (220, 200, 160),
        "info_text": (120, 100, 60),
        "text": (120, 100, 60),
        "button_idle": (140, 120, 80),
        "button_hover": (160, 140, 100),
        "button_border": (120, 100, 60),
        "player_color": (0, 150, 200),
        "enemy_color": (200, 80, 80),
        "hp_bar": GREEN,
        "status_glow": YELLOW,
        "progress_bar": (100, 255, 100),
        "progress_bg": (120, 100, 60),
        "menu_border": (100, 80, 40),
        "vs_color": (120, 100, 60),
        "heal_glow": (100, 255, 100),
        "particle_color": (255, 255, 0),
    }
}

# Difficulty Settings
DIFFICULTIES = {
    "Easy": {
        "hp_scale": 0.6,
        "attack_scale": 0.5,
        "defense_scale": 0.5,
        "attack_prob_adjust": -0.2,
        "heal_prob_adjust": -0.1,
        "special_prob_adjust": -0.2,
        "heal_effectiveness": 1.5
    },
    "Medium": {
        "hp_scale": 1.0,
        "attack_scale": 1.0,
        "defense_scale": 1.0,
        "attack_prob_adjust": 0.0,
        "heal_prob_adjust": 0.0,
        "special_prob_adjust": 0.0,
        "heal_effectiveness": 1.0
    },
    "Hard": {
        "hp_scale": 2.0,
        "attack_scale": 1.8,
        "defense_scale": 1.6,
        "attack_prob_adjust": 0.3,
        "heal_prob_adjust": 0.2,
        "special_prob_adjust": 0.3,
        "heal_effectiveness": 0.5
    }
}

# Game entities
class Character:
    def __init__(self, name, hp, attack, defense, role="dps", difficulty="Medium"):
        self.name = name
        self.base_hp = hp
        self.base_attack = attack
        self.base_defense = defense
        self.difficulty = difficulty
        self.hp_scale = DIFFICULTIES[difficulty]["hp_scale"]
        self.attack_scale = DIFFICULTIES[difficulty]["attack_scale"]
        self.defense_scale = DIFFICULTIES[difficulty]["defense_scale"]
        self.heal_effectiveness = DIFFICULTIES[difficulty]["heal_effectiveness"]
        self.max_hp = int(hp * self.hp_scale) if role != "dps" and role != "healer" else hp
        self.hp = self.max_hp
        self.attack = int(attack * self.attack_scale) if role != "dps" and role != "healer" else attack
        self.defense = int(defense * self.defense_scale) if role != "dps" and role != "healer" else defense
        self.role = role
        self.alive = True
        self.status = {}
        self.shake_offset = 0
        self.shake_timer = 0
        self.flash_timer = 0
        self.position_offset = [0, 0]
        self.glow_timer = 0
        self.particles = []

    def reset(self):
        self.hp = self.max_hp
        self.alive = True
        self.status = {}
        self.defense = int(self.base_defense * self.defense_scale) if self.role != "dps" and self.role != "healer" else self.base_defense
        self.glow_timer = 0
        self.particles = []

    def apply_status(self, status, duration):
        self.status[status] = duration
        self.flash_timer = 0.5

    def update_status(self):
        for status in list(self.status.keys()):
            if status == "poison":
                self.take_damage(5)
                self.status[status] -= 1
            elif status == "stun":
                self.status[status] -= 1
            if self.status[status] <= 0:
                del self.status[status]

    def take_damage(self, damage):
        actual_damage = max(0, damage - self.defense)
        self.hp = max(0, self.hp - actual_damage)
        if self.hp == 0:
            self.alive = False
        self.shake_timer = 0.5
        self.flash_timer = 0.5
        return actual_damage

    def heal(self, amount):
        adjusted_amount = int(amount * self.heal_effectiveness)
        self.hp = min(self.max_hp, self.hp + adjusted_amount)
        self.glow_timer = 0.5
        return adjusted_amount

# Battle system
class Battle:
    def __init__(self, players, enemies, enemy_behaviors):
        self.players = players
        self.enemies = enemies
        self.enemy_behaviors = enemy_behaviors
        self.current_enemy_behaviors = [list(beh) for beh in enemy_behaviors]
        self.turn = "player"
        self.log = []
        self.turn_count = 0
        self.active_player = 0
        self.active_enemy = 0
        self.last_ga_turn = -5
        self.player_action_history = []
        self.enemy_action_history = [[] for _ in enemies]
        self.animation_state = None
        self.animation_timer = 0
        self.current_message = None
        self.message_timer = 0

    def reset(self):
        for p in self.players + self.enemies:
            p.reset()
        self.turn = "player"
        self.log = []
        self.turn_count = 0
        self.active_player = 0
        self.active_enemy = 0
        self.last_ga_turn = -5
        self.player_action_history = []
        self.enemy_action_history = [[] for _ in self.enemies]
        self.current_enemy_behaviors = [list(beh) for beh in self.enemy_behaviors]
        self.animation_state = None
        self.animation_timer = 0
        self.current_message = None
        self.message_timer = 0

    def get_first_alive_enemy(self):
        for i, enemy in enumerate(self.enemies):
            if enemy.alive:
                return i
        return None

    def get_first_alive_player(self):
        for i, player in enumerate(self.players):
            if player.alive:
                return i
        return None

    def player_action(self, action, target_idx):
        alive_players = [i for i, p in enumerate(self.players) if p.alive]
        if not alive_players:
            return
        self.active_player = alive_players[self.active_player % len(alive_players)]
        player = self.players[self.active_player]

        if action != "heal" and action != "defend":
            if not (0 <= target_idx < len(self.enemies) and self.enemies[target_idx].alive):
                target_idx = self.get_first_alive_enemy()
                if target_idx is None:
                    self.log.append("No enemies left to target!")
                    return
            self.enemy_action_history[target_idx].append(action)
            if len(self.enemy_action_history[target_idx]) > 5:
                self.enemy_action_history[target_idx].pop(0)

        self.player_action_history.append(action)
        if len(self.player_action_history) > 5:
            self.player_action_history.pop(0)

        if action == "attack":
            damage = self.enemies[target_idx].take_damage(player.attack)
            self.log.append(f"{player.name} attacks {self.enemies[target_idx].name} for {damage} damage")
            self.animation_state = {"type": "attack", "user": "player", "target_idx": target_idx}
            self.animation_timer = 1.0
        elif action == "defend":
            player.defense += 5
            self.log.append(f"{player.name} defends, boosting defense")
            self.animation_state = {"type": "defend", "user": "player"}
            self.animation_timer = 0.5
        elif action == "heal":
            target = min(self.players, key=lambda p: p.hp / p.max_hp if p.alive else float('inf'))
            adjusted_amount = target.heal(20)
            self.log.append(f"{player.name} heals {target.name} for {adjusted_amount} HP")
            self.animation_state = {"type": "heal", "user": "player"}
            self.animation_timer = 0.5
        elif action == "special":
            if random.random() < 0.3:
                self.enemies[target_idx].apply_status("stun", 1)
                self.log.append(f"{player.name} stuns {self.enemies[target_idx].name}")
            else:
                damage = self.enemies[target_idx].take_damage(player.attack * 2)
                self.log.append(f"{player.name} uses special attack for {damage} damage")
            self.animation_state = {"type": "special", "user": "player", "target_idx": target_idx}
            self.animation_timer = 1.0

        self.active_player = (self.active_player + 1) % len(alive_players)
        self.turn = "enemy"
        self.current_message = self.log[-1]
        self.message_timer = 1.0

    def enemy_action(self):
        alive_enemies = [i for i, e in enumerate(self.enemies) if e.alive]
        if not alive_enemies:
            self.log.append("No enemies left to act!")
            self.turn = "player"
            return

        self.active_enemy = self.active_enemy % len(alive_enemies)
        self.active_enemy = alive_enemies[self.active_enemy]

        print(f"Enemy action: active_enemy={self.active_enemy}, len(enemies)={len(self.enemies)}, len(current_enemy_behaviors)={len(self.current_enemy_behaviors)}, len(enemy_action_history)={len(self.enemy_action_history)}")

        if not (0 <= self.active_enemy < len(self.current_enemy_behaviors)):
            self.log.append(f"Error: active_enemy {self.active_enemy} out of bounds for current_enemy_behaviors!")
            self.turn = "player"
            return
        if not (0 <= self.active_enemy < len(self.enemy_action_history)):
            self.log.append(f"Error: active_enemy {self.active_enemy} out of bounds for enemy_action_history!")
            self.turn = "player"
            return

        enemy = self.enemies[self.active_enemy]
        behavior = self.current_enemy_behaviors[self.active_enemy]

        attack_prob, heal_prob, heal_threshold, special_prob = behavior
        difficulty_adjust = DIFFICULTIES[enemy.difficulty]
        attack_prob += difficulty_adjust["attack_prob_adjust"]
        heal_prob += difficulty_adjust["heal_prob_adjust"]
        special_prob += difficulty_adjust["special_prob_adjust"]

        # Clamp probabilities immediately after difficulty adjustment
        attack_prob = max(0, min(1, attack_prob))
        heal_prob = max(0, min(1, heal_prob))
        special_prob = max(0, min(1, special_prob))

        recent_actions = self.player_action_history[-3:]
        attack_count = recent_actions.count("attack") + recent_actions.count("special")
        heal_count = recent_actions.count("heal")

        # Flag to track if the enemy heals during this turn
        did_heal = False

        if attack_count == 3 and enemy.name == "Goblin":
            target = min(self.enemies, key=lambda e: e.hp / e.max_hp if e.alive else float('inf'))
            adjusted_amount = target.heal(20)
            self.log.append(f"{enemy.name} heals {target.name} for {adjusted_amount} HP due to your consecutive attacks!")
            self.animation_state = {"type": "heal", "user": "enemy"}
            self.animation_timer = 0.5
            # Adjust probabilities since the Goblin healed
            heal_prob = min(1, heal_prob + 0.3)  # Increase heal_prob due to healing action
            attack_prob = max(0, attack_prob - 0.1)  # Slightly reduce attack_prob
            special_prob = max(0, special_prob - 0.05)  # Slightly reduce special_prob
            did_heal = True
        elif attack_count == 2 and enemy.name == "Goblin":
            enemy.defense += 5
            self.log.append(f"{enemy.name} defends due to your consecutive attacks!")
            self.animation_state = {"type": "defend", "user": "enemy"}
            self.animation_timer = 0.5
            # Adjust probabilities since the Goblin defended
            attack_prob = max(0, attack_prob - 0.1)  # Reduce attack_prob after defending
            heal_prob = min(1, heal_prob + 0.1)  # Slightly increase heal_prob
            special_prob = max(0, special_prob - 0.05)  # Slightly reduce special_prob
        elif heal_count >= 3 and enemy.name == "Goblin":
            alive_players = [i for i, p in enumerate(self.players) if p.alive]
            if not alive_players:
                self.log.append(f"{enemy.name} has no targets to attack!")
                self.turn = "player"
                return
            target_idx = random.choice(alive_players)
            self.players[target_idx].apply_status("poison", 3)
            self.log.append(f"{enemy.name} poisons {self.players[target_idx].name} due to your frequent healing!")
            damage = self.players[target_idx].take_damage(enemy.attack * 2.5)
            self.log.append(f"{enemy.name} uses special attack for {damage} damage")
            self.animation_state = {"type": "special", "user": "enemy", "target_idx": target_idx}
            self.animation_timer = 1.0
            # Adjust probabilities since the Goblin used a special attack
            special_prob = min(1, special_prob + 0.2)  # Increase special_prob
            attack_prob = max(0, attack_prob - 0.1)  # Slightly reduce attack_prob
            heal_prob = max(0, heal_prob - 0.1)  # Decrease heal_prob to reflect shift to special attack
        elif "stun" in enemy.status:
            self.log.append(f"{enemy.name} is stunned and skips its turn")
        else:
            # General behavior adjustments based on player actions
            if attack_count >= 2:
                heal_prob = min(1, heal_prob + 0.4)
                heal_threshold = max(0.5, heal_threshold - 0.2)
                self.log.append(f"{enemy.name} notices your aggressive attacks and prepares to heal!")
            if heal_count >= 2:
                special_prob = min(1, special_prob + 0.4)
                self.log.append(f"{enemy.name} notices your frequent healing and prepares a special attack!")
                heal_prob = max(0, heal_prob - 0.1)  # Decrease heal_prob due to preparing special attack

            # Adjustments based on the enemy's own recent actions
            recent_attacks = self.enemy_action_history[self.active_enemy][-3:]
            consecutive_attacks = recent_attacks.count("attack") + recent_attacks.count("special")
            if consecutive_attacks >= 3:
                attack_prob = max(0, attack_prob - 0.3)
                heal_prob = min(1, heal_prob + 0.2)
                self.log.append(f"{enemy.name} feels pressured and prepares to heal!")
            if consecutive_attacks >= 5 and enemy.hp / enemy.max_hp < 0.75:
                heal_prob = min(1, heal_prob + 0.4)
                heal_threshold = max(0.5, heal_threshold - 0.2)
                self.log.append(f"{enemy.name} is heavily damaged and prioritizes healing!")

            # Adjustments based on total player HP
            total_player_hp = sum(p.hp for p in self.players if p.alive) / sum(p.max_hp for p in self.players)
            if total_player_hp < 0.3:
                attack_prob = min(1, attack_prob + 0.3)
                special_prob = min(1, special_prob + 0.3)
                self.log.append(f"{enemy.name} senses weakness and goes for the kill!")

            # General action decision
            if enemy.hp / enemy.max_hp < heal_threshold and random.random() < heal_prob:
                target = min(self.enemies, key=lambda e: e.hp / e.max_hp if e.alive else float('inf'))
                adjusted_amount = target.heal(20)
                self.log.append(f"{enemy.name} heals {target.name} for {adjusted_amount} HP")
                self.animation_state = {"type": "heal", "user": "enemy"}
                self.animation_timer = 0.5
                # Adjust probabilities since the enemy healed
                heal_prob = min(1, heal_prob + 0.1)
                attack_prob = max(0, attack_prob - 0.05)
                special_prob = max(0, special_prob - 0.05)
                did_heal = True
            elif random.random() < special_prob:
                alive_players = [i for i, p in enumerate(self.players) if p.alive]
                if not alive_players:
                    self.log.append(f"{enemy.name} has no targets to attack!")
                    self.turn = "player"
                    return
                target_idx = random.choice(alive_players)
                if random.random() < 0.3:
                    self.players[target_idx].apply_status("poison", 3)
                    self.log.append(f"{enemy.name} poisons {self.players[target_idx].name}")
                else:
                    damage = self.players[target_idx].take_damage(enemy.attack * 2.5)
                    self.log.append(f"{enemy.name} uses special attack for {damage} damage")
                self.animation_state = {"type": "special", "user": "enemy", "target_idx": target_idx}
                self.animation_timer = 1.0
                # Adjust probabilities since the enemy used a special attack
                special_prob = min(1, special_prob + 0.2)
                attack_prob = max(0, attack_prob - 0.1)
                heal_prob = max(0, heal_prob - 0.1)  # Decrease heal_prob to reflect shift to special attack
            elif random.random() < attack_prob:
                alive_players = [i for i, p in enumerate(self.players) if p.alive]
                if not alive_players:
                    self.log.append(f"{enemy.name} has no targets to attack!")
                    self.turn = "player"
                    return
                target_idx = random.choice(alive_players)
                damage = self.players[target_idx].take_damage(enemy.attack)
                self.log.append(f"{enemy.name} attacks {self.players[target_idx].name} for {damage} damage")
                self.animation_state = {"type": "attack", "user": "enemy", "target_idx": target_idx}
                self.animation_timer = 1.0
                # Adjust probabilities since the enemy attacked
                attack_prob = min(1, attack_prob + 0.1)
                heal_prob = max(0, heal_prob - 0.1)
                special_prob = max(0, special_prob - 0.05)
            else:
                enemy.defense += 5
                self.log.append(f"{enemy.name} defends, boosting defense")
                self.animation_state = {"type": "defend", "user": "enemy"}
                self.animation_timer = 0.5
                # Adjust probabilities since the enemy defended
                attack_prob = max(0, attack_prob - 0.1)
                heal_prob = min(1, heal_prob + 0.1)
                special_prob = max(0, special_prob - 0.05)

        # Additional probability adjustment if the enemy healed
        if did_heal:
            heal_prob = min(1, heal_prob + 0.1)  # Further increase heal_prob after healing
            attack_prob = max(0, attack_prob - 0.05)  # Slightly reduce attack_prob
            special_prob = max(0, special_prob - 0.05)  # Slightly reduce special_prob

        # Clamp probabilities before storing
        attack_prob = max(0, min(1, attack_prob))
        heal_prob = max(0, min(1, heal_prob))
        special_prob = max(0, min(1, special_prob))

        # Update the enemy's behavior with the clamped probabilities
        self.current_enemy_behaviors[self.active_enemy] = [
            attack_prob,
            heal_prob,
            heal_threshold,
            special_prob
        ]

        self.active_enemy = (self.active_enemy + 1) % len(alive_enemies)
        self.turn = "player"
        self.turn_count += 1
        for p in self.players + self.enemies:
            p.update_status()
            p.defense = max(5 if p in self.players else 3, p.defense - 5)
        self.current_message = self.log[-1]
        self.message_timer = 1.0

    def is_over(self):
        players_alive = any(p.alive for p in self.players)
        enemies_alive = any(e.alive for e in self.enemies)
        return not players_alive or not enemies_alive

# GA functions
def initialize_population(size, num_enemies, difficulty="Medium"):
    adjust = DIFFICULTIES[difficulty]
    return [[
        [
            random.uniform(0.5, 0.9) + adjust["attack_prob_adjust"],
            random.uniform(0.2, 0.4) + adjust["heal_prob_adjust"],
            random.uniform(0.2, 0.6),
            random.uniform(0, 0.2) + adjust["special_prob_adjust"]
        ]
        for _ in range(num_enemies)
    ] for _ in range(size)]

def evaluate_fitness(battle, behaviors, max_turns=5):
    battle.reset()
    battle.enemy_behaviors = behaviors
    action_counts = {"attack": 0, "heal": 0, "special": 0, "defend": 0}

    for _ in range(max_turns):
        if battle.is_over():
            break
        if battle.turn == "player":
            alive_enemies = [i for i, e in enumerate(battle.enemies) if e.alive]
            if not alive_enemies:
                break
            if any(p.hp / p.max_hp < 0.3 for p in battle.players if p.alive):
                battle.player_action("heal", 0)
                action_counts["heal"] += 1
            elif random.random() < 0.2:
                target_idx = random.choice(alive_enemies)
                battle.player_action("special", target_idx)
                action_counts["special"] += 1
            elif random.random() < 0.7:
                target_idx = random.choice(alive_enemies)
                battle.player_action("attack", target_idx)
                action_counts["attack"] += 1
            else:
                battle.player_action("defend", 0)
                action_counts["defend"] += 1
        else:
            battle.enemy_action()

    duration_score = abs(battle.turn_count - 10) / 10
    hp_score = (sum(p.hp for p in battle.players if p.alive) / sum(p.max_hp for p in battle.players) - 0.3) / 0.3 * 2
    variety_score = 1 - (max(action_counts.values()) / (sum(action_counts.values()) + 1))
    enemy_hp_score = (sum(e.hp for e in battle.enemies if e.alive) / sum(e.max_hp for e in battle.enemies) - 0.3) / 0.3
    win_score = 0 if any(p.alive for p in battle.players) else 2
    fitness = duration_score + max(0, hp_score) + 0.5 * variety_score + win_score + max(0, -enemy_hp_score)
    return fitness, battle.turn_count, sum(p.hp for p in battle.players if p.alive)

def tournament_select(population, fitness_scores):
    tournament = random.sample(list(zip(population, fitness_scores)), 3)
    return min(tournament, key=lambda x: x[1])[0]

def crossover(parent1, parent2):
    return [
        [p1 if random.random() < 0.5 else p2 for p1, p2 in zip(b1, b2)]
        for b1, b2 in zip(parent1, parent2)
    ]

def mutate(individual, battle):
    if not battle.player_action_history:
        return [[min(1, max(0, gene + random.uniform(-0.02, 0.02))) for gene in behavior] for behavior in individual]

    heal_ratio = battle.player_action_history.count("heal") / len(battle.player_action_history)
    attack_ratio = battle.player_action_history.count("attack") / len(battle.player_action_history)

    mutated = []
    for behavior in individual:
        new_behavior = []
        for i, gene in enumerate(behavior):
            if i == 0:
                adjustment = 0.1 if attack_ratio > 0.5 else -0.1
            elif i == 1:
                adjustment = 0.05 if any(e.hp / e.max_hp < 0.5 for e in battle.enemies if e.alive) else 0
            elif i == 2:
                adjustment = random.uniform(-0.02, 0.02)
            elif i == 3:
                adjustment = 0.1 if heal_ratio > 0.5 else -0.1
            new_gene = min(1, max(0, gene + adjustment + random.uniform(-0.02, 0.02)))
            new_behavior.append(new_gene)
        mutated.append(new_behavior)
    return mutated

# GUI drawing with enhanced animations
def draw_battle(screen, battle, time_delta, training=False, training_progress=0, current_gen=0, total_gens=2, theme="Light"):
    theme_colors = THEMES[theme]
    screen.fill(theme_colors["battle_background"])

    vs_text = VS_FONT.render("VS", True, theme_colors["vs_color"])
    vs_rect = vs_text.get_rect(center=(BATTLE_WIDTH // 2, HEIGHT // 2))
    screen.blit(vs_text, vs_rect)

    if training:
        label = FONT.render(f"Training AI... Gen {current_gen + 1}/{total_gens} ({training_progress:.0%})", True, theme_colors["text"])
        screen.blit(label, (BATTLE_WIDTH // 2 - 100 * SCALE_FACTOR, HEIGHT // 2 - 20 * SCALE_FACTOR))
        bar_width = 200 * SCALE_FACTOR
        bar_height = 20 * SCALE_FACTOR
        progress_width = bar_width * training_progress
        pygame.draw.rect(screen, theme_colors["progress_bg"], (BATTLE_WIDTH // 2 - 100 * SCALE_FACTOR, HEIGHT // 2 + 10 * SCALE_FACTOR, bar_width, bar_height))
        pygame.draw.rect(screen, theme_colors["progress_bar"], (BATTLE_WIDTH // 2 - 100 * SCALE_FACTOR, HEIGHT // 2 + 10 * SCALE_FACTOR, progress_width, bar_height))
        return []

    player_pos = [(250 * SCALE_FACTOR, 600 * SCALE_FACTOR), (200 * SCALE_FACTOR, 650 * SCALE_FACTOR)]
    enemy_pos = [(BATTLE_WIDTH - 250 * SCALE_FACTOR, 200 * SCALE_FACTOR), (BATTLE_WIDTH - 200 * SCALE_FACTOR, 250 * SCALE_FACTOR)]

    if battle.animation_state:
        battle.animation_timer -= time_delta
        if battle.animation_timer <= 0:
            battle.animation_state = None
        else:
            action_type = battle.animation_state["type"]
            user = "player" if battle.animation_state["user"] == "player" else "enemy"
            target_idx = battle.animation_state.get("target_idx", 0)

            if user == "player":
                user_char = battle.players[battle.active_player]
                target_char = battle.enemies[target_idx]
                user_pos = player_pos[battle.active_player]
                target_pos = enemy_pos[target_idx]
            else:
                user_char = battle.enemies[battle.active_enemy]
                target_char = battle.players[target_idx]
                user_pos = enemy_pos[battle.active_enemy]
                target_pos = player_pos[target_idx]

            if action_type == "attack":
                progress = 1 - battle.animation_timer
                if progress < 0.5:
                    offset = progress * 50 * SCALE_FACTOR * (1 if user == "player" else -1)
                else:
                    offset = (1 - progress) * 50 * SCALE_FACTOR * (1 if user == "player" else -1)
                user_char.position_offset = [offset, 0]
            elif action_type == "special":
                target_char.flash_timer = 0.5
                if len(target_char.particles) < 10:
                    for _ in range(5):
                        target_char.particles.append({
                            "pos": list(target_pos),
                            "vel": [random.uniform(-50, 50), random.uniform(-50, 50)],
                            "timer": 0.5
                        })
            elif action_type == "heal":
                user_char.glow_timer = 0.5
            elif action_type == "defend":
                user_char.shake_timer = 0.5

    for char in battle.players + battle.enemies:
        new_particles = []
        for particle in char.particles:
            particle["pos"][0] += particle["vel"][0] * time_delta
            particle["pos"][1] += particle["vel"][1] * time_delta
            particle["timer"] -= time_delta
            if particle["timer"] > 0:
                new_particles.append(particle)
        char.particles = new_particles
        for particle in char.particles:
            pygame.draw.circle(screen, theme_colors["particle_color"], particle["pos"], 5 * SCALE_FACTOR)

    for i, player in enumerate(battle.players):
        if not player.alive:
            continue
        color = RED if player.flash_timer > 0 else theme_colors["player_color"]
        border_color = BLACK
        offset_x = player.shake_offset + player.position_offset[0]
        offset_y = player.position_offset[1]
        center = (player_pos[i][0] + offset_x, player_pos[i][1] + offset_y)
        radius = 35 * SCALE_FACTOR

        if player.glow_timer > 0:
            glow_radius = radius + 10 * SCALE_FACTOR * (1 + 0.2 * np.sin(pygame.time.get_ticks() / 100))
            pygame.draw.circle(screen, theme_colors["heal_glow"], center, glow_radius, 2)
            player.glow_timer -= time_delta

        pygame.draw.circle(screen, border_color, center, radius + 2)
        pygame.draw.circle(screen, color, center, radius)

        name_label = SMALL_FONT.render(player.name, True, theme_colors["text"])
        name_rect = name_label.get_rect(center=(center[0], center[1] - 60 * SCALE_FACTOR))
        screen.blit(name_label, name_rect)

        hp_rect = (player_pos[i][0] - 60 * SCALE_FACTOR, player_pos[i][1] - 40 * SCALE_FACTOR, 120 * SCALE_FACTOR, 40 * SCALE_FACTOR)
        pygame.draw.rect(screen, theme_colors["text_box_bg"], hp_rect)
        pygame.draw.rect(screen, theme_colors["text_box_border"], hp_rect, 2)
        hp_ratio = player.hp / player.max_hp
        pygame.draw.rect(screen, theme_colors["hp_bar"], (hp_rect[0] + 2, hp_rect[1] + 20 * SCALE_FACTOR, 116 * SCALE_FACTOR * hp_ratio, 10 * SCALE_FACTOR))
        label = SMALL_FONT.render(f"HP: {player.hp}/{player.max_hp}", True, theme_colors["text"])
        screen.blit(label, (hp_rect[0] + 5 * SCALE_FACTOR, hp_rect[1] + 5 * SCALE_FACTOR))

        if "poison" in player.status:
            pygame.draw.circle(screen, theme_colors["status_glow"], center, 20 * SCALE_FACTOR)
        if player.shake_timer > 0:
            player.shake_timer -= time_delta
            player.shake_offset = random.randint(-5, 5) if player.shake_timer > 0 else 0
        if player.flash_timer > 0:
            player.flash_timer -= time_delta
        player.position_offset = [0, 0]

    for i, enemy in enumerate(battle.enemies):
        if not enemy.alive:
            continue
        color = RED if enemy.flash_timer > 0 else theme_colors["enemy_color"]
        border_color = BLACK
        offset_x = enemy.shake_offset + enemy.position_offset[0]
        offset_y = enemy.position_offset[1]
        center = (enemy_pos[i][0] + offset_x, enemy_pos[i][1] + offset_y)
        radius = 35 * SCALE_FACTOR

        if enemy.glow_timer > 0:
            glow_radius = radius + 10 * SCALE_FACTOR * (1 + 0.2 * np.sin(pygame.time.get_ticks() / 100))
            pygame.draw.circle(screen, theme_colors["heal_glow"], center, glow_radius, 2)
            enemy.glow_timer -= time_delta

        pygame.draw.circle(screen, border_color, center, radius + 2)
        pygame.draw.circle(screen, color, center, radius)

        name_label = SMALL_FONT.render(enemy.name, True, theme_colors["text"])
        name_rect = name_label.get_rect(center=(center[0], center[1] - 60 * SCALE_FACTOR))
        screen.blit(name_label, name_rect)

        hp_rect = (enemy_pos[i][0] - 60 * SCALE_FACTOR, enemy_pos[i][1] - 40 * SCALE_FACTOR, 120 * SCALE_FACTOR, 40 * SCALE_FACTOR)
        pygame.draw.rect(screen, theme_colors["text_box_bg"], hp_rect)
        pygame.draw.rect(screen, theme_colors["text_box_border"], hp_rect, 2)
        hp_ratio = enemy.hp / enemy.max_hp
        pygame.draw.rect(screen, theme_colors["hp_bar"], (hp_rect[0] + 2, hp_rect[1] + 20 * SCALE_FACTOR, 116 * SCALE_FACTOR * hp_ratio, 10 * SCALE_FACTOR))
        label = SMALL_FONT.render(f"HP: {enemy.hp}/{enemy.max_hp}", True, theme_colors["text"])
        screen.blit(label, (hp_rect[0] + 5 * SCALE_FACTOR, hp_rect[1] + 5 * SCALE_FACTOR))

        if "stun" in enemy.status:
            pygame.draw.circle(screen, theme_colors["status_glow"], center, 20 * SCALE_FACTOR)
        if enemy.shake_timer > 0:
            enemy.shake_timer -= time_delta
            enemy.shake_offset = random.randint(-5, 5) if enemy.shake_timer > 0 else 0
        if enemy.flash_timer > 0:
            enemy.flash_timer -= time_delta
        enemy.position_offset = [0, 0]

    if battle.message_timer > 0:
        battle.message_timer -= time_delta
        if battle.message_timer <= 0:
            battle.current_message = None

    text_rect = (20 * SCALE_FACTOR, HEIGHT - 240 * SCALE_FACTOR, BATTLE_WIDTH - 40 * SCALE_FACTOR, 100 * SCALE_FACTOR)
    pygame.draw.rect(screen, theme_colors["menu_border"], (text_rect[0] - 5 * SCALE_FACTOR, text_rect[1] - 5 * SCALE_FACTOR, text_rect[2] + 10 * SCALE_FACTOR, text_rect[3] + 10 * SCALE_FACTOR))
    pygame.draw.rect(screen, theme_colors["text_box_bg"], text_rect)
    pygame.draw.rect(screen, theme_colors["text_box_border"], text_rect, 2)
    if battle.current_message:
        text = SMALL_FONT.render(battle.current_message, True, theme_colors["text"])
        screen.blit(text, (text_rect[0] + 10 * SCALE_FACTOR, text_rect[1] + 10 * SCALE_FACTOR))
    elif battle.turn == "player" and not battle.animation_state:
        text = SMALL_FONT.render("What will you do?", True, theme_colors["text"])
        screen.blit(text, (text_rect[0] + 10 * SCALE_FACTOR, text_rect[1] + 10 * SCALE_FACTOR))

    buttons = []
    mouse_pos = pygame.mouse.get_pos()
    if battle.turn == "player" and not battle.animation_state and not battle.current_message:
        menu_rect = (20 * SCALE_FACTOR, HEIGHT - 120 * SCALE_FACTOR, BATTLE_WIDTH - 40 * SCALE_FACTOR, 100 * SCALE_FACTOR)
        pygame.draw.rect(screen, theme_colors["menu_border"], (menu_rect[0] - 5 * SCALE_FACTOR, menu_rect[1] - 5 * SCALE_FACTOR, menu_rect[2] + 10 * SCALE_FACTOR, menu_rect[3] + 10 * SCALE_FACTOR))
        pygame.draw.rect(screen, theme_colors["text_box_bg"], menu_rect)
        pygame.draw.rect(screen, theme_colors["text_box_border"], menu_rect, 2)

        actions = []
        for i, enemy in enumerate(battle.enemies):
            if enemy.alive:
                actions.append((f"Attack {enemy.name}", "attack", i))
                actions.append((f"Special {enemy.name}", "special", i))
        actions.extend([
            ("Heal", "heal", 0),
            ("Defend", "defend", 0)
        ])

        for i, (text, action, target_idx) in enumerate(actions):
            x = (menu_rect[0] + 20 * SCALE_FACTOR + (i % 3) * 180 * SCALE_FACTOR)
            y = (menu_rect[1] + 10 * SCALE_FACTOR + (i // 3) * 40 * SCALE_FACTOR)
            rect = (x, y, 160 * SCALE_FACTOR, 30 * SCALE_FACTOR)
            is_hovered = rect[0] <= mouse_pos[0] < rect[0] + rect[2] and rect[1] <= mouse_pos[1] < rect[1] + rect[3]
            color = theme_colors["button_hover"] if is_hovered else theme_colors["button_idle"]
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, theme_colors["button_border"], rect, 1)
            label = SMALL_FONT.render(text, True, theme_colors["text"])
            label_rect = label.get_rect(center=(rect[0] + rect[2] // 2, rect[1] + rect[3] // 2))
            screen.blit(label, label_rect)
            buttons.append((action, target_idx, rect))

    return buttons

def draw_info(screen, battle, generation, best_fitness, log, theme="Light"):
    theme_colors = THEMES[theme]
    info_surface = pygame.Surface((INFO_WIDTH, HEIGHT))
    info_surface.fill(theme_colors["info_bg"])

    y_offset = 20 * SCALE_FACTOR
    info_surface.blit(FONT.render(f"Gen: {generation}", True, theme_colors["info_text"]), (10 * SCALE_FACTOR, y_offset))
    y_offset += 40 * SCALE_FACTOR
    info_surface.blit(FONT.render(f"Fitness: {best_fitness:.2f}", True, theme_colors["info_text"]), (10 * SCALE_FACTOR, y_offset))
    y_offset += 50 * SCALE_FACTOR

    labels = ["attack_prob", "heal_prob", "heal_threshold", "special_prob"]
    for i, (enemy_name, behavior) in enumerate(zip(["Goblin", "Wolf"], battle.current_enemy_behaviors)):
        behavior_str = ", ".join(f"{label}={value:.2f}" for label, value in zip(labels, behavior))
        text = SMALL_FONT.render(f"{enemy_name}: {behavior_str}", True, theme_colors["info_text"])
        info_surface.blit(text, (10 * SCALE_FACTOR, y_offset))
        y_offset += 30 * SCALE_FACTOR

    y_offset += 30 * SCALE_FACTOR
    info_surface.blit(FONT.render("Statuses:", True, theme_colors["info_text"]), (10 * SCALE_FACTOR, y_offset))
    y_offset += 40 * SCALE_FACTOR
    for char in battle.players + battle.enemies:
        status_text = f"{char.name}: {'Dead' if not char.alive else (', '.join(f'{k}:{v}' for k, v in char.status.items()) or 'None')}"
        text = SMALL_FONT.render(status_text, True, theme_colors["info_text"])
        info_surface.blit(text, (10 * SCALE_FACTOR, y_offset))
        y_offset += 30 * SCALE_FACTOR

    y_offset += 30 * SCALE_FACTOR
    info_surface.blit(FONT.render("Battle Log:", True, theme_colors["info_text"]), (10 * SCALE_FACTOR, y_offset))
    y_offset += 40 * SCALE_FACTOR
    for i, entry in enumerate(log[-5:]):
        text = SMALL_FONT.render(entry, True, theme_colors["info_text"])
        info_surface.blit(text, (10 * SCALE_FACTOR, y_offset + i * 40 * SCALE_FACTOR))

    screen.blit(info_surface, (BATTLE_WIDTH, 0))

def draw_theme_selector(screen, current_theme, theme_dropdown_open, theme_hovered, theme="Light"):
    theme_colors = THEMES[theme]
    dropdown_rect = (BATTLE_WIDTH + 10 * SCALE_FACTOR, 10 * SCALE_FACTOR, 220 * SCALE_FACTOR, 40 * SCALE_FACTOR)
    options = list(THEMES.keys())

    pygame.draw.rect(screen, theme_colors["button_idle"], dropdown_rect, border_radius=2)
    pygame.draw.rect(screen, theme_colors["button_border"], dropdown_rect, 2, border_radius=2)
    label = SMALL_FONT.render(f"Theme: {current_theme}", True, theme_colors["text"])
    label_rect = label.get_rect(center=(dropdown_rect[0] + dropdown_rect[2] // 2, dropdown_rect[1] + dropdown_rect[3] // 2))
    screen.blit(label, label_rect)

    theme_buttons = []
    if theme_dropdown_open:
        for i, option in enumerate(options):
            option_rect = (dropdown_rect[0], dropdown_rect[1] + (i + 1) * 40 * SCALE_FACTOR, 220 * SCALE_FACTOR, 40 * SCALE_FACTOR)
            color = theme_colors["button_hover"] if i == theme_hovered else theme_colors["button_idle"]
            pygame.draw.rect(screen, color, option_rect, border_radius=2)
            pygame.draw.rect(screen, theme_colors["button_border"], option_rect, 2, border_radius=2)
            label = SMALL_FONT.render(option, True, theme_colors["text"])
            label_rect = label.get_rect(center=(option_rect[0] + option_rect[2] // 2, option_rect[1] + option_rect[3] // 2))
            screen.blit(label, label_rect)
            theme_buttons.append((option, option_rect))

    return theme_buttons

def draw_difficulty_selector(screen, current_difficulty, difficulty_dropdown_open, difficulty_hovered, theme="Light"):
    theme_colors = THEMES[theme]
    dropdown_rect = (BATTLE_WIDTH + 240 * SCALE_FACTOR, 10 * SCALE_FACTOR, 180 * SCALE_FACTOR, 40 * SCALE_FACTOR)
    options = list(DIFFICULTIES.keys())

    pygame.draw.rect(screen, theme_colors["button_idle"], dropdown_rect, border_radius=2)
    pygame.draw.rect(screen, theme_colors["button_border"], dropdown_rect, 2, border_radius=2)
    label = SMALL_FONT.render(f"Difficulty: {current_difficulty}", True, theme_colors["text"])
    label_rect = label.get_rect(center=(dropdown_rect[0] + dropdown_rect[2] // 2, dropdown_rect[1] + dropdown_rect[3] // 2))
    screen.blit(label, label_rect)

    difficulty_buttons = []
    if difficulty_dropdown_open:
        for i, option in enumerate(options):
            option_rect = (dropdown_rect[0], dropdown_rect[1] + (i + 1) * 40 * SCALE_FACTOR, 180 * SCALE_FACTOR, 40 * SCALE_FACTOR)
            color = theme_colors["button_hover"] if i == difficulty_hovered else theme_colors["button_idle"]
            pygame.draw.rect(screen, color, option_rect, border_radius=2)
            pygame.draw.rect(screen, theme_colors["button_border"], option_rect, 2, border_radius=2)
            label = SMALL_FONT.render(option, True, theme_colors["text"])
            label_rect = label.get_rect(center=(option_rect[0] + option_rect[2] // 2, option_rect[1] + option_rect[3] // 2))
            screen.blit(label, label_rect)
            difficulty_buttons.append((option, option_rect))

    return difficulty_buttons

def main():
    clock = pygame.time.Clock()
    current_difficulty = "Medium"
    players = [
        Character("Hero", 100, 15, 5, "dps"),
        Character("Mage", 80, 12, 3, "healer")
    ]
    enemies = [
        Character("Goblin", 80, 15, 5, "dps", current_difficulty),
        Character("Wolf", 60, 12, 4, "support", current_difficulty)
    ]
    sim_battle = Battle(players, enemies, [])
    population = initialize_population(5, len(enemies), current_difficulty)
    generation = 0
    best_fitness = float('inf')
    best_behavior = population[0]
    training = True
    training_generations = 2
    current_gen = 0
    training_progress = 0
    fitness_scores = []
    current_eval_idx = 0
    current_theme = "Retro"
    theme_dropdown_open = False
    theme_hovered = -1
    difficulty_dropdown_open = False
    difficulty_hovered = -1

    battle = Battle(
        [Character("Hero", 100, 15, 5, "dps"), Character("Mage", 80, 12, 3, "healer")],
        [Character("Goblin", 80, 15, 5, "dps", current_difficulty),
         Character("Wolf", 60, 12, 4, "support", current_difficulty)],
        best_behavior
    )
    running = True
    enemy_turn_pending = False
    player_action_allowed = True

    while running:
        time_delta = clock.tick(30) / 1000.0
        buttons = draw_battle(SCREEN, battle, time_delta, training, training_progress, current_gen, training_generations, current_theme)
        draw_info(SCREEN, battle, generation, best_fitness, battle.log, current_theme)
        theme_buttons = draw_theme_selector(SCREEN, current_theme, theme_dropdown_open, theme_hovered, current_theme)
        difficulty_buttons = draw_difficulty_selector(SCREEN, current_difficulty, difficulty_dropdown_open, difficulty_hovered, current_theme)
        pygame.display.flip()

        mouse_pos = pygame.mouse.get_pos()
        theme_hovered = -1
        difficulty_hovered = -1
        for i, (_, rect) in enumerate(theme_buttons):
            if rect[0] <= mouse_pos[0] < rect[0] + rect[2] and rect[1] <= mouse_pos[1] < rect[1] + rect[3]:
                theme_hovered = i
        for i, (_, rect) in enumerate(difficulty_buttons):
            if rect[0] <= mouse_pos[0] < rect[0] + rect[2] and rect[1] <= mouse_pos[1] < rect[1] + rect[3]:
                difficulty_hovered = i

        if enemy_turn_pending and not battle.animation_state and not battle.current_message:
            if not battle.is_over():
                while True:
                    alive_enemies = [i for i, e in enumerate(battle.enemies) if e.alive]
                    if not alive_enemies:
                        break
                    battle.active_enemy = 0
                    battle.active_enemy = alive_enemies[battle.active_enemy % len(alive_enemies)]
                    enemy = battle.enemies[battle.active_enemy]
                    if "stun" not in enemy.status:
                        battle.enemy_action()
                        break
                    else:
                        battle.log.append(f"{enemy.name} is stunned and skips its turn")
                        battle.active_enemy = (battle.active_enemy + 1) % len(alive_enemies)
                        for p in battle.players + battle.enemies:
                            p.update_status()
                        continue
            enemy_turn_pending = False
            player_action_allowed = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                theme_dropdown_rect = (BATTLE_WIDTH + 10 * SCALE_FACTOR, 10 * SCALE_FACTOR, 220 * SCALE_FACTOR, 40 * SCALE_FACTOR)
                if theme_dropdown_rect[0] <= x < theme_dropdown_rect[0] + theme_dropdown_rect[2] and theme_dropdown_rect[1] <= y < theme_dropdown_rect[1] + theme_dropdown_rect[3]:
                    theme_dropdown_open = not theme_dropdown_open
                    difficulty_dropdown_open = False
                elif theme_dropdown_open:
                    for option, rect in theme_buttons:
                        if rect[0] <= x < rect[0] + rect[2] and rect[1] <= y < rect[1] + rect[3]:
                            current_theme = option
                            theme_dropdown_open = False
                            break
                difficulty_dropdown_rect = (BATTLE_WIDTH + 240 * SCALE_FACTOR, 10 * SCALE_FACTOR, 180 * SCALE_FACTOR, 40 * SCALE_FACTOR)
                if difficulty_dropdown_rect[0] <= x < difficulty_dropdown_rect[0] + difficulty_dropdown_rect[2] and difficulty_dropdown_rect[1] <= y < theme_dropdown_rect[1] + theme_dropdown_rect[3]:
                    difficulty_dropdown_open = not difficulty_dropdown_open
                    theme_dropdown_open = False
                elif difficulty_dropdown_open:
                    for option, rect in difficulty_buttons:
                        if rect[0] <= x < rect[0] + rect[2] and rect[1] <= y < rect[1] + rect[3]:
                            current_difficulty = option
                            difficulty_dropdown_open = False
                            battle = Battle(
                                [Character("Hero", 100, 15, 5, "dps"), Character("Mage", 80, 12, 3, "healer")],
                                [Character("Goblin", 80, 15, 5, "dps", current_difficulty),
                                 Character("Wolf", 60, 12, 4, "support", current_difficulty)],
                                best_behavior
                            )
                            sim_battle = Battle(
                                [Character("Hero", 100, 15, 5, "dps"), Character("Mage", 80, 12, 3, "healer")],
                                [Character("Goblin", 80, 15, 5, "dps", current_difficulty),
                                 Character("Wolf", 60, 12, 4, "support", current_difficulty)],
                                []
                            )
                            population = initialize_population(5, len(enemies), current_difficulty)
                            break
                elif not training and battle.turn == "player" and not battle.animation_state and player_action_allowed:
                    if battle.current_message:
                        battle.current_message = None
                        battle.message_timer = 0
                    else:
                        for action, target_idx, (bx, by, bw, bh) in buttons:
                            if bx <= x < bx + bw and by <= y < by + bh:
                                print(f"Button clicked: {action}")
                                if "attack" in action:
                                    battle.player_action("attack", target_idx)
                                elif "special" in action:
                                    battle.player_action("special", target_idx)
                                elif action == "heal":
                                    battle.player_action("heal", 0)
                                elif action == "defend":
                                    battle.player_action("defend", 0)
                                enemy_turn_pending = True
                                player_action_allowed = False

        if training:
            if current_eval_idx < len(population):
                fitness_scores.append(evaluate_fitness(sim_battle, population[current_eval_idx]))
                current_eval_idx += 1
                training_progress = current_eval_idx / len(population)
            else:
                best_idx = np.argmin([f[0] for f in fitness_scores])
                best_fitness = fitness_scores[best_idx][0]
                best_behavior = population[best_idx]
                new_population = [best_behavior]
                while len(new_population) < len(population):
                    parent1 = tournament_select(population, [f[0] for f in fitness_scores])
                    parent2 = tournament_select(population, [f[0] for f in fitness_scores])
                    child = crossover(parent1, parent2)
                    child = mutate(child, battle)
                    new_population.append(child)
                population = new_population
                generation += 1
                current_gen += 1
                print(f"Generation {generation}: Best fitness = {best_fitness:.2f}, Turns = {fitness_scores[best_idx][1]}, Player HP = {fitness_scores[best_idx][2]}")
                fitness_scores = []
                current_eval_idx = 0
                training_progress = 0
                if current_gen >= training_generations:
                    training = False
                    battle = Battle(
                        [Character("Hero", 100, 15, 5, "dps"), Character("Mage", 80, 12, 3, "healer")],
                        [Character("Goblin", 80, 15, 5, "dps", current_difficulty),
                         Character("Wolf", 60, 12, 4, "support", current_difficulty)],
                        best_behavior
                    )
                else:
                    best_fitness = float('inf')

        if not training and battle.turn_count >= battle.last_ga_turn + 5 and battle.turn == "player" and not battle.is_over():
            battle.last_ga_turn = battle.turn_count
            sim_battle = Battle(
                [Character("Hero", 100, 15, 5, "dps"), Character("Mage", 80, 12, 3, "healer")],
                [Character("Goblin", 80, 15, 5, "dps", current_difficulty),
                 Character("Wolf", 60, 12, 4, "support", current_difficulty)],
                []
            )
            fitness_scores = [evaluate_fitness(sim_battle, beh, max_turns=15) for beh in population]
            best_idx = np.argmin([f[0] for f in fitness_scores])
            if fitness_scores[best_idx][0] < best_fitness:
                best_fitness = fitness_scores[best_idx][0]
                best_behavior = population[best_idx]
                battle.enemy_behaviors = best_behavior
                battle.current_enemy_behaviors = [list(beh) for beh in best_behavior]
            new_population = [best_behavior]
            while len(new_population) < len(population):
                parent1 = tournament_select(population, [f[0] for f in fitness_scores])
                parent2 = tournament_select(population, [f[0] for f in fitness_scores])
                child = crossover(parent1, parent2)
                child = mutate(child, battle)
                new_population.append(child)
            population = new_population
            generation += 1
            print(f"Generation {generation}: Best fitness = {best_fitness:.2f}, Turns = {fitness_scores[best_idx][1]}, Player HP = {fitness_scores[best_idx][2]}")

        if not training and battle.is_over():
            battle.log.append(f"Battle over: {'Player wins' if any(p.alive for p in battle.players) else 'Enemy wins'}")
            battle = Battle(
                [Character("Hero", 100, 15, 5, "dps"), Character("Mage", 80, 12, 3, "healer")],
                [Character("Goblin", 80, 15, 5, "dps", current_difficulty),
                 Character("Wolf", 60, 12, 4, "support", current_difficulty)],
                best_behavior
            )
            player_action_allowed = True

    pygame.quit()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
        pygame.quit()