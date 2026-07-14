<script setup>
import { ref, watch, onMounted, nextTick } from 'vue'

const props = defineProps({
  url: { type: String, required: true },
})

const wrapper = ref(null)

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
  resetBlockquote()
  await nextTick()
  const instgrm = await loadEmbedScript()
  instgrm?.Embeds?.process()
}

onMounted(render)
watch(() => props.url, render)
</script>

<template>
  <div ref="wrapper" class="ig-embed-wrap"></div>
</template>

<style scoped>
.ig-embed-wrap {
  display: flex;
  justify-content: center;
  margin: 1rem 0;
}
</style>