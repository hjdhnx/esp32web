<template>
  <van-nav-bar
      title="登录"
      left-text="返回"
      left-arrow
      @click-left="onClickLeft"
  />
  <div class="login">
    <img :src="img" alt=""/>
    <van-form @submit="onSubmit">
      <van-cell-group inset>
        <van-field
            v-model="username"
            left-icon="phone-o"
            name="username"
            placeholder="手机号码"
            :rules="[{ required: true, message: '请填写用户名' }]"
        />
        <van-field
            v-model="password"
            left-icon="manager-o"
            type="password"
            name="password"
            placeholder="密码"
            :rules="[{ required: true, message: '请填写密码' }]"
        />
      </van-cell-group>
      <div style="margin: 16px">
        <van-button round block type="primary" native-type="submit">
          提交
        </van-button>
      </div>
    </van-form>
  </div>
  <div class="find">
    <router-link to="/enroll"><span>注册新用户</span></router-link>
    <router-link to="/verify"><span>找回密码</span></router-link>
  </div>
  <div class="ways">
    <span>其他登录方式</span>
    <div>
      <span class="iconfont">&#xe882;</span>
      <span class="iconfont">&#xe600;</span>
      <span class="iconfont">&#xe65a;</span>
    </div>
  </div>
</template>
<!-- 逻辑层 -->
<script setup>
import {reactive, ref} from "vue";
import {get, post, put, del} from "../utils/http";
import {showDialog} from "vant";
// 本地图片引入
import img from "../assets/vue.svg";
// 导入useRouter方法
import {useRouter} from "vue-router";

const router = useRouter();
// 返回上一页
const onClickLeft = () => {
  router.go(-1);
};
// 表单
const username = ref("");
const password = ref("");

//点击登录按钮事件
async function onSubmit(values) {
  console.log(values);
//axios调用json-server数据
  let res = await get("/api/infomation");
//foreach循环判断填入的手机号和密码是否正确
  res.data.forEach((element) => {
    if (
        element.iphone == values.username &&
        element.password == values.password
    ) {
      //本地存储数据的id值
      localStorage.setItem("key", JSON.stringify(element.id));
      router.push("/start");
      throw new Error();
    } else {
      username.value = "";
      password.value = "";
    }
  });
}
</script>
<!-- 样式层 -->
<style scoped>
.login {
  width: 100%;
  margin-top: 22.6667vw;
}

.login img {
  margin-left: 50vw;
  transform: translate(-50%, 0);
}

.find {
  display: flex;
  width: 70%;
  margin: 0 auto;
  justify-content: space-between;
}

.find span {
  color: #0079fe;
}

.ways {
  width: 80%;
  margin: 7.6667vw auto;
  text-align: center;
}

.ways > span {
  display: block;
  margin-bottom: 5.3333vw;
  color: #999999;
}

.ways div {
  display: flex;
  width: 80%;
  margin: 0 auto;
  justify-content: space-around;
}

.ways div span {
  font-size: 8.3333vw;
}
</style>