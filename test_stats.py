#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script de prueba para verificar la lógica de cálculo de stats
"""

def calculate_stats(lines):
    """
    Calcula stats con progresión cíclica [80, 40, 30]:
    
    Progresión de umbrales:
    - Stat 1: 80 líneas (+80)
    - Stat 2: 120 líneas (+40)
    - Stat 3: 150 líneas (+30)
    - Stat 4: 230 líneas (+80) ← Ciclo reinicia
    - Stat 5: 270 líneas (+40)
    - Stat 6: 300 líneas (+30)
    - Stat 7: 380 líneas (+80)
    - Stat 8: 420 líneas (+40)
    - Stat 9: 450 líneas (+30)
    """
    if lines < 80:
        return 0
    
    # Thresholds acumulativos de cada stat con ciclo [80, 40, 30]
    thresholds = []
    current = 0
    increments = [80, 40, 30]  # Ciclo de incrementos
    
    # Generar suficientes thresholds para cubrir hasta líneas muy altas
    for i in range(100):  # Generar hasta 100 stats
        current += increments[i % 3]
        thresholds.append(current)
    
    # Contar cuántos thresholds se alcanzan
    stats = 0
    for threshold in thresholds:
        if lines >= threshold:
            stats += 1
        else:
            break
    
    return stats

# Pruebas
test_cases = [
    (50, 0),
    (80, 1),
    (120, 2),
    (150, 3),
    (230, 4),
    (270, 5),
    (300, 6),
    (380, 7),
    (420, 8),
    (450, 9),
]

print("Tabla de Progresión de Stats")
print("=" * 40)
print(f"{'Líneas':<15} {'Stats Esperados':<15} {'Stats Obtenidos':<15} {'Estado':<10}")
print("-" * 40)

for lines, expected in test_cases:
    result = calculate_stats(lines)
    status = "✓" if result == expected else "✗"
    print(f"{lines:<15} {expected:<15} {result:<15} {status:<10}")

print("\nPrueba adicional con valores arbitrarios:")
print("=" * 40)
for lines in [1, 25, 79, 80, 120, 150, 230, 270, 300, 380, 420, 450, 530, 570, 600]:
    stats = calculate_stats(lines)
    print(f"Líneas: {lines:>4} → Stats: {stats}")
