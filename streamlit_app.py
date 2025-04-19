import streamlit as st

st.set_page_config(page_title="Diagnóstico de Diabetes", page_icon="🩺", layout="centered")

st.title("🩺 Sistema de Diagnóstico de Diabetes Tipo 2")
st.markdown("Este sistema estima el **riesgo de diabetes** basado en factores clínicos. No reemplaza la consulta médica.")

# Entradas del usuario
edad = st.number_input("Edad", min_value=0, max_value=120, step=1)
imc = st.number_input("IMC (Índice de Masa Corporal)", min_value=10.0, max_value=50.0, step=0.1)
glucosa = st.number_input("Glucosa en ayunas (mg/dL)", min_value=50, max_value=300)
presion = st.number_input("Presión arterial sistólica (mmHg)", min_value=80, max_value=200)
actividad = st.radio("¿Realiza actividad física regularmente?", ["Sí", "No"])
antecedentes = st.radio("¿Tiene antecedentes familiares de diabetes?", ["Sí", "No"])

<!--Start of Tawk.to Script-->
<script type="text/javascript">
var Tawk_API=Tawk_API||{}, Tawk_LoadStart=new Date();
(function(){
var s1=document.createElement("script"),s0=document.getElementsByTagName("script")[0];
s1.async=true;
s1.src='https://embed.tawk.to/6803d02e485a86191013bcde/1ip7eadrt';
s1.charset='UTF-8';
s1.setAttribute('crossorigin','*');
s0.parentNode.insertBefore(s1,s0);
})();
</script>
<!--End of Tawk.to Script-->


def diagnosticar_diabetes(edad, imc, glucosa, presion, actividad, antecedentes):
    riesgo = 0
    if edad > 45: riesgo += 1
    if imc > 30: riesgo += 1
    if glucosa > 126:
        riesgo += 2
    elif glucosa > 100:
        riesgo += 1
    if presion > 130: riesgo += 1
    if actividad == "No": riesgo += 1
    if antecedentes == "Sí": riesgo += 1

    if riesgo >= 5:
        return "Riesgo Alto", "🔴 Consulte con su médico urgentemente."
    elif riesgo >= 3:
        return "Riesgo Moderado", "🟠 Controle su glucosa y mejore sus hábitos."
    else:
        return "Riesgo Bajo", "🟢 Continúe con su estilo de vida saludable."

if st.button("Evaluar riesgo"):
    nivel, mensaje = diagnosticar_diabetes(edad, imc, glucosa, presion, actividad, antecedentes)
    st.subheader(f"Resultado: {nivel}")
    st.info(mensaje)

