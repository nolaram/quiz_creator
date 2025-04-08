# import all libraries needed for the program
import pygame
import sys

pygame.init()

# screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Quiz Creator')

font = pygame.font.SysFont(None, 32)
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

color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
active_box = current_label

file_name = 'quiz_questions.txt'

# convert input into file
def main(data):
    with open(file_name, 'a') as file:
        # options
        while True:
            # write the input in the file
            file.write(f'Question: {data[0]}\n')
            file.write(f'a) {data[1]}\n')
            file.write(f'b) {data[2]}\n')
            file.write(f'c) {data[3]}\n')
            file.write(f'd) {data[4]}\n')
            file.write(f'Correct Answer: {data[5].lower()}\n')
            file.write('-' * 40 + '\n')

# main loop
running = True
while running:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                active_box = (active_box + 1) % len(labels)
            elif event.key == pygame.K_RETURN:
                if all(inputs) and inputs[5].lower() in ["a", "b", "c", "d"]:
                    main(inputs)
                    inputs = [""] * len(inputs)
                    active_box = 0
                else:
                    print("Print all fields properly")
        
            elif event.key == pygame.K_BACKSPACE:
                inputs[active_box] = inputs[active_box][:-1]
            else:
                inputs[active_box] += event.unicode

    # add input fields and labels
    for input, box in enumerate(input_boxes):
        color = color_active if input == active_box else color_inactive
        pygame.draw.rect(screen, color, box, 2)
        text_surface = font.render(f"{labels[input]}: {inputs[input]}", True, pygame.Color("white"))
        screen.blit(text_surface, (box.x + 5, box.y + 5))

    pygame.display.flip()
    time.tick(30)

pygame.quit()
sys.exit()