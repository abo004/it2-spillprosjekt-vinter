
# Create an empty list to store the x's
xes = []

# Set the timeout for the x's
timeout = 500 # in milliseconds


# Get the mouse position and create a new x at that position
pos = pygame.mouse.get_pos()
x = {"pos": pos, "time": pygame.time.get_ticks()}
xes.append(x)
radius = 10


    # Draw the xes
for x in xes:
    pygame.draw.line(screen, (255, 100, 0), (x["pos"][0]+0, x["pos"][1]-13), (x["pos"][0]+0, x["pos"][1]+13), 2)
    pygame.draw.line(screen, (255, 100, 0), (x["pos"][0]-13, x["pos"][1]+0), (x["pos"][0]+13, x["pos"][1]-0), 2)
    pygame.draw.line(screen, (255, 255, 0), (x["pos"][0]-11, x["pos"][1]-11), (x["pos"][0]+11, x["pos"][1]+11), 2)
    pygame.draw.line(screen, (255, 255, 0), (x["pos"][0]-11, x["pos"][1]+11), (x["pos"][0]+11, x["pos"][1]-11), 2)
    # Check if the x has reached its timeout
    if pygame.time.get_ticks() - x["time"] > timeout:
        xes.remove(x)
    # Draw the circle
    pygame.draw.circle(screen, (255, 0, 0), x["pos"], radius, 2)
        
    radius += 0.03

