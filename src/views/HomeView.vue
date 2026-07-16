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
   <div class="home-root">
  <section class="hero">
    <div class="hero-bg" aria-hidden="true">
      <span class="hero-blob hero-blob-1"></span>
      <span class="hero-blob hero-blob-2"></span>
      <span class="hero-particles"></span>
    </div>

    <div class="container hero-grid">
      <div class="screen pixel-border">
        <p class="eyebrow" style="color: var(--pixel-green)">a.s.d. nuova amatese calcio</p>
        <h1 class="title">VIENI A GIOCARE<br />CON NOI!</h1>
        <p class="tagline">{{ club.mission }}</p>
        <div class="cta-row">
          <router-link class="btn btn-alt" to="/dove-siamo">▶ vieni a trovarci</router-link>
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
        <li
          v-for="(item, i) in latestUnlocked"
          :key="item.id"
          class="update-item"
          :style="{ '--delay': (i * 0.08) + 's' }"
        >
          <router-link :to="item.kind === 'storia' ? `/serie/storia/${item.id}` : `/serie/podcast/${item.id}`">
            <span class="badge" style="color: var(--pitch)">{{ item.kind === 'storia' ? 'Episodio' : 'Podcast' }}</span>
            <strong>{{ item.title }}</strong>
            <span class="date">{{ formatDate(item.date) }}</span>
          </router-link>
        </li>
      </ul>
    </div>
  </section>
  </div>
</template>

<style scoped>
.hero {
  position: relative;
  background: var(--pixel-dark);
  padding: 2.5rem 0 2rem;
  overflow: hidden;
  isolation: isolate;
}

/* ---------- SFONDO ANIMATO HERO ---------- */
.hero-bg {
  position: absolute;
  inset: -20% -10%;
  z-index: -1;
  pointer-events: none;
}

.hero-blob {
  position: absolute;
  border-radius: 50%;
  filter: blur(70px);
  opacity: 0.25;
  will-change: transform;
}

.hero-blob-1 {
  width: 380px;
  height: 380px;
  top: -10%;
  left: -5%;
  background: var(--pixel-green);
  animation: hero-float-1 16s ease-in-out infinite;
}

.hero-blob-2 {
  width: 320px;
  height: 320px;
  bottom: -15%;
  right: -5%;
  background: var(--amatese-yellow);
  animation: hero-float-2 20s ease-in-out infinite;
}

.hero-particles {
  position: absolute;
  inset: 0;
  background-image: radial-gradient(rgba(255, 255, 255, 0.05) 1px, transparent 1px);
  background-size: 24px 24px;
  animation: particles-drift 30s linear infinite;
}

@keyframes hero-float-1 {
  0%, 100% { transform: translate(0, 0) scale(1); }
  50%      { transform: translate(50px, 30px) scale(1.1); }
}

@keyframes hero-float-2 {
  0%, 100% { transform: translate(0, 0) scale(1); }
  50%      { transform: translate(-40px, -40px) scale(1.15); }
}

@keyframes particles-drift {
  0%   { background-position: 0 0; }
  100% { background-position: 120px 60px; }
}

@media (prefers-reduced-motion: reduce) {
  .hero-blob,
  .hero-particles {
    animation: none;
  }
}

/* ---------- CONTENUTO HERO ---------- */
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
  animation: hero-in 0.6s ease both;
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
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.btn-alt:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 18px -10px rgba(0, 0, 0, 0.5);
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
  animation: hero-in 0.6s ease both;
  animation-delay: 0.1s;
  cursor: pointer;
}

.hero-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  opacity: 0;
  transition: opacity 0.4s ease, transform 0.5s ease;
  transform-origin: center;
}

.hero-image.is-loaded {
  opacity: 1;
  transform: scale(1.03);
}

.hero-image-wrap:hover .hero-image.is-loaded {
  transform: scale(1.12);
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
  0%, 100% { transform: translateY(0) rotate(0deg); }
  50%      { transform: translateY(-10px) rotate(180deg); }
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
  transition: border-color 0.2s ease, transform 0.2s ease, background-color 0.2s ease;
}

.update-list a:hover {
  border-color: var(--pitch);
  transform: translateX(4px);
  background-color: rgba(0, 0, 0, 0.02);
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