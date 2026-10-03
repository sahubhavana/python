result = df.groupby('species')['body_mass_g'].agg(['min', 'max'])

result['range'] = result['max'] - result['min']

result
