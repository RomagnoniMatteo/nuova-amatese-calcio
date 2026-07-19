<template>
  <div class="bg-fx" aria-hidden="true">
    <span class="blob blob-1"></span>
    <span class="blob blob-2"></span>
    <span class="blob blob-3"></span>
    <span class="bg-grid"></span>
  </div>
</template>

<style scoped>
.bg-fx {
  position: fixed;
  inset: 0;
  z-index: -1;
  overflow: hidden;
  pointer-events: none;
}

.blob {
  position: absolute;
  border-radius: 50%;
  filter: blur(60px);
  opacity: 0.35;
  mix-blend-mode: multiply;
  will-change: transform;
}

.blob-1 {
  width: 420px;
  height: 420px;
  top: -10vh;
  left: -8vw;
  background: var(--pitch);
  animation: float1 18s ease-in-out infinite;
}

.blob-2 {
  width: 340px;
  height: 340px;
  top: 40vh;
  right: -6vw;
  background: var(--amatese-yellow, #f4c542);
  animation: float2 22s ease-in-out infinite;
}

.blob-3 {
  width: 300px;
  height: 300px;
  bottom: -8vh;
  left: 30vw;
  background: var(--paper-line, #cfcabf);
  animation: float3 26s ease-in-out infinite;
}

.bg-grid {
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(var(--paper-line) 1px, transparent 1px),
    linear-gradient(90deg, var(--paper-line) 1px, transparent 1px);
  background-size: 42px 42px;
  opacity: 0.06;
  animation: drift 40s linear infinite;
}

@keyframes float1 {

  0%,
  100% {
    transform: translate(0, 0) scale(1);
  }

  33% {
    transform: translate(60px, 40px) scale(1.1);
  }

  66% {
    transform: translate(-30px, 70px) scale(0.95);
  }
}

@keyframes float2 {

  0%,
  100% {
    transform: translate(0, 0) scale(1);
  }

  50% {
    transform: translate(-70px, -50px) scale(1.15);
  }
}

@keyframes float3 {

  0%,
  100% {
    transform: translate(0, 0) rotate(0deg);
  }

  50% {
    transform: translate(50px, -30px) rotate(20deg);
  }
}

@keyframes drift {
  0% {
    transform: translate(0, 0);
  }

  100% {
    transform: translate(42px, 42px);
  }
}

@media (prefers-reduced-motion: reduce) {

  .blob,
  .bg-grid {
    animation: none;
  }
}
</style>