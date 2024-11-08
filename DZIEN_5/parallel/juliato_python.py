import subprocess

# Kod w języku Julia
julia_code = """
println("Hello from Julia!")
"""

# Zapisujemy kod do pliku tymczasowego
with open("temp.jl", "w") as f:
    f.write(julia_code)

# Uruchamiamy kod Julii za pomocą subprocess
result = subprocess.run(["julia", "temp.jl"], capture_output=True, text=True)

# Wyświetlamy wynik
print(result.stdout)

# Usuwamy plik tymczasowy (opcjonalne)
import os
os.remove("temp.jl")
