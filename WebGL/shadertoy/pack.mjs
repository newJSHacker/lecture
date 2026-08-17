/**
 * Pack .glsl files into embed.js so the gallery works from file://
 * Run: node pack.mjs
 */
import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const dir = path.dirname(fileURLToPath(import.meta.url));

const list = [
  { id: "fire", title: "Fire", warn: true, group: "effects" },
  { id: "campfire", title: "Campfire", warn: false, group: "effects" },
  { id: "lava", title: "Lava", warn: false, group: "effects" },
  { id: "smoke", title: "Smoke", warn: false, group: "effects" },
  { id: "steam", title: "Steam", warn: false, group: "effects" },
  { id: "sparks", title: "Sparks", warn: false, group: "effects" },
  { id: "waterfall", title: "Waterfall", warn: false, group: "effects" },
  { id: "water", title: "Water (pond)", warn: false, group: "effects" },
  { id: "ocean", title: "Ocean", warn: false, group: "effects" },
  { id: "river", title: "River", warn: false, group: "effects" },
  { id: "fountain", title: "Fountain", warn: false, group: "effects" },
  { id: "rain", title: "Rain", warn: false, group: "effects" },
  { id: "foam", title: "Shore foam", warn: false, group: "effects" },
  { id: "caustics", title: "Caustics", warn: false, group: "effects" },
  { id: "ripples", title: "Ripples (click)", warn: false, group: "effects" },
  { id: "underwater", title: "Underwater", warn: false, group: "effects" },
  { id: "clouds", title: "Clouds", warn: false, group: "effects" },
  { id: "mist", title: "Mist", warn: false, group: "effects" },
  { id: "snow", title: "Snow", warn: false, group: "effects" },
  { id: "aurora", title: "Aurora", warn: false, group: "effects" },
  { id: "lightning", title: "Lightning", warn: true, group: "effects" },
  { id: "plasma", title: "Plasma", warn: true, group: "effects" },

  { id: "seascape", title: "Seascape", warn: false, group: "popular" },
  { id: "star-nest", title: "Star nest", warn: false, group: "popular" },
  { id: "creation", title: "Creation (RGB rings)", warn: true, group: "popular" },
  { id: "fractal-pyramid", title: "Fractal pyramid", warn: false, group: "popular" },
  { id: "primitives", title: "SDF primitives", warn: false, group: "popular" },
  { id: "happy", title: "Happy jumper", warn: false, group: "popular" },
  { id: "mandelbulb", title: "Mandelbulb", warn: false, group: "popular" },
  { id: "mandelbrot", title: "Mandelbrot zoom", warn: false, group: "popular" },
  { id: "julia", title: "Julia set", warn: false, group: "popular" },
  { id: "menger", title: "Menger sponge", warn: false, group: "popular" },
  { id: "metaballs", title: "Metaballs", warn: false, group: "popular" },
  { id: "tunnel", title: "Tunnel", warn: false, group: "popular" },
  { id: "terrain", title: "Terrain", warn: false, group: "popular" },
  { id: "volume-clouds", title: "Volume clouds", warn: false, group: "popular" },
  { id: "voxels", title: "Voxels", warn: false, group: "popular" },
  { id: "warp", title: "Domain warp", warn: true, group: "popular" },
  { id: "heart", title: "Heart", warn: false, group: "popular" },
  { id: "neon", title: "Neon glow", warn: false, group: "popular" },
];

const shaders = {};
for (const s of list) {
  const p = path.join(dir, s.id + ".glsl");
  if (!fs.existsSync(p)) throw new Error("missing " + s.id + ".glsl");
  shaders[s.id] = fs.readFileSync(p, "utf8").replace(/\r\n/g, "\n");
}

const js =
  "window.SHADERTOY_LIST = " +
  JSON.stringify(list, null, 2) +
  ";\nwindow.SHADERTOY_SHADERS = " +
  JSON.stringify(shaders) +
  ";\n";

fs.writeFileSync(path.join(dir, "embed.js"), js);
console.log("packed", list.length, "shaders into embed.js");
