<script setup>
defineProps({
  script: { type: Array, required: true },
})

// Give each unique speaker a stable color from a small rotating palette
const palette = ['#1b4332', '#9d4b2c', '#3a5a9b', '#7a5c9e', '#2f7a4f', '#a13d4f']
const speakerColor = (() => {
  const cache = new Map()
  return (name) => {
    const key = name.toLowerCase()
    if (!cache.has(key)) {
      cache.set(key, palette[cache.size % palette.length])
    }
    return cache.get(key)
  }
})()
</script>

<template>
  <div class="script">
    <template v-for="(item, i) in script" :key="i">
      <p v-if="item.type === 'stage'" class="stage">{{ item.text }}</p>
      <p v-else-if="item.type === 'note'" class="note">{{ item.text }}</p>
      <p v-else class="line">
        <span class="speaker" :style="{ color: speakerColor(item.speaker) }">{{ item.speaker }}</span>
        <span class="text">{{ item.text }}</span>
      </p>
    </template>
  </div>
</template>

<style scoped>
.script {
  font-family: var(--font-body);
  line-height: 1.65;
}
.line {
  margin: 0 0 0.85rem;
  display: flex;
  gap: 0.6rem;
  flex-wrap: wrap;
}
.speaker {
  font-family: var(--font-mono);
  font-weight: 700;
  white-space: nowrap;
}
.speaker::after {
  content: ':';
}
.text {
  flex: 1;
  min-width: 200px;
}
.stage {
  font-style: italic;
  color: var(--pitch);
  background: rgba(27, 67, 50, 0.08);
  padding: 0.5rem 0.75rem;
  border-left: 3px solid var(--pitch);
  border-radius: 4px;
  margin: 1rem 0;
}
.note {
  font-family: var(--font-mono);
  font-size: 0.85rem;
  color: var(--locked);
}
</style>
