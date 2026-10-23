import { reactive } from 'vue'

// url -> true (decodificata) | false (errore)
const state = reactive({})
const started = new Set()

export function preloadImage(url) {
  if (!url || started.has(url)) return
  started.add(url)

  const img = new Image()
  img.decoding = 'async'
  img.src = url

  const ok = () => { state[url] = true }
  const ko = () => { state[url] = false }

  if (img.decode) img.decode().then(ok).catch(ko)
  else { img.onload = ok; img.onerror = ko }
}

export const isLoaded = (url) => state[url] === true
