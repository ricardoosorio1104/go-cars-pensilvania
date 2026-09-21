# GO CARS Pensilvania — Sitio web

Sitio web oficial de **GO CARS Pensilvania** (buggy tours por las rutas de montaña de Pensilvania, Caldas).
Aplica el manual de identidad de marca (versión 2026): colores `#F5600B` / `#14442E` / `#5C3A21` / `#F4EEE3` / `#1E2327`, tipografías **Oswald** (títulos), **Poppins** (texto) y **Caveat** (taglines), logo oficial en base64.

## Cómo abrirlo

- **Doble clic** en `index.html` (o clic derecho → Abrir con el navegador).
- **Recomendado para probarlo bien:** abre una terminal en esta carpeta y ejecuta:

  ```
  python servir.py
  ```

  y visita **http://127.0.0.1:8099**

  > ⚠️ Usa `servir.py`, **no** `python -m http.server`. Los videos del sitio **avanzan con el scroll** (no se reproducen solos), y eso exige que el servidor soporte peticiones **Range (206)**. El `http.server` normal no las soporta, y con él los videos grandes se quedan congelados al desplazarse. (En Netlify o cualquier hosting real el soporte de rangos ya viene incluido.)

## Cómo publicarlo (gratis, 3 minutos)

**Netlify Drop:** entra a `app.netlify.com/drop` y arrastra **toda esta carpeta** (incluye los archivos `_redirects` y `_headers`, que son obligatorios: el primero hace el puente `/api/exec` hacia el backend de reservas y el segundo evita que el catálogo se sirva con una versión vieja). Te da un enlace `https://algo.netlify.app` para compartir por WhatsApp, TikTok y Facebook.

> 🔁 Si el catálogo o el sitio ya estaban publicados, al volver a arrastrar la carpeta Netlify publica la versión nueva y (con `_headers`) los visitantes la ven de inmediato, sin caché vieja.

Después puedes conectar un dominio propio (por ejemplo `gocarspensilvania.com`).

## Estructura

```
sitio-web/
├── index.html              ← el sitio (todo el código, diseño y datos)
├── catalogo.html           ← catálogo digital (se muestra embebido y se abre en pestaña aparte)
├── servir.py               ← servidor local con soporte Range (para previsualizar los videos)
├── README.md               ← este archivo
└── assets/
    ├── videos/             ← 3 clips de la ruta a la vereda La Cabaña (vertical 720x1280, sin audio)
    ├── img/                ← fotos, mapas de ruta y logo
    └── fonts/              ← Oswald, Poppins, Caveat (locales: el sitio no depende de Google Fonts)
```

## Qué contiene el sitio

| Sección | Contenido |
|---|---|
| Hero | Video de fondo **que no se reproduce solo**: avanza fotograma por fotograma según bajas (scroll). Logo, `go cars`, tagline y CTAs a WhatsApp |
| La experiencia | Descripción + 4 características de marca (cars 212 cc 4T, casco+seguro, 9 rutas, paradas con sabor) |
| El camino, en movimiento | **3 videos verticales que se mueven con el scroll**: el carril se desplaza, cada clip avanza con tu desplazamiento, fundidos y capítulos 01/02/03. Ningún video se reproduce por su cuenta |
| Rutas | Las 9 rutas con mapa satelital; al tocar una se abre su ficha completa (experiencia, «Qué incluye» y «Opcional») |
| Planes | Los 5 planes con precios por car |
| Catálogo digital | Mockup de navegador con el catálogo embebido + botón para abrirlo |
| Galería | 12 imágenes con visor (lightbox) |
| Contacto | WhatsApp **315 220 5659**, WhatsApp **320 738 4581**, correo **gocarspensilvania@gmail.com** · dirección: **Calle 5 # 4-42, Pensilvania, Caldas** · redes: **TikTok @gocarspensilvania** y **fanpage de Facebook: https://www.facebook.com/profile.php?id=61593590381138** |

## Cómo editar el contenido

Todo lo editable está en `index.html`:

1. **Contactos** — en el `<script>`, al inicio: `const WA1`, `const WA2`, `const MAIL`.
2. **Planes y precios** — array `PLANS` (nombre, descripción, precio).
3. **Rutas** — array `ROUTES` (nombre, distancia, mapa, frase, experiencia, qué incluye, opcionales).
4. **Galería** — array `GALLERY`.
5. **Textos de las secciones** — directamente en el HTML (busca el texto y cámbialo).

> Los videos y las imágenes se cargan con **rutas relativas**: si cambias una foto, reemplaza el archivo en `assets/img/` conservando el nombre. El **logo va incrustado en base64**, por eso se ve bien aunque abras el archivo en otro dispositivo.

## Notas técnicas

- Videos: H.264, 720×1280 (vertical), 30 fps, sin audio, `faststart`. Peso total ≈ 20 MB; los clips del film usan **carga diferida** y se reproducen de a uno.
- El sitio respeta `prefers-reduced-motion` (desactiva el parallax y las animaciones de scroll).
- Incluye datos estructurados JSON-LD (`LocalBusiness`) para SEO local.


---

## 🌐 Publicado en GitHub Pages (hosting principal, sep-2026)

Sitio en vivo: **https://ricardoosorio1104.github.io/go-cars-pensilvania/**

Repositorio: https://github.com/ricardoosorio1104/go-cars-pensilvania (público)

### Cómo publicar un cambio (2 comandos)

```bash
cd C:/Users/ricar/go-cars-pensilvania/sitio-web
git add -A && git commit -m "describe el cambio"
git push
```

GitHub Pages reconstruye solo en ~1 minuto. **No hay límite de ancho de banda** (a diferencia
de Netlify, que bloqueó los despliegues por créditos agotados).

### Puntos importantes de este hosting

- **`.nojekyll`** en la raíz: obliga a GitHub a servir los archivos tal cual (sin procesarlos con Jekyll).
- **El catálogo detecta el hosting**: si NO está en Netlify, llama directo al Apps Script (JSONP)
  y se salta el puente `/api/exec`. Es lo que hace que las reservas funcionen en GitHub Pages.
- Los archivos `_headers` y `_redirects` son exclusivos de Netlify; aquí se ignoran.
- **La insignia "Powered by Netlify" no existe en GitHub Pages** (no hay que ocultarla).
- El video de portada se sirve con soporte de rangos (HTTP 206), necesario para que el video
  avance con el scroll. Verificado.

### Netlify queda como respaldo

https://gocarspensilvania.netlify.app — sigue en línea, pero **no acepta despliegues nuevos**
hasta reponer créditos. Sólo se puede actualizar con `npx netlify-cli@latest deploy --prod --dir=.`

### Peso de los videos (optimizados sep-2026)

| Archivo | Tamaño | Uso |
|---|---|---|
| ruta-cabana-2.mp4 (640x1138) | 2,9 MB | Portada (carga al entrar) |
| ruta-cabana-3.mp4 (540x960) | 3,6 MB | Clip del film (carga diferida) |
| ruta-cabana-1.mp4 (540x960) | 6,3 MB | Clip del film (carga diferida) |
| **Total** | **12,8 MB** | (antes 26,8 MB) |

Scripts de re-codificación: `_optimizar.sh` (primera pasada) y `_optimizar2.sh` (segunda, la aplicada).
Mantienen keyframes densos (`-g 12` a `-g 18`) para que el scroll avance el video con fluidez.
