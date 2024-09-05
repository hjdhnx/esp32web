# 客户端参考文档

## 技术框架选型

- nvm
- nodejs v22
- vue3
- yarn
- vite
- elementPlus
- vant4

## 项目从零搭建

### 参考教程 
- [vite5+vue3从零开始搭建项目](https://zhuanlan.zhihu.com/p/712512741)
- [yarn vite脚手架 react+ts搭建项目](https://blog.csdn.net/Z_Wonderful/article/details/141427566)
- [vue3+vite+vant4手机端项目实录](https://blog.csdn.net/xiaowu1127/article/details/128935132)
- [最新总结，pinia保姆级教程，十分钟快速上手！](https://zhuanlan.zhihu.com/p/664785495)
- [搭建一个vue3+vant4+vite4+pinia 的移动端h5模板](https://juejin.cn/post/7366946662281265204)

### 涉及命令

```shell
nvm install 22
nvm use 22

// 查询源
npm config get registry

// 更换国内源
npm config set registry https://registry.npmmirror.com

npm install -g cnpm --registry=https://registry.npmmirror.com
npm install -g yarn
yarn create vite
yarn add sass
yarn add node-sass sass-loader --dev
yarn add @vitejs/plugin-vue-jsx
yarn add vite-plugin-vue-setup-extend
yarn add element-plus
yarn add unplugin-vue-components unplugin-auto-import
yarn add pinia
yarn add vant
yarn add vue-router@4
yarn add axios
yarn add @vitejs/plugin-legacy
yarn add terser
```