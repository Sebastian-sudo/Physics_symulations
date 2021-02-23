from vpython import *

canvas(width=1750, height=850)

g = 9.8
dt = 0.01
time = 0

projectile = sphere(pos=vector(-5, 0, 0), radius=0.1, color=color.red, make_trail=True)

projectile.velocity = 1
projectile.speed = 7
projectile.mass = 5.0
projectile.angle = 79 * pi / 180

projectile.velocity = vector(projectile.speed * cos(projectile.angle), projectile.speed * sin(projectile.angle), 0)

while (projectile.pos.y >= 0):
	rate(30)

	gravity_force = vector(0, - projectile.mass * g, 0)
	force = gravity_force

	projectile.velocity = projectile.velocity + force / projectile.mass * dt

	projectile.pos = projectile.pos + projectile.velocity * dt

	time = time + dt