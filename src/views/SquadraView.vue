<script setup>
import { computed, ref } from 'vue'
import players from '../data/pokedex.json'
import staff from '../data/staff.json'
import pokedexRaw from '../data/pokedex.json'
import { withUnlockState, formatDate } from '../composables/useUnlock'
import PokedexModal from '../components/PokedexModal.vue'

const groupLabels = {
  P: 'Portieri',
  D: 'Difensori',
  C: 'Centrocampisti',
  A: 'Attaccanti'
}

const pokedex = withUnlockState(pokedexRaw, 'unlockDate')

const grouped = computed(() => {
  const map = {}
  for (const p of players) {
    if (!map[p.group]) map[p.group] = []
    map[p.group].push(p)
  }
  return map
})

function cardFor(playerId) {
  return pokedex.find((c) => c.playerId === playerId) || null
}
const activeCard = ref(null)

function openCard(playerId) {
  const card = cardFor(playerId)
  if (card && card.unlocked) {
    activeCard.value = { ...card, unlockDateLabel: formatDate(card.unlockDate) }
  }
}
</script>

<template>
  <div class="page-wrap">
   
    <section class="container page">
      <h1 class="page-title">Prima Squadra</h1>
 <div class="coming-soon">
        <div class="coming-ball-wrap">
          <svg class="coming-ball" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <circle cx="50" cy="50" r="46" fill="#f7f3ea" stroke="var(--pitch)" stroke-width="4" />
            <path d="M 4 50 A 46 46 0 0 1 96 50 L 4 50 Z" fill="var(--pixel-green)" />
            <polygon points="35,20 44,26 41,36 29,36 26,26" fill="var(--pitch)" opacity="0.85" />
            <polygon points="63,18 73,23 71,33 60,32 58,24" fill="var(--pitch)" opacity="0.85" />
            <rect x="4" y="46" width="92" height="8" fill="var(--pitch)" />
            <circle cx="50" cy="50" r="12" fill="#f7f3ea" stroke="var(--pitch)" stroke-width="4" />
            <circle cx="50" cy="50" r="5" fill="var(--amatese-yellow)" />
          </svg>
          <span class="coming-shadow"></span>
        </div>

        <h2 class="coming-title">Prossimamente<span class="dots"><span>.</span><span>.</span><span>.</span></span></h2>

      </div>
      
      <!--
      <div class="cta-row">
        <a class="btn cta-big" href="#">▶ Classifica</a>
        <a class="btn cta-big" href="#">▶ Calendario</a>
      </div>

      <div
        v-for="(list, group) in grouped"
        :key="group"
        class="group"
      >
        <h2 class="group-title">{{ groupLabels[group] || group }}</h2>

        <div class="grid">
          <article
            v-for="(p, i) in list"
            :key="p.playerId"
            class="card-anim"
            :style="{ '--delay': (i * 0.06) + 's' }"
          >
            <div
              @click="openCard(p.playerId)"
              class="pokedex-btn unlocked player pixel-border"
            >
              <p class="player-name">{{ p.name }}</p>
              <p class="player-role">{{ p.role }}</p>
            </div>
          </article>
        </div>
      </div>

      <div class="group">
        <h2 class="group-title">Staff</h2>
        <div class="grid staff">
          <article
            v-for="(s, i) in staff"
            :key="s.id"
            class="player pixel-border staff-card card-anim"
            :style="{ '--delay': (i * 0.06) + 's' }"
          >
            <span>{{ s.role }}: </span><p class="player-name">{{ s.name }}</p>
          </article>
        </div>
      </div>
      -->

      <PokedexModal :card="activeCard" @close="activeCard = null" />
    </section>
  </div>
</template>

<style scoped>
.page-wrap {
  position: relative;
}

.page {
  padding-block: 2rem 3rem;
}

/* ---------- TITOLO ---------- */
.page-title {
  animation: fadeSlideUp 0.6s ease both;
}

/* ---------- PROSSIMAMENTE ---------- */
.coming-soon {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 4rem 1rem 5rem;
  animation: fadeSlideUp 0.6s ease both;
  animation-delay: 0.1s;
}

.coming-ball-wrap {
  position: relative;
  width: 90px;
  height: 90px;
  margin-bottom: 1.6rem;
}

.coming-ball {
  width: 100%;
  height: 100%;
  display: block;
  filter: drop-shadow(0 6px 6px rgba(0, 0, 0, 0.2));
}

.coming-shadow {
  position: absolute;
  bottom: -6px;
  left: 50%;
  width: 60px;
  height: 12px;
  background: radial-gradient(ellipse, rgba(20, 20, 20, 0.25), transparent 70%);
  border-radius: 50%;
  transform: translateX(-50%);
  animation: shadow-pulse 1.6s cubic-bezier(0.45, 0, 0.55, 1) infinite;
}

@keyframes shadow-pulse {
  0%, 100% {
    opacity: 0.7;
    transform: translateX(-50%) scale(1);
  }
  50% {
    opacity: 0.3;
    transform: translateX(-50%) scale(0.7);
  }
}

.coming-title {
  font-size: 1.1rem;
  color: var(--pitch);
  margin: 0 0 0.5rem;
  display: flex;
  align-items: baseline;
  gap: 0.1rem;
}

.dots span {
  display: inline-block;
  animation: dot-bounce 1.4s ease-in-out infinite;
}

.dots span:nth-child(2) {
  animation-delay: 0.2s;
}

.dots span:nth-child(3) {
  animation-delay: 0.4s;
}

@keyframes dot-bounce {
  0%, 60%, 100% {
    opacity: 0.3;
    transform: translateY(0);
  }
  30% {
    opacity: 1;
    transform: translateY(-3px);
  }
}


@media (prefers-reduced-motion: reduce) {
  .dots span {
    animation: none;
  }
}

.cta-row {
  display: flex;
  justify-content: start;
  gap: 1rem;
  animation: fadeSlideUp 0.6s ease both;
  animation-delay: 0.1s;
}

/* ---------- GRUPPI / CARD ---------- */
.group {
  margin-bottom: 2.2rem;
  margin-top: 2.2rem;
}

.group-title {
  font-size: 0.85rem;
  color: var(--pitch);
  border-bottom: 2px dashed var(--paper-line);
  padding-bottom: 0.5rem;
  animation: fadeSlideUp 0.5s ease both;
}

.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 1rem;
}

.grid.staff {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1rem;
}

.card-anim {
  animation: fadeSlideUp 0.5s ease both;
  animation-delay: var(--delay, 0s);
}

.staff-card {
  background: var(--pitch) !important;
  color: var(--paper);
  justify-content: space-between;
  display: flex;
  transition: transform 0.25s ease, box-shadow 0.25s ease;
}

.staff-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 10px 20px -8px rgba(0, 0, 0, 0.35);
}

.player {
  background: var(--paper);
  padding: 1rem;
}

.player-name {
  font-weight: 700;
  margin: 0 0 0.2rem;
}

.staff-card span {
  font-weight: 400;
}

.player-role {
  font-family: var(--font-mono);
  font-size: 0.78rem;
  color: var(--pitch);
  margin: 0 0 0.6rem;
}

/* ---------- CTA ---------- */
.cta-big {
  justify-content: center;
  text-align: center;
  font-size: 0.9rem;
  padding: 0.9rem 1rem;
  transition: background-color 0.2s ease, transform 0.2s ease;
}

.cta-big:hover {
  background-color: var(--paper);
  transform: translateY(-2px);
}

/* ---------- POKEDEX CARD ---------- */
.pokedex-btn.unlocked {
  transition: transform 0.25s ease, background-color 0.2s ease, box-shadow 0.25s ease;
}

.pokedex-btn.unlocked:hover {
  cursor: pointer;
  background-color: var(--amatese-yellow);
  transform: translateY(-5px) scale(1.02);
  box-shadow: 0 12px 22px -10px rgba(0, 0, 0, 0.4);
}

.pokedex-btn.unlocked:active {
  transform: translateY(-2px) scale(0.99);
}

/* ---------- KEYFRAME COMUNE ---------- */
@keyframes fadeSlideUp {
  from {
    opacity: 0;
    transform: translateY(14px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>