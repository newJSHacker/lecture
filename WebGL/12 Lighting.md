# 12 — Lighting snippets

Parent: [[07 WebGL and Shader Snippets]]

Assume `N`, `V`, `L` are **normalized**. `N` world or view, as long as they match. `L` points **toward the light**. `H = normalize(L + V)`.

## Lambert (diffuse)

```glsl
float ndotl = max(dot(N, L), 0.0);
vec3 color = albedo * (u_ambient + u_lightColor * ndotl);
```

Hemisphere ambient (cheap sky/ground):

```glsl
vec3 hemi = mix(u_ground, u_sky, N.y * 0.5 + 0.5);
vec3 color = albedo * hemi + albedo * u_lightColor * ndotl;
```

## Phong specular

```glsl
vec3 R = reflect(-L, N);
float spec = pow(max(dot(R, V), 0.0), u_shininess);
vec3 color = albedo * ndotl * u_lightColor + u_specColor * spec * u_lightColor;
```

`u_shininess` 8–128. Phong blows out if you add spec without `ndotl` gating; multiply spec by `step(0.0, ndotl)` so the back face is dark.

## Blinn-Phong (preferred in class)

```glsl
vec3 H = normalize(L + V);
float spec = pow(max(dot(N, H), 0.0), u_shininess);
```

Same energy caveats. Demo: `06-phong-cube.html`.

## Attenuation (point light)

```glsl
float d = length(lightPos - worldPos);
vec3 L = (lightPos - worldPos) / max(d, 1e-5);
float att = 1.0 / (u_c + u_l * d + u_q * d * d);
```

Start with `c=1, l=0, q=0.1` or a smooth window:

```glsl
float att = clamp(1.0 - d / u_radius, 0.0, 1.0);
att *= att;
```

## Toon / ramp

```glsl
float d = max(dot(N, L), 0.0);
float bands = 4.0;
float toon = floor(d * bands) / bands;
vec3 color = albedo * mix(u_ambient, u_lightColor, toon);
```

Add a specular tick:

```glsl
float spec = step(0.92, pow(max(dot(N, H), 0.0), 32.0));
```

Demo: `12-toon-fresnel.html`.

## Fresnel (Schlick)

```glsl
vec3 F0 = vec3(0.04); // dielectric
vec3 F = F0 + (1.0 - F0) * pow(1.0 - max(dot(N, V), 0.0), 5.0);
```

Rim / shell:

```glsl
float rim = pow(1.0 - max(dot(N, V), 0.0), u_rimPow);
vec3 color += u_rimColor * rim;
```

## Matcap (view-space normal)

```glsl
vec3 vn = normalize(mat3(u_view) * N);
vec2 uv = vn.xy * 0.5 + 0.5;
vec3 color = texture(u_matcap, uv).rgb;
```

Demo: `24-matcap.html`. Generate a matcap as a procedural sphere lighting if you have no file.

## Normal mapping (tangent space, TBN in fragment)

Vertex: pass `v_T, v_B, v_N` (orthonormalize). Fragment:

```glsl
vec3 nTex = texture(u_normalMap, v_uv).xyz * 2.0 - 1.0;
nTex.xy *= u_normalScale;
vec3 N = normalize(mat3(normalize(v_T), normalize(v_B), normalize(v_N)) * nTex);
```

If you only have a normal map and UV derivatives:

```glsl
vec3 nTex = texture(u_normalMap, v_uv).xyz * 2.0 - 1.0;
vec3 dp1 = dFdx(v_worldPos);
vec3 dp2 = dFdy(v_worldPos);
vec2 du1 = dFdx(v_uv);
vec2 du2 = dFdy(v_uv);
vec3 T = normalize(dp1 * du2.y - dp2 * du1.y);
vec3 B = normalize(-dp1 * du2.x + dp2 * du1.x);
vec3 N = normalize(mat3(T, B, normalize(v_worldN)) * nTex);
```

## Cook–Torrance PBR (direct light, teaching form)

```glsl
const float PI = 3.14159265;

float D_GGX(float NoH, float a) {
  float a2 = a * a;
  float d = NoH * NoH * (a2 - 1.0) + 1.0;
  return a2 / (PI * d * d);
}

float G_Smith(float NoV, float NoL, float a) {
  float k = (a + 1.0) * (a + 1.0) / 8.0;
  float gv = NoV / (NoV * (1.0 - k) + k);
  float gl = NoL / (NoL * (1.0 - k) + k);
  return gv * gl;
}

vec3 F_Schlick(float VoH, vec3 F0) {
  return F0 + (1.0 - F0) * pow(1.0 - VoH, 5.0);
}

vec3 pbr(vec3 albedo, float metallic, float roughness, vec3 N, vec3 V, vec3 L, vec3 lightColor) {
  float a = max(roughness * roughness, 0.002);
  vec3 H = normalize(V + L);
  float NoV = max(dot(N, V), 1e-4);
  float NoL = max(dot(N, L), 0.0);
  float NoH = max(dot(N, H), 0.0);
  float VoH = max(dot(V, H), 0.0);
  vec3 F0 = mix(vec3(0.04), albedo, metallic);
  vec3 F = F_Schlick(VoH, F0);
  float D = D_GGX(NoH, a);
  float G = G_Smith(NoV, NoL, roughness);
  vec3 spec = (D * G * F) / max(4.0 * NoV * NoL, 1e-4);
  vec3 kD = (1.0 - F) * (1.0 - metallic);
  vec3 diffuse = kD * albedo / PI;
  return (diffuse + spec) * lightColor * NoL;
}
```

Demo: `16-pbr-direct.html`. This is **one punctual light**. IBL is a later week.

## Image-based ambient (fake)

```glsl
vec3 ibl = mix(u_ground, u_sky, N.y * 0.5 + 0.5);
vec3 F = F0 + (1.0 - F0) * pow(1.0 - NoV, 5.0);
vec3 ambient = ibl * albedo * (1.0 - metallic) + ibl * F * (1.0 - roughness);
```

Not energy-conserving. Good enough to kill flat black creases.

## Fog

```glsl
float z = length(v_viewPos);
float fog = clamp((u_fogFar - z) / (u_fogFar - u_fogNear), 0.0, 1.0);
color = mix(u_fogColor, color, fog);
```

Height fog:

```glsl
float h = smoothstep(u_fogY0, u_fogY1, v_worldPos.y);
color = mix(color, u_fogColor, (1.0 - fog) * (1.0 - h));
```
