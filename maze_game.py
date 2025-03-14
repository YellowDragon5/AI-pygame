import pygame  
import sys  
  
# Initialize Pygame  
pygame.init()  
  
# Set up display  
width, height = 800, 600  
window = pygame.display.set_mode((width, height))  
pygame.display.set_caption('Complex Adventure Game')  
  
# Player settings  
player_pos = [width // 2, height // 2]  
player_speed = 5  
  
# Run the game loop  
running = True  
while running:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            running = False  
  
    # Handle key presses for movement  
    keys = pygame.key.get_pressed()  
    if keys[pygame.K_LEFT]:  
        player_pos[0] -= player_speed  
    if keys[pygame.K_RIGHT]:  
        player_pos[0] += player_speed  
    if keys[pygame.K_UP]:  
        player_pos[1] -= player_speed  
    if keys[pygame.K_DOWN]:  
        player_pos[1] += player_speed  
  # Define the correct sequence  
correct_sequence = ['a', 'd', 'c', 'b']  
current_input = []  
  
# Function to check the sequence  
def check_sequence():  
    if current_input == correct_sequence:  
        print("Door unlocked!")  
        return True  
    return False  
  
# Main loop  
while running:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            running = False  
        if event.type == pygame.KEYDOWN:  
            key_name = pygame.key.name(event.key)  
            if key_name in correct_sequence:  
                current_input.append(key_name)  
                if len(current_input) > len(correct_sequence):  
                    current_input.pop(0)  # Keep input length consistent  
                if check_sequence():  
                    # Reset or progress game  
                    current_input = []  
  
    # Drawing and other game logic...  

    # Drawing  
    window.fill((0, 0, 0))  # Clear screen  
    pygame.draw.rect(window, (255, 0, 0), (*player_pos, 50, 50))  # Player as a red square  
    pygame.display.flip()  
  
pygame.quit()  
sys.exit()  
