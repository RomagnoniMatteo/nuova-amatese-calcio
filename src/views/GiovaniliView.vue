<script setup>
import { computed, ref } from 'vue'
import teamsRaw from '../data/giovanili.json'
import '../styles/page.css'
import ComingSoon from '../components/ComingSoon.vue'

const teams = teamsRaw
const currentIndex = ref(0)
const currentTeam = computed(() => teams[currentIndex.value])

// numerazione tipo album figurine, progressiva su tutte le squadre
const startIndexOf = (teamIdx) =>
  teams.slice(0, teamIdx).reduce((sum, t) => sum + t.players.length, 0)
const totalCards = computed(() => teams.reduce((sum, t) => sum + t.players.length, 0))

function cardNumber(teamIdx, playerIdx) {
  return String(startIndexOf(teamIdx) + playerIdx + 1).padStart(3, '0')
}

function prevTeam() {
  currentIndex.value = (currentIndex.value - 1 + teams.length) % teams.length
}
function nextTeam() {
  currentIndex.value = (currentIndex.value + 1) % teams.length
}
function goTo(i) {
  currentIndex.value = i
}

const flipped = ref({})
function toggleFlip(playerId) {
  flipped.value = { ...flipped.value, [playerId]: !flipped.value[playerId] }
}

const roleClass = {
  Portiere: 'role-portiere',
  Difensore: 'role-difensore',
  Centrocampista: 'role-centrocampista',
  Attaccante: 'role-attaccante',
}

function initials(name) {
  return name
    .split(' ')
    .map((w) => w[0])
    .join('')
    .slice(0, 2)
    .toUpperCase()
}
</script>

<template>
  <section class="container page">
    <h1 class="page-title">Giovanili</h1>

    <ComingSoon />
    <!-- 
    <nav class="team-pager">
      <button class="pager-arrow" @click="prevTeam" aria-label="Squadra precedente">←</button>

      <div class="team-tabs">
        <button v-for="(t, i) in teams" :key="t.id" class="team-tab" :class="{ active: i === currentIndex }"
          @click="goTo(i)">
          {{ t.name }}
        </button>
      </div>

      <button class="pager-arrow" @click="nextTeam" aria-label="Squadra successiva">→</button>
    </nav>

    <div class="team-header pixel-border">
      <div>
        <h2 class="team-name">{{ currentTeam.name }}</h2>
        <p class="team-meta">Annata {{ currentTeam.yearRange }}</p>
      </div>
      <div class="team-meta-col">
        <p class="team-meta">👔 {{ currentTeam.coach }}</p>
      </div>
    </div>

    <div class="grid">
      <button v-for="(p, i) in currentTeam.players" :key="p.id" class="card-flip" :class="{ flipped: flipped[p.id] }"
        @click="toggleFlip(p.id)">
        <div class="card-inner">
          <div class="card-face card-front pixel-border" :class="roleClass[p.role]">
            <span class="card-number">N. {{ cardNumber(currentIndex, i) }}/{{ String(totalCards).padStart(3, '0')
              }}</span>
            <div class="avatar">
              <span class="avatar-initials">{{ initials(p.name) }}</span>
            </div>
            <p class="player-name">{{ p.name }}</p>
            <p class="player-role">{{ p.role }}</p>
          </div>

        </div>
      </button>
    </div>
    -->

  </section>
</template>

<style scoped>
/* selettore squadre */
.team-pager {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  margin-bottom: 1.2rem;
}

.pager-arrow {
  flex: none;
  background: var(--pitch);
  color: var(--paper);
  border: 3px solid var(--pixel-dark);
  border-radius: var(--radius-card);
  width: 2.4rem;
  height: 2.4rem;
  font-size: 1rem;
  cursor: pointer;
}

.team-tabs {
  display: flex;
  gap: 0.5rem;
  overflow-x: auto;
  flex: 1;
  padding-bottom: 0.2rem;
}

.team-tab {
  flex: none;
  font-family: var(--font-mono);
  font-size: 0.78rem;
  padding: 0.5rem 0.9rem;
  background: var(--paper);
  border: 2px solid var(--paper-line);
  border-radius: 999px;
  cursor: pointer;
  color: var(--ink);
}

.team-tab.active {
  background: var(--amatese-yellow);
  border-color: var(--pitch);
  font-weight: 700;
}

/* header squadra */
.team-header {
  background: var(--pitch);
  color: var(--paper);
  padding: 1.1rem 1.3rem;
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 0.6rem;
  margin-bottom: 1.6rem;
}

.team-name {
  margin: 0 0 0.2rem;
  color: var(--amatese-yellow);
  font-size: 1.1rem;
}

.team-meta-col {
  text-align: right;
}

.team-meta {
  font-family: var(--font-mono);
  font-size: 0.78rem;
  margin: 0.15rem 0;
  opacity: 0.9;
}

/* grid di figurine */
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
  gap: 1rem;
}

.card-flip {
  background: none;
  border: none;
  padding: 0;
  cursor: pointer;
  perspective: 1000px;
  height: 200px;
  width: 100%;
  font: inherit;
  text-align: left;
}

.card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  transition: transform 0.5s;
  transform-style: preserve-3d;
}

.card-flip.flipped .card-inner {
  transform: rotateY(180deg);
}

.card-face {
  position: absolute;
  inset: 0;
  backface-visibility: hidden;
  background: var(--paper);
  padding: 0.8rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  overflow: hidden;
}

/* colori per ruolo, come i "tipi" pokémon */
.role-portiere {
  border-top: 6px solid #4a7fd6;
}

.role-difensore {
  border-top: 6px solid var(--pixel-green);
}

.role-centrocampista {
  border-top: 6px solid var(--amatese-yellow);
}

.role-attaccante {
  border-top: 6px solid #d64550;
}

.card-number {
  align-self: flex-start;
  font-family: var(--font-mono);
  font-size: 0.62rem;
  color: var(--pitch);
  opacity: 0.75;
}

.avatar {
  width: 72px;
  height: 72px;
  border-radius: 50%;
  background: var(--pixel-dark);
  border: 3px solid var(--pitch);
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0.5rem 0;
}

.avatar-initials {
  font-weight: 700;
  color: var(--paper);
  font-size: 1.1rem;
  font-family: var(--font-mono);
}

.player-name {
  font-weight: 700;
  margin: 0.2rem 0 0.1rem;
  font-size: 0.85rem;
}

.player-role {
  font-family: var(--font-mono);
  font-size: 0.7rem;
  color: var(--pitch);
  margin: 0;
}

@media (max-width: 560px) {
  .team-header {
    flex-direction: column;
  }

  .team-meta-col {
    text-align: left;
  }
}
</style>