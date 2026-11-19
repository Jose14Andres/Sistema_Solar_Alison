# Sol, Tierra y Luna — Experiencia de RA/RV para 3.º EGB

Prototipo educativo de realidad virtual y aumentada para Ciencias Naturales (subnivel Elemental, 3.º de EGB). Su objetivo es que los estudiantes expliquen que el día y la noche ocurren porque la Tierra gira sobre sí misma frente al Sol, y que comparen el Sol, la Tierra y la Luna por su forma, su tamaño y su movimiento.

Todo funciona desde un solo archivo, `index.html`, de unos 3,3 MB (incluye la narración grabada). No necesita internet, ni cuentas, ni instalar nada.

## Actividades

| Modo | Qué hace |
| --- | --- |
| Explorar | El Sol, la Tierra y la Luna en 3D, con datos que se escuchan en voz alta |
| Día y noche | Predecir, observar y explicar qué pasa en Quito cuando gira la Tierra, con el cielo de Quito y una vista desde arriba |
| Reto | 6 preguntas que siempre explican la respuesta, sin nota ni nombres |
| RV | Vista 360° con o sin visor de cartón; se elige un astro mirándolo 2 segundos |
| RA | La Tierra y la Luna sobre la cámara, o sobre una foto del aula sin personas |
| Guía docente | Secuencia ERCA, accesibilidad, baja conectividad y criterios éticos |

## Cómo usarlo

- **Sin internet:** copien `index.html` al celular (por USB, Bluetooth o WhatsApp) y ábranlo en Chrome.
- **En línea:** si GitHub Pages está activado en este repositorio, el enlace es `https://jose14andres.github.io/Sistema_Solar_Alison/`. Al ser HTTPS, ahí funcionan la cámara (RA) y los sensores de movimiento (RV).

## Accesibilidad y baja conectividad

- Voces grabadas de personajes (ElevenLabs, modelo eleven_v4): el Sol (voz JosePlan), la Tierra (Natalia), la Luna (Lulu) y una voz guía (Betty) narran 90 frases con entonación expresiva. Van dentro de `index.html`, así que suenan igual en cualquier equipo y sin internet. Las frases sin grabación usan la voz del dispositivo como respaldo.
- Voz con personajes: el Sol, la Tierra y la Luna hablan en primera persona, cada uno con su tono, y una voz guía lee las preguntas. Cada oración y cada opción se resalta mientras suena. En ⚙️ Ajustes se elige la voz del equipo y la velocidad, y se pueden apagar los personajes y los efectos de sonido. Usa las voces del dispositivo (Web Speech API), así que funciona sin internet.
- Efectos de sonido sintetizados en el navegador (Web Audio), sin archivos de audio.
- Tamaño de letra, alto contraste y opción para detener el movimiento. Respeta la preferencia «reducir movimiento» del sistema.
- Botones de al menos 48 px como alternativa a todos los gestos; funciona con teclado y lector de pantalla.
- Modo ligero y vista 2D para equipos lentos o sin 3D.
- Plan C sin dispositivos (linterna, pelota y plastilina), descrito en la Guía docente.

## Privacidad y ética

- No pide nombres, no guarda respuestas, no se conecta a internet y no graba la cámara.
- Las evidencias de aplicación no deben incluir datos ni imágenes que identifiquen a menores.
- Este prototipo se programó con ayuda de IA generativa (Claude, de Anthropic). Ese uso está declarado en el registro de uso ético de IA del equipo.

## Desarrollo

`src/app.html` es el código fuente. `audio/` guarda cada frase grabada y `audio/manifest.json` dice qué texto dice cada archivo y qué personaje lo dice. Para regenerar `index.html` con Three.js incluido dentro del archivo:

```bash
npm install three@0.149.0
python3 build.py
```

## Créditos y licencias

- Equipo: José Andrés Ureta Granda y equipo docente en formación.
- Voces generadas con [ElevenLabs](https://elevenlabs.io) (plan gratuito, uso educativo no comercial con atribución).
- [Three.js](https://threejs.org) r149, licencia MIT, © 2010-2023 Three.js Authors. Va incluido dentro de `index.html` junto con su aviso de licencia.
