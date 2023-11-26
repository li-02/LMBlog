import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server:{
    https:false,
    port:8080,
    host:"0.0.0.0",
    proxy:{
      "^api/.*":{
        target:"https://127.0.0.1:5001",
        changeOrigin:true,
        rewrite:path=>path.replace(/^\/api/,"")
      }
    }
  }
})
