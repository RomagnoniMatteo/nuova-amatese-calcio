<script setup>
import { computed, ref } from 'vue'
import players from '../data/players.json'
import staff from '../data/staff.json'
import pokedexRaw from '../data/pokedex.json'
import { withUnlockState, formatDate } from '../composables/useUnlock'
import PokedexModal from '../components/PokedexModal.vue'


const pokedex = withUnlockState(pokedexRaw, 'unlockDate')

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
  <section class="container page">
    <h1>Prima Squadra</h1>

    <div class="group">
       <h2 class="group-title">Staff</h2>
    <div class="grid">
      <article v-for="s in staff" :key="s.id" class="player pixel-border staff-card">
        <p class="player-name">{{ s.name }}</p>
        <p class="player-role">{{ s.role }}</p>
        <p class="player-bio">{{ s.bio }}</p>
      </article>
    </div>
    </div>

      <h2 class="group-title">Giocatori</h2>
      <div class="grid">
        <article v-for="p in players" :key="p.id" class="player pixel-border">
          <p class="player-name">{{ p.name }}</p>
          <p class="player-role">{{ p.role }}</p>

          <template v-if="cardFor(p.id)">
            <button
              v-if="cardFor(p.id).unlocked"
              class="pokedex-btn unlocked"
              @click="openCard(p.id)"
            >
              🟢 Apri scheda pokédex
            </button>
            <p v-else class="pokedex-btn locked">
             🔒 Il Pokedex si sblocca il {{ formatDate(cardFor(p.id).unlockDate) }}
            </p>
          </template>
        </article>
      </div>

    <PokedexModal :card="activeCard" @close="activeCard = null" />
  </section>
</template>

<style scoped>
.page {
  padding-block: 2rem 3rem;
}
.group {
  margin-bottom: 2.2rem;
}
.group-title {
  font-size: 0.85rem;
  color: var(--pitch);
  border-bottom: 2px dashed var(--paper-line);
  padding-bottom: 0.5rem;
}
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 1rem;
}
.player {
  background: var(--paper);
  padding: 1rem;
}
.player-name {
  font-weight: 700;
  margin: 0 0 0.2rem;
}
.player-role {
  font-family: var(--font-mono);
  font-size: 0.78rem;
  color: var(--pitch);
  margin: 0 0 0.6rem;
}
.pokedex-btn {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  border-radius: 6px;
  padding: 0.45rem 0.6rem;
  margin: 0;
  display: block;
  width: 100%;
  text-align: left;
}
.pokedex-btn.unlocked {
  background: var(--pixel-green);
  border: 2px solid var(--pitch);
  color: var(--ink);
  cursor: pointer;
}
.pokedex-btn.locked {
  background: repeating-linear-gradient(45deg, var(--locked), var(--locked) 4px, #5a5e51 4px, #5a5e51 8px);
  color: var(--paper);
  border: 2px solid var(--pitch);
}
.player-bio {
  font-size: 0.88rem;
  margin: 0;
}
</style>
