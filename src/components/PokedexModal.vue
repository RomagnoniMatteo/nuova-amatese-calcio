<script setup>
import { ref, watch } from 'vue'
import PokeballLoader from './PokeballLoader.vue'

const props = defineProps({
  card: { type: Object, default: null },
})

const emit = defineEmits(['close'])

const imageLoaded = ref(false)

// ogni volta che cambia la card (o si apre/chiude), resettiamo il loader
watch(
  () => props.card,
  (newCard) => {
    imageLoaded.value = !newCard?.instagramUrl
  },
  { immediate: true }
)
</script>

<template>
  <Teleport to="body">
    <transition name="modal-fade">
      <div v-if="card" class="overlay" @click.self="emit('close')">
        <transition name="modal-pop" appear>
          <div class="modal pixel-border" role="dialog" aria-modal="true" :key="card.playerId">
            <button class="close" @click="emit('close')" aria-label="Chiudi">✕</button>
            <h3>{{ card.name }}</h3>
            <div v-if="card.instagramUrl" class="image-wrap">
              <div v-if="!imageLoaded">
                <PokeballLoader />
              </div>
              <img style="max-width: 100%;" :src="card.instagramUrl" :class="{ 'is-loaded': imageLoaded }"
                alt="Pokedex giocatore Amatese" @load="imageLoaded = true" />
            </div>
            <div v-else style="margin-bottom: 2rem;">
              <p class="player-name">
                Pokedex non ancora presente :/<br />
                Guarda le statistiche intanto!
              </p>
            </div>

            <a class="btn cta-big" href="#">▶ Statistiche</a>
          </div>
        </transition>
      </div>
    </transition>
  </Teleport>
</template>

<style scoped>
.overlay {
  position: fixed;
  inset: 0;
  background: rgba(15, 42, 32, 0.75);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1.5rem;
  z-index: 50;
}

.modal {
  background: var(--paper);
  padding: 1.6rem;
  max-width: 340px;
  width: 100%;
  text-align: center;
  position: relative;
}

.close {
  position: absolute;
  top: 0.6rem;
  right: 0.7rem;
  background: none;
  border: none;
  font-size: 1.1rem;
  cursor: pointer;
  color: var(--pitch);
  transition: transform 0.2s ease, opacity 0.2s ease;
}

.close:hover {
  transform: rotate(90deg);
  opacity: 0.7;
}

.image-wrap {
  position: relative;
  min-height: 140px;
}

.image-wrap img {
  opacity: 0;
  transform: scale(0.97);
  transition: opacity 0.35s ease, transform 0.35s ease;
}

.image-wrap img.is-loaded {
  opacity: 1;
  transform: scale(1);
}

/* ---------- TRANSIZIONI OVERLAY / MODAL ---------- */
.modal-fade-enter-active,
.modal-fade-leave-active {
  transition: opacity 0.25s ease;
}

.modal-fade-enter-from,
.modal-fade-leave-to {
  opacity: 0;
}

.modal-pop-enter-active {
  transition: opacity 0.25s ease, transform 0.25s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.modal-pop-leave-active {
  transition: opacity 0.2s ease, transform 0.2s ease;
}

.modal-pop-enter-from {
  opacity: 0;
  transform: scale(0.9) translateY(8px);
}

.modal-pop-leave-to {
  opacity: 0;
  transform: scale(0.96);
}

@media (prefers-reduced-motion: reduce) {

  .modal-pop-enter-active,
  .modal-pop-leave-active,
  .modal-fade-enter-active,
  .modal-fade-leave-active {
    transition: none;
  }
}
</style>