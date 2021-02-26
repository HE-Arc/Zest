/**
 *      ___           ___           ___                   
 *     /__/\         /  /\         /  /\          ___     
 *     \  \:\       /  /::\       /  /::\        /__/\    
 *      \  \:\     /  /:/\:\     /__/:/\:\       \  \:\   
 *       \  \:\   /  /::\ \:\   _\_ \:\ \:\       \__\:\  
 *  ______\__\:\ /__/:/\:\ \:\ /__/\ \:\ \:\      /  /::\ 
 * \  \::::::::/ \  \:\ \:\_\/ \  \:\ \:\_\/     /  /:/\:\
 *  \  \:\~~~~~   \  \:\ \:\    \  \:\_\:\      /  /:/__\/
 *   \  \:\        \  \:\_\/     \  \:\/:/     /__/:/     
 *    \  \:\        \  \:\        \  \::/      \__\/      
 *     \__\/         \__\/         \__\/         
 * 
 * by Danz Robin, Mendes Reis Steve, Fridez Lucas
 */

import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
