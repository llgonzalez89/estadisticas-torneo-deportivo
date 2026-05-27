import pandas as pd
import matplotlib.pyplot as plt

# Leer datos
df = pd.read_csv('datos/partidos.csv')

equipos = pd.concat([df['local'], df['visitante']]).unique()

victorias = {equipo: 0 for equipo in equipos}
puntos = {equipo: 0 for equipo in equipos}

goles_totales = 0

for _, fila in df.iterrows():
    local = fila['local']
    visitante = fila['visitante']
    gl = fila['goles_local']
    gv = fila['goles_visitante']

    goles_totales += gl + gv

    if gl > gv:
        victorias[local] += 1
        puntos[local] += 3

    elif gv > gl:
        victorias[visitante] += 1
        puntos[visitante] += 3

    else:
        puntos[local] += 1
        puntos[visitante] += 1

# Tabla de posiciones
tabla = pd.DataFrame({
    'Equipo': puntos.keys(),
    'Puntos': puntos.values(),
    'Victorias': [victorias[e] for e in puntos.keys()]
})

tabla = tabla.sort_values(by='Puntos', ascending=False)

print(tabla)

# Promedio de goles
promedio = goles_totales / len(df)

print("Promedio de goles:", promedio)

# Gráfico
tabla.plot(x='Equipo', y='Puntos', kind='bar')

plt.title('Rendimiento de Equipos')
plt.ylabel('Puntos')
plt.savefig('resultados/grafico.png')
plt.show()