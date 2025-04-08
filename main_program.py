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
for i, label in enumerate(labels):
    rect = pygame.Rect(50, 50 + i * 60, 700, 40)
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
        if event.type == pygame.QUIT():
            running == False

pygame.quit()
sys.exit()