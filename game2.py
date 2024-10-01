
import pygame
import random
import subprocess


pygame.init()

correct_sound = pygame.mixer.Sound("correct.wav")
wrong_sound = pygame.mixer.Sound("wrong.wav")
win_sound = pygame.mixer.Sound("win.wav")
welcome_sound = pygame.mixer.Sound("welcome.wav")
choose_sound = pygame.mixer.Sound("choose.mp3")
about_sound = pygame.mixer.Sound("about.wav")
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 60
ITEMS = ['plastic', 'glass', 'paper', 'organic', 'non_recyclable']
BIN_COLORS = {
    'plastic': (255, 0, 0),
    'organic': (0, 255, 0),
    'paper': (0, 0, 255),
    'glass': (255, 255, 0),
    'non_recyclable': (128, 128, 128),  
    'selected': (255, 255, 255)
}
BIN_LABELS = {
    'plastic': "Plastic",
    'organic': "Organic",
    'paper': "Paper",
    'glass': "Glass",
    'non_recyclable': "Non-Recyclable"  
}
BIN_IMAGES = {
    'plastic': "plastics.png",
    'organic': "organic.png",
    'paper': "papers.png",
    'glass': "glass.png",
    'non_recyclable': "non-recyclable.png"
}

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Eco Sorter")

background_image = pygame.image.load('welcome_page.jpg').convert()
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

bins = ['plastic', 'glass', 'paper', 'organic', 'non_recyclable'] 
bin_position = 0  
bin_width = 120  
left_margin = 40 
bin_spacing = (SCREEN_WIDTH - left_margin * 2) / len(bins)  
falling_item = random.choice(ITEMS)
item_position = [(bin_spacing - 50) / 2 + bin_spacing * bin_position + left_margin, 0]  
score = 0  
level = 1  

font = pygame.font.SysFont(None, 24) 

paused = False
item_falling = False
item_position_y = 0



def pick_random_image(image_list):
    return random.choice(image_list)


def create_item():
    global item_image, falling_item, item_falling, item_position_y
    item_image = None
    if environment == 1:
        if falling_item == 'plastic':
            image_list = ["blue.png", "cola.png", "plastic1.png"]
            selected_image = pick_random_image(image_list)
            item_image = pygame.image.load(selected_image).convert_alpha()
            item_position_y = 0 
            item_falling = True
        elif falling_item == 'organic':
            image_list = ["banana.png", "food.png", "pencil.png"]
            selected_image = pick_random_image(image_list)
            item_image = pygame.image.load(selected_image).convert_alpha()
            item_position_y = 0  
            item_falling = True
        elif falling_item == 'paper':
            image_list = ["paper.png", "origami.png", "kite.png"]
            selected_image = pick_random_image(image_list)
            item_image = pygame.image.load(selected_image).convert_alpha()
            item_position_y = 0  
            item_falling = True
        elif falling_item == 'glass':
            image_list = ["beaker.png", "flask.png"]
            selected_image = pick_random_image(image_list)
            item_image = pygame.image.load(selected_image).convert_alpha()
            item_position_y = 0  
            item_falling = True
        elif falling_item == 'non_recyclable':
            image_list = ["school-bag.png", "calculator.png", "microphone.png"]
            selected_image = pick_random_image(image_list)
            item_image = pygame.image.load(selected_image).convert_alpha()
            item_position_y = 0 
            item_falling = True
    elif environment == 2:
        if falling_item == 'plastic':
            image_list = ["bin.png", "bag.png", "garbage.png"]
            selected_image = pick_random_image(image_list)
            item_image = pygame.image.load(selected_image).convert_alpha()
            item_position_y = 0  
            item_falling = True
        elif falling_item == 'organic':
            image_list = ["stink.png", "acorn.png", "clothes.png"]
            selected_image = pick_random_image(image_list)
            item_image = pygame.image.load(selected_image).convert_alpha()
            item_position_y = 0  
            item_falling = True
        elif falling_item == 'paper':
            image_list = ["open-box.png", "origami.png", "kite.png"]
            selected_image = pick_random_image(image_list)
            item_image = pygame.image.load(selected_image).convert_alpha()
            item_position_y = 0 
            item_falling = True
        elif falling_item == 'glass':
            image_list = ["kvass.png", "broken-glass.png", "alcohol.png"]
            selected_image = pick_random_image(image_list)
            item_image = pygame.image.load(selected_image).convert_alpha()
            item_position_y = 0 
            item_falling = True
        elif falling_item == 'non_recyclable':
            image_list = ["beam.png", "calculator.png", "brake.png"]
            selected_image = pick_random_image(image_list)
            item_image = pygame.image.load(selected_image).convert_alpha()
            item_position_y = 0 
            item_falling = True
    elif environment ==3:
        if falling_item == 'plastic':
            image_list = ["candy.png", "chair.png", "plastic.png"]
            selected_image = pick_random_image(image_list)
            item_image = pygame.image.load(selected_image).convert_alpha()
            item_position_y = 0  
            item_falling = True
        elif falling_item == 'organic':
            image_list = ["wood.png", "apple.png", "pizza.png"]
            selected_image = pick_random_image(image_list)
            item_image = pygame.image.load(selected_image).convert_alpha()
            item_position_y = 0  
            item_falling = True
        elif falling_item == 'paper':
            image_list = ["book.png", "newspaper.png", "paper-fan.png"]
            selected_image = pick_random_image(image_list)
            item_image = pygame.image.load(selected_image).convert_alpha()
            item_position_y = 0  
            item_falling = True
        elif falling_item == 'glass':
            image_list = ["glasses.png", "broken-glass.png", "liquor.png"]
            selected_image = pick_random_image(image_list)
            item_image = pygame.image.load(selected_image).convert_alpha()
            item_position_y = 0  
            item_falling = True
        elif falling_item == 'non_recyclable':
            image_list = ["beam.png", "vase.png", ".png"]
            selected_image = pick_random_image(image_list)
            item_image = pygame.image.load(selected_image).convert_alpha()
            item_position_y = 0  
            item_falling = True
    
def draw_item():
    global item_image, item_position_y, item_falling
    if item_image and item_falling:        
        item_image = pygame.transform.scale(item_image, (50, 50))  
        item_rect = item_image.get_rect()
        item_rect.topleft = (item_position[0], item_position[1])  
        screen.blit(item_image, item_rect)
        item_position_y += 5  
        if item_position_y > SCREEN_HEIGHT:
            item_falling = False 



def draw_bins():
    for i, bin in enumerate(bins):
        bin_x = bin_spacing * i + left_margin  
        bin_rect = pygame.Rect(bin_x, SCREEN_HEIGHT - 50, bin_width, 50)
        pygame.draw.rect(screen, BIN_COLORS[bin], bin_rect)
        if i == bin_position:
            pygame.draw.rect(screen, BIN_COLORS['selected'], bin_rect, 5)  
        text = font.render(BIN_LABELS[bin], True, (255, 255, 255))
        text_rect = text.get_rect(center=(bin_x + bin_width / 2, SCREEN_HEIGHT - 30))
        screen.blit(text, text_rect)



def move_item():
    global paused
    if not paused:
        item_position[1] += 5  
        if item_position[1] >= SCREEN_HEIGHT - 50:
            check_sorting()
            reset_item()


congratulations_shown = False

def check_sorting():
    global score, congratulations_shown
    correct_bin = falling_item if falling_item in bins else None
    if bins[bin_position] == correct_bin:
        score += 1
        correct_sound.play() 
        print("Correct sorting! Score:", score)
        if score >= 50:
            win_sound.play() 
            show_level_completed_screen()
        elif score >= 30 and not congratulations_shown:
            win_sound.play() 
            show_congratulations_screen()
            congratulations_shown = True
    else:
        # score -= 1
        wrong_sound.play()  
        print("Incorrect sorting! Score:", score)

def reset_item():
    global falling_item, item_position
    falling_item = random.choice(ITEMS)
    item_position = [(bin_spacing - 50) / 2 + bin_spacing * bin_position + left_margin, 0] 


def draw_score():
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))


def draw_pause_button():
    if paused:
        pause_text = font.render("Play (_)", True, (255, 255, 255))
    else:
        pause_text = font.render("Pause (_)", True, (255, 255, 255))
    screen.blit(pause_text, (SCREEN_WIDTH - pause_text.get_width() - 10, 10))
    back_text = font.render("Back", True, (255, 255, 255))
    screen.blit(back_text, (SCREEN_WIDTH - back_text.get_width() - 10, 50)) 
    



def welcome_screen():
    welcome_sound.play()
    screen.blit(background_image, (0, 0))
    welcome_font = pygame.font.SysFont(None, 48)
    welcome_text = welcome_font.render("Welcome to Eco Sorter", True, (255, 255, 255))
    screen.blit(welcome_text, (SCREEN_WIDTH // 2 - welcome_text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
    play_text = font.render("Press SPACE to Play", True, (255, 255, 255))
    screen.blit(play_text, (SCREEN_WIDTH // 2 - play_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting = False
choose_sound_playing = False
about_sound_playing = False


def level_selection():
    stop_about_sound()
    stop_choose_sound()
    global running, choose_sound_playing
    start_choose_sound()
    screen.fill((0, 0, 0))
    title_font = pygame.font.SysFont(None, 48)
    title_text = title_font.render("Select Environment to clean", True, (255, 255, 255))
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 20))

    image_width, image_height = 200, 140  
    vertical_spacing = 20  
    label_font = pygame.font.SysFont(None, 20)

    environment1_image = pygame.image.load('environment1.jpg').convert()
    environment1_image = pygame.transform.scale(environment1_image, (image_width, image_height))

    environment2_image = pygame.image.load('environment2.jpg').convert()
    environment2_image = pygame.transform.scale(environment2_image, (image_width, image_height))

    environment3_image = pygame.image.load('environment3.jpg').convert()
    environment3_image = pygame.transform.scale(environment3_image, (image_width, image_height))

    y_positions = [
        80,  
        80 + image_height + vertical_spacing,
        80 + 2 * (image_height + vertical_spacing)
    ]

    environment_texts = ["School", "River", "Street"]
    for index, (image, y_pos) in enumerate(zip([environment1_image, environment2_image, environment3_image], y_positions)):
        x_pos = SCREEN_WIDTH // 2 - image_width // 2
        screen.blit(image, (x_pos, y_pos))
        pygame.draw.rect(screen, (255, 255, 255), (x_pos, y_pos, image_width, image_height), 2, border_radius=10)
        
        desc_text = font.render(environment_texts[index], True, (255, 255, 255))
        text_y = y_pos + image_height + 2  
        screen.blit(desc_text, (SCREEN_WIDTH // 2 - desc_text.get_width() // 2, text_y))

    about_text = font.render("About", True, (255, 255, 255))
    about_button_rect = about_text.get_rect()
    about_button_rect.bottomright = (SCREEN_WIDTH - 10, SCREEN_HEIGHT - 10)  
    screen.blit(about_text, about_button_rect) 

    pygame.display.flip()
    level_selected = False
    while not level_selected:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if about_button_rect.collidepoint(x, y):
                    about_page() 
                for i, (y_pos) in enumerate(y_positions):
                    x_pos = SCREEN_WIDTH // 2 - image_width // 2
                    if x_pos < x < x_pos + image_width and y_pos < y < y_pos + image_height:
                        level_selected = True
                        start_game(i + 1)

def about_page():
    stop_choose_sound()
    global about_sound_playing
    screen.fill((0, 0, 0))
    about_font = pygame.font.SysFont(None, 30)
    about_text = about_font.render("About Eco Sorter", True, (255, 255, 255))
    screen.blit(about_text, (SCREEN_WIDTH // 2 - about_text.get_width() // 2, 20))
    about_sound_playing = True 
    about_sound.play()  
   
    game_info = [
        "Eco Sorter is a game where you help clean different environments by sorting recyclable",
        "and non-recyclable items. Each environment presents a unique set of challenges and",
        "requires you to sort items quickly and correctly.",
        "",
        "Controls:",
        "- Use the left and right arrow keys to move between bins.",
        "- Use the down arrow key to drop the item into the bin below.",
        "- Press SPACE to pause the game.",
        "- Press ESC to return to the environment selection screen.",
        "",
        "Have fun playing and remember to recycle!",
    ]
    line_height = 20
    y = 70
    for line in game_info:
        text_render = font.render(line, True, (255, 255, 255))
        screen.blit(text_render, (50, y))
        y += line_height
    
    examples_text = font.render("Examples of items for each bin:", True, (255, 255, 255))
    screen.blit(examples_text, (50, y + 20))
    y += 40

    example_images = {
        'plastic': pygame.image.load("plastic.png").convert_alpha(),
        'organic': pygame.image.load("food.png").convert_alpha(),
        'paper': pygame.image.load("paper.png").convert_alpha(),
        'glass': pygame.image.load("beaker.png").convert_alpha(),
        'non_recyclable': pygame.image.load("calculator.png").convert_alpha()
    }
    example_image_size = (30, 30) 

 
    x_offset = 50
    for bin_name, example_image in example_images.items():
        bin_name_text = font.render(bin_name.capitalize(), True, (255, 255, 255))
        screen.blit(bin_name_text, (x_offset, y))
        
        small_example_image = pygame.transform.scale(example_image, example_image_size)
        screen.blit(small_example_image, (x_offset + 150, y))
        
        y += 50  
    
    back_text = font.render("Back", True, (255, 255, 255))
    screen.blit(back_text, (SCREEN_WIDTH - back_text.get_width() - 10, 10))  

    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if SCREEN_WIDTH - back_text.get_width() - 10 < x < SCREEN_WIDTH - 10 and 10 < y < 40:
                    waiting = False 
                    level_selection()  
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                waiting = False  
                level_selection()
    about_sound.stop()
def start_choose_sound():
    global choose_sound_playing
    choose_sound_playing = True
    choose_sound.play()

def stop_choose_sound():
    global choose_sound_playing
    choose_sound_playing = False
    choose_sound.stop()

def stop_about_sound():
    global about_sound_playing
    about_sound_playing = False
    about_sound.stop()


def start_game(environment_id):
    global level, environment
    level = environment_id
    environment = environment_id  
    print(f"Starting game in environment {environment_id}")
    reset_item() 



def toggle_pause():
    global paused
    paused = not paused




def show_congratulations_screen():
    global running  
    screen.fill((0, 0, 0))
    congrats_font = pygame.font.SysFont(None, 48)
    congrats_text = congrats_font.render("Congratulations!", True, (255, 255, 255))
    screen.blit(congrats_text, (SCREEN_WIDTH // 2 - congrats_text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
    restart_text = font.render("Press R to Restart", True, (255, 255, 255))
    screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit() 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  
                    subprocess.Popen(["python", "game.py"])  
                    pygame.quit()
                    exit()



def show_level_completed_screen():
    screen.fill((0, 0, 0))
    level_completed_font = pygame.font.SysFont(None, 48)
    level_completed_text = level_completed_font.render("Level 1 Completed!", True, (255, 255, 255))
    screen.blit(level_completed_text, (SCREEN_WIDTH // 2 - level_completed_text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

def start_level_2():
    global level, score
    level = 2
    score = 0  
    


level_selection()
running = True
while running:
    if choose_sound_playing and not pygame.mixer.get_busy():
        start_choose_sound()
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  
                level_selection() 
            if not paused:  
                if event.key == pygame.K_LEFT:
                    bin_position = max(0, bin_position - 1)
                    item_position[0] = (bin_spacing - 50) / 2 + bin_spacing * bin_position + left_margin 
                elif event.key == pygame.K_RIGHT:
                    bin_position = min(len(bins) - 1, bin_position + 1)
                    item_position[0] = (bin_spacing - 50) / 2 + bin_spacing * bin_position + left_margin 
            if event.key == pygame.K_SPACE:
                toggle_pause()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if SCREEN_WIDTH - 100 < pygame.mouse.get_pos()[0] < SCREEN_WIDTH and 0 < pygame.mouse.get_pos()[1] < 30:
                toggle_pause()
            elif SCREEN_WIDTH - 100 < pygame.mouse.get_pos()[0] < SCREEN_WIDTH and 50 < pygame.mouse.get_pos()[1] < 80:
                show_welcome_screen = False  
                level_selection()
    move_item()

    screen.fill((0, 0, 0))  
    draw_bins()
    if not item_falling:
            create_item()
    draw_item()
    draw_score() 
    draw_pause_button()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
