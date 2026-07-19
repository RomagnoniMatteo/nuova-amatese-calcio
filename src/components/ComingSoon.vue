<template>
  <div class="coming-soon">
    <div class="coming-ball-wrap">
      <svg class="coming-ball" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
        <circle cx="50" cy="50" r="46" fill="#f7f3ea" stroke="var(--pitch)" stroke-width="4" />
        <path d="M 4 50 A 46 46 0 0 1 96 50 L 4 50 Z" fill="var(--pixel-green)" />
        <polygon points="35,20 44,26 41,36 29,36 26,26" fill="var(--pitch)" opacity="0.85" />
        <polygon points="63,18 73,23 71,33 60,32 58,24" fill="var(--pitch)" opacity="0.85" />
        <rect x="4" y="46" width="92" height="8" fill="var(--pitch)" />
        <circle cx="50" cy="50" r="12" fill="#f7f3ea" stroke="var(--pitch)" stroke-width="4" />
        <circle cx="50" cy="50" r="5" fill="var(--amatese-yellow)" />
      </svg>
      <span class="coming-shadow"></span>
    </div>

    <h2 class="coming-title">Prossimamente<span class="dots"><span>.</span><span>.</span><span>.</span></span></h2>

  </div>
</template>
<style scoped>
.coming-soon {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 4rem 1rem 5rem;
  animation: fadeSlideUp 0.6s ease both;
  animation-delay: 0.1s;
}

.coming-ball-wrap {
  position: relative;
  width: 90px;
  height: 90px;
  margin-bottom: 1.6rem;
}

.coming-ball {
  width: 100%;
  height: 100%;
  display: block;
  filter: drop-shadow(0 6px 6px rgba(0, 0, 0, 0.2));
}

.coming-shadow {
  position: absolute;
  bottom: -6px;
  left: 50%;
  width: 60px;
  height: 12px;
  background: radial-gradient(ellipse, rgba(20, 20, 20, 0.25), transparent 70%);
  border-radius: 50%;
  transform: translateX(-50%);
  animation: shadow-pulse 1.6s cubic-bezier(0.45, 0, 0.55, 1) infinite;
}

@keyframes shadow-pulse {

  0%,
  100% {
    opacity: 0.7;
    transform: translateX(-50%) scale(1);
  }

  50% {
    opacity: 0.3;
    transform: translateX(-50%) scale(0.7);
  }
}

.coming-title {
  font-size: 1.1rem;
  color: var(--pitch);
  margin: 0 0 0.5rem;
  display: flex;
  align-items: baseline;
  gap: 0.1rem;
}

.dots span {
  display: inline-block;
  animation: dot-bounce 1.4s ease-in-out infinite;
}

.dots span:nth-child(2) {
  animation-delay: 0.2s;
}

.dots span:nth-child(3) {
  animation-delay: 0.4s;
}

@keyframes dot-bounce {

  0%,
  60%,
  100% {
    opacity: 0.3;
    transform: translateY(0);
  }

  30% {
    opacity: 1;
    transform: translateY(-3px);
  }
}


@media (prefers-reduced-motion: reduce) {
  .dots span {
    animation: none;
  }
}
</style>