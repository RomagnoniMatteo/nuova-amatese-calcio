<script setup>
import { ref } from 'vue'
import club from './data/club.json'
import amateseImg from './assets/images/amatese.png'

const navOpen = ref(false)
//{ to: '/squadra', label: 'Prima Squadra' },
const links = [
  { to: '/serie', label: 'La Serie' },
]
</script>

<template>
  <header class="topbar">
    <div class="container topbar-inner">
      <router-link to="/" class="brand" @click="navOpen = false">
        <img class="logo" :src="amateseImg"/>
       Amatese
      </router-link>
      <button class="nav-toggle" @click="navOpen = !navOpen" :aria-expanded="navOpen" aria-label="Apri il menu">
        ☰
      </button>
      <nav class="nav" :class="{ open: navOpen }">
        <router-link v-for="l in links" :key="l.to" :to="l.to" @click="navOpen = false">{{ l.label }}</router-link>
        <router-link to="/dove-siamo" class="cta" @click="navOpen = false">Vieni a giocare</router-link>
      </nav>
    </div>
  </header>

  <main class="main">
    <router-view />
  </main>

  <footer class="footer">
    <div class="container footer-inner">
      <span> {{club.legal}}</span>
      <span>
        © 2026 Matteo Romagnoni
      </span>
    </div>
  </footer>
</template>

<style scoped>
.topbar {
  background: var(--pitch);
  border-bottom: 4px solid var(--pixel-dark);
  position: sticky;
  top: 0;
  z-index: 20;
}

.logo{
   width: 25px;
  height: 25px;
  margin-right: 1rem;
}
.topbar-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-block: 0.85rem;
  flex-wrap: wrap;
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
.nav-toggle {
  display: none;
  background: none;
  border: 2px solid var(--amatese-yellow);
  color: var(--amatese-yellow);
  font-size: 1.1rem;
  padding: 0.2rem 0.6rem;
  border-radius: 6px;
}
.nav {
  display: flex;
  align-items: center;
  gap: 1.4rem;
  font-family: var(--font-mono);
  font-size: 0.85rem;
}
.nav a {
  color: var(--paper);
  text-decoration: none;
  opacity: 0.85;
  padding-bottom: 2px;
  border-bottom: 2px solid transparent;
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
}
.nav a.cta:hover {
  color: var(--pitch-dark);
  border-bottom: none;
  transform: translateY(-1px);
}
.main {
  flex: 1;
}
.footer {
  background: var(--pixel-dark);
  color: var(--pixel-green);
  font-family: var(--font-mono);
  font-size: 0.8rem;
  padding: 1.2rem 0;
}
.footer-inner {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 0.5rem;
}

@media (max-width: 640px) {
  .nav-toggle { display: inline-block; }
  .nav {
    display: none;
    flex-direction: column;
    align-items: flex-start;
    width: 100%;
    gap: 0.6rem;
    padding-top: 0.8rem;
  }
  .nav.open { display: flex; }
}
</style>
