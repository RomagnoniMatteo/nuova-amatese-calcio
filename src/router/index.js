import { createRouter, createWebHashHistory } from 'vue-router'

const routes = [
  { path: '/', name: 'home', component: () => import('../views/HomeView.vue') },
  { path: '/squadra', name: 'squadra', component: () => import('../views/SquadraView.vue') },
   { path: '/serie', name: 'serie', component: () => import('../views/SerieView.vue') },
  { path: '/serie/storia/:id', name: 'episodio', component: () => import('../views/EpisodioView.vue'), props: true },
  { path: '/serie/podcast/:id', name: 'podcast-episodio', component: () => import('../views/PodcastEpisodioView.vue'), props: true },
  { path: '/dove-siamo', name: 'dove-siamo', component: () => import('../views/DoveSiamoView.vue') },
  { path: '/giovanili', name: 'giovanili', component: () => import('../views/GiovaniliView.vue') },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes,
  scrollBehavior() {
    return { top: 0 }
  },
})

export default router
