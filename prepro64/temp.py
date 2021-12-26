"""more about TEMP V.1"""

def change():
    """function change"""
    celsius = float(input())
    cel = "Celsius"
    fah = "Fahrenheit"
    kel = "Kelvin"
    ran = "Rankine"
    rea = "Reaumer"
    print("%-10s"%cel, "=", "%.4f"%celsius)
    print("%-10s"%fah, "=", "%.4f"%(((9/5)*celsius)+32))
    print("%-10s"%kel, "=", "%.4f"%(celsius+273.15))
    print("%-10s"%ran, "=", "%.4f"%((9/5)*(celsius+273.15)))
    print("%-10s"%rea, "=", "%.4f"%((4/5)*celsius))
change()
