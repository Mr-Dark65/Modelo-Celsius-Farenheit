const STATUS_TEXT = document.getElementById("status-text");
const STATUS = document.getElementById("status");
const RESULT = document.getElementById("result");
const OUTPUT = document.getElementById("fahrenheit-output");
const FORM = document.getElementById("predict-form");
const INPUT = document.getElementById("celsius-input");

const API_URL = "/api/predict/";

// Verificar que el servidor está listo
async function checkServer() {
  STATUS.classList.remove("error", "loaded");
  STATUS_TEXT.textContent = "Conectando con el servidor...";
  STATUS.classList.add("loaded");
  STATUS_TEXT.textContent = "Listo para predecir.";
}

async function predict(celsiusValue) {
  const response = await fetch(API_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ celsius: parseFloat(celsiusValue) }),
  });

  if (!response.ok) {
    throw new Error("Error en la respuesta del servidor");
  }

  const data = await response.json();
  
  if (!data.success) {
    throw new Error(data.error || "Error desconocido");
  }
  
  return data.fahrenheit;
}

FORM.addEventListener("submit", async (event) => {
  event.preventDefault();
  const value = INPUT.value;
  if (value === "" || isNaN(value)) {
    return;
  }
  
  try {
    STATUS.classList.remove("error");
    const prediction = await predict(value);
    OUTPUT.textContent = prediction.toFixed(2);
    RESULT.classList.remove("hidden");
  } catch (error) {
    console.error("Error durante la inferencia:", error);
    STATUS.classList.add("error");
    STATUS_TEXT.textContent = "Ocurrió un problema al ejecutar la predicción.";
  }
});

window.addEventListener("DOMContentLoaded", checkServer);


