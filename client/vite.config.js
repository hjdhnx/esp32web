import { defineConfig } from 'vite'

import vue from '@vitejs/plugin-vue'
import vueJsx from '@vitejs/plugin-vue-jsx'
import VueSetupExtend from 'vite-plugin-vue-setup-extend'

import AutoImport from 'unplugin-auto-import/vite'
import Components from 'unplugin-vue-components/vite'
import { ElementPlusResolver } from 'unplugin-vue-components/resolvers'

// 引入path： 别名
import { resolve } from 'path'

export default defineConfig({
  plugins: [ // 插件引用（标准vite插件放这里引用）
    vue(), // vue插件
    vueJsx(), // jsx拓展插件
    VueSetupExtend(), // setup拓展插件
    AutoImport({ // 自动引入，不需要手动去写import
      // 这里可以不需要写import调用大部分vue/vue-router/pinia方法（记住是大部分）
      imports: ['vue', 'vue-router', 'pinia'],
      // element需要通过resolvers引用
      resolvers: [ElementPlusResolver()],
      // 会自动生成eslint规则，防止eslint报错，后续selint配置的时候会讲到
      eslintrc: {
        enabled: true
      }
    }),
    Components({ // 按需引入，避免没使用的组件也打包
      resolvers: [ElementPlusResolver({ importStyle: 'sass' })]
    })
  ],
  resolve: {
    // 别名配置
    alias: [
      {
        find: '@',
        replacement: resolve(__dirname, 'src')
      }
    ]
  },
  css: {
    preprocessorOptions: {
      scss: {
        additionalData: '@use "@/style/globalvar.scss" as *;'
      }
    }
  },
  server: {
    host: '0.0.0.0', // 服务监听地址，设置该值表示监听所有
    cors: true, // 允许跨源
    port: 9527, // 本地服务端口号
    proxy: { // 代理
      '^/api': { // api地址匹配的字符串，可以使用正则，此处表示以/api为开头的接口地址
        target: 'http://xxx.com/', // 指向，表示上述需要匹配的地址都指向这个域名，注意要用/结尾
        rewrite: (path) => path.replace(/^\/api/, ''), // 如果匹配字符不需要了，可以使用重写去掉
        changeOrigin: true // 是否修改请求头的origin，让服务器认为这个请求来自本域名
      }
    }
  }
})