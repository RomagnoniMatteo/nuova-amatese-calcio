<script setup>
import { computed, ref } from 'vue'
import { useRouter } from 'vue-router'
import podcastsRaw from '../data/podcasts.json'
import club from '../data/club.json'
import { isUnlocked, formatDate } from '../composables/useUnlock'
import InstagramEmbed from '../components/InstagramEmbed.vue'

const props = defineProps({ id: { type: String, required: true } })
const router = useRouter()

const episode = computed(() => podcastsRaw.find((e) => e.id === props.id))
const unlocked = computed(() => episode.value && isUnlocked(episode.value.date))
const hasRealPost = computed(() => !!episode.value?.instagramUrl)
const showText = ref(false)

const index = computed(() => podcastsRaw.findIndex((e) => e.id === props.id))
const prev = computed(() => podcastsRaw[index.value - 1])
const next = computed(() => podcastsRaw[index.value + 1])
</script>

<template>
  <section class="container page" v-if="episode">
    <button class="back" @click="router.push('/serie?tab=podcast')">← torna alla serie</button>
    <p class="eyebrow episode-tag">puntata {{ String(episode.number).padStart(2, '0') }} · {{ formatDate(episode.date) }}</p>
    <h1 class="episode-title">{{ episode.title }}</h1>

    <transition name="content-fade" mode="out-in">
      <template v-if="unlocked" :key="episode.id">
        <InstagramEmbed v-if="hasRealPost" :url="episode.instagramUrl" class="embed-anim" />
        <a v-else class="btn ig-btn embed-anim" :href="club.social.instagram" target="_blank" rel="noopener">
          📸 Vai al profilo Instagram
        </a>
      </template>
    </transition>

    <nav class="pager">
      <router-link v-if="prev" :to="`/serie/podcast/${prev.id}`">← ep. {{ String(prev.number).padStart(2, '0') }}</router-link>
      <span v-else></span>
      <router-link v-if="next" :to="`/serie/podcast/${next.id}`">ep. {{ String(next.number).padStart(2, '0') }} →</router-link>
    </nav>
  </section>
  <section class="container page" v-else>
    <p>Puntata non trovata.</p>
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
  transition: transform 0.2s ease, opacity 0.2s ease;
}

.back:hover {
  transform: translateX(-3px);
  opacity: 0.75;
}

.episode-tag {
  animation: fadeSlideUp 0.5s ease both;
}

.episode-title {
  animation: fadeSlideUp 0.5s ease both;
  animation-delay: 0.08s;
}

.content-fade-enter-active {
  transition: opacity 0.35s ease, transform 0.35s ease;
}
.content-fade-enter-from {
  opacity: 0;
  transform: translateY(10px);
}

.embed-anim {
  animation: fadeSlideUp 0.5s ease both;
  animation-delay: 0.16s;
}

.ig-btn {
  margin-top: 0.8rem;
  background: linear-gradient(135deg, #f2c94c, #d64550, #833ab4);
  background-size: 200% 200%;
  color: #fff;
  border-color: var(--pitch-dark);
  transition: background-position 0.6s ease, transform 0.2s ease, box-shadow 0.2s ease;
}

.ig-btn:hover {
  background-position: 100% 100%;
  transform: translateY(-2px);
  box-shadow: 0 10px 20px -10px rgba(0, 0, 0, 0.5);
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
  animation: fadeSlideUp 0.5s ease both;
  animation-delay: 0.24s;
}

.pager a {
  text-decoration: none;
  color: var(--pitch);
  transition: transform 0.2s ease, opacity 0.2s ease;
  display: inline-block;
}

.pager a:hover {
  opacity: 0.7;
}

.pager a:first-child:hover {
  transform: translateX(-3px);
}

.pager a:last-child:hover {
  transform: translateX(3px);
}

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