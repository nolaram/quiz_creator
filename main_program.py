# import all libraries needed for the program
import pygame
import sys
import os
import csv

pygame.init()

# screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Quiz Creator')

# add colors
COLOR_BACKGROUND = pygame.Color("#1e1e1e")
COLOR_TEXT = pygame.Color("#ffffff")
COLOR_ACTIVE = pygame.Color("#00bfff")
COLOR_INACTIVE = pygame.Color("#3a3f55")
COLOR_CONFIRM = pygame.Color("lightgreen")

font = pygame.font.SysFont("comic sans ms", 28)
confirm_font = pygame.font.SysFont("comic sans ms", 32)
title_font = pygame.font.SysFont("arial", 50, bold=True)

time = pygame.time.Clock()

# inputs and labels
labels = [
    "Questions",
    "Option A",
    "Option B",
    "Option C",
    "Option D",
    "Correct Answer (a/b/c/d)"
]
inputs = [""] * len(labels)
current_label = 0

input_boxes = []
for input, label in enumerate(labels):
    rect = pygame.Rect(50, 50 + input * 60, 700, 40)
    input_boxes.append(rect)

active_box = current_label

csv_filename = 'quiz_output.csv' 

if not os.path.exists(csv_filename):
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['question', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_answer'])

# convert input into file
def main(data):
    with open(file_name, 'a') as file:
            # options
            # write the input in the file
            file.write(f'Question: {data[0]}\n')
            file.write(f'a) {data[1]}\n')
            file.write(f'b) {data[2]}\n')
            file.write(f'c) {data[3]}\n')
            file.write(f'd) {data[4]}\n')
            file.write(f'Correct Answer: {data[5].lower()}\n')
            file.write('-' * 40 + '\n')

state = "input"

# main loop
running = True
while running:
    screen.fill((COLOR_BACKGROUND))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if state == "input":
                if event.key == pygame.K_TAB:
                    active_box = (active_box + 1) % len(labels)
                elif event.key == pygame.K_RETURN:
                    if all(inputs) and inputs[5].lower() in ["a", "b", "c", "d"]:
                        main(inputs)
                        inputs = [""] * len(inputs)
                        state = 'confirm'
                    else:
                        print("Print all fields properly")
        
                elif event.key == pygame.K_BACKSPACE:
                    inputs[active_box] = inputs[active_box][:-1]
                else:
                    inputs[active_box] += event.unicode

            elif state == 'confirm':
                if event.key == pygame.K_y:
                    inputs = [""] * len(labels)
                    active_box = 0
                    state = "input"
                elif event.key == pygame.K_n:
                    running = False

    # add input fields and labels
    for input, box in enumerate(input_boxes):
        color = COLOR_ACTIVE if input == active_box else COLOR_INACTIVE
        pygame.draw.rect(screen, color, box, 0)
        pygame.draw.rect(screen, pygame.Color("white"), box, 2)

        full_text = f"{labels[input]}: {inputs[input]}"
        temp_font = font
        max_width = input_boxes[input].width - 10
        font_size = temp_font.get_height()
        
        while temp_font.size(full_text)[0] > max_width and temp_font.get_height() > 16:
            font_size -= 1
            temp_font = pygame.font.SysFont("comic sans ms", font_size)

        text_surface = temp_font.render(full_text, True, COLOR_TEXT)
        text_rect = text_surface.get_rect()
        screen.blit(text_surface, (box.x + 5, box.y + (box.height - text_rect.height) // 2))

    # confirmation program to ask for another question
    if state == "confirm":
        pygame.draw.rect(screen, COLOR_INACTIVE, (200, HEIGHT // 2 + 120, 400, 60), border_radius=10)
        confirm_text = confirm_font.render("Add another question? (Y/N)", True, COLOR_CONFIRM)
        confirm_rect = confirm_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 140))
        screen.blit(confirm_text, confirm_rect)

    # add title at the bottom
    title_text = title_font.render("Quiz Creator", True, COLOR_TEXT)
    title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT - 110))
    screen.blit(title_text, title_rect)


    pygame.display.flip()
    time.tick(30)

pygame.quit()
sys.exit()