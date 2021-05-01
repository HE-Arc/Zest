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
import vuetify from './plugins/vuetify'

import DatePicker from 'v-calendar/lib/components/date-picker.umd'

Vue.config.productionTip = false

Vue.component('date-picker', DatePicker)

new Vue({
 router,
 store,
 vuetify,
 render: h => h(App)
}).$mount('#app')
