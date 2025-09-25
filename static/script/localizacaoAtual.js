const inputEndereco = document.getElementById("endereco");
const sugestoesLista = document.getElementById("sugestoes-endereco");

// Lista de cidades permitidas (Curitiba e região metropolitana)
const cidadesPermitidas = [
  "Curitiba", "São José dos Pinhais", "Colombo", "Araucária", "Pinhais",
  "Campo Largo", "Almirante Tamandaré", "Fazenda Rio Grande", "Piraquara",
  "Campina Grande do Sul", "Campo Magro", "Quatro Barras", "Itaperuçu",
  "Balsa Nova", "Adrianópolis", "Mandirituba", "Tunas do Paraná", "Rio Branco do Sul", "Cerro Azul"
];

// Formata o endereço como: "Rua, Número, Bairro, Cidade"
function formatarEndereco(address) {
  const rua = address.road || "";
  const numero = address.house_number || "";
  const bairro = address.suburb || address.neighbourhood || "";
  const cidade = address.city || address.town || address.village || address.municipality || "";
  return [rua, numero, bairro, cidade].filter(Boolean).join(", ");
}

// Verifica se a cidade está na lista de cidades permitidas
function cidadeEhPermitida(address) {
  const cidade = address.city || address.town || address.village || address.municipality || "";
  return cidadesPermitidas.includes(cidade);
}

// Debounce: espera o usuário parar de digitar
let timeout = null;
inputEndereco.addEventListener("input", () => {
  clearTimeout(timeout);
  timeout = setTimeout(buscarSugestoes, 300);
});

// Busca sugestões
async function buscarSugestoes() {
  const query = inputEndereco.value.trim();

  if (query.length < 3) {
    sugestoesLista.innerHTML = "";
    return;
  }

  try {
    const url = `https://nominatim.openstreetmap.org/search?format=json&addressdetails=1&limit=10&q=${encodeURIComponent(query)}`;
    const response = await fetch(url);
    const resultados = await response.json();

    sugestoesLista.innerHTML = "";

    resultados.forEach(item => {
      const enderecoFormatado = formatarEndereco(item.address);

      if (!cidadeEhPermitida(item.address)) return; // Ignora se não for da região

      const li = document.createElement("li");
      li.textContent = enderecoFormatado;

      li.addEventListener("click", () => {
        inputEndereco.value = enderecoFormatado;
        sugestoesLista.innerHTML = "";

        localStorage.setItem("user_lat", item.lat);
        localStorage.setItem("user_lon", item.lon);
      });

      sugestoesLista.appendChild(li);
    });
  } catch (err) {
    console.error("Erro ao buscar sugestões:", err);
    sugestoesLista.innerHTML = "";
  }
}

// Botão de localização automática
async function obterLocalizacao() {
  if (!navigator.geolocation) {
    alert("Geolocalização não suportada.");
    return;
  }

  navigator.geolocation.getCurrentPosition(async (pos) => {
    const lat = pos.coords.latitude;
    const lon = pos.coords.longitude;

    try {
      const resp = await fetch(`https://nominatim.openstreetmap.org/reverse?lat=${lat}&lon=${lon}&format=json&addressdetails=1`);
      const data = await resp.json();

      if (!cidadeEhPermitida(data.address)) {
        alert("Localização fora de Curitiba ou região metropolitana.");
        return;
      }

      const enderecoFormatado = formatarEndereco(data.address);
      inputEndereco.value = enderecoFormatado;

      localStorage.setItem("user_lat", lat);
      localStorage.setItem("user_lon", lon);
    } catch (err) {
      console.error("Erro ao buscar endereço:", err);
      alert("Não foi possível identificar sua localização.");
    }
  }, () => {
    alert("Não foi possível acessar sua localização.");
  });
}

// Fecha a lista ao clicar fora
document.addEventListener("click", (e) => {
  if (!sugestoesLista.contains(e.target) && e.target !== inputEndereco) {
    sugestoesLista.innerHTML = "";
  }
});
