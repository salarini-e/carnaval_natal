const canvas = document.querySelector(".neve");
const ctx = canvas.getContext("2d");

let flocosDeNeve = [];

function draw_floco(floco) {
  ctx.beginPath();
  ctx.arc(floco.x, floco.y, floco.r, 0, Math.PI * 2);
  ctx.fillStyle = "#fff";
  ctx.fill();
}

function animacao() {
  requestAnimationFrame(animacao);

  ctx.clearRect(0, 0, canvas.width, canvas.height);
  for (let floco of flocosDeNeve) {
    draw_floco(floco);

    floco.y += floco.r / 2;
    floco.x += Math.sin(floco.i);
    floco.i += Math.random() * Math.random() * 0.1;

    if (floco.y > canvas.height) {
      floco.y = 0;
      floco.x = Math.random() * canvas.width;
    }
  }
}

window.addEventListener("resize", () => resize_canvas(canvas));

function resize_canvas(canvas) {
  canvas.height = document.documentElement.scrollHeight;
  canvas.width = window.innerWidth;
}

  resize_canvas(canvas);
  flocosDeNeve = [];
  for (let i = 0; i < canvas.width / 6; i++) {
    flocosDeNeve.push({
      x: Math.random() * canvas.width,
      y: Math.random() * canvas.height,
      i: Math.random() * Math.PI * 2,
      r: Math.random() + 1.6,
    });
  }
  animacao();
