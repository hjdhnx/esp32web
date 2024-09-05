<script setup>
import {ref} from 'vue'
import {useRouter} from 'vue-router'

const router = useRouter()
const goto_index = () => {
  router.push('/')
}

defineProps({
  msg: String,
})

</script>

<template>
  <p>hello {{ msg }}</p>
  <el-button @click="goto_index">回到首页</el-button>
</template>

<style scoped>

</style>