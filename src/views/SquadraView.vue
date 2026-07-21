<script setup>

import { computed, ref } from 'vue'
import players from '../data/pokedex.json'
import staff from '../data/staff.json'
import pokedexRaw from '../data/pokedex.json'
import { withUnlockState, formatDate } from '../composables/useUnlock'
import PokedexModal from '../components/PokedexModal.vue'
import ComingSoon from '../components/ComingSoon.vue'

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

      <ComingSoon />
       <!--
      <div class="cta-row">
        <a class="btn cta-big" href="#">▶ Classifica</a>
        <a class="btn cta-big" href="#">▶ Calendario</a>
      </div>

      <div v-for="(list, group) in grouped" :key="group" class="group">
        <h2 class="group-title">{{ groupLabels[group] || group }}</h2>

        <div class="grid">
          <article v-for="(p, i) in list" :key="p.playerId" class="card-anim" :style="{ '--delay': (i * 0.06) + 's' }">
            <div @click="openCard(p.playerId)" class="pokedex-btn unlocked player pixel-border">
              <p class="player-name">{{ p.name }}</p>
              <p class="player-role">{{ p.role }}</p>
            </div>
          </article>
        </div>
      </div>

      <div class="group">
        <h2 class="group-title">Staff</h2>
        <div class="grid staff">
          <article v-for="(s, i) in staff" :key="s.id" class="player pixel-border staff-card"
            :style="{ '--delay': (i * 0.06) + 's' }">
            <span>{{ s.role }}: </span>
            <p class="player-name">{{ s.name }}</p>
          </article>
        </div>
      </div>

      <PokedexModal :card="activeCard" @close="activeCard = null" />
    -->
    </section>
  </div>

</template>

<style scoped>
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
</style>