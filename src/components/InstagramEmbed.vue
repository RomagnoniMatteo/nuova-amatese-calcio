<script setup>
import { ref, watch, onMounted, nextTick } from 'vue'

const props = defineProps({
  url: { type: String, required: true },
})

const wrapper = ref(null)
const ready = ref(false)

function loadEmbedScript() {
  return new Promise((resolve) => {
    if (window.instgrm) {
      resolve(window.instgrm)
      return
    }
    const existing = document.querySelector('script[data-instagram-embed]')
    if (existing) {
      existing.addEventListener('load', () => resolve(window.instgrm))
      return
    }
    const script = document.createElement('script')
    script.src = 'https://www.instagram.com/embed.js'
    script.async = true
    script.dataset.instagramEmbed = 'true'
    script.onload = () => resolve(window.instgrm)
    document.body.appendChild(script)
  })
}

function resetBlockquote() {
  if (!wrapper.value) return
  wrapper.value.innerHTML = `
    <blockquote
      class="instagram-media"
      data-instgrm-permalink="${props.url}"
      data-instgrm-version="14"
      style="background:#FFF; border:0; border-radius:3px; margin: 0 auto; max-width:540px; width:100%;"
    >
      <a href="${props.url}" target="_blank" rel="noopener">Visualizza il post su Instagram</a>
    </blockquote>
  `
}

async function render() {
  ready.value = false
  resetBlockquote()
  await nextTick()
  const instgrm = await loadEmbedScript()
  instgrm?.Embeds?.process()
  // l'embed di Instagram non espone un evento "completato" affidabile,
  // quindi diamo un piccolo margine prima di mostrare il contenuto finale
  setTimeout(() => {
    ready.value = true
  }, 400)
}

onMounted(render)
watch(() => props.url, render)
</script>

<template>
  <div class="ig-embed-outer">
    <div v-if="!ready" class="ig-skeleton" aria-hidden="true">
      <div class="skeleton-header">
        <span class="skeleton-avatar"></span>
        <span class="skeleton-line short"></span>
      </div>
      <span class="skeleton-line block"></span>
    </div>
    <div ref="wrapper" class="ig-embed-wrap" :class="{ 'is-ready': ready }"></div>
  </div>
</template>

<style scoped>
.ig-embed-outer {
  position: relative;
  margin: 1rem 0;
}

.ig-embed-wrap {
  display: flex;
  justify-content: center;
  opacity: 0;
  transform: translateY(6px);
  transition: opacity 0.4s ease, transform 0.4s ease;
}

.ig-embed-wrap.is-ready {
  opacity: 1;
  transform: translateY(0);
}

/* ---------- SKELETON ---------- */
.ig-skeleton {
  max-width: 540px;
  width: 100%;
  margin: 0 auto;
  padding: 1rem;
  background: var(--paper);
  border: 3px solid var(--pitch);
  border-radius: 3px;
}

.skeleton-header {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  margin-bottom: 0.9rem;
}

.skeleton-avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: var(--paper-line, #e2ded3);
  animation: pulse 1.4s ease-in-out infinite;
}

.skeleton-line {
  display: block;
  border-radius: 4px;
  background: var(--paper-line, #e2ded3);
  animation: pulse 1.4s ease-in-out infinite;
}

.skeleton-line.short {
  width: 40%;
  height: 12px;
}

.skeleton-line.block {
  width: 100%;
  height: 260px;
}

@keyframes pulse {

  0%,
  100% {
    opacity: 0.6;
  }

  50% {
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {

  .skeleton-avatar,
  .skeleton-line {
    animation: none;
  }

  .ig-embed-wrap {
    transition: none;
  }
}
</style>