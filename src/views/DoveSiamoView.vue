<script setup>
import club from '../data/club.json'

const mapQuery = encodeURIComponent('Nuova amatese calcio')
const mapSrc = `https://www.google.com/maps?q=${mapQuery}&output=embed`
</script>

<template>
  <section class="container page">
    <h1>Dove siamo</h1>

    <div class="grid">
      <div class="col">
        <div class="pixel-border map-wrap">
          <iframe
            :src="mapSrc"
            title="Mappa del campo dell'Amatese a Cassina Amata"
            loading="lazy"
            referrerpolicy="no-referrer-when-downgrade"
          ></iframe>
        </div>

        <div class="addresses">
          <div v-for="loc in club.locations" :key="loc.label" class="address-row">
            <span class="address-label">{{ loc.label }}</span>
            <span>{{ loc.address }}</span>
          </div>
        </div>
      </div>

      <div class="col">
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
</template>

<style scoped>
.page {
  padding-block: 2rem 3rem;
}
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
.map-wrap {
  overflow: hidden;
  background: var(--paper);
}
.map-wrap iframe {
  width: 100%;
  height: 320px;
  border: 0;
  display: block;
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
.card {
  background: var(--paper);
  padding: 1.1rem;
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
}
.cta-big {
  justify-content: center;
  text-align: center;
  font-size: 0.9rem;
  padding: 0.9rem 1rem;
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
