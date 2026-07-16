<script setup>
import { ref } from 'vue'
import club from './data/club.json'
import amateseImg from './assets/images/amatese.png'
import AnimatedBackground from './components/AnimatedBackground.vue'

const navOpen = ref(false)
const links = [
  { to: '/squadra', label: 'Prima Squadra' },
  { to: '/serie', label: 'La Serie' },
]
</script>

<template>
  <AnimatedBackground />
  <header class="topbar">
    <div class="topbar-bg" aria-hidden="true">
      <svg class="topbar-ball" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
        <circle cx="50" cy="50" r="46" fill="none" stroke="#f7f3ea" stroke-width="3" />
        <path d="M 4 50 A 46 46 0 0 1 96 50" fill="none" stroke="#f7f3ea" stroke-width="3" />
        <polygon points="35,20 44,26 41,36 29,36 26,26" fill="none" stroke="#f7f3ea" stroke-width="2.5" />
        <polygon points="63,18 73,23 71,33 60,32 58,24" fill="none" stroke="#f7f3ea" stroke-width="2.5" />
        <rect x="4" y="46" width="92" height="8" fill="none" stroke="#f7f3ea" stroke-width="3" />
        <circle cx="50" cy="50" r="12" fill="none" stroke="#f7f3ea" stroke-width="3" />
      </svg>
      <svg class="topbar-ball topbar-ball-2" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
        <circle cx="50" cy="50" r="46" fill="none" stroke="#f7f3ea" stroke-width="3" />
        <path d="M 4 50 A 46 46 0 0 1 96 50" fill="none" stroke="#f7f3ea" stroke-width="3" />
        <polygon points="35,20 44,26 41,36 29,36 26,26" fill="none" stroke="#f7f3ea" stroke-width="2.5" />
        <polygon points="63,18 73,23 71,33 60,32 58,24" fill="none" stroke="#f7f3ea" stroke-width="2.5" />
        <rect x="4" y="46" width="92" height="8" fill="none" stroke="#f7f3ea" stroke-width="3" />
        <circle cx="50" cy="50" r="12" fill="none" stroke="#f7f3ea" stroke-width="3" />
      </svg>
    </div>
    <div class="container topbar-inner">
      <router-link to="/" class="brand" @click="navOpen = false">
        <img class="logo" :src="amateseImg" />
        Amatese
      </router-link>
      <button class="nav-toggle" @click="navOpen = !navOpen" :aria-expanded="navOpen" aria-label="Apri il menu">
        <span class="burger" :class="{ open: navOpen }">
          <span></span><span></span><span></span>
        </span>
      </button>
      <nav class="nav" :class="{ open: navOpen }">
        <router-link v-for="l in links" :key="l.to" :to="l.to" @click="navOpen = false">{{ l.label }}</router-link>
        <router-link to="/dove-siamo" class="cta" @click="navOpen = false">Vieni a giocare</router-link>
      </nav>
    </div>
  </header>

  <main class="main">
    <router-view v-slot="{ Component, route }">
      <transition name="page-fade" mode="out-in">
        <component :is="Component" :key="route.path" />
      </transition>
    </router-view>
  </main>

  <footer class="footer">
    <div class="footer-bg" aria-hidden="true"></div>
    <div class="footer-line" aria-hidden="true"></div>
    <div class="footer-line footer-line-2" aria-hidden="true"></div>
    <div class="container footer-inner">
      <span class="footer-legal">{{ club.legal }}</span>
      <span class="footer-credit">
       
        © 2026 Matteo Romagnoni
      </span>
    </div>
  </footer>
</template>

<style scoped>
.page-wrap {
  position: relative;
}

.page {
  padding-block: 2rem 3rem;
}

/* ---------- TITOLO / TAB ---------- */
.page-title {
  animation: fadeSlideUp 0.6s ease both;
}

.topbar {
  position: sticky;
  top: 0;
  z-index: 20;
  background: var(--pitch);
  border-bottom: 4px solid var(--pixel-dark);
  overflow: hidden;
}

/* ---------- SFONDO ANIMATO HEADER: palloni rotanti ---------- */
.topbar-bg {
  position: absolute;
  inset: 0;
  z-index: 0;
  pointer-events: none;
  overflow: hidden;
}

.topbar-ball {
  position: absolute;
  width: 160px;
  height: 160px;
  top: 50%;
  opacity: 0.08;
  animation: ball-spin-slow 180s linear infinite;
}

.topbar-ball:first-child {
  left: -30px;
  transform: translateY(-50%);
}

.topbar-ball-2 {
  right: -40px;
  width: 200px;
  height: 200px;
  transform: translateY(-50%);
  animation-duration: 55s;
  animation-direction: reverse;
  opacity: 0.03;
}

@keyframes ball-spin-slow {
  from { transform: translateY(-50%) rotate(0deg); }
  to   { transform: translateY(-50%) rotate(360deg); }
}

.topbar-inner {
  position: relative;
  z-index: 1;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-block: 0.85rem;
  flex-wrap: wrap;
}

.logo {
  width: 25px;
  height: 25px;
  margin-right: 1rem;
  transition: transform 0.4s ease;
}

.brand:hover .logo {
  transform: rotate(-12deg) scale(1.15);
}

.brand {
  font-family: var(--font-display);
  color: var(--amatese-yellow);
  text-decoration: none;
  font-size: 0.85rem;
  display: flex;
  align-items: center;
  gap: 0.6rem;
}

.brand-dot {
  width: 12px;
  height: 12px;
  background: var(--pixel-green);
  border: 2px solid var(--pixel-dark);
}

/* hamburger animato */
.nav-toggle {
  display: none;
  background: none;
  border: 2px solid var(--amatese-yellow);
  padding: 0.4rem 0.6rem;
  border-radius: 6px;
  cursor: pointer;
}

.burger {
  display: flex;
  flex-direction: column;
  gap: 4px;
  width: 18px;
}

.burger span {
  display: block;
  height: 2px;
  background: var(--amatese-yellow);
  transition: transform 0.3s ease, opacity 0.3s ease;
}

.burger.open span:nth-child(1) {
  transform: translateY(6px) rotate(45deg);
}
.burger.open span:nth-child(2) {
  opacity: 0;
}
.burger.open span:nth-child(3) {
  transform: translateY(-6px) rotate(-45deg);
}

.nav {
  display: flex;
  align-items: center;
  gap: 1.4rem;
  font-family: var(--font-mono);
  font-size: 0.85rem;
}

.nav a {
  position: relative;
  color: var(--paper);
  text-decoration: none;
  opacity: 0.85;
  padding-bottom: 2px;
  border-bottom: 2px solid transparent;
  transition: opacity 0.2s ease, color 0.2s ease, border-color 0.2s ease;
}

.nav a:hover,
.nav a.router-link-exact-active {
  opacity: 1;
  color: var(--amatese-yellow);
  border-bottom-color: var(--amatese-yellow);
}

.nav a.cta {
  background: var(--amatese-yellow);
  color: var(--pitch-dark);
  opacity: 1;
  padding: 0.4rem 0.8rem;
  border-radius: 999px;
  border-bottom: none;
  font-weight: 700;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.nav a.cta:hover {
  color: var(--pitch-dark);
  border-bottom: none;
  transform: translateY(-2px);
  box-shadow: 0 8px 16px -8px rgba(0, 0, 0, 0.5);
}

.main {
  flex: 1;
}

/* transizione tra pagine */
.page-fade-enter-active,
.page-fade-leave-active {
  transition: opacity 0.25s ease, transform 0.25s ease;
}
.page-fade-enter-from {
  opacity: 0;
  transform: translateY(10px);
}
.page-fade-leave-to {
  opacity: 0;
  transform: translateY(-6px);
}
.footer {
  position: relative;
  background: var(--pixel-dark);
  color: var(--pixel-green);
  font-family: var(--font-mono);
  font-size: 0.8rem;
  padding: 1.2rem 0;
  overflow: hidden;
}


/* ---------- LINEE LUMINOSE ---------- */
.footer-line {
  position: absolute;
  top: 0;
  left: -30%;
  width: 30%;
  height: 2px;
  background: linear-gradient(90deg, transparent, var(--pixel-green), transparent);
  animation: line-sweep 6s linear infinite;
}

.footer-line-2 {
  top: auto;
  bottom: 0;
  width: 20%;
  animation: line-sweep 8s linear infinite;
  animation-delay: 2.5s;
  opacity: 0.6;
}

@keyframes line-sweep {
  0%   { left: -30%; }
  100% { left: 100%; }
}

/* ---------- CONTENUTO ---------- */
.footer-inner {
  position: relative;
  z-index: 1;
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 0.5rem;
  align-items: center;
}

.footer-legal {
  transition: color 0.3s ease;
}

.footer-legal:hover {
  color: var(--paper);
}

.footer-credit {
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
}



@media (prefers-reduced-motion: reduce) {
  .footer-bg,
  .footer-line {
    animation: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .topbar-ball,
  .footer-line {
    animation: none;
  }
  .page-fade-enter-active,
  .page-fade-leave-active {
    transition: none;
  }
}

@media (max-width: 640px) {
  .nav-toggle {
    display: inline-block;
  }
  .nav {
    display: none;
    flex-direction: column;
    align-items: flex-start;
    width: 100%;
    gap: 1rem;
    padding-top: 1rem;
    padding-bottom: 1rem;
  }
  .nav.open {
    display: flex;
    border-top: 1px solid var(--amatese-yellow);
    border-bottom: 1px solid var(--amatese-yellow);
    align-items: center;
    margin-top: 1.5rem;
    animation: nav-drop 0.3s ease;
  }
}

@keyframes nav-drop {
  from {
    opacity: 0;
    transform: translateY(-8px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* ---------- KEYFRAME COMUNE ---------- */
@keyframes fadeSlideUp {
  from {
    opacity: 0;
    transform: translateY(14px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

</style>