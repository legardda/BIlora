# archivo: main.py
from flask import Flask, request, jsonify
import hashlib
import datetime
import re
import os
from typing import Tuple

app = Flask(__name__)
CLAVE_SECRETA = os.environ.get('LICENSE_SECRET', 'BILORA2025')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

def generar_codigo(email: str, mes: int, año: int) -> str:
    """
    Genera un código de licencia único usando SHA-256
    
    Args:
        email: Correo del usuario
        mes: Mes actual (1-12)
        año: Año actual (4 dígitos)
    
    Returns:
        Código de licencia de 10 caracteres en mayúsculas
    """
    base = f"{email.strip().lower()}-{mes}-{año}-{CLAVE_SECRETA}"
    return hashlib.sha256(base.encode()).hexdigest()[:10].upper()

def validar_email(email: str) -> Tuple[bool, str]:
    """Valida el formato del email y devuelve (resultado, mensaje)"""
    if not email:
        return False, "Email requerido"
    if not EMAIL_REGEX.match(email):
        return False, "Formato de email inválido"
    return True, ""

@app.route("/licencia", methods=["POST"])
def generar_licencia():
    """
    Endpoint para generación de licencias
    ---
    parameters:
      - name: email
        in: formData
        type: string
        required: true
    responses:
      200:
        description: Código de licencia generado
      400:
        description: Error en los parámetros
      500:
        description: Error interno del servidor
    """
    try:
        email = request.form.get("email", "").strip()
        
        # Validar email
        es_valido, mensaje = validar_email(email)
        if not es_valido:
            return jsonify(error=mensaje), 400
        
        # Generar código
        hoy = datetime.date.today()
        codigo = generar_codigo(email, hoy.month, hoy.year)
        
        return jsonify(
            licencia=codigo,
            email=email,
            expiracion=hoy.replace(day=1) + datetime.timedelta(days=32)  # Próximo mes
        ), 200
    
    except Exception as e:
        app.logger.error(f"Error generando licencia: {str(e)}")
        return jsonify(error="Error interno del servidor"), 500

@app.route("/health", methods=["GET"])
def health_check():
    """Endpoint de verificación de estado del servicio"""
    return jsonify(
        status="OK",
        version="1.0",
        server_time=datetime.datetime.utcnow().isoformat()
    ), 200

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8080,
        debug=False  # Siempre False en producción!
    )