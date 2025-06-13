import tkinter as tk

class AvatarApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=650, height=900, bg="white")
        self.canvas.pack()

        # Tamaño del avatar y su posición inicial
        self.avatar_x, self.avatar_y = 200, 200
        self.avatar_size = 200  # Aumentando el tamaño
        self.eye_size = 50  # Tamaño del ojo
        #self.eye_size = 100
        self.obstacle_x, self.obstacle_y = 250, 300
        self.obstacle_size = 700
        self.obstacle_size = 200
        # Dibujar avatar (cuerpo) y su ojo
        self.avatar = self.canvas.create_oval(self.avatar_x, self.avatar_y,
                                              self.avatar_x + self.avatar_size, self.avatar_y + self.avatar_size,
                                              fill="blue")
        self.eye = self.canvas.create_oval(self.avatar_x + self.avatar_size // 3, self.avatar_y + self.avatar_size // 3,
                                           self.avatar_x + self.avatar_size // 3 + self.eye_size, self.avatar_y + self.avatar_size // 3 + self.eye_size,
                                           fill="white")

        # Dibujar obstáculo
        self.obstacle = self.canvas.create_rectangle(self.obstacle_x, self.obstacle_y,
                                                     self.obstacle_x + self.obstacle_size, self.obstacle_y + self.obstacle_size,
                                                     fill="red")

        # Vincular teclas para movimiento
        self.root.bind("<Up>", lambda event: self.move_avatar(0, -25))
        self.root.bind("<Down>", lambda event: self.move_avatar(0, 25))
        self.root.bind("<Left>", lambda event: self.move_avatar(-25, 0))
        self.root.bind("<Right>", lambda event: self.move_avatar(25, 0))

    def move_avatar(self, dx, dy):
        new_x = self.avatar_x + dx
        new_y = self.avatar_y + dy

        # Comprobar colisión con el obstáculo
        if self.check_collision(new_x, new_y):
            print("¡Choque detectado!")
            return

        # Comprobar si el avatar está dentro del lienzo
        if 0 <= new_x <= 440 and 0 <= new_y <= 440:
            self.avatar_x, self.avatar_y = new_x, new_y
            self.canvas.coords(self.avatar, self.avatar_x, self.avatar_y,
                               self.avatar_x + self.avatar_size, self.avatar_y + self.avatar_size)
            self.canvas.coords(self.eye, self.avatar_x + self.avatar_size // 3, self.avatar_y + self.avatar_size // 3,
                               self.avatar_x + self.avatar_size // 3 + self.eye_size, self.avatar_y + self.avatar_size // 3 + self.eye_size)

    def check_collision(self, x, y):
        return (self.obstacle_x < x < self.obstacle_x + self.obstacle_size and
                self.obstacle_y < y < self.obstacle_y + self.obstacle_size)

root = tk.Tk()
app = AvatarApp(root)
root.mainloop()
