<script setup>
defineProps({
  label: { type: String, default: 'Contenuto bloccato' },
  daysUntil: { type: Number, default: null },
  unlockDate: { type: String, default: null },
})
</script>

<template>
  <div class="locked">
    <div class="scanlines" aria-hidden="true"></div>
    <div class="locked-body">
      <span class="lock-icon" aria-hidden="true">▚▞</span>
      <p class="locked-label">{{ label }}</p>
      <p v-if="daysUntil !== null" class="locked-sub">
        <template v-if="daysUntil === 1">si sblocca domani</template>
        <template v-else-if="daysUntil > 1">si sblocca tra {{ daysUntil }} giorni</template>
        <template v-else>in arrivo</template>
      </p>
    </div>
  </div>
</template>

<style scoped>
.locked {
  position: relative;
  overflow: hidden;
  background: repeating-linear-gradient(45deg, var(--locked), var(--locked) 6px, #5a5e51 6px, #5a5e51 12px);
  border: 3px solid var(--pitch);
  border-radius: var(--radius-card);
  min-height: 140px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--paper);
  transition: transform 0.25s ease, filter 0.25s ease;
}

.locked:hover {
  transform: translateY(-3px);
  filter: brightness(1.05);
}

.scanlines {
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(
    to bottom,
    rgba(15, 42, 32, 0.25) 0px,
    rgba(15, 42, 32, 0.25) 1px,
    transparent 2px,
    transparent 4px
  );
  animation: scan 6s linear infinite;
}

@keyframes scan {
  from { transform: translateY(0); }
  to { transform: translateY(20px); }
}

.locked-body {
  position: relative;
  text-align: center;
  padding: 1rem;
}

.lock-icon {
  display: inline-block;
  font-family: var(--font-mono);
  font-size: 1.4rem;
  letter-spacing: 0.3em;
  animation: flicker 3.2s ease-in-out infinite;
}

@keyframes flicker {
  0%, 100% { opacity: 1; }
  4%       { opacity: 0.4; }
  6%       { opacity: 1; }
  46%      { opacity: 1; }
  48%      { opacity: 0.5; }
  50%      { opacity: 1; }
}

.locked-label {
  font-family: var(--font-mono);
  font-weight: 500;
  margin: 0.4rem 0 0.1rem;
}

.locked-sub {
  font-family: var(--font-mono);
  font-size: 0.78rem;
  opacity: 0.85;
  margin: 0;
}

@media (prefers-reduced-motion: reduce) {
  .scanlines,
  .lock-icon {
    animation: none;
  }
}
</style>