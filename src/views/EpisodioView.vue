<script setup>
import '../styles/episode.css'
import { computed, ref } from 'vue'
import { useRouter } from 'vue-router'
import episodesRaw from '../data/episodes.json'
import club from '../data/club.json'
import { isUnlocked, formatDate } from '../composables/useUnlock'
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
  <section class="container episode" v-if="episode">
    <button class="back" @click="router.push('/serie?tab=storia')">← episodi</button>
    <p class="eyebrow episode-tag">episodio {{ String(episode.number).padStart(2, '0') }} · {{ formatDate(episode.date)
      }}</p>
    <h3 class="episode-title">{{ episode.title }}</h3>

    <transition name="content-fade" mode="out-in">
      <template v-if="unlocked" :key="episode.id">
        <InstagramEmbed v-if="hasRealPost" :url="episode.instagramUrl" class="embed-anim" />
        <a v-else class="btn ig-btn embed-anim" :href="club.social.instagram" target="_blank" rel="noopener">
          📸 Vai al profilo Instagram
        </a>
      </template>
    </transition>

    <nav class="pager">
      <router-link v-if="prev" :to="`/serie/storia/${prev.id}`">← ep. {{ String(prev.number).padStart(2, '0')
        }}</router-link>
      <span v-else></span>
      <router-link v-if="next" :to="`/serie/storia/${next.id}`">ep. {{ String(next.number).padStart(2, '0') }}
        →</router-link>
    </nav>
  </section>
  <section class="container episode" v-else>
    <p>Episodio non trovato.</p>
  </section>
</template>
