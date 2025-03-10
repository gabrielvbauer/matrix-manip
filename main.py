import pygame
from mathh.entities.point_2d import Point2D
from mathh.operations.utils import calc_center

CELL_SIZE = 50   # Size of each cell in pixels
MARGIN = 5       # Space between cells
WINDOW_COLOR = (3, 3, 3)  # Background color of the window (dark)

COLOR_MAP = {
    "green": (0, 255, 0),
    "black": (10, 10, 10)
}

def create_matrix():
    while True:
        try:
            rows = int(input("Enter the number of rows (maximum 10): "))
            columns = int(input("Enter the number of columns (maximum 10): "))
            if 1 <= rows <= 10 and 1 <= columns <= 10:
                break
            else:
                print("Invalid values. Please try again with numbers between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter integers.")

    matrix = [[None for _ in range(columns)] for _ in range(rows)]
    matrix[0][0] = "green"
    return matrix

def draw_matrix(screen, matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    
    screen.fill(WINDOW_COLOR)
    
    for i in range(rows):
        for j in range(columns):
            # Calculate the top-left corner position of the cell
            x = MARGIN + j * (CELL_SIZE + MARGIN)
            y = MARGIN + i * (CELL_SIZE + MARGIN)
            cell_rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            
            # Draw the cell rectangle (can be a background color to distinguish it)
            pygame.draw.rect(screen, (34, 34, 34), cell_rect)
            
            # Calculate the center of the cell using the custom library function
            center = calc_center(point=Point2D(x, y), width=CELL_SIZE, height=CELL_SIZE)
            radius = CELL_SIZE // 2 - 5  # Define the radius of the circle
            
            if matrix[i][j] is not None:
                # If there is a figure, fill the circle with the defined color
                color = COLOR_MAP.get(matrix[i][j], (255, 255, 255))
                pygame.draw.circle(screen, color, center, radius)
            else:
                # If empty, draw only the outline of the circle (in a light tone)
                pygame.draw.circle(screen, (100, 100, 100), center, radius, 2)
    
    pygame.display.flip()

def change_position(matrix, point: Point2D, color):
    rows = len(matrix)
    columns = len(matrix[0])
    
    x, y = point.x, point.y
    
    if 0 <= x < rows and 0 <= y < columns:
        if matrix[x][y] == "green":
            matrix[x][y] = None;
        else:
            matrix[x][y] = color
    else:
        print("Coordinates out of bounds!")
    return matrix

def main():
    pygame.init()
    
    matrix = create_matrix()
    rows = len(matrix)
    columns = len(matrix[0])
    
    screen_width = columns * (CELL_SIZE + MARGIN) + MARGIN
    screen_height = rows * (CELL_SIZE + MARGIN) + MARGIN
    screen = pygame.display.set_mode((screen_width, screen_height))
    
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                col = (mouse_x - MARGIN) // (CELL_SIZE + MARGIN)
                row = (mouse_y - MARGIN) // (CELL_SIZE + MARGIN)
                
                if 0 <= row < rows and 0 <= col < columns:
                    change_position(matrix, Point2D(row, col), 'green')

        # Draw the matrix on the screen
        draw_matrix(screen, matrix)

    pygame.quit()

if __name__ == "__main__":
    main()
