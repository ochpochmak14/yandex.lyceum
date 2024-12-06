temp = input()
weather_type = input()
residue = input()

if residue == 'да':
    print(f"Сегодня {temp} градусов Цельсия, {weather_type}, осадки в виде дождя или снега.")
    
else:
    print(f"Сегодня {temp} градусов Цельсия, {weather_type}, солнечно.")