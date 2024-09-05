//1. 导入vue-router相关函数
import {createRouter, createWebHashHistory, createWebHistory} from "vue-router"
import HelloWorld from '../components/HelloWorld.vue'
import Demo from '../components/demo.vue'
import Login from '../components/login.vue'
// 2.路由规则
const routes = [
    {
        path: "/",
        name: "首页",
        component: HelloWorld
    },
    {
        path: "/demo",
        name: "按钮",
        component: Demo
    },
    {
        path: "/login",
        name: "登录",
        component: Login
    }
]
// 3.路由对象实例化
const router = createRouter({
    history: createWebHashHistory(),//就用这个，避免下面那个打包后无法访问的问题
    // history: createWebHistory(), // 这样可以去掉 /#，但是python静态目录加载可能会出问题
    routes
})
// 暴露导出
export default router
