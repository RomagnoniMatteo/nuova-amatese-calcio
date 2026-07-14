<script setup>
defineProps({
  card: { type: Object, default: null },
})
const emit = defineEmits(['close'])
</script>

<template>
  <Teleport to="body">
    <div v-if="card" class="overlay" @click.self="emit('close')">
      <div class="modal pixel-border" role="dialog" aria-modal="true">
        <button class="close" @click="emit('close')" aria-label="Chiudi">✕</button>
        <div class="card-head">
          <span class="number">#{{ String(card.number).padStart(3, '0') }}</span>
        </div>
        <div class="portrait">🟢</div>
        <h2 class="name">{{ card.name }}</h2>
        <p class="role">{{ card.role }}</p>
        <div class="desc">
          <p class="desc-label">Descrizione:</p>
          <p>{{ card.description }}</p>
        </div>
        <p class="unlock-note">Scheda sbloccata il {{ card.unlockDateLabel }}</p>
      </div>
    </div>
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
}
.card-head {
  display: flex;
  justify-content: flex-end;
}
.number {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  color: var(--pitch);
}
.portrait {
  width: 96px;
  height: 96px;
  margin: 0.2rem auto 0.6rem;
  border-radius: 50%;
  background: var(--pixel-green);
  border: 2px solid var(--pitch);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2rem;
}
.name {
  font-size: 1rem;
  margin: 0.2rem 0 0.1rem;
}
.role {
  font-family: var(--font-mono);
  font-size: 0.78rem;
  color: var(--pitch);
  margin: 0 0 0.8rem;
}
.desc {
  background: rgba(27, 67, 50, 0.06);
  border-radius: 8px;
  padding: 0.8rem;
  text-align: left;
}
.desc-label {
  font-family: var(--font-mono);
  font-size: 0.7rem;
  color: var(--pitch);
  margin: 0 0 0.3rem;
}
.desc p {
  font-size: 0.85rem;
  margin: 0;
}
.unlock-note {
  font-family: var(--font-mono);
  font-size: 0.7rem;
  color: var(--locked);
  margin-top: 0.8rem;
}
</style>
