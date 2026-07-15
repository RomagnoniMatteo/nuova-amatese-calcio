<script setup>
import { computed, ref } from 'vue'
import { useRouter } from 'vue-router'
import episodesRaw from '../data/podcasts.json'
import club from '../data/club.json'
import { isUnlocked, formatDate } from '../composables/useUnlock'
import DialogueScript from '../components/DialogueScript.vue'
import LockedCard from '../components/LockedCard.vue'
import InstagramEmbed from '../components/InstagramEmbed.vue'

const props = defineProps({ id: { type: String, required: true } })
const router = useRouter()

const episode = computed(() => episodesRaw.find((e) => e.id === props.id))
const unlocked = computed(() => episode.value && isUnlocked(episode.value.date))
const hasRealPost = computed(() => !!episode.value?.instagramUrl)
const showText = ref(false)

const index = computed(() => episodesRaw.findIndex((e) => e.id === props.id))
const prev = computed(() => episodesRaw[index.value - 1])
const next = computed(() => episodesRaw[index.value + 1])
</script>

<template>
  <section class="container page" v-if="episode">
    <button class="back" @click="router.push('/serie?tab=storia')">← torna alla serie</button>
    <p class="eyebrow">episodio {{ String(episode.number).padStart(2, '0') }} · {{ formatDate(episode.date) }}</p>
    <h1>{{ episode.title }}</h1>

    <template v-if="unlocked">
      <InstagramEmbed v-if="hasRealPost" :url="episode.instagramUrl" />
      <a v-else class="btn ig-btn" :href="club.social.instagram" target="_blank" rel="noopener">
        📸 Vai al profilo Instagram
      </a>
    </template>

    <div v-if="unlocked && (showText || !hasRealPost)" class="script-wrap pixel-border">
      <DialogueScript :script="episode.script" />
    </div>
    <LockedCard v-else-if="!unlocked" label="Questo episodio non è ancora uscito" />

    <nav class="pager">
      <router-link v-if="prev" :to="`/serie/storia/${prev.id}`">← ep. {{ String(prev.number).padStart(2, '0') }}</router-link>
      <span v-else></span>
      <router-link v-if="next" :to="`/serie/storia/${next.id}`">ep. {{ String(next.number).padStart(2, '0') }} →</router-link>
    </nav>
  </section>
  <section class="container page" v-else>
    <p>Episodio non trovato.</p>
  </section>
</template>

<style scoped>
.page {
  padding-block: 2rem 3rem;
  max-width: 760px;
}
.back {
  background: none;
  border: none;
  font-family: var(--font-mono);
  color: var(--pitch);
  cursor: pointer;
  padding: 0;
  margin-bottom: 1rem;
  font-size: 0.85rem;
}
.ig-btn {
  margin-top: 0.8rem;
  background: linear-gradient(135deg, #f2c94c, #d64550, #833ab4);
  color: #fff;
  border-color: var(--pitch-dark);
}
.toggle-text {
  display: block;
  margin: 1rem 0 0;
  background: none;
  border: none;
  font-family: var(--font-mono);
  font-size: 0.78rem;
  color: var(--pitch);
  cursor: pointer;
  text-decoration: underline dotted;
  padding: 0;
}
.script-wrap {
  background: var(--paper);
  padding: 1.5rem;
  margin-top: 1.2rem;
}
.pager {
  display: flex;
  justify-content: space-between;
  margin-top: 2rem;
  font-family: var(--font-mono);
  font-size: 0.85rem;
}
.pager a {
  text-decoration: none;
  color: var(--pitch);
}
</style>
