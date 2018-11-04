# Programa para calcular la altura de una pelita en movimiento vertical.
v_0 = 5			# Velocidad inicial en m/s.
g = 9.81		# Aceleración de la gravedad en m/s^2.
t = 0.6			# Tiempo en segundos.

y = v_0*t - 0.5*g*t**2	# Posición vertical.
print(y)
