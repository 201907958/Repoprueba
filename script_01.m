# Gráfica de la función seno en el intervalo [0,2*pi]
x=0:0.01:2*pi;
y=sin(x);

# Cambiar el renderizador gráfico.
# El backend de OpenGL tiene conflictos con el sistema.
graphics_toolkit("gnuplot")
plot(x,y)
