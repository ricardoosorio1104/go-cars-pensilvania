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

  > ⚠️ Usa `servir.py`, **no** `python -m http.server`. Los videos del sitio **avanzan con el scroll** (no se reproducen solos), y eso exige que el servidor soporte peticiones **Range (206)**. El `http.server` normal no las soporta, y con él los videos grandes se quedan congelados al desplazarse. (En GitHub Pages o cualquier hosting real el soporte de rangos ya viene incluido.)

## Cómo publicarlo

El sitio vive en **GitHub Pages**, con el dominio propio **https://gocarspensilvania.com**.
Publicar un cambio son 3 comandos:

```bash
cd C:/Users/ricar/go-cars-pensilvania/sitio-web
git add -A && git commit -m "describe el cambio"
git push
```

GitHub reconstruye solo en **~40 segundos**. No hay que subir archivos a mano ni arrastrar carpetas.

## Estructura

```
sitio-web/
├── index.html              ← el sitio (todo el código, diseño y datos)
├── catalogo.html           ← catálogo digital (se muestra embebido y se abre en pestaña aparte)
├── servir.py               ← servidor local con soporte Range (para previsualizar los videos)
├── README.md               ← este archivo
└── assets/
    ├── videos/             ← portada + 3 clips de las rutas (vertical 9:16, sin audio)
    │                          rodada-trocha.mp4 (portada) · clip-01/02/03.mp4
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
| Galería | 12 **fotos** + 4 **clips de video** reales de las rutas (del TikTok @gocarspensilvania). Los clips se previsualizan al pasar el mouse y se abren en el visor |
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

### ✅ Sitio en vivo con dominio propio: **https://gocarspensilvania.com**

También responde en `https://www.gocarspensilvania.com` (redirige al principal) y la URL
`https://ricardoosorio1104.github.io/go-cars-pensilvania/` redirige al dominio propio.

Repositorio: https://github.com/ricardoosorio1104/go-cars-pensilvania (público)

### Dominio propio (comprado sep-2026)

- **Dominio:** `gocarspensilvania.com` — registrado en **Cloudflare Registrar** (a costo, sin margen).
  Vence **21-sep-2028** (2 años prepagados → el precio quedó congelado antes de la subida de Verisign de nov-2026).
- **DNS (Cloudflare):** 4 registros `A` al apex → `185.199.108.153`, `.109.153`, `.110.153`, `.111.153`;
  1 `CNAME` en `www` → `ricardoosorio1104.github.io`. **Todos con Proxy status = DNS only (nube GRIS)** —
  con la nube naranja GitHub no puede emitir el certificado HTTPS.
- **GitHub Pages:** custom domain `gocarspensilvania.com` + **Enforce HTTPS** activado. El archivo `CNAME`
  en la raíz del repo (lo crea GitHub) es lo que mantiene el dominio amarrado al sitio.
- **Certificado:** emitido automáticamente por GitHub (Let's Encrypt), estado `approved`.

> ⚠️ Si algún día se cambia el proxy de Cloudflare a "Proxied" (nube naranja), verificar primero que
> GitHub siga renovando el certificado; el flujo seguro es dejar los registros en "DNS only".

### Cómo publicar un cambio (2 comandos)

```bash
cd C:/Users/ricar/go-cars-pensilvania/sitio-web
git add -A && git commit -m "describe el cambio"
git push
```

GitHub Pages reconstruye solo en ~1 minuto. El plan gratuito permite **100 GB de tráfico al mes**
(de sobra: el catálogo pesa ~1,4 MB por visita).

### Puntos importantes de este hosting

- **`.nojekyll`** en la raíz: obliga a GitHub a servir los archivos tal cual (sin procesarlos con Jekyll).
- **El catálogo llama directo al Apps Script** (primero `fetch` y, si falla, JSONP). Ya no existe
  el puente `/api/exec` ni detección de hosting: hay un solo camino, y funciona en GitHub Pages.
- `_headers`, `_redirects` y `.netlify/` se eliminaron (sep-2026): eran exclusivos de Netlify.
- El video de portada se sirve con soporte de rangos (HTTP 206), necesario para que el video
  avance con el scroll. Verificado.

### Netlify: retirado (sep-2026)

`https://gocarspensilvania.netlify.app` **ya no se usa ni se puede actualizar**: la cuenta agotó los
300 créditos/mes del plan gratis y rechaza todo despliegue con `JSONHTTPError: Forbidden`.
Se retiró del sitio (la imagen de WhatsApp apuntaba ahí, el puente `/api/exec`, y el CSS/JS que
ocultaba su insignia) y se borraron `_headers`, `_redirects` y `.netlify/`.
El sitio oficial es **https://gocarspensilvania.com**. No intentar `netlify-cli deploy` otra vez.

### Peso de los videos (contenido real del TikTok, oct-2026)

| Archivo | Tamaño | Uso |
|---|---|---|
| rodada-trocha.mp4 (640x1138, 13 s) | 3,1 MB | Portada (carga al entrar) |
| clip-01.mp4 (540x960, 22 s) | 3,1 MB | Clip del film · sendero entre pinos (Ruta 2) |
| clip-02.mp4 (540x960, 24 s) | 2,7 MB | Clip del film · camino de tierra |
| clip-03.mp4 (540x960, 20 s) | 1,9 MB | Clip del film · el valle y el refrigerio |
| gal-01.mp4 (540x960) | 1,0 MB | Clip de la galería (carga diferida, sólo al interactuar) |
| gal-02.mp4 (540x960) | 1,2 MB | Clip de la galería |
| gal-03.mp4 (540x960) | 1,5 MB | Clip de la galería |
| **Total** | **14,5 MB** | (antes 12,8 MB; los clips de la galería no se descargan solos) |

Script: `_tiktok/encode_sitio.sh` (fuera del repo). Mantiene keyframes densos (`-g 12` a `-g 18`)
para que el scroll avance el video con fluidez; la portada usa `crf 34` y los clips `crf 32`.

> ⚠️ **El orden de los clips manda el texto.** En `index.html`, los `film-cap` (título, frase y
> ruta) se muestran junto al clip del mismo índice: `clip-01` ↔ primer `film-cap`, y así.
> Si cambias un video, cambia su descripción o el clip quedará anunciando otra ruta.

### Galería: fotos y clips reales (oct-2026)

Las 12 fotos de `assets/img/galeria/` salen del TikTok **@gocarspensilvania** (carruseles y
fotogramas de los videos). Para reemplazar una: deja el archivo con el **mismo nombre** y
máximo 1200 px de ancho, o cambia la ruta en el array `GALLERY`.
Las tarjetas recortan en **3:4 desde el centro** (`object-fit:cover`): si el sujeto (el car)
queda muy arriba o muy abajo en la foto, en la cuadrícula no se verá.

**Los clips** son 4 piezas del mismo array, con dos campos extra:

```js
{src:'assets/videos/gal-01.jpg',      // póster (el .jpg se genera al codificar)
 alt:'Clip: la gente, los cars y las montañas',
 video:'assets/videos/gal-01.mp4',    // el clip
 dur:'18 s', wide:false},             // lo que muestra la etiqueta "Clip · 18 s"
```

- `preload="none"` + póster: **el clip no se descarga** hasta que el visitante pasa el mouse o
  lo abre (por eso la galería puede tener varios videos sin encarecer la entrada al sitio).
- Los clips van **sin audio** (`-an`), igual que los del scroll; el visor los abre en `muted`
  para que el navegador nunca bloquee la reproducción.
- Al cerrar el visor (✕, tocar fuera, Escape o el **botón atrás**) un `MutationObserver`
  pausa el video: cubre todos los caminos de cierre con una sola regla.


---

## 🧩 Enlaces con plan preseleccionado (sep-2026)

En la sección **Planes y precios** de la portada, cada casilla es un **enlace real** al catálogo
(antes eran `div` que parecían botones pero no hacían nada — confundía a la gente).

- Portada: `<a class="plan" href="catalogo.html?plan=G1">…</a>` — la clave del plan va en `PLANS[].k`.
- Catálogo: al cargar lee `?plan=` (y opcionalmente `&ruta=`) con `URLSearchParams`, deja el plan
  **seleccionado** y muestra un aviso: «Plan elegido: … · ahora elige tu ruta».

Claves de plan en el catálogo: `G1` Básico · `G2` Refrigerio · `G3` Mazamorrada ·
`G4` Con paradas · `G5` Fiesta/Grupal. Claves de ruta: `r1`…`r9`.

**Ejemplos:** `catalogo.html?plan=G3` · `catalogo.html?plan=G4&ruta=r2`

> Si algún día se agrega un plan nuevo, hay que añadirlo **en los dos archivos**: en `PLANS` de
> `index.html` (con su `k`) y en `PLANS` de `catalogo.html` (con la misma clave).

En teléfono (`max-width:640px`) la rejilla de planes va a **una casilla por fila** para que se lea
y se toque bien.


---

## 🛡️ Si el catálogo dice «No pudimos cargar las horas» (sep-2026)

**Causa:** el catálogo pide la disponibilidad a Apps Script con un `<script>` (JSONP) a
`script.google.com`. Si el navegador bloquea ese script —bloqueadores de anuncios, modos de
ahorro de datos, el navegador interno de otra app (WhatsApp/Instagram) o filtros de DNS— la
consulta falla y antes quedaba un botón «Reintentar» sin salida.

**Solución aplicada (nunca se queda trabada):**

1. Fallo detectado en **9 s** por intento (antes 30 s), hasta **4 intentos** con aviso del
   número de intento en pantalla.
2. Si no hay respuesta, se muestra el **horario completo** con la etiqueta *Por confirmar*,
   seleccionable, con un aviso claro y botón «Volver a intentar».
3. Al enviar en ese estado, la reserva **no** se agenda a ciegas: va por WhatsApp con la nota
   *«no pude verificar la disponibilidad en vivo: ¿me confirman si esa hora está libre?»*.

**Arreglo definitivo (pendiente):** publicar un proxy propio en el dominio (Cloudflare Worker en
un subdominio tipo `api.gocarspensilvania.com` que devuelva JSONP). Al ser el propio dominio, no
lo bloquea ningún filtro. Requiere acceso a la API de Cloudflare.

## ↩️ El botón «atrás» del navegador cierra las capas internas (sep-2026)

Antes, si el visitante abría la ficha de una ruta, el visor del mapa o la galería y pulsaba **atrás**,
salía del sitio y perdía todo el avance. Ahora esas capas viven dentro del historial: **atrás cierra la
capa y lo deja donde estaba**.

**Cómo funciona** (bloque «CAPAS INTERNAS Y EL BOTÓN ATRÁS» en `index.html` y `catalogo.html`):

1. Cada capa abierta empila una entrada con `history.pushState()`. La lista `CAPAS` va de la capa más
   superficial a la más profunda:
   - `index.html`:  `#mapLb` (mapa) → `#lb` (galería) → `#waPop` (WhatsApp) → `#det` (ficha de ruta)
   - `catalogo.html`: `#advOverlay` (asesoría) → `#overlay` (ficha de ruta)
2. `popstate` cierra **solo la capa de más arriba** (el contador `capasGC` baja uno). Si no hay capas,
   no se intercepta nada y el navegador sale del sitio como siempre.
3. Cerrar desde la interfaz (✕, tocar fuera, **Escape**, «Volver y elegir otra», «Elegir esta ruta»)
   descuenta la entrada con `history.back()` — así el historial no se ensucia y el siguiente «atrás» sí
   sale del sitio.

**⚠️ Trampa al tocar este código:** la pregunta «¿ya estaba abierta la capa?» hay que hacerla **antes**
de añadir la clase que la abre. Si se evalúa después (`if (!capaOn('det')) capaPush()`), siempre da falso,
nunca se empila la entrada y **el botón atrás vuelve a sacar al visitante del sitio**. Por eso se guarda
primero en una variable: `const yaFicha = capaOn('det'); …; if (!yaFicha) capaPush();`

**Cómo verificarlo** (no basta con mirar la pantalla):

```js
capasGC         // contador de capas: 0 al inicio, +1 por capa abierta, 0 al cerrar todas
history.back()  // simula el botón atrás REAL del navegador
```

Secuencia correcta: abrir la ficha (capasGC=1) → atrás → la ficha se cierra y la URL **sigue** siendo la
del sitio (capasGC=0). Con dos niveles: ficha+mapa (capasGC=2) → atrás cierra **solo** el mapa
(capasGC=1) → atrás cierra la ficha. Y tras cerrar con la ✕, capasGC debe volver exacto a 0.
