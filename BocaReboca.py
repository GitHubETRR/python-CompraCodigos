import pygame

# Inicialización de Pygame
pygame.init()

# Configuración de la ventana
ventana = pygame.display.set_mode((820, 820))
pygame.display.set_caption("Se viene Boocaaaaaa")

# Carga de la imagen del escudo (Boca Juniors)
ball = pygame.image.load("BocaJuniors.png")

# Obtener el rectángulo del objeto para manejar su posición
ballrect = ball.get_rect()

# Velocidad con la que se moverá el escudo
speed = [6,6]

# Inicializar posición del escudo
ballrect.move_ip(0, 0)

# Bucle principal del juego
playing = True
while playing:
    # Procesar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    
    # Mover el escudo según la velocidad
    ballrect = ballrect.move(speed)

    # Verificar si el escudo toca los bordes de la ventana y cambiar dirección
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]  # Cambiar dirección horizontal
        
    if ballrect.top < 0 or ballrect.bottom > ventana.get_height():
        speed[1] = -speed[1]  # Cambiar dirección vertical
    
    # Llenar la ventana con un color (beige en este caso)
    ventana.fill((0, 0,0))

    # Dibujar el escudo en la nueva posición
    ventana.blit(ball, ballrect)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar los FPS (Frames per Second)
    pygame.time.Clock().tick(60)

# Salir de Pygame
pygame.quit()
