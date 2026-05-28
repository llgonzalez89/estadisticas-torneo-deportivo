import pandas as pd
import matplotlib.pyplot as plt

# Se utiliza un archivo CSV con los resultados de los partidos porque permite
# almacenar y manipular los datos de manera sencilla.
df = pd.read_csv("datos/partidos.csv")

# Diccionario para almacenar puntos
equipos = {}

# Ciclo for para recorrer partidos
for _, fila in df.iterrows():

    local = fila["local"]
    visitante = fila["visitante"]

    goles_local = fila["goles_local"]
    goles_visitante = fila["goles_visitante"]

    # Se inicializan los equipos al sumar puntos a claves que no existen
    # dentro del diccionario
    for equipo in [local, visitante]:

        if equipo not in equipos:
            equipos[equipo] = 0

    # Se asignan los puntos
    if goles_local > goles_visitante:

        equipos[local] += 3

    elif goles_visitante > goles_local:

        equipos[visitante] += 3

    else:

        equipos[local] += 1
        equipos[visitante] += 1

# Transformamos la tabla en un DataFrame para que la visualizacion y el análisis
# estadístico sea más sencillo.
tabla = pd.DataFrame(
    equipos.items(),
    columns=["Equipo", "Puntos"]
)

# Se utiliza el método sort values para ordenar los datos
# según valores controlando el órden.
tabla = tabla.sort_values(
    by="Puntos",
    ascending=False
)

# Mostrar tabla
print(tabla)

# Creamos el gráfico que permite comparar visualmente
# el rendimiento de cada equipo según los resultados.
plt.figure(figsize=(8,5))

plt.bar(
    tabla["Equipo"],
    tabla["Puntos"]
)

plt.title("Puntos por equipo")
plt.xlabel("Equipos")
plt.ylabel("Puntos")

# Guardar gráfico
plt.savefig("resultados/grafico.png")

print("Grafico generado correctamente.")