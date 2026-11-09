import pygame
pygame.init()

wsc = 500
hsc = 500
judul = "<>-{PING/P0NG}-<>"
cbg = (255, 255, 255)
gRUN = True
gEND = False

p1 = "img1-removebg-preview.png"
p2 = "img2-removebg-preview.png"
b = "img3-removebg-preview.png"

scene = pygame.display.set_mode((wsc, hsc))
scene.fill(cbg)
pygame.display.set_caption(judul)
fps = pygame.time.Clock()

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, gambar, x, y, lebar, tinggi, kecepatan):
        super().__init__()
        self.lebar = lebar
        self.tinggi = tinggi
        self.gambar = pygame.transform.scale(
            pygame.image.load(gambar), (self.lebar, self.tinggi))
        self.kecepatan = kecepatan
        self.rect = self.gambar.get_rect()
        self.rect.x = x
        self.rect.y = y
    def tampil(self):
        scene.blit(self.gambar,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def p_kiri(self):
            tombol = pygame.key.get_pressed()
            if tombol[pygame.K_w] and self.rect.y>0: #keatas
                self.rect.y -= self.kecepatan
            elif tombol[pygame.K_s] and self.rect.y<hsc-self.tinggi: #kebawah
                self.rect.y += self.kecepatan

    def p_kanan(self):
            tombol = pygame.key.get_pressed()
            if tombol[pygame.K_UP] and self.rect.y>0: #keatas
                self.rect.y -= self.kecepatan
            elif tombol[pygame.K_DOWN] and self.rect.y<hsc-self.tinggi: #kebawah
                self.rect.y += self.kecepatan

p1 = Player(gambar=p1, x=10, y=10, lebar=90, tinggi=110, kecepatan=10)
p2 = Player(gambar=p2, x=400, y=10, lebar=90, tinggi=110, kecepatan=10)
b = GameSprite(gambar=b, x=200, y=200, lebar=50, tinggi=50, kecepatan=10)

while gRUN:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gRUN = False

    if gEND == False:
        scene.fill(cbg)
        p1.tampil()
        p2.tampil()
        b.tampil()
        p1.p_kiri()
        p2.p_kanan()

    fps.tick(60)
    pygame.display.update()