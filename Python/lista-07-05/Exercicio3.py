def fahrenheit(temp):
    temp_f = (temp * 1.8) + 32
    print(f"{temp:.2f}°C é equivalente a {temp_f:.2f}°F")

celcius = float(input("Digite a temperatura em °C para ser convertida: "))

fahrenheit(celcius)