<script setup>
import { computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import episodesRaw from '../data/episodes.json'
import podcastsRaw from '../data/podcasts.json'
import { withUnlockState, formatDate } from '../composables/useUnlock'
import LockedCard from '../components/LockedCard.vue'

const route = useRoute()
const router = useRouter()

const tab = computed(() => (route.query.tab === 'podcast' ? 'podcast' : 'storia'))
function setTab(t) {
  router.replace({ path: '/serie', query: { tab: t } })
}

const episodes = withUnlockState(episodesRaw, 'date')
const podcasts = withUnlockState(podcastsRaw, 'date').slice().reverse()
</script>

<template>
  <section class="container page">
    <h1>La Serie</h1>
    <div class="tabs" role="tablist">
      <button role="tab" :aria-selected="tab === 'storia'" :class="{ active: tab === 'storia' }" @click="setTab('storia')">
        📖 Storia
      </button>
      
      <button role="tab" :aria-selected="tab === 'podcast'" :class="{ active: tab === 'podcast' }" @click="setTab('podcast')">
        🎙️ Podcast
      </button>
    </div>

    <div v-if="tab === 'storia'" class="tab-panel">
      <p class="eyebrow">Prima stagione</p>
      <ol class="timeline">
        <li v-for="ep in episodes" :key="ep.id" class="entry">
          <span class="ep-number">{{ String(ep.number).padStart(2, '0') }}</span>
          <router-link v-if="ep.unlocked" :to="`/serie/storia/${ep.id}`" class="entry-card pixel-border">
            <p class="entry-date">{{ formatDate(ep.date) }}</p>
            <p class="entry-title">{{ ep.title }}</p>
          </router-link>
          <LockedCard v-else label="Episodio bloccato" :days-until="ep.daysUntil" :unlock-date="ep.date" />
        </li>
      </ol>
    </div>

    <div v-else class="tab-panel">
      <div class="grid">
        <template v-for="p in podcasts" :key="p.id">
          <router-link v-if="p.unlocked" :to="`/serie/podcast/${p.id}`" class="card pixel-border">
            <p class="card-date">{{ formatDate(p.date) }}</p>
            <p class="card-title">{{ p.title }}</p>
          </router-link>
          <LockedCard v-else label="Puntata in arrivo" :days-until="p.daysUntil" />
        </template>
      </div>
    </div>
  </section>
</template>

<style scoped>
.page {
  padding-block: 2rem 3rem;
}
.tabs {
  display: flex;
  gap: 0.6rem;
  margin: 1.5rem 0;
  border-bottom: 3px solid var(--pitch);
}
.tabs button {
  font-family: var(--font-mono);
  font-size: 0.85rem;
  background: none;
  border: none;
  padding: 0.6rem 1rem;
  cursor: pointer;
  color: var(--pitch);
  opacity: 0.6;
  border-bottom: 3px solid transparent;
  margin-bottom: -3px;
}
.tabs button.active {
  opacity: 1;
  border-bottom-color: var(--amatese-yellow);
  font-weight: 700;
}
.tab-panel {
  margin-top: 1rem;
}
.timeline {
  list-style: none;
  padding: 0;
  margin: 1rem 0 0;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
.entry {
  display: grid;
  grid-template-columns: 3rem 1fr;
  gap: 1rem;
  align-items: stretch;
}
.ep-number {
  font-family: var(--font-display);
  font-size: 0.85rem;
  color: var(--pitch);
  align-self: center;
  text-align: center;
}
.entry-card {
  background: var(--paper);
  text-decoration: none;
  color: var(--ink);
  padding: 0.9rem 1.1rem;
  display: block;
}
.entry-card:hover {
  border-color: var(--amatese-yellow);
}
.entry-date {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  color: var(--pitch);
  margin: 0 0 0.2rem;
}
.entry-title {
  margin: 0;
  font-weight: 700;
}
.preview {
  width: 100%;
  max-width: 420px;
  border-radius: var(--radius-card);
  border: 3px solid var(--pitch);
  margin-bottom: 1rem;
  display: block;
}
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(230px, 1fr));
  gap: 1rem;
}
.card {
  background: var(--pitch);
  color: var(--paper);
  text-decoration: none;
  padding: 1rem;
  min-height: 140px;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
}
.card:hover {
  border-color: var(--amatese-yellow);
}
.card-date {
  font-family: var(--font-mono);
  font-size: 0.7rem;
  color: var(--pixel-green);
  margin: 0 0 0.3rem;
}
.card-title {
  margin: 0;
  font-weight: 700;
  font-size: 0.95rem;
}
</style>