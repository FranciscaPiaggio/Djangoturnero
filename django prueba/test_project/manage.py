#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(

        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


import sqlite3

def crear_base_datos():
    # Conectar a la base de datos (se creará si no existe)
    conn = sqlite3.connect('turnero.db')
    cursor = conn.cursor()

    # Crear una tabla para almacenar los turnos
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS turnos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha TEXT NOT NULL,
        hora TEXT NOT NULL,
        nombre_cliente TEXT NOT NULL
    )
    ''')

    # Confirmar los cambios y cerrar la conexión
    conn.commit()
    conn.close()

if __name__ == '__main__':
    crear_base_datos()
    print("Base de datos creada con éxito.")

    import sqlite3

def insertar_turno(fecha, hora, nombre_cliente):
    conn = sqlite3.connect('turnero.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO turnos (fecha, hora, nombre_cliente)
    VALUES (?, ?, ?)
    ''', (fecha, hora, nombre_cliente))

    conn.commit()
    conn.close()

if __name__ == '__main__':
    # Ejemplo de cómo insertar un turno
    insertar_turno('2024-08-06', '14:00', 'Juan Pérez')
    print("Turno insertado con éxito.")

import sqlite3

def consultar_turnos():
    conn = sqlite3.connect('turnero.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM turnos')
    turnos = cursor.fetchall()

    conn.close()
    return turnos

if __name__ == '__main__':
    turnos = consultar_turnos()
    for turno in turnos:
        print(turno)
