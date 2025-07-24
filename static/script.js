function mudarCor() {
    const cores = ["#fefefe", "#f9f9ff", "#e0f7fa", "#fff8e1", "#f3e5f5"];
    const corAleatoria = cores[Math.floor(Math.random() * cores.length)];
    document.body.style.backgroundColor = corAleatoria;
}
