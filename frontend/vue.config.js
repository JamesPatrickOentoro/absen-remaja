// const { defineConfig } = require('@vue/cli-service')
module.exports = {
  outputDir: 'frontend', // Output directory for Vue build
  devServer: {
    // disableHostCheck: true,
    allowedHosts: [
      'localhost',
      '.ngrok-free.app',
      '.ngrok.io',
    ],
    proxy: {
      '/absen': {
        target: 'http://127.0.0.1:5000', // Target URL of Flask backend
        changeOrigin: true,
        pathRewrite: {
          '^/absen': '' // Rewrite path if needed
        }
      }
    }
  }
}