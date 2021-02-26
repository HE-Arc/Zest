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
import vuetify from './plugins/vuetify';

Vue.config.productionTip = false

new Vue({
 router,
 store,
 vuetify,
 render: h => h(App)
}).$mount('#app')
