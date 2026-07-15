<script setup>
import { computed, ref } from 'vue'
import episodesRaw from '../data/episodes.json'
import podcastsRaw from '../data/podcasts.json'
import club from '../data/club.json'
import { withUnlockState, formatDate } from '../composables/useUnlock'
import spogliatoioImg from '../assets/images/amatese_copertina.png'
import amateseImg from '../assets/images/amatese.png'

const episodes = withUnlockState(episodesRaw, 'date')
const podcasts = withUnlockState(podcastsRaw, 'date')

const heroImageLoaded = ref(false)

const latestUnlocked = computed(() => {
  const all = [
    ...episodes.filter((e) => e.unlocked).map((e) => ({ ...e, kind: 'storia' })),
    ...podcasts.filter((p) => p.unlocked).map((p) => ({ ...p, kind: 'podcast' })),
  ]
  all.sort((a, b) => new Date(b.date) - new Date(a.date))
  return all.slice(0, 3)
})
</script>

<template>
  <section class="hero">
    <div class="container hero-grid">
      <div class="screen pixel-border">
        <!--img class="logo" :src="amateseImg"/-->
        <p class="eyebrow" style="color: var(--pixel-green)">a.s.d. nuova amatese calcio</p>
        <h1 class="title">VIENI A GIOCARE<br />CON NOI!</h1>
        <p class="tagline">{{ club.mission }}</p>
        <div class="cta-row">
          <!--a class="btn" :href="`tel:${club.contacts.phones[0].replace(/\s/g, '')}`">📞 chiamaci ora</a-->
          <router-link class="btn btn-alt" to="/dove-siamo">dove siamo</router-link>
        </div>
      </div>
      <div class="hero-image-wrap">
        <div v-if="!heroImageLoaded" class="pokeball-loader" aria-label="Caricamento immagine">
          <div class="pokeball">
            <div class="pokeball-top"></div>
            <div class="pokeball-band"></div>
            <div class="pokeball-bottom"></div>
            <div class="pokeball-button"></div>
          </div>
        </div>
        <img
          class="hero-image"
          :class="{ 'is-loaded': heroImageLoaded }"
          :src="spogliatoioImg"
          alt="Scena disegnata dello spogliatoio dell'Amatese con lo staff riunito"
          @load="heroImageLoaded = true"
        />
      </div>
    </div>
  </section>

  <!-- affitta campo?
  <section class="container field-rental">
    <div class="rental-card pixel-border">
      <h2>{{ club.rentField.title }}</h2>
      <p>{{ club.rentField.description }}</p>
      <p class="rental-contacts">
        📞 {{ club.contacts.phones.join(' · ') }} &nbsp;·&nbsp; ✉️ {{ club.contacts.email }}
      </p>
    </div>
  </section>

-->
  <section class="container lore-teaser">
    <div class="lore-head">
      <h2 class="section-title">Non solo calcio: la storia dell'Amatese</h2>
    </div>
    <div class="lore-links">
      <router-link class="btn btn-alt" to="/serie">▶ scopri la storia</router-link>
    </div>

    <div v-if="latestUnlocked.length" class="update-col">
      <h3 class="section-title small">Ultimi Post</h3>
      <ul class="update-list">
        <li v-for="item in latestUnlocked" :key="item.id">
          <router-link :to="item.kind === 'storia' ? `/serie/storia/${item.id}` : `/serie/podcast/${item.id}`">
            <span class="badge" style="color: var(--pitch)">{{ item.kind === 'storia' ? 'Episodio' : 'Podcast' }}</span>
            <strong>{{ item.title }}</strong>
            <span class="date">{{ formatDate(item.date) }}</span>
          </router-link>
        </li>
      </ul>
    </div>
  </section>
</template>

<style scoped>
.hero {
  background: var(--pixel-dark);
  padding: 2.5rem 0 2rem;
}
.hero-grid {
  display: grid;
  grid-template-columns: 1.1fr 0.9fr;
  gap: 1.5rem;
  align-items: stretch;
}
.screen {
  background: var(--pitch);
  color: var(--paper);
  padding: 1.8rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 0.9rem;
}
.title {
  font-size: 1.5rem;
  margin: 0;
  color: var(--amatese-yellow);
}
.tagline {
  font-family: var(--font-mono);
  font-size: 0.9rem;
  opacity: 0.9;
  max-width: 38ch;
}
.cta-row {
  display: flex;
  gap: 0.75rem;
  flex-wrap: wrap;
}
.btn-alt {
  background: var(--pixel-green);
}

.logo {
   width: 25%;
  object-fit: cover;
}
.hero-image-wrap {
  position: relative;
  width: 100%;
  height: 100%;
  min-height: 220px;
  border-radius: var(--radius-card);
  border: 3px solid var(--pixel-dark);
  overflow: hidden;
  background: var(--pitch);
}
.hero-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  opacity: 0;
  transition: opacity 0.4s ease;
}
.hero-image.is-loaded {
  opacity: 1;
}
.pokeball-loader {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}
.pokeball {
  position: relative;
  width: 56px;
  height: 56px;
  border-radius: 50%;
  background: #f7f3ea;
  border: 3px solid #141414;
  overflow: hidden;
  animation: pokeball-bounce 1s ease-in-out infinite;
}
.pokeball-top {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 50%;
  background: #d64550;
}
.pokeball-bottom {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 50%;
  background: #f7f3ea;
}
.pokeball-band {
  position: absolute;
  top: 50%;
  left: 0;
  width: 100%;
  height: 6px;
  background: #141414;
  transform: translateY(-50%);
}
.pokeball-button {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 16px;
  height: 16px;
  background: #f7f3ea;
  border: 3px solid #141414;
  border-radius: 50%;
  transform: translate(-50%, -50%);
}
@keyframes pokeball-bounce {
  0%, 100% {
    transform: translateY(0) rotate(0deg);
  }
  50% {
    transform: translateY(-10px) rotate(180deg);
  }
}
.field-rental {
  padding-block: 2rem 0;
}
.rental-card {
  background: var(--amatese-yellow);
  padding: 1.4rem;
  text-align: center;
}
.rental-card h2 {
  font-size: 1rem;
  margin: 0 0 0.4rem;
}
.rental-contacts {
  font-family: var(--font-mono);
  font-size: 0.8rem;
  margin: 0.6rem 0 0;
}
.lore-teaser {
  padding-block: 2.5rem 3rem;
}
.lore-head {
  max-width: 80ch;
}
.section-title {
  font-size: 1rem;
  color: var(--pitch);
}
.section-title.small {
  font-size: 0.85rem;
}
.lore-sub {
  font-family: var(--font-mono);
  font-size: 0.85rem;
  color: var(--ink);
  opacity: 0.85;
}
.lore-links {
  display: flex;
  gap: 0.75rem;
  flex-wrap: wrap;
  margin: 1.2rem 0 2rem;
}
.update-list {
  list-style: none;
  padding: 0;
  margin: 0.8rem 0 0;
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
}
.update-list a {
  display: flex;
  align-items: baseline;
  gap: 0.6rem;
  flex-wrap: wrap;
  text-decoration: none;
  color: var(--ink);
  padding: 0.6rem 0.8rem;
  border: 2px solid var(--paper-line);
  border-radius: 8px;
}
.update-list a:hover {
  border-color: var(--pitch);
}
.date {
  margin-left: auto;
  font-family: var(--font-mono);
  font-size: 0.78rem;
  opacity: 0.7;
}

@media (max-width: 760px) {
  .hero-grid {
    grid-template-columns: 1fr;
  }
}
</style>