from rest_framework import serializers
from .models import Persona, Cliente


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ("id", "nombre", "peso", "estatura")

    def to_representation(self, instance):
        data = super().to_representation(instance)
        imc = instance.calcular_imc()
        data["imc"] = round(imc, 2)  # Redondea el IMC a 2 decimales
        data["categoria_imc"] = instance.calcular_categoria_imc()
        if imc < 18.5:
            data[
                "mensaje"
            ] = "IMC está por debajo del rango saludable. Consulte a un profesional médico."
        else:
            data["mensaje"] = "IMC dentro del rango saludable."
        return data


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"
