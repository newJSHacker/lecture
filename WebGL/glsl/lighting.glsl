// GLSL ES 3.00 — copy into a fragment shader. See WebGL/12 Lighting.md
const float PI = 3.14159265;

float D_GGX(float NoH, float a) {
  float a2 = a * a;
  float d = NoH * NoH * (a2 - 1.0) + 1.0;
  return a2 / (PI * d * d);
}

float G_Smith(float NoV, float NoL, float r) {
  float k = (r + 1.0) * (r + 1.0) / 8.0;
  float gv = NoV / (NoV * (1.0 - k) + k);
  float gl = NoL / (NoL * (1.0 - k) + k);
  return gv * gl;
}

vec3 F_Schlick(float VoH, vec3 F0) {
  return F0 + (1.0 - F0) * pow(1.0 - VoH, 5.0);
}

vec3 blinnPhong(vec3 albedo, vec3 N, vec3 V, vec3 L, vec3 lightColor, float shininess) {
  vec3 H = normalize(L + V);
  float nd = max(dot(N, L), 0.0);
  float spec = pow(max(dot(N, H), 0.0), shininess) * step(0.0, nd);
  return albedo * (0.12 + 0.88 * nd) * lightColor + lightColor * spec * 0.5;
}

vec3 pbrDirect(vec3 albedo, float metallic, float roughness, vec3 N, vec3 V, vec3 L, vec3 lightColor) {
  float a = max(roughness * roughness, 0.002);
  vec3 H = normalize(V + L);
  float NoV = max(dot(N, V), 1e-4);
  float NoL = max(dot(N, L), 0.0);
  float NoH = max(dot(N, H), 0.0);
  float VoH = max(dot(V, H), 0.0);
  vec3 F0 = mix(vec3(0.04), albedo, metallic);
  vec3 F = F_Schlick(VoH, F0);
  vec3 spec = (D_GGX(NoH, a) * G_Smith(NoV, NoL, roughness) * F) / max(4.0 * NoV * NoL, 1e-4);
  vec3 kD = (1.0 - F) * (1.0 - metallic);
  return (kD * albedo / PI + spec) * lightColor * NoL;
}
