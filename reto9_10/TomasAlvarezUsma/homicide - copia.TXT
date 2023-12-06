# -*- coding: utf-8 -*-
"""

@author: tomas alvarez usma
1193130489
"""
import pandas as pd
import os

# Nombre del archivo CSV
csv_file = 'database.csv'

# Ruta completa al archivo CSV en la misma carpeta que el script
csv_path = os.path.join(os.path.dirname(__file__), csv_file)

# Carga los datos desde el archivo CSV
data = pd.read_csv(csv_path)

# A partir de aquí, puedes usar 'data' para realizar el análisis de datos.

# 1) Listar las cinco primeras ciudades con el mayor número de agencias
city_may = data.groupby('City')['Agency Name'].nunique().sort_values(ascending=False).head()
cities = list(city_may.index)
print(f'Las 5 ciudades con el mayor número de agencias son: {cities}')

# 2) Forma 1: De los tipos de agencia, determinar las de tipo Sheriff y mostrar el nombre
sheriff = data[data['Agency Type'] == 'Sheriff']['Agency Name'].unique()
df_sheriff = pd.DataFrame(sheriff, columns=['Agency Name'])
print(df_sheriff)

# 2) Forma 2: De los tipos de agencia, determinar las de tipo Sheriff y mostrar el nombre
df_sheriff = data[data['Agency Type'].str.contains('Sheriff')]['Agency Name'].unique()
print(df_sheriff)

# 3) Listar los estados más afectados por crímenes perpetrados por mujeres
perp_woman = data[data['Perpetrator Sex'] == 'Female']['State'].value_counts().head()
print(perp_woman)

# 4) Listar los estados más afectados por crímenes perpetrados por hombres
perp_male = data[data['Perpetrator Sex'] == 'Male']['State'].value_counts().head()
print(perp_male)

# 5) Determinar el número exacto del número de crímenes hechos por mujeres de raza Asian/Pacific Islander
perp_fem_asia = data[(data['Perpetrator Race'] == 'Asian/Pacific Islander') & (data['Perpetrator Sex'] == 'Female')]
T_perp_fem_asia = perp_fem_asia['Incident'].sum()
print(f'El número exacto de crímenes cometidos por mujeres de raza Asian/Pacific Islander es: {T_perp_fem_asia}')

# 6) Determinar la raza más criminal
race_counts = data['Perpetrator Race'].value_counts().head(1)
print(f'La raza más criminal es:\n{race_counts}')

# 7) Determinar el número exacto de hispanos que han asesinado mediante la estrangulación
num_hisp = data[(data['Victim Ethnicity'] == 'Hispanic') & (data['Weapon'] == 'Strangulation')]['Incident'].sum()
print(f'El número exacto de hispanos que han asesinado mediante la estrangulación es: {num_hisp}')

# 8) Determinar el tipo de relación más peligrosa, el cual comete más homicidios con armas de tipo Shotgun
rel_pel = data[data['Weapon'] == 'Shotgun']['Relationship'].value_counts().head(1)
print(f'El tipo de relación más peligrosa que comete más homicidios con armas de tipo Shotgun es:\n{rel_pel}')

# 9) Cuál es el sexo que más homicidios ha cometido con Veneno= Poison
sex_ven = data[data['Weapon'] == 'Poison']['Perpetrator Sex'].value_counts().head(1)
print(f'El sexo que más homicidios ha cometido con veneno es:\n{sex_ven}')

# 10) Cuántos asesinos de raza negra atrapó el FBI
ase_black = data[data['Perpetrator Race'] == 'Black']['Record Source'].value_counts().head(1)
print(f'El número de asesinos de raza negra atrapados por el FBI es:\n{ase_black}')

# 11) Cuántas víctimas de tipo hispanas han muerto y por qué tipo de medio (arma blanca, arma de fuego, etc)
hisp_victims = data[data['Victim Ethnicity'] == 'Hispanic']['Weapon'].value_counts().sum()
print(f'El número de víctimas de tipo hispanas que han muerto y el tipo de medio utilizado es:\n{hisp_victims}')

# 12) Cuál ha sido el asesino más viejo
data['Perpetrator Age'] = pd.to_numeric(data['Perpetrator Age'], errors='coerce')
oldest_perpetrator = data[data['Perpetrator Age'].notnull()]['Perpetrator Age'].idxmax()
oldest_age = data.loc[oldest_perpetrator, 'Perpetrator Age']
print(f'El asesino más viejo tenía {oldest_age} años.')

# 13) Cuál ha sido el asesino más joven
youngest_perpetrator = data[data['Perpetrator Age'].notnull()]['Perpetrator Age'].idxmin()
youngest_age = data.loc[youngest_perpetrator, 'Perpetrator Age']
print(f'El asesino más joven tenía {youngest_age} años.')

# 14) Cuál es el total de homicidios desde el año 1995 hasta el año 2000
total_homicides_95_to_00 = data[(data['Year'] >= 1995) & (data['Year'] <= 2000)]['Incident'].sum()
print(f'El total de homicidios desde 1995 hasta 2000 es: {total_homicides_95_to_00}')

# 15) Cuál es el total de homicidios desde el año 1995 hasta el año 2000 perpetrados por hombres de raza negra por sofocación
total_homicides_95_to_00_black_suffocation = data[(data['Year'] >= 1995) & (data['Year'] <= 2000) & (data['Perpetrator Race'] == 'Black') & (data['Weapon'] == 'Suffocation')]['Incident'].sum()
print(f'El total de homicidios desde 1995 hasta 2000 perpetrados por hombres de raza negra por sofocación es: {total_homicides_95_to_00_black_suffocation}')

# 16) Determinar los homicidios anteriores a 1980 perpetrados por hombres del estado de Alaska de raza negra
bef_80 = data[(data['Year'] < 1980) & (data['Perpetrator Race'] == 'Black') & (data['Perpetrator Sex'] == 'Male') & (data['State'] == 'Alaska')]
print(f'Los homicidios anteriores a 1980 perpetrados por hombres de raza negra en el estado de Alaska son:\n{bef_80}')

# 17) Determinar los homicidios de la policía municipal de la ciudad de Nueva York del cual hayan sido por relaciones de tipo Ex-Wife y además que su arma haya sido la estrangulación
ny_homicides = data[(data['City'] == 'New York') & (data['Agency Type'] == 'Municipal Police') & (data['Relationship'] == 'Ex-Wife') & (data['Weapon'] == 'Strangulation')]
print(f'Los homicidios de la policía municipal de la ciudad de Nueva York por relaciones de tipo Ex-Wife y con arma de estrangulación son:\n{ny_homicides}')

# 18) Listar todos los homicidios que hayan ocurrido desde 1980 hasta 1970 en el estado de Illinois del cual el grupo étnico de la víctima no es hispano y la relación con el asesino fue de amigos y el arma utilizada fue una escopeta
illinois_homicides = data[(data['Year'] >= 1970) & (data['Year'] <= 1980) & (data['State'] == 'Illinois') & (data['Victim Ethnicity'] != 'Hispanic') & (data['Weapon'] == 'Shotgun') & (data['Relationship'] == 'Friend')]
print(f'Los homicidios en el estado de Illinois entre 1970 y 1980 que cumplen con los criterios son:\n{illinois_homicides}')
