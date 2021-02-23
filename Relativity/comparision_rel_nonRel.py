from vpython import *

c = 1

graph(ytitle='pos', xtitle='time')

pos_graph = gcurve(color=color.red, label='rel x')
non_pos_graph = gcurve(color=color.blue, label='non_rel x')

graph(ytitle='vel', xtitle='time')

vel_graph = gcurve(color=color.red, label='rel v_x')
non_vel_graph = gcurve(color=color.blue, label='non_rel v_x')

rel = sphere(radius=0.5, pos=vector(-5, 0, 0), color=color.red)
rel.momentum = vector(0, 0, 0)
rel.mass = 1.0

non_rel = sphere(radius=0.5, pos=vector(-5, 0, 0), color=color.blue)
non_rel.momentum = vector(0, 0, 0)
non_rel.mass = 1.0

dt = 0.01
time = 0

while (True):
	rate(60)
	force = vector(1, 0, 0)

	rel.momentum = rel.momentum + force * dt
	rel.rel_fac = 1 / sqrt(1 + (mag(rel.momentum) ** 2 / (rel.mass ** 2 * c ** 2)))
	rel.pos = rel.pos + rel.rel_fac * rel.momentum / rel.mass * dt

	pos_graph.plot(pos=(time, rel.pos.x))
	vel_graph.plot(pos=(time, (rel.momentum/rel.mass*rel.rel_fac).x))

	non_rel.momentum = non_rel.momentum + force * dt
	nonrel_fac = 1.0
	non_rel.pos = non_rel.pos + nonrel_fac * non_rel.momentum / non_rel.mass * dt

	non_pos_graph.plot(pos=(time, non_rel.pos.x))
	non_vel_graph.plot(pos=(time, (non_rel.momentum/non_rel.mass).x))

	time = time + dt