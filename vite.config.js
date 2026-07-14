import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// Relative base ('./') so the build works when served from
// https://<user>.github.io/<repo>/ without extra configuration.
export default defineConfig({
  plugins: [vue()],
  base: './',
})
