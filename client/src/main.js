import {createApp} from 'vue'
import './style.css'
import App from './App.vue'

import vant from 'vant';
import {Icon} from 'vant';
import 'vant/lib/index.css';
// 导入router配置文件
import router from "./router"
// 导入阿里图标
import './assets/font/iconfont.css'
// 导入vuex,后面换pinia
// import store from './store'

const app = createApp(App)
app.use(router)
// app.use(store)
app.use(vant)
app.use(Icon)
app.mount('#app')
