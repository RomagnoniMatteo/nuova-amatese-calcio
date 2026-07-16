<script setup>
import { ref, onMounted } from 'vue'
import club from '../data/club.json'
import '../styles/page.css'

const mapQuery = encodeURIComponent('Nuova amatese calcio')
const mapSrc = `https://www.google.com/maps?q=${mapQuery}&output=embed`
const mapLink = `https://www.google.com/maps?q=${mapQuery}`

const mapFailed = ref(false)
const mapLoaded = ref(false)

function onMapLoad() {
  mapLoaded.value = true
}
function onMapError() {
  mapFailed.value = true
}

function isInAppBrowser() {
  const ua = navigator.userAgent || ''
  return /Instagram|FBAN|FBAV/i.test(ua)
}

onMounted(() => {
  if (isInAppBrowser()) {
    mapFailed.value = true
    return
  }

  setTimeout(() => {
    if (!mapLoaded.value) mapFailed.value = true
  }, 4000)
})
</script>

<template>
  <div class="page-wrap">
  
    <section class="container page">
      <h1 class="page-title">Dove siamo</h1>

      <div class="grid">
        <div class="col col-left">
          <div class="pixel-border map-wrap">
            <iframe
              v-if="!mapFailed"
              :src="mapSrc"
              title="Mappa del campo dell'Amatese a Cassina Amata"
              loading="lazy"
              referrerpolicy="no-referrer-when-downgrade"
              @load="onMapLoad"
              @error="onMapError"
            ></iframe>

            <a v-else :href="mapLink" target="_blank" rel="noopener" class="map-fallback">
              📍 Apri la mappa su Google Maps
            </a>
          </div>

          <div class="addresses">
            <div v-for="loc in club.locations" :key="loc.label" class="address-row">
              <span class="address-label">{{ loc.label }}</span>
              <span>{{ loc.address }}</span>
            </div>
          </div>
        </div>

        <div class="col col-right">
          <div class="card pixel-border">
            <h2 class="card-title">Contatti</h2>
            <p class="contact-line">
              📞 <a :href="`tel:${club.contacts.phones[0].replace(/\s/g, '')}`">{{ club.contacts.phones[0] }}</a>
              &nbsp;/&nbsp;
              <a :href="`tel:${club.contacts.phones[1].replace(/\s/g, '')}`">{{ club.contacts.phones[1] }}</a>
            </p>
            <p class="contact-line">✉️ <a :href="`mailto:${club.contacts.email}`">{{ club.contacts.email }}</a></p>
            <p class="contact-line">🕒 Segreteria: {{ club.contacts.secretaryHours }}</p>
          </div>

          <div class="card pixel-border">
            <h2 class="card-title">Seguici</h2>
            <div class="social-row">
              <a :href="club.social.instagram" target="_blank" rel="noopener">Instagram</a>
              <a :href="club.social.facebook" target="_blank" rel="noopener">Facebook</a>
              <a :href="club.social.tiktok" target="_blank" rel="noopener">Tiktok</a>
            </div>
          </div>

          <a class="btn cta-big" :href="`tel:${club.contacts.phones[0].replace(/\s/g, '')}`">
            ▶ Chiamaci ed entra anche tu in questo magico mondo!
          </a>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>

/* ---------- LAYOUT ---------- */
.grid {
  display: grid;
  grid-template-columns: 1.1fr 0.9fr;
  gap: 1.5rem;
  margin-top: 1.5rem;
  align-items: start;
}

.col {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.col-left {
  animation: fadeSlideUp 0.6s ease both;
  animation-delay: 0.1s;
}

.col-right {
  animation: fadeSlideUp 0.6s ease both;
  animation-delay: 0.2s;
}

/* ---------- MAPPA ---------- */
.map-wrap {
  overflow: hidden;
  background: var(--paper);
  transition: box-shadow 0.3s ease;
}

.map-wrap:hover {
  box-shadow: 0 14px 26px -14px rgba(0, 0, 0, 0.4);
}

.map-wrap iframe {
  width: 100%;
  height: 320px;
  border: 0;
  display: block;
}

.map-fallback {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 320px;
  text-decoration: none;
  color: var(--pitch);
  font-weight: 600;
  font-family: var(--font-mono);
  text-align: center;
  padding: 0 1rem;
  transition: background-color 0.2s ease;
}

.map-fallback:hover {
  background-color: var(--paper-line);
}

.addresses {
  background: var(--paper);
  border: 3px solid var(--pitch);
  border-radius: var(--radius-card);
  padding: 1rem;
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
}

.address-row {
  display: flex;
  flex-direction: column;
  font-size: 0.9rem;
}

.address-label {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  color: var(--pitch);
  text-transform: uppercase;
}

/* ---------- CARD CONTATTI ---------- */
.card {
  background: var(--paper);
  padding: 1.1rem;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.card:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 18px -12px rgba(0, 0, 0, 0.35);
}

.card-title {
  font-size: 0.85rem;
  margin: 0 0 0.5rem;
}

.card p {
  margin: 0.2rem 0;
}

.contact-line a {
  color: var(--pitch);
  font-weight: 600;
  transition: opacity 0.2s ease;
}

.contact-line a:hover {
  opacity: 0.7;
}

.social-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.6rem;
  font-family: var(--font-mono);
  font-size: 0.82rem;
}

.social-row a {
  text-decoration: none;
  color: var(--pitch);
  border-bottom: 1px dotted var(--pitch);
  transition: border-color 0.2s ease, opacity 0.2s ease;
}

.social-row a:hover {
  opacity: 0.7;
  border-bottom-style: solid;
}

.cta-big {
  justify-content: center;
  text-align: center;
  font-size: 0.9rem;
  padding: 0.9rem 1rem;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.cta-big:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 18px -10px rgba(0, 0, 0, 0.5);
}

.legal {
  margin-top: 2rem;
  font-family: var(--font-mono);
  font-size: 0.7rem;
  color: var(--locked);
}

@media (max-width: 760px) {
  .grid {
    grid-template-columns: 1fr;
  }
}
</style>