# This is my first attempt at John Conway's "Game of Life" using Pygame
# For this first try I will just follow along Auctux tutorial on YouTube

import pygame
import os
import grid

os.environ["SDL_VIDEO_CENTERED"]='1'

width, height = 800, 600
size = (width, height)

pygame.init()
pygame.display.set_caption("Conway's Game of Life")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

black = (0, 0, 0)
blue = (0, 14, 71)
white = (255, 255, 255)

scaler = 20
offset = 1

Grid = grid.Grid(width, height, scaler, offset)
Grid.random2d_array()

run = True

while run:
  clock.tick(fps)
  screen.fill(black)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  Grid.Conway(off_color = white, on_color = blue, surface = screen)

  pygame.display.update()

pygame.quit()