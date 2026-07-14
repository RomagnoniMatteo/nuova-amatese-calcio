<script setup>
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import podcastsRaw from '../data/podcasts.json'
import { isUnlocked, formatDate } from '../composables/useUnlock'
import DialogueScript from '../components/DialogueScript.vue'
import LockedCard from '../components/LockedCard.vue'

const props = defineProps({ id: { type: String, required: true } })
const router = useRouter()

const pod = computed(() => podcastsRaw.find((p) => p.id === props.id))
const unlocked = computed(() => pod.value && isUnlocked(pod.value.date))
</script>

<template>
  <section class="container page" v-if="pod">
    <button class="back" @click="router.push('/serie?tab=podcast')">← torna al podcast</button>
    <p class="eyebrow">{{ formatDate(pod.date) }}</p>
    <h1>{{ pod.title }}</h1>

    <div v-if="unlocked" class="script-wrap pixel-border">
      <DialogueScript :script="pod.script" />
    </div>
    <LockedCard v-else label="Questa puntata non è ancora uscita" />
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
}
.script-wrap {
  background: var(--paper);
  padding: 1.5rem;
  margin-top: 1rem;
}
</style>
